/* Brand page: results slider (4 at a time, Previous / Next / Pause, 5 s autoplay, reduced motion) and coaches paging (6 per page on desktop, swipe on phones). */
(function () {
  'use strict';
  var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  // ---- Results ----
  var cards = Array.prototype.slice.call(document.querySelectorAll('#mockResults .rcard'));
  if (cards.length) {
    var cur = 0, count = document.getElementById('mockCount'), btn = document.getElementById('resultsAutoplay'), sec = document.getElementById('results'), play = !reduce;
    var show = function () {
      cards.forEach(function (c, i) { var pos = (i - cur + cards.length) % cards.length; c.hidden = pos >= 4; c.style.order = pos; });
      count.textContent = (cur + 1) + ' / ' + cards.length;
    };
    var move = function (d) { cur = (cur + d + cards.length) % cards.length; show(); };
    var ui = function () { btn.textContent = play ? 'Pause slideshow' : 'Play slideshow'; btn.setAttribute('aria-pressed', String(!play)); count.setAttribute('aria-live', play ? 'off' : 'polite'); };
    document.getElementById('mockPrev').addEventListener('click', function () { move(-1); });
    document.getElementById('mockNext').addEventListener('click', function () { move(1); });
    btn.addEventListener('click', function () { play = !play; ui(); });
    window.setInterval(function () {
      if (play && !document.hidden && !sec.matches(':hover') && (document.activeElement === btn || !sec.contains(document.activeElement))) move(1);
    }, 5000);
    show(); ui();
  }

  // ---- Coaches ----
  var tsec = document.getElementById('trainers');
  if (tsec) {
    var track = tsec.querySelector('.track'), tc = Array.prototype.slice.call(track.children), prev = tsec.querySelector('[data-dir="-1"]'), next = tsec.querySelector('[data-dir="1"]'), lab = tsec.querySelector('.cpage');
    var mq = window.matchMedia('(min-width:700px)'), page = 0, PER = 6, pages = Math.ceil(tc.length / PER);
    var render = function () {
      if (mq.matches) {
        tc.forEach(function (c, i) { c.hidden = Math.floor(i / PER) !== page; });
        prev.disabled = page === 0; next.disabled = page >= pages - 1; if (lab) lab.textContent = (page + 1) + ' / ' + pages;
      } else { tc.forEach(function (c) { c.hidden = false; }); prev.disabled = false; next.disabled = false; }
    };
    var go = function (d) {
      if (mq.matches) { page = Math.max(0, Math.min(pages - 1, page + d)); render(); }
      else { track.scrollBy({ left: d * (tc[0].getBoundingClientRect().width + 20), behavior: reduce ? 'auto' : 'smooth' }); }
    };
    prev.addEventListener('click', function () { go(-1); }); next.addEventListener('click', function () { go(1); });
    if (mq.addEventListener) mq.addEventListener('change', render); else mq.addListener(render);
    render();
  }
})();

(function(){var v=document.getElementById('ffVideo');if(!v)return;var b=v.querySelector('.vid-play');if(!b)return;
b.addEventListener('click',function(){var f=document.createElement('iframe');f.src='https://www.youtube-nocookie.com/embed/'+v.getAttribute('data-yt')+'?autoplay=1&rel=0';f.title='Formula Fitness video';f.allow='autoplay; encrypted-media; picture-in-picture; fullscreen';f.allowFullscreen=true;v.replaceChild(f,b);f.focus();});})();

(function(){var box=document.getElementById('heroVideo');if(!box)return;var v=box.querySelector('video'),btn=box.querySelector('.hv-play');if(!v||!btn)return;
v.controls=false;btn.hidden=false;
btn.addEventListener('click',function(){btn.hidden=true;v.controls=true;v.play().catch(function(){});v.focus();});
v.addEventListener('play',function(){btn.hidden=true;v.controls=true;});
v.addEventListener('ended',function(){btn.hidden=false;v.controls=false;});
})();
