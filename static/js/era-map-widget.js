/**
 * Era Map Widget — Interactive Ancient Near East Map Timeline
 * Maps by Enyavar (Wikimedia Commons, CC BY-SA 4.0)
 *
 * Usage:
 *   <div class="era-map-widget" data-start-era="1500"></div>
 *   <script src="/js/era-map-widget.js"></script>
 *
 * data-start-era: the year to start on (positive = BC, negative = AD)
 *   e.g. data-start-era="1500" → 1500 BC
 *        data-start-era="-100" → 100 AD
 */
(function () {
  var ERAS = [
    { year: 2600, label: '2600 BC', file: 'ane-2600bc.svg', desc: 'Early Dynastic Egypt · Rise of Akkadian Empire · Pyramids of Giza under construction' },
    { year: 2500, label: '2500 BC', file: 'ane-2500bc.svg', desc: 'Old Kingdom Egypt at its height · Great Pyramid complete · Ebla flourishes in Syria' },
    { year: 2400, label: '2400 BC', file: 'ane-2400bc.svg', desc: 'Late Old Kingdom · Akkadian Empire expanding · Sumer under pressure' },
    { year: 2300, label: '2300 BC', file: 'ane-2300bc.svg', desc: 'Sargon of Akkad · First empire in history · Old Kingdom Egypt declining' },
    { year: 2200, label: '2200 BC', file: 'ane-2200bc.svg', desc: 'First Intermediate Period begins · Akkadian Empire collapses · 4.2 kiloyear climate event' },
    { year: 2100, label: '2100 BC', file: 'ane-2100bc.svg', desc: 'Ur III dynasty · Egypt reunifying · Abraham born in Ur (traditional dating)' },
    { year: 2000, label: '2000 BC', file: 'ane-2000bc.svg', desc: 'Middle Kingdom Egypt (11th Dynasty) · Abraham\u2019s era · Elam dominates Sumer' },
    { year: 1900, label: '1900 BC', file: 'ane-1900bc.svg', desc: 'Middle Kingdom Egypt (12th Dynasty) · Old Assyrian trade colonies · Patriarchal period' },
    { year: 1800, label: '1800 BC', file: 'ane-1800bc.svg', desc: 'Age of the Patriarchs · Hammurabi\u2019s Babylon rising · Egypt controls Nubia' },
    { year: 1700, label: '1700 BC', file: 'ane-1700bc.svg', desc: 'Second Intermediate Period · Hyksos entering Delta · Hammurabi\u2019s empire has fallen' },
    { year: 1600, label: '1600 BC', file: 'ane-1600bc.svg', desc: 'Hyksos rule Lower Egypt · Joseph\u2019s era · Old Hittite Empire sacks Babylon' },
    { year: 1500, label: '1500 BC', file: 'ane-1500bc.svg', desc: 'New Kingdom Egypt conquers Levant · Moses\u2019 era · Egypt vs. Hittites vs. Mitanni' },
    { year: 1400, label: '1400 BC', file: 'ane-1400bc.svg', desc: 'Amarna Period · Akhenaten\u2019s religious revolution · Amarna Letters · Ugarit flourishes' },
    { year: 1300, label: '1300 BC', file: 'ane-1300bc.svg', desc: 'Ramesses II · Battle of Kadesh · Treaty with Hittites · Height of Egyptian empire' },
    { year: 1200, label: '1200 BC', file: 'ane-1200bc.svg', desc: 'Sea Peoples invasion · Bronze Age Collapse · Hittite Empire falls · Israelite settlement' },
    { year: 1100, label: '1100 BC', file: 'ane-1100bc.svg', desc: 'Post-collapse world · Judges period in Israel · Phoenician cities rising · Egypt fragmented' },
    { year: 1000, label: '1000 BC', file: 'ane-1000bc.svg', desc: 'Third Intermediate Period · David & Solomon · Phoenician golden age · Assyria vs. Babylon' },
    { year: 900, label: '900 BC', file: 'ane-0900bc.svg', desc: 'Divided Kingdom (Israel & Judah) · Neo-Assyrian Empire expanding · Phoenician colonization' },
    { year: 800, label: '800 BC', file: 'ane-0800bc.svg', desc: 'Assyrian dominance · Prophets Amos & Hosea · Kushite dynasty rising in Egypt' },
    { year: 700, label: '700 BC', file: 'ane-0700bc.svg', desc: 'Assyria conquers Israel (722 BC) · Sennacherib besieges Jerusalem · Kushite pharaohs' },
    { year: 600, label: '600 BC', file: 'ane-0600bc.svg', desc: 'Babylonian Empire · Fall of Jerusalem (586 BC) · Exile · Late Period Egypt · Rise of Persia' },
    { year: 500, label: '500 BC', file: 'ane-0500bc.svg', desc: 'Persian Empire at its height · Jews return from exile · Elephantine colony · Second Temple built' },
    { year: 400, label: '400 BC', file: 'ane-0400bc.svg', desc: 'Late Persian period · Elephantine temple destroyed (410 BC) · Ezra & Nehemiah · Greek wars with Persia' },
    { year: 300, label: '300 BC', file: 'ane-0300bc.svg', desc: 'Alexander\u2019s conquests · Ptolemaic Egypt begins · Alexandria founded · Septuagint era \u00b7 [German labels]' },
    { year: 200, label: '200 BC', file: 'ane-0200bc.svg', desc: 'Ptolemaic vs. Seleucid · Maccabean revolt · Hor\u2019s papyri created in Thebes \u00b7 [German labels]' },
    { year: 100, label: '100 BC', file: 'ane-0100bc.svg', desc: 'Roman expansion · Hasmonean kingdom · Cleopatra VII · Julius Caesar \u00b7 [German labels]' },
    { year: -1, label: '1 AD', file: 'ane-0001ad.svg', desc: 'Roman Empire · Herod the Great · Birth of Christ · Philo of Alexandria \u00b7 [German labels]' },
    { year: -100, label: '100 AD', file: 'ane-0100ad.svg', desc: 'Roman Empire at its height · Destruction of Jerusalem (70 AD) · Kitos War (115\u2013117) · Diaspora' },
    { year: -200, label: '200 AD', file: 'ane-0200ad.svg', desc: 'Roman provinces · Rabbinic Judaism consolidates · Mishnah compiled \u00b7 [German labels]' },
    { year: -300, label: '300 AD', file: 'ane-0300ad.svg', desc: 'Constantine · Christianity legalized · Last hieroglyphic inscription (394 AD) \u00b7 [German labels]' },
    { year: -400, label: '400 AD', file: 'ane-0400ad.svg', desc: 'Theodosian edicts · Temples closed · Nag Hammadi texts buried · Western Empire falling \u00b7 [German labels]' },
    { year: -500, label: '500 AD', file: 'ane-0500ad.svg', desc: 'Byzantine Empire · Justinian closes Philae (537 AD) · End of ancient Egyptian religion \u00b7 [German labels]' },
    { year: -600, label: '600 AD', file: 'ane-0600ad.svg', desc: 'Rise of Islam · Arab conquest of Egypt (642 AD) · Byzantine retreat \u00b7 [German labels]' }
  ];

  var BASE_PATH = '/images/culture/egypt/maps/';

  function findIndex(startEra) {
    for (var i = 0; i < ERAS.length; i++) {
      if (ERAS[i].year === startEra) return i;
    }
    // Find closest
    var closest = 0;
    var minDiff = Math.abs(ERAS[0].year - startEra);
    for (var j = 1; j < ERAS.length; j++) {
      var diff = Math.abs(ERAS[j].year - startEra);
      if (diff < minDiff) { minDiff = diff; closest = j; }
    }
    return closest;
  }

  function createWidget(container) {
    var startVal = parseInt(container.getAttribute('data-start-era') || '1500', 10);
    var currentIndex = findIndex(startVal);

    var html = '<div class="era-map-inner">';

    // Controls header
    html += '<div class="era-map-header">';
    html += '<button class="era-map-btn era-map-prev" aria-label="Previous era">\u2190</button>';
    html += '<span class="era-map-title"></span>';
    html += '<button class="era-map-btn era-map-next" aria-label="Next era">\u2192</button>';
    html += '</div>';

    // Slider
    html += '<div class="era-map-slider-wrap">';
    html += '<input type="range" class="era-map-slider" min="0" max="' + (ERAS.length - 1) + '" value="' + currentIndex + '" step="1">';
    html += '</div>';

    // Map image
    html += '<div class="era-map-image-wrap">';
    html += '<img class="era-map-img" alt="" loading="lazy">';
    html += '</div>';

    // Description
    html += '<p class="era-map-desc"></p>';

    // Attribution
    html += '<p class="era-map-attribution">Maps by <a href="https://commons.wikimedia.org/wiki/User:Enyavar" target="_blank">Enyavar</a> \u00b7 <a href="https://creativecommons.org/licenses/by-sa/4.0/" target="_blank">CC BY-SA 4.0</a> \u00b7 Wikimedia Commons</p>';

    html += '</div>';
    container.innerHTML = html;

    var img = container.querySelector('.era-map-img');
    var title = container.querySelector('.era-map-title');
    var desc = container.querySelector('.era-map-desc');
    var prevBtn = container.querySelector('.era-map-prev');
    var nextBtn = container.querySelector('.era-map-next');
    var slider = container.querySelector('.era-map-slider');

    function update() {
      var era = ERAS[currentIndex];
      img.src = BASE_PATH + era.file;
      img.alt = 'Ancient Near East \u2014 ' + era.label;
      title.textContent = era.label;
      desc.textContent = era.desc;
      prevBtn.disabled = currentIndex === 0;
      nextBtn.disabled = currentIndex === ERAS.length - 1;
      slider.value = currentIndex;
    }

    prevBtn.addEventListener('click', function () {
      if (currentIndex > 0) { currentIndex--; update(); }
    });
    nextBtn.addEventListener('click', function () {
      if (currentIndex < ERAS.length - 1) { currentIndex++; update(); }
    });
    slider.addEventListener('input', function () {
      currentIndex = parseInt(this.value, 10);
      update();
    });

    // Keyboard navigation when focused
    container.setAttribute('tabindex', '0');
    container.addEventListener('keydown', function (e) {
      if (e.key === 'ArrowLeft' && currentIndex > 0) {
        currentIndex--; update(); e.preventDefault();
      }
      if (e.key === 'ArrowRight' && currentIndex < ERAS.length - 1) {
        currentIndex++; update(); e.preventDefault();
      }
    });

    update();
  }

  function init() {
    var widgets = document.querySelectorAll('.era-map-widget');
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
