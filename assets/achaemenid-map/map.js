/* Dependency-free, progressively enhanced map. Content is compiled locally by Hugo. */
(function () {
  'use strict';
  function init(root) {
    if (root.dataset.amReady) return;
    const dialog = root.querySelector('.am-dialog');
    if (!dialog || typeof dialog.showModal !== 'function') return;
    const content = root.querySelector('.am-dialog-content');
    const inline = root.querySelector('.am-inline');
    const choices = Array.from(root.querySelectorAll('[data-am-site]'));
    const entries = new Map(Array.from(root.querySelectorAll('[data-am-excerpt]')).map(e => [e.dataset.amExcerpt, e]));
    let opener = null;
    // Resolve overlapping circle targets using actual SVG coordinates. Labels,
    // keyboard activation and the location list retain their explicit IDs.
    function pointerChoice(event, trigger) {
      if (event.detail === 0 || !trigger.classList.contains('am-map-pin') ||
          !event.target || event.target.localName !== 'circle') return trigger;
      let nearest = trigger, distance = Infinity;
      choices.forEach(choice => {
        if (!choice.classList.contains('am-map-pin')) return;
        const hit = choice.querySelector('circle.am-hit');
        if (!hit) return;
        try {
          const svg = hit.ownerSVGElement;
          const matrix = hit.getScreenCTM();
          if (!svg || !matrix) return;
          const center = svg.createSVGPoint();
          center.x = Number(hit.getAttribute('cx'));
          center.y = Number(hit.getAttribute('cy'));
          const screen = center.matrixTransform(matrix);
          const dx = event.clientX - screen.x;
          const dy = event.clientY - screen.y;
          const squared = dx * dx + dy * dy;
          if (squared < distance) { nearest = choice; distance = squared; }
        } catch (_) { /* Keep the explicit target if geometry is unavailable. */ }
      });
      return nearest;
    }
    function clearEntryPopup() {
      dialog.dispatchEvent(new Event('am:entry-changing', {bubbles:true}));
    }
    function deactivate() {
      choices.forEach(e => { e.classList.remove('is-selected'); e.removeAttribute('aria-current'); });
    }
    function restoreFocus() { if (opener && opener.isConnected) opener.focus({preventScroll:true}); }
    function close() {
      clearEntryPopup();
      inline.hidden = true;
      if (dialog.open) dialog.close();
      else restoreFocus();
    }
    function open(id, trigger) {
      const entry = entries.get(id);
      if (!entry) return;
      clearEntryPopup();
      opener = trigger;
      deactivate();
      choices.filter(e => e.dataset.amSite === id).forEach(e => { e.classList.add('is-selected'); e.setAttribute('aria-current','location'); });
      const clone = entry.querySelector('[data-am-content]').cloneNode(true);
      // Only the selected card loads its photograph, keeping the initial map light.
      clone.querySelectorAll('img[data-am-src]').forEach(img => { img.src = img.dataset.amSrc; });
      clone.querySelector('[data-am-title]').id = dialog.getAttribute('aria-labelledby');
      if (root.dataset.amMode === 'inline') {
        content.replaceChildren();
        if (dialog.open) dialog.close();
        inline.replaceChildren(clone);
        inline.hidden = false;
        inline.scrollIntoView({block:'nearest', behavior:'auto'});
        inline.focus({preventScroll:true});
      } else {
        inline.hidden = true;
        inline.replaceChildren();
        content.replaceChildren(clone);
        if (!dialog.open) dialog.showModal();
        root.querySelector('[data-am-close]').focus({preventScroll:true});
        root.querySelector('.am-dialog-scroll').scrollTop = 0;
      }
    }
    choices.forEach(trigger => {
      trigger.setAttribute('aria-haspopup','dialog');
      trigger.addEventListener('click', e => {
        if (e.metaKey || e.ctrlKey || e.shiftKey || e.altKey) return;
        const selected = pointerChoice(e, trigger);
        e.preventDefault(); open(selected.dataset.amSite, selected);
      });
      trigger.addEventListener('keydown', e => {
        if (e.key === ' ') { e.preventDefault(); open(trigger.dataset.amSite, trigger); }
      });
    });
    root.querySelector('[data-am-close]').addEventListener('click',close);
    dialog.addEventListener('close',restoreFocus);
    // Native Escape handling closes the modal and fires "close"; no custom focus trap.
    root.querySelector('[data-am-zoom]').addEventListener('click',function () {
      const on = this.getAttribute('aria-pressed') !== 'true';
      this.setAttribute('aria-pressed',String(on));
      this.textContent = on ? 'Fit map' : 'Enlarge map';
      root.classList.toggle('am-enlarged',on);
    });
    root.querySelector('[data-am-extent]').addEventListener('click',function () {
      const on = this.getAttribute('aria-pressed') !== 'true';
      this.setAttribute('aria-pressed',String(on));
      root.querySelectorAll('[id$="-empire-overlay"], [id$="-muted-terrain"]').forEach(e => e.style.display = on ? '' : 'none');
    });
    // The private fixture may request the inline alternative, without changing production UI.
    root.addEventListener('am:mode',e => {
      close(); root.dataset.amMode = e.detail === 'inline' ? 'inline' : 'popup';
      choices.forEach(x => x.setAttribute('aria-haspopup', root.dataset.amMode === 'inline' ? 'false' : 'dialog'));
    });
    root.querySelector('.am-tools').hidden = false;
    root.querySelector('.am-excerpts').hidden = true;
    root.dataset.amReady = 'true';
  }
  function start() { document.querySelectorAll('[data-am-widget]').forEach(init); }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded',start,{once:true});
  else start();
}());
