/**
 * Image Lightbox — click any .lightbox-img to view full-size in an overlay.
 * Click overlay or press Escape to close.
 * No dependencies. Add to any page with <script src="/js/image-lightbox.js"></script>
 */
(function () {
  // Create overlay once
  var overlay = document.createElement('div');
  overlay.id = 'lightbox-overlay';
  overlay.innerHTML = '<img id="lightbox-full" alt=""><span id="lightbox-close">&times;</span>';
  document.body.appendChild(overlay);

  // Inject styles
  var style = document.createElement('style');
  style.textContent =
    '#lightbox-overlay{display:none;position:fixed;top:0;left:0;width:100%;height:100%;' +
    'background:rgba(0,0,0,0.88);z-index:10000;cursor:zoom-out;justify-content:center;align-items:center;}' +
    '#lightbox-overlay.active{display:flex;}' +
    '#lightbox-full{max-width:95%;max-height:92vh;border-radius:6px;box-shadow:0 4px 30px rgba(0,0,0,0.4);object-fit:contain;}' +
    '#lightbox-close{position:fixed;top:16px;right:24px;color:#fff;font-size:2.2em;cursor:pointer;' +
    'font-weight:300;line-height:1;opacity:0.7;transition:opacity 0.15s;}' +
    '#lightbox-close:hover{opacity:1;}' +
    '.lightbox-img{cursor:zoom-in;}';
  document.head.appendChild(style);

  var fullImg = document.getElementById('lightbox-full');

  function open(src, alt) {
    fullImg.src = src;
    fullImg.alt = alt || '';
    overlay.classList.add('active');
  }

  function close() {
    overlay.classList.remove('active');
    fullImg.src = '';
  }

  overlay.addEventListener('click', close);
  document.getElementById('lightbox-close').addEventListener('click', function (e) {
    e.stopPropagation();
    close();
  });
  document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape') close();
  });

  // Attach to all .lightbox-img elements
  document.addEventListener('click', function (e) {
    var img = e.target.closest('.lightbox-img');
    if (img) {
      e.preventDefault();
      open(img.src, img.alt);
    }
  });
})();
