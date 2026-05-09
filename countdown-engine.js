/* ═══════════════════════════════════════════════════════════════
   COUNTDOWN ENGINE — countdowns.site
   Shared logic for hub + individual countdown pages
═══════════════════════════════════════════════════════════════ */
(function () {
  'use strict';

  /* ─── FULL MOON DATES (UTC, ±12h) ──────────────────────────── */
  var FULL_MOONS = [
    '2026-01-03T22:03Z','2026-02-01T22:09Z','2026-03-03T14:38Z',
    '2026-04-02T04:12Z','2026-05-01T14:23Z','2026-05-31T00:45Z',
    '2026-06-29T11:57Z','2026-07-29T01:36Z','2026-08-27T17:25Z',
    '2026-09-26T11:49Z','2026-10-26T08:12Z','2026-11-25T05:53Z',
    '2026-12-25T02:28Z','2027-01-23T22:17Z','2027-02-22T16:23Z',
    '2027-03-24T08:35Z','2027-04-22T22:35Z','2027-05-22T10:05Z',
    '2027-06-20T19:58Z','2027-07-20T05:02Z','2027-08-18T14:30Z',
    '2027-09-17T01:05Z','2027-10-16T13:15Z','2027-11-15T02:00Z',
    '2027-12-15T16:00Z',
  ].map(function (s) { return new Date(s); });

  /* ─── HELPERS ───────────────────────────────────────────────── */
  function nthWeekday(year, month, n, weekday) {
    var d = new Date(year, month, 1);
    var offset = (weekday - d.getDay() + 7) % 7;
    return new Date(year, month, 1 + offset + (n - 1) * 7);
  }

  function lastWeekday(year, month, weekday) {
    var d = new Date(year, month + 1, 0); /* last day of month */
    var offset = (d.getDay() - weekday + 7) % 7;
    return new Date(year, month, d.getDate() - offset);
  }

  function nextOccurrence(getForYear) {
    var now = new Date();
    var y = now.getFullYear();
    var d = getForYear(y);
    if (d <= now) d = getForYear(y + 1);
    return d;
  }

  function nextFullMoon() {
    var now = new Date();
    for (var i = 0; i < FULL_MOONS.length; i++) {
      if (FULL_MOONS[i] > now) return FULL_MOONS[i];
    }
    return null;
  }

  /* Easter — Meeus/Jones/Butcher algorithm */
  function easterDate(y) {
    var a = y % 19, b = Math.floor(y / 100), c = y % 100;
    var d = Math.floor(b / 4), e = b % 4;
    var f = Math.floor((b + 8) / 25);
    var g = Math.floor((b - f + 1) / 3);
    var h = (19 * a + b - d - g + 15) % 30;
    var i = Math.floor(c / 4), k = c % 4;
    var l = (32 + 2 * e + 2 * i - h - k) % 7;
    var m = Math.floor((a + 11 * h + 22 * l) / 451);
    var month = Math.floor((h + l - 7 * m + 114) / 31) - 1;
    var day   = ((h + l - 7 * m + 114) % 31) + 1;
    return new Date(y, month, day);
  }

  /* ─── AUTO DATE GETTERS ─────────────────────────────────────── */
  var AUTO = {
    /* ── Holidays ── */
    'christmas':        function () { return { date: nextOccurrence(function (y) { return new Date(y, 11, 25); }) }; },
    'new-year':         function () { return { date: nextOccurrence(function (y) { return new Date(y + 1, 0, 1); }) }; },
    'halloween':        function () { return { date: nextOccurrence(function (y) { return new Date(y, 9, 31); }) }; },
    'valentines':       function () { return { date: nextOccurrence(function (y) { return new Date(y, 1, 14); }) }; },
    'easter':           function () { return { date: nextOccurrence(easterDate) }; },
    'st-patricks':      function () { return { date: nextOccurrence(function (y) { return new Date(y, 2, 17); }) }; },
    'dia-de-los-muertos': function () { return { date: nextOccurrence(function (y) { return new Date(y, 10, 1); }) }; },
    'cinco-de-mayo':    function () { return { date: nextOccurrence(function (y) { return new Date(y, 4, 5); }) }; },
    'fiestas-patrias':  function () { return { date: nextOccurrence(function (y) { return new Date(y, 8, 18); }) }; },
    'bastille-day':     function () { return { date: nextOccurrence(function (y) { return new Date(y, 6, 14); }) }; },
    'oktoberfest':      function () { return { date: nextOccurrence(function (y) { return new Date(y, 8, 19); }) }; },

    /* ── US Holidays ── */
    'thanksgiving':     function () { return { date: nextOccurrence(function (y) { return nthWeekday(y, 10, 4, 4); }) }; },
    'independence-day': function () { return { date: nextOccurrence(function (y) { return new Date(y, 6, 4); }) }; },
    'memorial-day':     function () { return { date: nextOccurrence(function (y) { return lastWeekday(y, 4, 1); }) }; },
    'labor-day':        function () { return { date: nextOccurrence(function (y) { return nthWeekday(y, 8, 1, 1); }) }; },
    'mothers-day': function () {
      var country = (typeof localStorage !== 'undefined' ? localStorage.getItem('cd_country') : null) || 'global';
      var getDate;
      if (country === 'AR' || country === 'UY') {
        getDate = function (y) { return nthWeekday(y, 9, 3, 0); };   /* 3rd Sun Oct */
      } else if (['MX','DO','GT','HN','SV','NI','CO','EC','PE','VE','BO','CU','PR'].indexOf(country) >= 0) {
        getDate = function (y) { return new Date(y, 4, 10); };        /* May 10 */
      } else if (country === 'FR') {
        getDate = function (y) { return lastWeekday(y, 4, 0); };      /* Last Sun May */
      } else {
        getDate = function (y) { return nthWeekday(y, 4, 2, 0); };   /* 2nd Sun May (US/UK/CA/AU) */
      }
      return { date: nextOccurrence(getDate) };
    },
    'fathers-day': function () {
      var country = (typeof localStorage !== 'undefined' ? localStorage.getItem('cd_country') : null) || 'global';
      var getDate;
      if (country === 'ES') {
        getDate = function (y) { return new Date(y, 2, 19); };         /* March 19 (San José) */
      } else if (country === 'BR') {
        getDate = function (y) { return nthWeekday(y, 7, 2, 0); };    /* 2nd Sun Aug */
      } else {
        getDate = function (y) { return nthWeekday(y, 5, 3, 0); };    /* 3rd Sun Jun */
      }
      return { date: nextOccurrence(getDate) };
    },

    /* ── Sports (recurring) ── */
    'super-bowl':       function () { return { date: nextOccurrence(function (y) { return nthWeekday(y, 1, 2, 0); }), note: '2nd Sunday of February' }; },
    'oscars':           function () { return { date: nextOccurrence(function (y) { return nthWeekday(y, 1, 4, 0); }), note: '~Last Sunday of February (estimated)' }; },
    'met-gala':         function () { return { date: nextOccurrence(function (y) { return nthWeekday(y, 4, 1, 1); }) }; },

    /* ── Sales ── */
    'black-friday':     function () { return { date: nextOccurrence(function (y) { return nthWeekday(y, 10, 4, 5); }) }; },
    'cyber-monday':     function () {
      return {
        date: nextOccurrence(function (y) {
          var bf = nthWeekday(y, 10, 4, 5);
          return new Date(bf.getFullYear(), bf.getMonth(), bf.getDate() + 3);
        }),
        note: 'Monday after Black Friday'
      };
    },

    /* ── Nature ── */
    'full-moon':        function () { return { date: nextFullMoon(), note: 'Approximate date (±12 hours)' }; },

    /* ── Next weekend ── */
    'weekend':          function () {
      var now = new Date(), day = now.getDay();
      var dts = (6 - day + 7) % 7 || 7;
      var d = new Date(now);
      d.setDate(d.getDate() + dts); d.setHours(0, 0, 0, 0);
      return { date: d };
    },

    /* ── Latin American Holidays ── */
    '25-de-mayo':       function () { return { date: nextOccurrence(function (y) { return new Date(y, 4, 25); }) }; },
    'dia-del-nino': function () {
      var country = (typeof localStorage !== 'undefined' ? localStorage.getItem('cd_country') : null) || 'global';
      var m, d;
      if      (country === 'MX') { m = 3;  d = 30; }  /* Apr 30 */
      else if (country === 'AR') { m = 7;  d = 9;  }  /* Aug 9  */
      else if (country === 'BR') { m = 9;  d = 12; }  /* Oct 12 */
      else                       { m = 10; d = 20; }  /* Nov 20 (UN) */
      return { date: nextOccurrence(function (y) { return new Date(y, m, d); }) };
    },

    /* ── One-time political ── */
    'elecciones-ar':    function () { return { date: new Date(2027, 9, 26, 8, 0, 0), note: 'Estimated date. Argentine general elections 2027.' }; },

    /* ── LA 2028 Olympics ── */
    'olympics-2028':    function () { return { date: new Date(2028, 6, 14, 20, 0, 0), note: 'Los Angeles 2028 — Opening Ceremony' }; },
  };

  /* ─── DATA CACHE ────────────────────────────────────────────── */
  var _cache = null;
  var _pending = [];

  function loadData(cb) {
    if (_cache !== null) { cb(_cache); return; }
    _pending.push(cb);
    if (_pending.length > 1) return;
    fetch('/countdowns-data.json?_=' + Math.floor(Date.now() / 60000))
      .then(function (r) { return r.json(); })
      .then(function (d) {
        _cache = d;
        _pending.forEach(function (fn) { fn(_cache); });
        _pending = [];
      })
      .catch(function () {
        _cache = {};
        _pending.forEach(function (fn) { fn(_cache); });
        _pending = [];
      });
  }

  /* ─── FORMATTING ────────────────────────────────────────────── */
  function pad(n) { return n < 10 ? '0' + n : '' + n; }

  function fmtDate(d, lang) {
    var locale = lang === 'es' ? 'es' : lang === 'pt' ? 'pt-BR' : lang === 'fr' ? 'fr' : lang === 'de' ? 'de' : 'en-US';
    return d.toLocaleDateString(locale, { weekday: 'long', year: 'numeric', month: 'long', day: 'numeric' });
  }

  function daysUntil(d) {
    return Math.ceil((d - new Date()) / 86400000);
  }

  /* ─── TICKER ────────────────────────────────────────────────── */
  var _tickerHandle = null;

  function startTicker(targetDate) {
    if (_tickerHandle) { clearInterval(_tickerHandle); _tickerHandle = null; }
    function tick() {
      var diff = targetDate - new Date();
      if (diff <= 0) { location.reload(); return; }
      var days  = Math.floor(diff / 86400000);
      var hours = Math.floor((diff % 86400000) / 3600000);
      var mins  = Math.floor((diff % 3600000) / 60000);
      var secs  = Math.floor((diff % 60000) / 1000);
      var dEl = document.getElementById('cd-d');
      var hEl = document.getElementById('cd-h');
      var mEl = document.getElementById('cd-m');
      var sEl = document.getElementById('cd-s');
      if (dEl) dEl.textContent = days;
      if (hEl) hEl.textContent = pad(hours);
      if (mEl) mEl.textContent = pad(mins);
      if (sEl) sEl.textContent = pad(secs);
    }
    tick();
    _tickerHandle = setInterval(tick, 1000);
  }

  /* ─── CATEGORY COLORS ───────────────────────────────────────── */
  var CAT_COLORS = {
    'Releases':      { color: '#C084FC', glow: 'rgba(192,132,252,.25)', soft: 'rgba(192,132,252,.1)' },
    'Sports':        { color: '#FB923C', glow: 'rgba(251,146,60,.25)',  soft: 'rgba(251,146,60,.1)'  },
    'Holidays':      { color: '#4ADE80', glow: 'rgba(74,222,128,.2)',   soft: 'rgba(74,222,128,.08)' },
    'Entertainment': { color: '#FBBF24', glow: 'rgba(251,191,36,.2)',   soft: 'rgba(251,191,36,.08)' },
    'Sales':         { color: '#60A5FA', glow: 'rgba(96,165,250,.2)',   soft: 'rgba(96,165,250,.08)' },
    'Nature':        { color: '#22D3EE', glow: 'rgba(34,211,238,.2)',   soft: 'rgba(34,211,238,.08)' },
    'Music':         { color: '#F472B6', glow: 'rgba(244,114,182,.2)',  soft: 'rgba(244,114,182,.08)'},
    'Politics':      { color: '#94A3B8', glow: 'rgba(148,163,184,.2)',  soft: 'rgba(148,163,184,.08)'},
    'Fashion':       { color: '#FDA4AF', glow: 'rgba(253,164,175,.2)',  soft: 'rgba(253,164,175,.08)'},
    'Technology':    { color: '#34D399', glow: 'rgba(52,211,153,.2)',   soft: 'rgba(52,211,153,.08)' },
  };

  function catColors(cat) {
    return CAT_COLORS[cat] || { color: '#818CF8', glow: 'rgba(129,140,248,.2)', soft: 'rgba(129,140,248,.08)' };
  }

  /* ─── HTML BUILDER (individual pages) ──────────────────────── */
  function buildCountdownSection(targetDate, isPast, isUnknown, note) {
    if (isUnknown) {
      return '<div class="cd-unknown"><div class="cd-unknown-text">Date to be confirmed</div>' +
             (note ? '<div class="cd-unknown-sub">' + note + '</div>' : '') + '</div>';
    }
    if (isPast) {
      return '<div class="cd-past"><div class="cd-past-badge">Already happened</div>' +
             '<div class="cd-past-date">' + fmtDate(targetDate, 'en') + '</div></div>';
    }
    return [
      '<div class="cd-grid">',
      '<div class="cd-box"><div class="cd-num" id="cd-d">—</div><div class="cd-lbl">days</div></div>',
      '<div class="cd-sep">:</div>',
      '<div class="cd-box"><div class="cd-num" id="cd-h">—</div><div class="cd-lbl">hours</div></div>',
      '<div class="cd-sep">:</div>',
      '<div class="cd-box"><div class="cd-num" id="cd-m">—</div><div class="cd-lbl">min</div></div>',
      '<div class="cd-sep">:</div>',
      '<div class="cd-box"><div class="cd-num" id="cd-s">—</div><div class="cd-lbl">sec</div></div>',
      '</div>',
      '<div class="cd-date-label">' + fmtDate(targetDate, 'en') + '</div>',
    ].join('');
  }

  function buildPage(config, targetDate, extra, isPast, isUnknown) {
    var cc = catColors(config.category);
    var note     = (extra && extra.note) || config.note || '';
    var subtitle = (extra && extra.subtitle) || '';
    var cdSection = buildCountdownSection(targetDate, isPast, isUnknown, note);

    var articleHTML = '';
    if (config.content || (config.faqs && config.faqs.length)) {
      articleHTML += '<div class="cd-article">';
      if (config.content) articleHTML += '<p class="cd-article-body">' + config.content + '</p>';
      if (config.faqs && config.faqs.length) {
        articleHTML += '<div class="cd-faq"><h2 class="cd-faq-title">Frequently asked questions</h2>';
        config.faqs.forEach(function (faq) {
          articleHTML += '<div class="cd-faq-item"><h3 class="cd-faq-q">' + faq.q + '</h3><p class="cd-faq-a">' + faq.a + '</p></div>';
        });
        articleHTML += '</div>';
      }
      articleHTML += '</div>';
    }

    return [
      '<div class="cd-page">',
      '<div class="cd-hero" style="--cat:' + cc.color + ';--cat-glow:' + cc.glow + ';--cat-soft:' + cc.soft + '">',
      '<div class="cd-breadcrumb"><a href="/">countdowns.site</a><span>/</span><a href="/#' + (config.category || '').toLowerCase() + '">' + (config.category || '') + '</a><span>/</span><span>' + config.name + '</span></div>',
      '<div class="cd-badge">' + config.category + '</div>',
      '<h1 class="cd-title">' + config.name + '</h1>',
      subtitle ? '<div class="cd-subtitle">' + subtitle + '</div>' : '',
      '<p class="cd-desc">' + (config.description || '') + '</p>',
      cdSection,
      '</div>',
      '<div class="cd-below">',
      (note && !isUnknown) ? '<div class="cd-note-card">' + note + '</div>' : '',
      '<a href="/" class="cd-back-link">← All countdowns</a>',
      '</div>',
      articleHTML,
      '</div>',
    ].join('\n');
  }

  /* ─── PUBLIC API ────────────────────────────────────────────── */
  window.CountdownEngine = {

    render: function (rootId, config) {
      var root = document.getElementById(rootId);
      if (!root) return;

      function init(targetDate, extra) {
        var isPast    = config.type === 'one-time' && targetDate && targetDate < new Date();
        var isUnknown = !targetDate;
        root.innerHTML = buildPage(config, targetDate, extra || {}, isPast, isUnknown);
        if (!isPast && !isUnknown) startTicker(targetDate);
      }

      if (config.type === 'fixed') {
        init(config.date || null, {});
      } else if (config.type === 'auto') {
        var getter = AUTO[config.slug];
        if (!getter) { root.textContent = '[Engine] No auto getter for: ' + config.slug; return; }
        var res = getter();
        init(res.date, res);
      } else {
        loadData(function (data) {
          var ev   = ((data || {}).events || {})[config.slug] || {};
          var date = ev.date ? new Date(ev.date) : null;
          init(date, { note: ev.note, subtitle: ev.raceName || '' });
        });
      }
    },

    getCardData: function (config, cb) {
      function resolve(date, isPast) {
        if (!date) { cb({ state: 'unknown' }); return; }
        if (isPast) { cb({ state: 'past', date: date }); return; }
        var days = daysUntil(date);
        cb({ state: days <= 0 ? 'today' : 'future', days: days, date: date });
      }

      if (config.type === 'auto') {
        var getter = AUTO[config.slug];
        if (!getter) { cb({ state: 'unknown' }); return; }
        var res = getter();
        resolve(res.date, false);
      } else {
        loadData(function (data) {
          var ev   = ((data || {}).events || {})[config.slug] || {};
          var date = ev.date ? new Date(ev.date) : null;
          resolve(date, config.type === 'one-time' && date && date < new Date());
        });
      }
    },

    catColors: catColors,
    fmtDate:   fmtDate,
  };

})();
