+++
title = "Explore the Floor Plan"
description = "Walk Solomon's Temple from the courtyard altar to the golden cube of the Holy of Holies."
image = "/images/culture/first-temple/temple-floorplan.svg"
hotspotKey = "first-temple"
dataNamespace = "first-temple"
weight = 3
layout = "tabernacle"
draft = true
+++

<!--
  PREVIEW STUB — build lane (Claude Code). draft=true so it does NOT enter the
  production build / nav until Codex finalizes it.

  Visual deliverables are done and verified:
    - base image: static/images/culture/first-temple/temple-floorplan.svg
    - hotspot data: data/first-temple/hotspots.yaml  (11 points, content verbatim
      from the verified vault draft; x/y set against the SVG)

  This page intentionally carries NO prose body — the §3 prose belongs to the
  content (vault) lane, not the visual lane.

  TO ACTIVATE (Codex lane): the shared layout themes/cfm/layouts/culture/tabernacle.html
  currently hardcodes its data lookup to `site.Data.tabernacle.*`, so hotspotKey =
  "first-temple" will NOT resolve against data/first-temple/ as written. Generalize
  the lookup to honor the `dataNamespace` param above (or add a parallel layout/partial),
  then register the section + nav and flip draft=false. See INTEGRATION_NOTES.md.

  Local rendering of the SVG + the 11 hotspot positions is verifiable now, without
  any theme change, via static/previews/first-temple-floorplan-preview.html.
-->
