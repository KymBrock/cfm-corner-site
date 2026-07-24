#!/bin/bash
# Produce narration for the Achaemenid and Assyria field guides end to end.
#
# For each script: load into the Narration Studio -> engaged preset -> auto-curve
# -> produce (1 take/phrase, resumes from any wav already on disk) -> export
# -> re-encode to the published spec -> install into the site -> commit -> push.
#
# Each episode is pushed as it finishes, so Cloudflare rebuilds and the audio is
# reviewable on a phone within ~2 minutes of completion.
#
# Safe to re-run: finished episodes are skipped, and produce.py resumes phrases.
set -uo pipefail

NS="$HOME/Developer/narration-studio"
SITE="$HOME/Developer/cfm-corner-site"
VAULT="$HOME/Obsidian/K Master Vault/Master Project Folder/Ongoing/CFM Corner/OT_2026/Culture"
LOG=/tmp/narration-run.log

export TTS_PYTHON="$NS/tts-venv/bin/python"

say() { echo "[$(date '+%H:%M:%S')] $*" | tee -a "$LOG"; }

produce_one() {  # $1=guide(Achaemenid|Assyria)  $2=slug
  local guide="$1" slug="$2"
  local lguide; lguide=$(echo "$guide" | tr '[:upper:]' '[:lower:]')
  local eid="${lguide}-${slug}"
  local dest="$SITE/static/audio/culture/${lguide}/${slug}.mp3"

  if [ -f "$dest" ]; then say "SKIP  $guide/$slug (already installed)"; return 0; fi
  say "START $guide/$slug"

  # 1. load the SCRIPT body only
  python3 - "$VAULT/$guide/_narration/$slug.script.md" "$eid" <<'PY'
import sys, re, json, pathlib, urllib.request
src, eid = sys.argv[1], sys.argv[2]
t = pathlib.Path(src).read_text()
body = t.split("# SCRIPT",1)[-1].split("# Pronunciation")[0]
body = re.sub(r"\n-{3,}\s*$", "", body.strip()) + "\n"
req = urllib.request.Request("http://localhost:8770/episode/load",
      data=json.dumps({"title": eid, "script": body}).encode(),
      headers={"Content-Type":"application/json"})
d = json.load(urllib.request.urlopen(req, timeout=120))
print(f"    loaded {d['id']}: {len(d.get('phrases',{}))} phrases", flush=True)
PY
  [ $? -ne 0 ] && { say "FAIL  $guide/$slug (load)"; return 1; }

  # 2. engaged preset + auto curve, matching the Babylon episodes
  curl -s --max-time 60 -X POST "http://localhost:8770/episode/$eid/direction" \
    -H "Content-Type: application/json" -d '{"scope":"episode","preset":"engaged"}' -o /dev/null
  curl -s --max-time 60 -X POST "http://localhost:8770/episode/$eid/auto-curve" \
    -H "Content-Type: application/json" -d '{"on":true}' -o /dev/null

  # 3. produce; retry, since produce.py resumes from wavs already on disk
  local ok=0
  for attempt in 1 2 3 4 5 6; do
    if "$NS/.venv/bin/python" "$NS/scripts/produce.py" "$eid" >>"$LOG" 2>&1; then ok=1; break; fi
    say "      produce attempt $attempt aborted; retrying (resumes from disk)"
    sleep 20
  done
  [ "$ok" -ne 1 ] && { say "FAIL  $guide/$slug (produce gave up after 6)"; return 1; }

  # 4. re-encode to the published spec and install
  local master="$NS/episodes/$eid/export/$eid.mp3"
  [ -f "$master" ] || { say "FAIL  $guide/$slug (no master mp3)"; return 1; }
  mkdir -p "$(dirname "$dest")"
  ffmpeg -nostdin -v error -y -i "$master" -ac 1 -ar 48000 -b:a 64k -map_metadata -1 "$dest" \
    || { say "FAIL  $guide/$slug (ffmpeg)"; return 1; }

  # 5. commit + push so it appears on the preview
  cd "$SITE" || return 1
  git add "static/audio/culture/${lguide}/${slug}.mp3"
  git commit -q -m "${guide} guide: narration for ${slug}

Produced in the Narration Studio from the drafted script, engaged preset
with auto energy curve. Re-encoded to the published spec (mono, 48 kHz,
64 kbps) rather than shipping the 160 kbps studio master." \
    && git push -q origin claude/staging-pipeline
  say "DONE  $guide/$slug -> $(du -h "$dest" | cut -f1)"
}

say "===== narration run starting ====="
say "worker cap: ${NARRATE_WORKER_MAX_GB:-default}"

# Achaemenid 09 first — it is already 36/39 generated, so it finishes fastest
produce_one Achaemenid 09-major-sites

for s in 01-from-persis-to-empire 02-timeline-and-kings 03-how-the-empire-worked \
         04-religion-zoroastrianism 05-cyrus-and-the-return 06-rebuilding-jerusalem \
         07-esthers-world 08-writing-and-records 10-lds-connections; do
  produce_one Achaemenid "$s"
done

for s in 01-the-assyrian-heartland 02-timeline-and-empire 03-the-war-machine \
         04-religion-and-the-god-ashur 05-writing-and-the-great-library \
         06-the-great-cities 07-the-fall-of-the-north 08-sennacherib-and-hezekiah \
         09-assyria-and-the-bible 10-major-sites-and-discoveries 11-lds-connections; do
  produce_one Assyria "$s"
done

say "===== narration run finished ====="
