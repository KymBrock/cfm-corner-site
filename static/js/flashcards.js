/**
 * CFM Corner Flashcard System
 * Interactive vocabulary flashcards with shuffle/randomize capability
 */

class Flashcards {
  constructor(containerId, terms) {
    this.container = document.getElementById(containerId);
    this.originalTerms = [...terms];
    this.terms = [...terms];
    this.currentIndex = 0;
    this.isFlipped = false;
    this.init();
  }

  init() {
    this.render();
    this.bindEvents();
  }

  shuffle() {
    // Fisher-Yates shuffle
    for (let i = this.terms.length - 1; i > 0; i--) {
      const j = Math.floor(Math.random() * (i + 1));
      [this.terms[i], this.terms[j]] = [this.terms[j], this.terms[i]];
    }
    this.currentIndex = 0;
    this.isFlipped = false;
    this.updateCard();
  }

  reset() {
    this.terms = [...this.originalTerms];
    this.currentIndex = 0;
    this.isFlipped = false;
    this.updateCard();
  }

  next() {
    if (this.currentIndex < this.terms.length - 1) {
      this.currentIndex++;
      this.isFlipped = false;
      this.updateCard();
    }
  }

  prev() {
    if (this.currentIndex > 0) {
      this.currentIndex--;
      this.isFlipped = false;
      this.updateCard();
    }
  }

  flip() {
    this.isFlipped = !this.isFlipped;
    const card = this.container.querySelector('.flashcard');
    if (card) {
      card.classList.toggle('flipped', this.isFlipped);
    }
  }

  updateCard() {
    const term = this.terms[this.currentIndex];
    const front = this.container.querySelector('.flashcard-front');
    const back = this.container.querySelector('.flashcard-back');
    const counter = this.container.querySelector('.flashcard-counter');
    const card = this.container.querySelector('.flashcard');

    if (front && term) {
      front.innerHTML = `
        <div class="flashcard-original">${term.original}</div>
        <div class="flashcard-translit"><em>${term.translit}</em></div>
        ${term.audio ? `<button class="flashcard-audio" type="button" aria-label="Play pronunciation for ${term.translit}" onclick="playFlashcardAudio('${term.audio}', event)">🔊 Listen</button>` : ''}
      `;
    }

    if (back && term) {
      back.innerHTML = `
        ${term.proto ? `<div class="flashcard-proto"><span class="proto-sin">${term.proto}</span></div>` : ''}
        <div class="flashcard-meaning">${term.meaning}</div>
        ${term.audio ? `<button class="flashcard-audio flashcard-audio-back" type="button" aria-label="Play pronunciation for ${term.translit}" onclick="playFlashcardAudio('${term.audio}', event)">🔊 Listen</button>` : ''}
        ${term.strongs ? `<div class="flashcard-strongs">${term.strongs}</div>` : ''}
      `;
    }

    if (counter) {
      counter.textContent = `${this.currentIndex + 1} / ${this.terms.length}`;
    }

    if (card) {
      card.classList.remove('flipped');
      this.isFlipped = false;
    }

    // Update button states
    const prevBtn = this.container.querySelector('.flashcard-prev');
    const nextBtn = this.container.querySelector('.flashcard-next');
    if (prevBtn) prevBtn.disabled = this.currentIndex === 0;
    if (nextBtn) nextBtn.disabled = this.currentIndex === this.terms.length - 1;
  }

  render() {
    const term = this.terms[this.currentIndex];

    this.container.innerHTML = `
      <div class="flashcard-wrapper">
        <div class="flashcard">
          <div class="flashcard-inner">
            <div class="flashcard-front">
              <div class="flashcard-original">${term.original}</div>
              <div class="flashcard-translit"><em>${term.translit}</em></div>
              ${term.audio ? `<button class="flashcard-audio" type="button" aria-label="Play pronunciation for ${term.translit}" onclick="playFlashcardAudio('${term.audio}', event)">🔊 Listen</button>` : ''}
            </div>
            <div class="flashcard-back">
              ${term.proto ? `<div class="flashcard-proto"><span class="proto-sin">${term.proto}</span></div>` : ''}
              <div class="flashcard-meaning">${term.meaning}</div>
              ${term.audio ? `<button class="flashcard-audio flashcard-audio-back" type="button" aria-label="Play pronunciation for ${term.translit}" onclick="playFlashcardAudio('${term.audio}', event)">🔊 Listen</button>` : ''}
              ${term.strongs ? `<div class="flashcard-strongs">${term.strongs}</div>` : ''}
            </div>
          </div>
        </div>
        <div class="flashcard-controls">
          <button class="flashcard-prev" ${this.currentIndex === 0 ? 'disabled' : ''}>&#8592; Prev</button>
          <span class="flashcard-counter">${this.currentIndex + 1} / ${this.terms.length}</span>
          <button class="flashcard-next" ${this.currentIndex === this.terms.length - 1 ? 'disabled' : ''}>Next &#8594;</button>
        </div>
        <div class="flashcard-actions">
          <button class="flashcard-shuffle">Shuffle</button>
          <button class="flashcard-reset">Reset Order</button>
        </div>
        <p class="flashcard-hint">Click the card to flip</p>
      </div>
    `;
  }

  bindEvents() {
    const card = this.container.querySelector('.flashcard');
    const prevBtn = this.container.querySelector('.flashcard-prev');
    const nextBtn = this.container.querySelector('.flashcard-next');
    const shuffleBtn = this.container.querySelector('.flashcard-shuffle');
    const resetBtn = this.container.querySelector('.flashcard-reset');

    if (card) card.addEventListener('click', () => this.flip());
    if (prevBtn) prevBtn.addEventListener('click', () => this.prev());
    if (nextBtn) nextBtn.addEventListener('click', () => this.next());
    if (shuffleBtn) shuffleBtn.addEventListener('click', () => this.shuffle());
    if (resetBtn) resetBtn.addEventListener('click', () => this.reset());

    // Keyboard navigation
    document.addEventListener('keydown', (e) => {
      // Only respond if this container is visible
      if (!this.container.offsetParent) return;

      if (e.key === 'ArrowLeft') this.prev();
      else if (e.key === 'ArrowRight') this.next();
      else if (e.key === ' ' || e.key === 'Enter') {
        e.preventDefault();
        this.flip();
      }
    });
  }
}

let currentFlashcardAudio = null;

function playFlashcardAudio(url, event) {
  if (event) {
    event.preventDefault();
    event.stopPropagation();
  }

  if (currentFlashcardAudio) {
    currentFlashcardAudio.pause();
    currentFlashcardAudio = null;
  }

  currentFlashcardAudio = new Audio(url);
  currentFlashcardAudio.play().catch(err => console.error('Failed to play flashcard audio:', err));
}

// Initialize flashcards from JSON data
function initFlashcards(containerId, sectionKey) {
  fetch('/data/cfm-glossary.json')
    .then(response => response.json())
    .then(data => {
      const section = data.weeks[sectionKey];
      if (section && section.terms) {
        new Flashcards(containerId, section.terms);
      }
    })
    .catch(err => console.error('Failed to load flashcard data:', err));
}
