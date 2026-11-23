/* Formula Fitness Brand landing page: event tracking and campaign-attribution passthrough.
 *
 * This file only pushes events to window.dataLayer (picked up by Google Tag Manager, container GTM-K28JZ7N).
 * It never talks to Google Ads directly: connect whichever conversion action is approved in GTM by using the
 * event names below as triggers. To change names or settings, define window.FF_TRACKING_CONFIG BEFORE this file loads.
 *
 * Four SEPARATE events:
 *   consultation_cta_click  any "Book a Consultation Call" button (data-booking-cta)         - NOT a conversion
 *   booking_started         first interaction with the booking calendar (see note)             - NOT a conversion
 *   booking_completed       only on the booking-confirmation page, once per booking reference  - the conversion candidate
 *   phone_click             any tel: link (header / location / footer). The dialled number is
 *                           whatever the GHL number pool swapped in, so it is sent as phone_number.
 */
(function () {
  'use strict';
  var user = window.FF_TRACKING_CONFIG || {};
  var CFG = {
    variant: 'brand',
    events: { cta: 'consultation_cta_click', started: 'booking_started', completed: 'booking_completed', phone: 'phone_click' },
    confirmationPath: '/booking-confirmed/',     // where GHL redirects after a successful booking
    confirmationParam: 'booking_ref',            // query parameter that must carry a booking/appointment reference
    storageKey: 'ff_booking_completed',          // remembers references already counted (blocks refresh/repeat counts)
    attrKeys: ['utm_source', 'utm_medium', 'utm_campaign', 'utm_term', 'utm_content', 'gclid', 'gbraid', 'wbraid', 'msclkid'],
    debug: false
  };
  Object.keys(user).forEach(function (k) {
    if (k === 'events') Object.keys(user.events || {}).forEach(function (e) { CFG.events[e] = user.events[e]; });
    else CFG[k] = user[k];
  });

  window.dataLayer = window.dataLayer || [];
  function push(obj) {
    obj.page_variant = CFG.variant;
    var a = getAttr();
    ['utm_source', 'utm_medium', 'utm_campaign'].forEach(function (k) { if (a[k]) obj[k] = a[k]; });
    obj.has_click_id = !!(a.gclid || a.gbraid || a.wbraid);
    window.dataLayer.push(obj);
    if (CFG.debug && window.console) console.log('[ff-tracking]', obj);
  }

  /* ---------- storage helpers (never throw) ---------- */
  function sGet(store, k) { try { return window[store].getItem(k); } catch (e) { return null; } }
  function sSet(store, k, v) { try { window[store].setItem(k, v); } catch (e) {} }

  /* ---------- campaign attribution: capture once, reuse everywhere ---------- */
  function getAttr() {
    var out = {}, i, k, q = new URLSearchParams(window.location.search), found = false;
    for (i = 0; i < CFG.attrKeys.length; i++) { k = CFG.attrKeys[i]; if (q.get(k)) { out[k] = q.get(k); found = true; } }
    if (found) { sSet('sessionStorage', 'ff_attr', JSON.stringify(out)); return out; }
    try { return JSON.parse(sGet('sessionStorage', 'ff_attr') || '{}') || {}; } catch (e) { return {}; }
  }
  function withAttr(url) {
    var a = getAttr(), u;
    try { u = new URL(url, window.location.href); } catch (e) { return url; }
    Object.keys(a).forEach(function (k) { if (!u.searchParams.has(k)) u.searchParams.set(k, a[k]); });
    return u.toString();
  }

  /* ---------- booking_completed with duplicate protection ---------- */
  function completed() { try { return JSON.parse(sGet('localStorage', CFG.storageKey) || '[]'); } catch (e) { return []; } }
  function validRef(r) { return typeof r === 'string' && /^[A-Za-z0-9_\-]{4,100}$/.test(r); }
  function completeBooking(ref) {
    if (!validRef(ref)) return false;               // no reference = no conversion (blocks direct visits)
    var done = completed();
    if (done.indexOf(ref) !== -1) return false;     // same booking already counted (refresh, back button, repeat)
    done.push(ref); sSet('localStorage', CFG.storageKey, JSON.stringify(done.slice(-50)));
    push({ event: CFG.events.completed, booking_ref: ref });
    return true;
  }

  var onConfirmation = window.location.pathname.indexOf(CFG.confirmationPath) === 0;
  if (onConfirmation) {
    var ref = new URLSearchParams(window.location.search).get(CFG.confirmationParam);
    if (window.top !== window) {
      // GHL redirected INSIDE the booking iframe: hand the reference to the parent page (same origin) to record.
      if (validRef(ref)) { try { window.parent.postMessage({ type: 'ff_booking_confirmed', ref: ref }, window.location.origin); } catch (e) {} }
    } else {
      completeBooking(ref);
    }
  }
  window.addEventListener('message', function (e) {
    if (e.origin !== window.location.origin) return;
    var d = e.data;
    if (d && d.type === 'ff_booking_confirmed') completeBooking(d.ref);
  });

  /* ---------- DOM wiring (main page only) ---------- */
  function ready(fn) { if (document.readyState !== 'loading') fn(); else document.addEventListener('DOMContentLoaded', fn); }
  ready(function () {
    var frame = document.getElementById('bookingCalendar');
    if (frame && frame.getAttribute('data-src')) frame.src = withAttr(frame.getAttribute('data-src'));
    Array.prototype.forEach.call(document.querySelectorAll('a[data-carry-attr]'), function (a) { a.href = withAttr(a.href); });

    document.addEventListener('click', function (e) {
      var cta = e.target.closest && e.target.closest('[data-booking-cta]');
      if (cta) push({ event: CFG.events.cta, cta_location: cta.getAttribute('data-booking-cta'), cta_text: (cta.getAttribute('aria-label') || cta.textContent).trim() });
      var tel = e.target.closest && e.target.closest('a[href^="tel:"]');
      if (tel) push({ event: CFG.events.phone, phone_location: tel.getAttribute('data-phone') || 'other', phone_number: tel.textContent.trim(), phone_href: tel.getAttribute('href') });
    }, true);

    // booking_started: the calendar is a cross-origin iframe, so the page cannot see inside it. The first click or tap on the
    // calendar moves focus into the iframe (the window "blurs"); that is used as the "started" signal, once per page view.
    var startedSent = false;
    window.addEventListener('blur', function () {
      if (startedSent || !frame) return;
      window.setTimeout(function () {
        if (!startedSent && document.activeElement === frame) { startedSent = true; push({ event: CFG.events.started, trigger: 'calendar_interaction' }); }
      }, 0);
    });
  });

  window.FFTracking = { config: CFG, completeBooking: completeBooking, withAttr: withAttr };
})();
