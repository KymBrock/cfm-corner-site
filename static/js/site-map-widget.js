/**
 * Site Map Widget — Interactive clickable map of Ancient Egypt
 *
 * Usage:
 *   <div class="site-map-widget">
 *     <div class="smw-site" data-id="giza" data-name="Pyramids of Giza"
 *          data-top="18" data-left="38">
 *       ...site content (images, paragraphs, links)...
 *     </div>
 *     ...more sites...
 *   </div>
 *   <link rel="stylesheet" href="/css/site-map-widget.css">
 *   <script src="/js/site-map-widget.js"></script>
 *
 * Each .smw-site provides:
 *   data-id    — unique slug
 *   data-name  — display name
 *   data-top   — hotspot Y position as % of map height
 *   data-left  — hotspot X position as % of map width
 *   data-icon  — visual marker type
 *
 * The widget reads site content from the DOM, builds the interactive map
 * with hotspot dots, a site selector bar, and a detail panel below.
 */
(function () {
  var MAP_SRC = '/images/culture/egypt/08-egypt-sites-map.svg?v=2';

  function createWidget(container) {
    // Read site data from hidden .smw-site divs
    var siteDivs = container.querySelectorAll('.smw-site');
    var labelDivs = container.querySelectorAll('.smw-label-data');
    if (!siteDivs.length) return;

    var sites = [];
    var labels = [];
    for (var i = 0; i < siteDivs.length; i++) {
      var div = siteDivs[i];
      sites.push({
        id: div.getAttribute('data-id'),
        name: div.getAttribute('data-name'),
        top: parseFloat(div.getAttribute('data-top')),
        left: parseFloat(div.getAttribute('data-left')),
        icon: div.getAttribute('data-icon') || 'city',
        iconSrc: div.getAttribute('data-icon-src') || '',
        iconLg: div.hasAttribute('data-icon-lg'),
        iconXl: div.hasAttribute('data-icon-xl'),
        iconSize: div.getAttribute('data-icon-size') || '',
        iconClip: div.getAttribute('data-icon-clip') || '',
        markerTop: parseFloat(div.getAttribute('data-marker-top') || div.getAttribute('data-top')),
        markerLeft: parseFloat(div.getAttribute('data-marker-left') || div.getAttribute('data-left')),
        lineTop: parseFloat(div.getAttribute('data-line-top') || div.getAttribute('data-top')),
        lineLeft: parseFloat(div.getAttribute('data-line-left') || div.getAttribute('data-left')),
        content: div.innerHTML
      });
    }

    for (var l = 0; l < labelDivs.length; l++) {
      var labelDiv = labelDivs[l];
      labels.push({
        text: labelDiv.getAttribute('data-text'),
        top: parseFloat(labelDiv.getAttribute('data-top')),
        left: parseFloat(labelDiv.getAttribute('data-left')),
        className: labelDiv.getAttribute('data-class') || ''
      });
    }

    // Build widget HTML
    var html = '';

    // Instruction
    html += '<p class="smw-instruction">Click a location on the map or select from the list below to explore each site.</p>';

    // Map container with hotspots
    html += '<div class="smw-map-wrap">';
    html += '<img class="smw-map-img" src="' + MAP_SRC + '" alt="Map of Ancient Egypt showing major archaeological sites along the Nile" loading="lazy">';

    for (var m = 0; m < labels.length; m++) {
      var label = labels[m];
      html += '<div class="smw-map-label ' + label.className + '" '
        + 'style="top:' + label.top + '%;left:' + label.left + '%">'
        + label.text
        + '</div>';
    }

    // Hotspot dots
    for (var j = 0; j < sites.length; j++) {
      var s = sites[j];
      html += '<button class="smw-dot smw-dot--' + s.icon + '" data-index="' + j + '" data-name="' + s.name + '" '
        + 'data-site-top="' + s.lineTop + '" data-site-left="' + s.lineLeft + '" '
        + 'style="top:' + s.markerTop + '%;left:' + s.markerLeft + '%" '
        + 'aria-label="' + s.name + '" title="' + s.name + '">'
        + '<span class="smw-dot-hit" aria-hidden="true"></span>'
        + '<span class="smw-dot-line" aria-hidden="true"></span>'
        + '<span class="smw-dot-glyph"></span>'
        + '</button>';
    }
    html += '<div class="smw-bottom-mask" aria-hidden="true"></div>';
    html += '</div>';

    // Site selector bar (scrollable, for mobile and accessibility)
    html += '<div class="smw-selector">';
    for (var k = 0; k < sites.length; k++) {
      html += '<button class="smw-sel-btn" data-index="' + k + '">' + sites[k].name + '</button>';
    }
    html += '</div>';

    // Detail panel
    html += '<div class="smw-detail">';
    html += '<h4 class="smw-detail-title"></h4>';
    html += '<div class="smw-detail-body"></div>';
    html += '</div>';

    // Replace container contents
    container.innerHTML = html;

    // References
    var dots = container.querySelectorAll('.smw-dot');
    var dotHits = container.querySelectorAll('.smw-dot-hit');
    var selBtns = container.querySelectorAll('.smw-sel-btn');
    var detailTitle = container.querySelector('.smw-detail-title');
    var detailBody = container.querySelector('.smw-detail-body');
    var mapImg = container.querySelector('.smw-map-img');
    var currentIndex = -1;

    function updateLeaderLines() {
      var mapWidth = mapImg.clientWidth;
      var mapHeight = mapImg.clientHeight;
      if (!mapWidth || !mapHeight) return;

      for (var i = 0; i < dots.length; i++) {
        var dot = dots[i];
        var line = dot.querySelector('.smw-dot-line');
        var markerLeft = parseFloat(dot.style.left);
        var markerTop = parseFloat(dot.style.top);
        var siteLeft = parseFloat(dot.getAttribute('data-site-left'));
        var siteTop = parseFloat(dot.getAttribute('data-site-top'));
        var dx = (siteLeft - markerLeft) * mapWidth / 100;
        var dy = (siteTop - markerTop) * mapHeight / 100;
        var lineLength = Math.sqrt(dx * dx + dy * dy);
        var lineAngle = Math.atan2(dy, dx) * (180 / Math.PI);

        if (lineLength < 6) {
          line.style.display = 'none';
        } else {
          line.style.display = 'block';
          line.style.width = lineLength + 'px';
          line.style.transform = 'translateY(-50%) rotate(' + lineAngle + 'deg)';
        }
      }
    }

    function select(index) {
      if (index === currentIndex) return;
      currentIndex = index;
      var site = sites[index];

      // Update dots
      for (var d = 0; d < dots.length; d++) {
        dots[d].classList.toggle('active', d === index);
      }
      // Update selector buttons
      for (var b = 0; b < selBtns.length; b++) {
        selBtns[b].classList.toggle('active', b === index);
      }
      // Scroll selector button into view
      selBtns[index].scrollIntoView({ behavior: 'smooth', block: 'nearest', inline: 'center' });

      // Update detail panel
      if (site.iconSrc) {
        var iconClass = 'smw-title-icon' + (site.iconXl ? ' smw-title-icon--xl' : site.iconLg ? ' smw-title-icon--lg' : '');
        var styleParts = [];
        if (site.iconSize) styleParts.push('max-height:' + site.iconSize + 'px');
        if (site.iconClip) styleParts.push('clip-path:' + site.iconClip);
        var iconStyle = styleParts.length ? ' style="' + styleParts.join(';') + '"' : '';
        detailTitle.innerHTML = site.name + '<img class="' + iconClass + '" src="' + site.iconSrc + '"' + iconStyle + ' alt="">';
      } else {
        detailTitle.textContent = site.name;
      }
      detailBody.innerHTML = site.content;

      // Initialize any galleries in the new content
      initGalleries(detailBody);

      // Scroll detail panel into view on mobile
      if (window.innerWidth < 640) {
        detailTitle.scrollIntoView({ behavior: 'smooth', block: 'start' });
      }
    }

    // Attach click handlers to dots
    for (var d = 0; d < dotHits.length; d++) {
      dotHits[d].addEventListener('mouseenter', function () {
        this.parentNode.classList.add('hovered');
      });
      dotHits[d].addEventListener('mouseleave', function () {
        this.parentNode.classList.remove('hovered');
      });
      dotHits[d].addEventListener('click', function () {
        select(parseInt(this.parentNode.getAttribute('data-index'), 10));
      });
    }

    // Attach click handlers to selector buttons
    for (var b = 0; b < selBtns.length; b++) {
      selBtns[b].addEventListener('click', function () {
        select(parseInt(this.getAttribute('data-index'), 10));
      });
    }

    // Default: select first site
    select(0);
    updateLeaderLines();

    if (mapImg.complete) {
      updateLeaderLines();
    } else {
      mapImg.addEventListener('load', updateLeaderLines, { once: true });
    }

    window.addEventListener('resize', updateLeaderLines);
  }

  function initGalleries(container) {
    var galleries = container.querySelectorAll('.smw-gallery');
    for (var g = 0; g < galleries.length; g++) {
      (function(gallery) {
        var items = gallery.querySelectorAll('.smw-gallery-item');
        var counter = gallery.querySelector('.smw-gallery-counter');
        var prevBtn = gallery.querySelector('.smw-gallery-prev');
        var nextBtn = gallery.querySelector('.smw-gallery-next');
        if (items.length < 2) {
          // Hide nav if only 1 image
          var nav = gallery.querySelector('.smw-gallery-nav');
          if (nav) nav.style.display = 'none';
          return;
        }
        var current = 0;
        function show(idx) {
          for (var i = 0; i < items.length; i++) {
            items[i].classList.toggle('active', i === idx);
          }
          current = idx;
          if (counter) counter.textContent = (idx + 1) + ' / ' + items.length;
        }
        if (prevBtn) prevBtn.addEventListener('click', function() {
          show((current - 1 + items.length) % items.length);
        });
        if (nextBtn) nextBtn.addEventListener('click', function() {
          show((current + 1) % items.length);
        });
        // Swipe support
        var startX = 0;
        var track = gallery.querySelector('.smw-gallery-track');
        if (track) {
          track.addEventListener('touchstart', function(e) { startX = e.touches[0].clientX; }, { passive: true });
          track.addEventListener('touchend', function(e) {
            var diff = startX - e.changedTouches[0].clientX;
            if (Math.abs(diff) > 40) {
              show(diff > 0 ? (current + 1) % items.length : (current - 1 + items.length) % items.length);
            }
          });
        }
        show(0);
      })(galleries[g]);
    }
  }

  function init() {
    var widgets = document.querySelectorAll('.site-map-widget');
    for (var i = 0; i < widgets.length; i++) {
      createWidget(widgets[i]);
    }
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
