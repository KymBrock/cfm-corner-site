import json, urllib.request, time
BASE="http://localhost:8770/episode/weekly-insights-week-30"
req=urllib.request.Request(BASE+"/generate-all", data=json.dumps({"only_missing":True}).encode(),
    headers={"Content-Type":"application/json"}, method="POST")
t0=time.time()
r=json.load(urllib.request.urlopen(req, timeout=1800))
print("elapsed_sec:", round(time.time()-t0,1), "generated:", r.get("generated"))
# verify no phrase missing a take
s=json.load(urllib.request.urlopen(BASE, timeout=30))
ph=s["phrases"]; miss=[p for p,v in ph.items() if not v["takes"]]
print("phrases:", len(ph), "missing takes:", miss or "none ✅")
