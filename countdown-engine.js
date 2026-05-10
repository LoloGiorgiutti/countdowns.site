/* ═══════════════════════════════════════════════════════════════
   COUNTDOWN ENGINE — countdowns.site
   Shared logic for hub + individual countdown pages
═══════════════════════════════════════════════════════════════ */
(function () {
  'use strict';

  /* ─── LANGUAGE DETECTION ────────────────────────────────────── */
  var _pageLang = (window.location.pathname.match(/^\/(es|pt|fr)\//) || [])[1] || 'en';

  /* ─── UI STRING TRANSLATIONS ────────────────────────────────── */
  var UI = {
    en: {
      days: 'days', hours: 'hours', min: 'min', sec: 'sec',
      dateTBC: 'Date to be confirmed',
      alreadyHappened: 'Already happened',
      backLink: '← All countdowns',
      faqTitle: 'Frequently Asked Questions',
copyLink: 'Copy link', copied: '✓ Copied!',
      shareBtn: 'Share', whatsapp: 'WhatsApp',
      screenshot: 'Screenshot', embed: 'Embed',
      embedTitle: 'Embed this countdown',
      embedNote: 'Paste this code on any website:',
      close: 'Close',
      shareMsg: 'Countdown to ',    },
    es: {
      days: 'días', hours: 'horas', min: 'min', sec: 'seg',
      dateTBC: 'Fecha por confirmar',
      alreadyHappened: 'Ya ocurrió',
      backLink: '← Todos los countdowns',
      faqTitle: 'Preguntas Frecuentes',
copyLink: 'Copiar enlace', copied: '✓ ¡Copiado!',
      shareBtn: 'Compartir', whatsapp: 'WhatsApp',
      screenshot: 'Captura', embed: 'Insertar',
      embedTitle: 'Insertar este countdown',
      embedNote: 'Pegá este código en cualquier sitio:',
      close: 'Cerrar',
      shareMsg: 'Countdown para ',    },
    pt: {
      days: 'dias', hours: 'horas', min: 'min', sec: 's',
      dateTBC: 'Data a confirmar',
      alreadyHappened: 'Já aconteceu',
      backLink: '← Todos os countdowns',
      faqTitle: 'Perguntas Frequentes',
copyLink: 'Copiar link', copied: '✓ Copiado!',
      shareBtn: 'Compartilhar', whatsapp: 'WhatsApp',
      screenshot: 'Captura', embed: 'Incorporar',
      embedTitle: 'Incorporar este countdown',
      embedNote: 'Cole este código em qualquer site:',
      close: 'Fechar',
      shareMsg: 'Countdown para ',    },
    fr: {
      days: 'jours', hours: 'heures', min: 'min', sec: 's',
      dateTBC: 'Date à confirmer',
      alreadyHappened: 'Déjà passé',
      backLink: '← Tous les comptes à rebours',
      faqTitle: 'Questions Fréquentes',
copyLink: 'Copier le lien', copied: '✓ Copié !',
      shareBtn: 'Partager', whatsapp: 'WhatsApp',
      screenshot: 'Capture', embed: 'Intégrer',
      embedTitle: 'Intégrer ce countdown',
      embedNote: 'Collez ce code sur n\'importe quel site :',
      close: 'Fermer',
      shareMsg: 'Compte à rebours : ',    },
  };
  var T = UI[_pageLang] || UI.en;

  /* ─── CATEGORY NAME TRANSLATIONS ───────────────────────────── */
  var CAT_I18N = {
    es: { Releases:'Lanzamientos', Sports:'Deportes', Holidays:'Feriados',
          Entertainment:'Entretenimiento', Sales:'Ofertas', Nature:'Naturaleza',
          Music:'Música', Politics:'Política', Fashion:'Moda', Technology:'Tecnología' },
    pt: { Releases:'Lançamentos', Sports:'Esportes', Holidays:'Feriados',
          Entertainment:'Entretenimento', Sales:'Promoções', Nature:'Natureza',
          Music:'Música', Politics:'Política', Fashion:'Moda', Technology:'Tecnologia' },
    fr: { Releases:'Sorties', Sports:'Sports', Holidays:'Jours Fériés',
          Entertainment:'Divertissement', Sales:'Promotions', Nature:'Nature',
          Music:'Musique', Politics:'Politique', Fashion:'Mode', Technology:'Technologie' },
  };
  function tCat(cat) {
    return (CAT_I18N[_pageLang] && CAT_I18N[_pageLang][cat]) || cat;
  }

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

  /* ─── SHARE BAR ────────────────────────────────────────────── */
  var ICON_COPY   = '<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="9" y="9" width="13" height="13" rx="2"/><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"/></svg>';
  var ICON_SHARE  = '<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 12v8a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2v-8"/><polyline points="16 6 12 2 8 6"/><line x1="12" y1="2" x2="12" y2="15"/></svg>';
  var ICON_WA     = '<svg width="15" height="15" viewBox="0 0 24 24" fill="currentColor"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 0 1-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 0 1-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 0 1 2.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0 0 12.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 0 0 5.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 0 0-3.48-8.413z"/></svg>';
  var ICON_X      = '<svg width="15" height="15" viewBox="0 0 24 24" fill="currentColor"><path d="M18.244 2.25h3.308l-7.227 8.26 8.502 11.24H16.17l-4.714-6.231-5.401 6.231H2.744l7.73-8.835L1.254 2.25H8.08l4.259 5.622Zm-1.161 17.52h1.833L7.084 4.126H5.117z"/></svg>';
  var ICON_CAM    = '<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M23 19a2 2 0 0 1-2 2H3a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h4l2-3h6l2 3h4a2 2 0 0 1 2 2z"/><circle cx="12" cy="13" r="4"/></svg>';
  var ICON_EMBED  = '<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="16 18 22 12 16 6"/><polyline points="8 6 2 12 8 18"/></svg>';

  function buildShareBar(config) {
    var slug    = config.slug || '';
    var name    = config.name || '';
    var pageUrl = window.location.href.split('?')[0].split('#')[0];
    var waHref  = 'https://wa.me/send?text=' + encodeURIComponent(T.shareMsg + name + ' → ' + pageUrl);
    var xHref   = 'https://twitter.com/intent/tweet?text=' + encodeURIComponent(T.shareMsg + name) + '&url=' + encodeURIComponent(pageUrl);
    var embedSrc = 'https://countdowns.site/embed/' + slug + '/';
    var iframeCode = '<iframe src="' + embedSrc + '" width="320" height="200" frameborder="0" style="border-radius:16px;overflow:hidden" allowtransparency="true"></iframe>';
    return [
      '<div class="cd-share-bar">',
      '<button class="cd-share-btn" id="cd-copy-btn" onclick="window._cdCopy()">' + ICON_COPY + T.copyLink + '</button>',
      '<button class="cd-share-btn cd-share-native" onclick="window._cdNativeShare()">' + ICON_SHARE + T.shareBtn + '</button>',
      '<a class="cd-share-btn" href="' + waHref + '" target="_blank" rel="noopener">' + ICON_WA + T.whatsapp + '</a>',
      '<a class="cd-share-btn" href="' + xHref + '" target="_blank" rel="noopener">' + ICON_X + 'X</a>',
      '<button class="cd-share-btn" onclick="window._cdScreenshot()">' + ICON_CAM + T.screenshot + '</button>',
      '<button class="cd-share-btn" onclick="window._cdEmbed()">' + ICON_EMBED + T.embed + '</button>',
      '</div>',
      /* embed modal */
      '<div id="cd-embed-modal" class="cd-embed-modal" onclick="if(event.target===this)window._cdCloseEmbed()">',
      '<div class="cd-embed-dialog">',
      '<div class="cd-embed-header"><h3>' + T.embedTitle + '</h3>',
      '<button class="cd-embed-close" onclick="window._cdCloseEmbed()">&#x2715;</button></div>',
      '<p class="cd-embed-note">' + T.embedNote + '</p>',
      '<textarea class="cd-embed-code" readonly onclick="this.select()" spellcheck="false">' + iframeCode.replace(/</g,'&lt;').replace(/>/g,'&gt;') + '</textarea>',
      '<button class="cd-share-btn cd-embed-copy" onclick="window._cdCopyEmbed()">' + ICON_COPY + T.copyLink + '</button>',
      '</div></div>',
    ].join('');
  }

  function setupShare(config) {
    var pageUrl = window.location.href.split('?')[0].split('#')[0];
    var name    = config.name || '';
    var slug    = config.slug || '';
    var iframeCode = '<iframe src="https://countdowns.site/embed/' + slug + '/" width="320" height="200" frameborder="0" style="border-radius:16px;overflow:hidden" allowtransparency="true"></iframe>';

    window._cdCopy = function () {
      navigator.clipboard.writeText(pageUrl).then(function () {
        var btn = document.getElementById('cd-copy-btn');
        if (btn) { btn.innerHTML = ICON_COPY + T.copied; setTimeout(function () { btn.innerHTML = ICON_COPY + T.copyLink; }, 2000); }
      }).catch(function () {
        /* fallback: select a hidden input */
        var ta = document.createElement('textarea');
        ta.value = pageUrl; document.body.appendChild(ta); ta.select();
        document.execCommand('copy'); document.body.removeChild(ta);
        var btn = document.getElementById('cd-copy-btn');
        if (btn) { btn.innerHTML = ICON_COPY + T.copied; setTimeout(function () { btn.innerHTML = ICON_COPY + T.copyLink; }, 2000); }
      });
    };

    window._cdNativeShare = function () {
      if (navigator.share) {
        navigator.share({ title: name, text: T.shareMsg + name, url: pageUrl });
      } else {
        window._cdCopy();
      }
    };

    window._cdScreenshot = function () {
      var hero = document.querySelector('.cd-hero');
      if (!hero) return;
      if (window.html2canvas) { _doShot(hero); return; }
      var s = document.createElement('script');
      s.src = 'https://html2canvas.hertzen.com/dist/html2canvas.min.js';
      s.onload = function () { _doShot(hero); };
      document.head.appendChild(s);
    };

    function _doShot(hero) {
      html2canvas(hero, { backgroundColor: null, scale: 2 }).then(function (canvas) {
        var link = document.createElement('a');
        link.download = (name || 'countdown').replace(/\s+/g, '-').toLowerCase() + '.png';
        link.href = canvas.toDataURL('image/png');
        link.click();
      });
    }

    window._cdEmbed = function () {
      var m = document.getElementById('cd-embed-modal');
      if (m) m.style.display = 'flex';
    };
    window._cdCloseEmbed = function () {
      var m = document.getElementById('cd-embed-modal');
      if (m) m.style.display = 'none';
    };
    window._cdCopyEmbed = function () {
      var ta = document.querySelector('.cd-embed-code');
      if (ta) { ta.select(); navigator.clipboard.writeText(iframeCode).catch(function () { document.execCommand('copy'); }); }
      var btn = document.querySelector('.cd-embed-copy');
      if (btn) { btn.innerHTML = ICON_COPY + T.copied; setTimeout(function () { btn.innerHTML = ICON_COPY + T.copyLink; }, 2000); }
    };

    /* hide native share btn on desktop where navigator.share is unavailable */
    if (!navigator.share) {
      var nb = document.querySelector('.cd-share-native');
      if (nb) nb.style.display = 'none';
    }
  }

  /* ─── HTML BUILDER (individual pages) ──────────────────────── */
  function buildCountdownSection(targetDate, isPast, isUnknown, note) {
    if (isUnknown) {
      return '<div class="cd-unknown"><div class="cd-unknown-text">' + T.dateTBC + '</div>' +
             (note ? '<div class="cd-unknown-sub">' + note + '</div>' : '') + '</div>';
    }
    if (isPast) {
      return '<div class="cd-past"><div class="cd-past-badge">' + T.alreadyHappened + '</div>' +
             '<div class="cd-past-date">' + fmtDate(targetDate, _pageLang) + '</div></div>';
    }
    return [
      '<div class="cd-grid">',
      '<div class="cd-box"><div class="cd-num" id="cd-d">—</div><div class="cd-lbl">' + T.days + '</div></div>',
      '<div class="cd-sep">:</div>',
      '<div class="cd-box"><div class="cd-num" id="cd-h">—</div><div class="cd-lbl">' + T.hours + '</div></div>',
      '<div class="cd-sep">:</div>',
      '<div class="cd-box"><div class="cd-num" id="cd-m">—</div><div class="cd-lbl">' + T.min + '</div></div>',
      '<div class="cd-sep">:</div>',
      '<div class="cd-box"><div class="cd-num" id="cd-s">—</div><div class="cd-lbl">' + T.sec + '</div></div>',
      '</div>',
      '<div class="cd-date-label">' + fmtDate(targetDate, _pageLang) + '</div>',
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
        articleHTML += '<div class="cd-faq"><h2 class="cd-faq-title">' + T.faqTitle + '</h2>';
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
      '<div class="cd-breadcrumb"><a href="/">countdowns.site</a><span>/</span><a href="/#' + (config.category || '').toLowerCase() + '">' + tCat(config.category || '') + '</a><span>/</span><span>' + config.name + '</span></div>',
      '<div class="cd-badge">' + tCat(config.category || '') + '</div>',
      '<h1 class="cd-title">' + config.name + '</h1>',
      subtitle ? '<div class="cd-subtitle">' + subtitle + '</div>' : '',
      '<p class="cd-desc">' + (config.description || '') + '</p>',
      cdSection,
      '</div>',
      '<div class="cd-below">',
      (note && !isUnknown) ? '<div class="cd-note-card">' + note + '</div>' : '',
buildShareBar(config),      '<a href="/" class="cd-back-link">' + T.backLink + '</a>',
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
        setupShare(config);
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
          var _lang = (window.location.pathname.match(/^\/(es|pt|fr)\//) || [])[1] || 'en';
          var _note = (_lang !== 'en' && ev['note_' + _lang]) || ev.note || '';
          init(date, { note: _note, subtitle: ev.raceName || '' });
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
