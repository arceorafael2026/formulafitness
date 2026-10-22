// Formula Fitness page: mobile menu, carousels, shared consultation modal.
// No tracking, no form submission and no conversion logic lives here.
(function () {
  'use strict';
  var $ = function (s, c) { return (c || document).querySelector(s); };
  var $$ = function (s, c) { return Array.prototype.slice.call((c || document).querySelectorAll(s)); };
  var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  // ---------- Mobile menu ----------
  var mb = $('.menu-btn'), nav = $('#site-nav');
  function setMenu(o) { mb.setAttribute('aria-expanded', String(o)); nav.classList.toggle('open', o); }
  mb.addEventListener('click', function () { setMenu(mb.getAttribute('aria-expanded') !== 'true'); });
  $$('#site-nav a').forEach(function (a) { a.addEventListener('click', function () { setMenu(false); }); });
  document.addEventListener('keydown', function (e) { if (e.key === 'Escape') setMenu(false); });

  // ---------- Carousels ----------
  // One step = exact distance between the left edges of two neighbouring cards (card width + gap).
  $$('[data-carousel]').forEach(function (c) {
    var t = $('.track', c), prev = $('[data-dir="-1"]', c), next = $('[data-dir="1"]', c), raf = 0;
    function step() {
      var k = t.children;
      if (k.length < 2) return t.clientWidth;
      return k[1].getBoundingClientRect().left - k[0].getBoundingClientRect().left;
    }
    function setDisabled(b, d) {
      if (b.disabled === d) return;
      if (d && document.activeElement === b) { // never strand keyboard focus on a button that just disabled itself
        var other = b === prev ? next : prev;
        (other.disabled ? t : other).focus();
      }
      b.disabled = d;
    }
    function update() {
      raf = 0;
      var max = t.scrollWidth - t.clientWidth;
      setDisabled(prev, t.scrollLeft <= 1);
      setDisabled(next, t.scrollLeft >= max - 1);
    }
    function queue() { if (!raf) raf = requestAnimationFrame(update); }
    function go(dir) {
      var s = step(), max = t.scrollWidth - t.clientWidth;
      var idx = Math.round(t.scrollLeft / s) + dir;
      var left = Math.max(0, Math.min(idx * s, max));
      t.scrollTo({ left: left, behavior: reduce ? 'auto' : 'smooth' });
    }
    prev.addEventListener('click', function () { go(-1); });
    next.addEventListener('click', function () { go(1); });
    t.addEventListener('scroll', queue, { passive: true });
    t.addEventListener('keydown', function (e) {
      if (e.target !== t) return;
      if (e.key === 'ArrowRight') { e.preventDefault(); go(1); }
      else if (e.key === 'ArrowLeft') { e.preventDefault(); go(-1); }
    });
    window.addEventListener('resize', queue);
    if (window.ResizeObserver) new ResizeObserver(queue).observe(t);
    update();
  });

  // ---------- Consultation modal (one shared native <dialog>) ----------
  // Native <dialog> gives Escape, a focus trap and an inert page behind it.
  // The GHL iframe is given its src once, on first open. It is never reloaded afterwards, so typed data survives close/reopen.
  var dlg = $('#form-modal');
  var TIMEOUT_MS = 15000;
  var last = null;

  if (dlg && typeof dlg.showModal === 'function') {
    var frame = $('iframe', dlg), status = $('#form-status'), stext = $('#form-status-text'),
        retry = $('#form-retry'), closeBtn = $('.modal-close', dlg), timer = 0;

    var startLoad = function () {
      clearTimeout(timer);
      stext.textContent = 'Loading the form…';
      retry.hidden = true;
      status.hidden = false;
      frame.src = frame.getAttribute('data-src');
      // A load event fires for any document, including an error page, so it is NOT proof the form works.
      // That is why the "Open it in a new tab" link in the modal footer is always visible.
      timer = setTimeout(function () {
        stext.textContent = 'The form is taking longer than expected to load. You can wait, try again, or use the "Open it in a new tab" link below.';
        retry.hidden = false;
      }, TIMEOUT_MS);
    };

    frame.addEventListener('load', function () {
      if (!frame.getAttribute('src')) return; // ignore the empty initial document
      clearTimeout(timer);
      status.hidden = true; // only hides the spinner; no claim is made that the form rendered
    });
    retry.addEventListener('click', startLoad);

    $$('[data-open-form]').forEach(function (el) {
      el.addEventListener('click', function (e) {
        e.preventDefault(); // otherwise the link opens the form URL in a new tab (no-JS / old-browser fallback)
        last = el;
        if (!frame.getAttribute('src')) startLoad();
        document.body.classList.add('lock');
        dlg.showModal();
        closeBtn.focus();
      });
    });

    closeBtn.addEventListener('click', function () { dlg.close(); });
    dlg.addEventListener('click', function (e) { if (e.target === dlg) dlg.close(); });
    dlg.addEventListener('close', function () {
      document.body.classList.remove('lock');
      if (last) last.focus();
    });
  }
})();
