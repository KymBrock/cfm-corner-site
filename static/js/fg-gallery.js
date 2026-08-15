/**
 * fg-gallery — Field-Guide image slideshow / gallery
 *
 * Initializes every .fg-gallery on the page: arrows, dots, counter, keyboard
 * (← / →), touch-swipe, and a per-slide caption + credit line. Standalone —
 * does not depend on the site-map-widget. Safe to load on any page.
 *
 * See /css/fg-gallery.css for the expected markup.
 */
(function () {
  function initGallery(gallery) {
    var items = Array.prototype.slice.call(gallery.querySelectorAll('.fg-item'));
    if (items.length === 0) return;

    var cap = gallery.querySelector('.fg-cap');
    var counter = gallery.querySelector('.fg-counter');
    var dotsWrap = gallery.querySelector('.fg-dots');
    var prevBtn = gallery.querySelector('.fg-prev');
    var nextBtn = gallery.querySelector('.fg-next');
    var i = 0;

    // Single image: show it, hide the chrome.
    if (items.length < 2) {
      items[0].classList.add('active');
      if (counter) counter.style.display = 'none';
      if (prevBtn) prevBtn.style.display = 'none';
      if (nextBtn) nextBtn.style.display = 'none';
      renderCaption();
      return;
    }

    // Build dots
    var dots = [];
    if (dotsWrap) {
      items.forEach(function (_, idx) {
        var d = document.createElement('button');
        d.className = 'fg-dot';
        d.setAttribute('type', 'button');
        d.setAttribute('aria-label', 'Slide ' + (idx + 1));
        d.addEventListener('click', function () { go(idx); });
        dotsWrap.appendChild(d);
        dots.push(d);
      });
    }

    function renderCaption() {
      if (!cap) return;
      var it = items[i];
      var c = it.getAttribute('data-caption') || '';
      var cr = it.getAttribute('data-credit') || '';
      cap.innerHTML = c + (cr ? '<span class="fg-credit">' + cr + '</span>' : '');
    }

    function render() {
      items.forEach(function (s, idx) { s.classList.toggle('active', idx === i); });
      dots.forEach(function (d, idx) { d.classList.toggle('active', idx === i); });
      if (counter) counter.textContent = (i + 1) + ' / ' + items.length;
      renderCaption();
    }

    function go(n) { i = (n + items.length) % items.length; render(); }

    if (nextBtn) nextBtn.addEventListener('click', function () { go(i + 1); });
    if (prevBtn) prevBtn.addEventListener('click', function () { go(i - 1); });

    gallery.tabIndex = 0;
    gallery.addEventListener('keydown', function (e) {
      if (e.key === 'ArrowRight') { go(i + 1); e.preventDefault(); }
      else if (e.key === 'ArrowLeft') { go(i - 1); e.preventDefault(); }
    });

    // Touch swipe
    var x0 = null;
    gallery.addEventListener('touchstart', function (e) { x0 = e.touches[0].clientX; }, { passive: true });
    gallery.addEventListener('touchend', function (e) {
      if (x0 === null) return;
      var dx = e.changedTouches[0].clientX - x0;
      if (Math.abs(dx) > 40) go(dx < 0 ? i + 1 : i - 1);
      x0 = null;
    });

    render();
  }

  function init() {
    var galleries = document.querySelectorAll('.fg-gallery');
    for (var g = 0; g < galleries.length; g++) initGallery(galleries[g]);
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
