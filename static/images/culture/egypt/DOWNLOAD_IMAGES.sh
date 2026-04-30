#!/bin/bash
# Egypt Cultural Supplement — Image Download Script
# Run this from a terminal: bash DOWNLOAD_IMAGES.sh
# All images are PD or CC-BY-SA from Wikimedia Commons
#
# NOTE: If curl fails, open the URLs in a browser and Save As to this directory.

DIR="$(cd "$(dirname "$0")" && pwd)"
cd "$DIR"

echo "Downloading Egypt supplement images to: $DIR"
echo ""

# === PRIORITY 1: Essential ===

echo "--- Section 06: Weighing of the Heart (Papyrus of Hunefer, PD) ---"
curl -sL -H "User-Agent: CFMCorner/1.0" -o "06-weighing-of-heart-hunefer.jpg" \
  "https://upload.wikimedia.org/wikipedia/commons/5/5a/The_judgement_of_the_dead_in_the_presence_of_Osiris.jpg"

echo "--- Section 08: Ancient Egypt Map (Jeff Dahl, CC-BY-SA) ---"
curl -sL -H "User-Agent: CFMCorner/1.0" -o "map-ancient-egypt.svg" \
  "https://upload.wikimedia.org/wikipedia/commons/1/10/Ancient_Egypt_map-en.svg"

echo "--- Section 09: Levant Trade Routes (CC-BY-SA) ---"
curl -sL -H "User-Agent: CFMCorner/1.0" -o "map-levant-routes.png" \
  "https://upload.wikimedia.org/wikipedia/commons/b/b5/Ancient_Levant_routes.png"

# === PRIORITY 2: High-Value PD Images ===

echo "--- Section 01: Pyramids of Giza (CC-BY-SA 2.0) ---"
curl -sL -H "User-Agent: CFMCorner/1.0" -o "01-pyramids-giza.jpg" \
  "https://upload.wikimedia.org/wikipedia/commons/a/af/All_Giza_Pyramids.jpg"

echo "--- Section 01: Beni Hasan Asiatic Visitors (PD) ---"
curl -sL -H "User-Agent: CFMCorner/1.0" -o "01-beni-hasan-aamu.jpg" \
  "https://upload.wikimedia.org/wikipedia/commons/a/a7/Drawing_of_the_procession_of_the_Aamu_group_tomb_of_Khnumhotep_II_at_Beni_Hassan.jpg"

echo "--- Section 01: Merneptah Stele (CC-BY-SA 3.0) ---"
curl -sL -H "User-Agent: CFMCorner/1.0" -o "01-merneptah-stele.jpg" \
  "https://upload.wikimedia.org/wikipedia/commons/e/e0/Merneptah_Israel_Stele_Cairo.JPG"

echo "--- Section 02: Abu Simbel Panoramic (CC-BY-SA 4.0) ---"
curl -sL -H "User-Agent: CFMCorner/1.0" -o "02-abu-simbel-panoramic.jpg" \
  "https://upload.wikimedia.org/wikipedia/commons/0/02/The_two_temples_of_Abu_simbel%2Cpanoramic_view..JPG"

echo "--- Section 03: Flight into Egypt, Giotto (PD) ---"
curl -sL -H "User-Agent: CFMCorner/1.0" -o "03-flight-into-egypt-giotto.jpg" \
  "https://upload.wikimedia.org/wikipedia/commons/a/ab/Giotto_-_Scrovegni_-_-20-_-_Flight_into_Egypt.jpg"

echo "--- Section 04: Rosetta Stone (CC-BY-SA) ---"
curl -sL -H "User-Agent: CFMCorner/1.0" -o "04-rosetta-stone.jpg" \
  "https://upload.wikimedia.org/wikipedia/commons/b/bf/Rosetta_Stone%2C_British_Museum_009.JPG"

echo "--- Section 04: Champollion Portrait (PD, Cogniet 1831) ---"
curl -sL -H "User-Agent: CFMCorner/1.0" -o "04-champollion-portrait.jpg" \
  "https://upload.wikimedia.org/wikipedia/commons/7/75/Jean-Fran%C3%A7ois_Champollion%2C_by_L%C3%A9on_Cogniet.jpg"

echo "--- Section 04: Ebers Papyrus hieratic (PD Mark 1.0) ---"
curl -sL -H "User-Agent: CFMCorner/1.0" -o "04-ebers-papyrus-hieratic.png" \
  "https://upload.wikimedia.org/wikipedia/commons/3/3c/Papyrus_Ebers_2.png"

echo "--- Section 05: Library of Alexandria (PD, Von Corven 19th c.) ---"
curl -sL -H "User-Agent: CFMCorner/1.0" -o "05-library-of-alexandria.jpg" \
  "https://upload.wikimedia.org/wikipedia/commons/6/64/Ancientlibraryalex.jpg"

echo "--- Section 09: Sea Peoples at Medinet Habu (CC-BY-SA 3.0) ---"
curl -sL -H "User-Agent: CFMCorner/1.0" -o "09-sea-peoples-medinet-habu.jpg" \
  "https://upload.wikimedia.org/wikipedia/commons/c/c7/Medinet_Habu_Ramses_III._Tempel_Nordostwand_Abzeichnung_01.jpg"

echo "--- Section 10: Facsimile 2, Times and Seasons 1842 (PD Mark 1.0) ---"
curl -sL -H "User-Agent: CFMCorner/1.0" -o "10-facsimile-2-times-seasons.jpg" \
  "https://upload.wikimedia.org/wikipedia/commons/a/a2/Facsimile_2_Times_and_Seasons_1842.JPG"

# === PRIORITY 3: Maps (SVG for Illustrator editing) ===

echo "--- Map: Egypt 1450 BC extent (PD) ---"
curl -sL -H "User-Agent: CFMCorner/1.0" -o "map-egypt-1450bc.svg" \
  "https://upload.wikimedia.org/wikipedia/commons/0/0a/Egypt_1450_BC.svg"

echo "--- Map: Ptolemaic Kingdom (CC-BY-SA 4.0) ---"
curl -sL -H "User-Agent: CFMCorner/1.0" -o "map-ptolemaic-kingdom.svg" \
  "https://upload.wikimedia.org/wikipedia/commons/3/3b/Ptolemaic_Kingdom_III-II_century_BC_-_en.svg"

echo "--- Map: Exodus route (CC-BY-SA 4.0) ---"
curl -sL -H "User-Agent: CFMCorner/1.0" -o "map-exodus-route.svg" \
  "https://upload.wikimedia.org/wikipedia/commons/6/6a/Exodus.svg"

echo "--- Map: Jewish Diaspora with Acts (CC-BY-SA 4.0) ---"
curl -sL -H "User-Agent: CFMCorner/1.0" -o "map-jewish-diaspora.svg" \
  "https://upload.wikimedia.org/wikipedia/commons/4/4f/Antique_jew_diaspora_map_with_Acts_of_the_Apostles_mention_highlight.svg"

echo "--- Map: Roman Egypt 125 AD (CC-BY-SA 4.0) ---"
curl -sL -H "User-Agent: CFMCorner/1.0" -o "map-roman-egypt.svg" \
  "https://upload.wikimedia.org/wikipedia/commons/7/79/Roman_Empire_-_Aegyptus_%28125_AD%29.svg"

echo "--- Map: Alexander's Empire (PD, 1913) ---"
curl -sL -H "User-Agent: CFMCorner/1.0" -o "map-alexander-empire.png" \
  "https://upload.wikimedia.org/wikipedia/commons/4/40/Map-alexander-empire.png"

echo ""
echo "Download complete. Check file sizes — any file under 1KB likely failed."
echo "For failed downloads, open the Wikimedia Commons URL in a browser and Save As."
ls -lh *.jpg *.png *.svg 2>/dev/null
