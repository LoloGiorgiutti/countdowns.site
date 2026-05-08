/* ═══════════════════════════════════════════════════════════════
   COUNTDOWN ENGINE — shared logic for all countdown pages
   Calculadora.live · 2026
═══════════════════════════════════════════════════════════════ */
(function () {
  'use strict';

  /* ─── ARGENTINA HOLIDAYS LIST ─────────────────────────────── */
  /* [year, month(0-based), day, name] */
  var AR_FERIADOS = [
    [2026, 0,  1, 'Año Nuevo'],
    [2026, 1, 16, 'Carnaval'],
    [2026, 1, 17, 'Carnaval'],
    [2026, 2, 24, 'Día Nacional de la Memoria por la Verdad y la Justicia'],
    [2026, 3,  2, 'Día del Veterano y los Caídos en la Guerra de Malvinas'],
    [2026, 3,  3, 'Viernes Santo'],
    [2026, 4,  1, 'Día del Trabajador'],
    [2026, 4, 25, 'Día de la Revolución de Mayo'],
    [2026, 5, 15, 'Paso a la Inmortalidad del Gral. Manuel Belgrano'],
    [2026, 6,  9, 'Día de la Independencia'],
    [2026, 7, 17, 'Paso a la Inmortalidad del Gral. José de San Martín'],
    [2026, 9, 12, 'Día del Respeto a la Diversidad Cultural'],
    [2026, 10, 20, 'Día de la Soberanía Nacional'],
    [2026, 11,  8, 'Inmaculada Concepción de María'],
    [2026, 11, 25, 'Navidad'],
    [2027, 0,  1, 'Año Nuevo'],
    [2027, 1, 15, 'Carnaval'],
    [2027, 1, 16, 'Carnaval'],
    [2027, 2, 24, 'Día Nacional de la Memoria por la Verdad y la Justicia'],
    [2027, 3,  2, 'Día del Veterano y los Caídos en la Guerra de Malvinas'],
    [2027, 3, 26, 'Viernes Santo'],
    [2027, 4,  1, 'Día del Trabajador'],
    [2027, 4, 25, 'Día de la Revolución de Mayo'],
    [2027, 5, 21, 'Paso a la Inmortalidad del Gral. Manuel Belgrano'],
    [2027, 6,  9, 'Día de la Independencia'],
    [2027, 7, 16, 'Paso a la Inmortalidad del Gral. José de San Martín'],
    [2027, 9, 11, 'Día del Respeto a la Diversidad Cultural'],
    [2027, 10, 22, 'Día de la Soberanía Nacional'],
    [2027, 11,  8, 'Inmaculada Concepción de María'],
    [2027, 11, 25, 'Navidad'],
    [2028, 0,  1, 'Año Nuevo'],
  ];

  /* "Fechas patrias" subset (month, day pairs) */
  var FECHAS_PATRIAS_KEYS = [
    [2, 24], [3, 2], [4, 25], [6, 9],
    [7, 17], [7, 16], [7, 18], [10, 20],
  ];

  /* ─── FULL MOON DATES (UTC, approximate ±12h) ─────────────── */
  var FULL_MOONS = [
    '2026-01-03T22:03Z', '2026-02-01T22:09Z', '2026-03-03T14:38Z',
    '2026-04-02T04:12Z', '2026-05-01T14:23Z', '2026-05-31T00:45Z',
    '2026-06-29T11:57Z', '2026-07-29T01:36Z', '2026-08-27T17:25Z',
    '2026-09-26T11:49Z', '2026-10-26T08:12Z', '2026-11-25T05:53Z',
    '2026-12-25T02:28Z', '2027-01-23T22:17Z', '2027-02-22T16:23Z',
    '2027-03-24T08:35Z', '2027-04-22T22:35Z', '2027-05-22T10:05Z',
    '2027-06-20T19:58Z', '2027-07-20T05:02Z', '2027-08-18T14:30Z',
    '2027-09-17T01:05Z', '2027-10-16T13:15Z',
  ].map(function (s) { return new Date(s); });

  /* ─── HELPERS ──────────────────────────────────────────────── */
  function nthWeekday(year, month, n, weekday) {
    /* nth occurrence (1-based) of weekday (0=Sun..6=Sat) in month */
    var d = new Date(year, month, 1);
    var offset = (weekday - d.getDay() + 7) % 7;
    return new Date(year, month, 1 + offset + (n - 1) * 7);
  }

  function nextOccurrence(getForYear) {
    var now = new Date();
    var y = now.getFullYear();
    var d = getForYear(y);
    if (d <= now) d = getForYear(y + 1);
    return d;
  }

  function nextFeriado() {
    var now = new Date(); now.setHours(0, 0, 0, 0);
    for (var i = 0; i < AR_FERIADOS.length; i++) {
      var f = AR_FERIADOS[i];
      var d = new Date(f[0], f[1], f[2]);
      if (d >= now) return { date: d, name: f[3] };
    }
    return null;
  }

  function nextFechaPatria() {
    var now = new Date(); now.setHours(0, 0, 0, 0);
    for (var i = 0; i < AR_FERIADOS.length; i++) {
      var f = AR_FERIADOS[i];
      var d = new Date(f[0], f[1], f[2]);
      if (d >= now) {
        for (var j = 0; j < FECHAS_PATRIAS_KEYS.length; j++) {
          if (FECHAS_PATRIAS_KEYS[j][0] === f[1] && FECHAS_PATRIAS_KEYS[j][1] === f[2]) {
            return { date: d, name: f[3] };
          }
        }
      }
    }
    return null;
  }

  function nextFullMoon() {
    var now = new Date();
    for (var i = 0; i < FULL_MOONS.length; i++) {
      if (FULL_MOONS[i] > now) return FULL_MOONS[i];
    }
    return null;
  }

  /* ─── AUTO DATE GETTERS ────────────────────────────────────── */
  var AUTO = {
    'fin-de-semana': function () {
      var now = new Date(), day = now.getDay();
      var dts = (6 - day + 7) % 7 || 7; /* days to next Saturday */
      var d = new Date(now);
      d.setDate(d.getDate() + dts); d.setHours(0, 0, 0, 0);
      return { date: d };
    },
    'ano-que-viene': function () {
      var y = new Date().getFullYear() + 1;
      return { date: new Date(y, 0, 1), note: '1° de enero de ' + y };
    },
    'feriado': function () {
      var f = nextFeriado();
      return f ? { date: f.date, subtitle: f.name } : { date: null };
    },
    'fecha-patria': function () {
      var f = nextFechaPatria();
      return f ? { date: f.date, subtitle: f.name } : { date: null };
    },
    'luna-llena': function () {
      return { date: nextFullMoon(), note: 'Fecha aproximada (±12 horas)' };
    },
    'navidad': function () {
      return { date: nextOccurrence(function (y) { return new Date(y, 11, 25); }) };
    },
    'ano-nuevo': function () {
      return { date: nextOccurrence(function (y) { return new Date(y + 1, 0, 1); }) };
    },
    'reyes': function () {
      return { date: nextOccurrence(function (y) { return new Date(y, 0, 6); }) };
    },
    'san-valentin': function () {
      return { date: nextOccurrence(function (y) { return new Date(y, 1, 14); }) };
    },
    'halloween': function () {
      return { date: nextOccurrence(function (y) { return new Date(y, 9, 31); }) };
    },
    'dia-padre': function () { /* 3rd Sunday of June */
      return { date: nextOccurrence(function (y) { return nthWeekday(y, 5, 3, 0); }) };
    },
    'dia-nino': function () { /* 2nd Sunday of August */
      return { date: nextOccurrence(function (y) { return nthWeekday(y, 7, 2, 0); }) };
    },
    'dia-madre': function () { /* 3rd Sunday of October */
      return { date: nextOccurrence(function (y) { return nthWeekday(y, 9, 3, 0); }) };
    },
    'superbowl': function () { /* 2nd Sunday of February */
      return { date: nextOccurrence(function (y) { return nthWeekday(y, 1, 2, 0); }), note: '2do domingo de febrero' };
    },
    'oscars': function () { /* approx 4th Sunday of February */
      return { date: nextOccurrence(function (y) { return nthWeekday(y, 1, 4, 0); }), note: '~Último domingo de febrero (fecha tentativa)' };
    },
    'met-gala': function () { /* 1st Monday of May */
      return { date: nextOccurrence(function (y) { return nthWeekday(y, 4, 1, 1); }) };
    },
    'black-friday': function () { /* 4th Friday of November */
      return { date: nextOccurrence(function (y) { return nthWeekday(y, 10, 4, 5); }) };
    },
    'cyber-monday': function () { /* 3 days after Black Friday */
      return {
        date: nextOccurrence(function (y) {
          var bf = nthWeekday(y, 10, 4, 5);
          return new Date(bf.getFullYear(), bf.getMonth(), bf.getDate() + 3);
        }),
        note: 'Lunes siguiente al Black Friday'
      };
    },
    'elecciones': function () {
      /* Argentina presidential elections Oct 2027 */
      return { date: new Date(2027, 9, 26, 8, 0, 0), note: 'Fecha estimada. Elecciones generales Argentina 2027.' };
    },
    'nuevo-presidente': function () {
      /* New president sworn in Dec 10, 2027 */
      return { date: new Date(2027, 11, 10, 10, 0, 0), note: 'Fecha de asunción presidencial (10 de diciembre).' };
    },
    'olimpicos': function () {
      /* LA 2028 Opening Ceremony: July 14, 2028 */
      return { date: new Date(2028, 6, 14, 20, 0, 0), note: 'Juegos Olímpicos de Los Ángeles 2028 — Ceremonia de Apertura.' };
    },
  };

  /* ─── DATA CACHE ───────────────────────────────────────────── */
  var _cache = null;
  var _pending = [];

  function loadData(cb) {
    if (_cache !== null) { cb(_cache); return; }
    _pending.push(cb);
    if (_pending.length > 1) return; /* already fetching */
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

  function fmtDate(d) {
    return d.toLocaleDateString('es-AR', {
      weekday: 'long', year: 'numeric', month: 'long', day: 'numeric'
    });
  }

  function daysUntil(d) {
    return Math.ceil((d - new Date()) / 86400000);
  }

  /* ─── CATEGORY ACCENT COLORS ───────────────────────────────── */
  var CAT_COLORS = {
    'Lanzamientos': { accent: '#8B5CF6', soft: 'rgba(139,92,246,.13)', glow: 'rgba(139,92,246,.07)' },
    'Tiempo':       { accent: '#0EA5E9', soft: 'rgba(14,165,233,.13)', glow: 'rgba(14,165,233,.06)' },
    'Eventos':      { accent: '#F43F5E', soft: 'rgba(244,63,94,.13)',  glow: 'rgba(244,63,94,.06)' },
    'Argentina':    { accent: '#60A5FA', soft: 'rgba(96,165,250,.14)', glow: 'rgba(96,165,250,.06)' },
    'Descuentos':   { accent: '#10B981', soft: 'rgba(16,185,129,.13)', glow: 'rgba(16,185,129,.06)' },
    'Días festivos':{ accent: '#F59E0B', soft: 'rgba(245,158,11,.13)', glow: 'rgba(245,158,11,.06)' },
  };

  function catColors(category) {
    return CAT_COLORS[category] || { accent: '#4F6BFF', soft: 'rgba(79,107,255,.12)', glow: 'rgba(79,107,255,.06)' };
  }

  /* ─── CSS LOADER ────────────────────────────────────────────── */
  function ensureCSS() {
    if (document.getElementById('cd-stylesheet')) return;
    var link = document.createElement('link');
    link.id = 'cd-stylesheet';
    link.rel = 'stylesheet';
    link.href = '/countdowns/countdown.css';
    document.head.appendChild(link);
  }

  /* ─── HTML BUILDER ──────────────────────────────────────────── */
  function buildCountdownSection(targetDate, isPast, isUnknown, note) {
    if (isUnknown) {
      return [
        '<div class="cd-unknown">',
        '  <div class="cd-unknown-icon">📅</div>',
        '  <div class="cd-unknown-text">Fecha por confirmar</div>',
        note ? '<div class="cd-unknown-sub">' + note + '</div>' : '',
        '</div>',
      ].join('');
    }
    if (isPast) {
      return [
        '<div class="cd-past">',
        '  <div class="cd-past-badge">✓ Ya ocurrió</div>',
        '  <div class="cd-past-date">' + fmtDate(targetDate) + '</div>',
        '  <div class="cd-past-sub">El contador se actualizará para el próximo evento.</div>',
        '</div>',
      ].join('');
    }
    return [
      '<div class="cd-grid">',
      '  <div class="cd-box"><div class="cd-num" id="cd-d">—</div><div class="cd-lbl">días</div></div>',
      '  <div class="cd-sep">:</div>',
      '  <div class="cd-box"><div class="cd-num" id="cd-h">—</div><div class="cd-lbl">horas</div></div>',
      '  <div class="cd-sep">:</div>',
      '  <div class="cd-box"><div class="cd-num" id="cd-m">—</div><div class="cd-lbl">min</div></div>',
      '  <div class="cd-sep">:</div>',
      '  <div class="cd-box"><div class="cd-num" id="cd-s">—</div><div class="cd-lbl">seg</div></div>',
      '</div>',
      '<div class="cd-date-label">' + fmtDate(targetDate) + '</div>',
    ].join('');
  }

  function buildPage(config, targetDate, extra, isPast, isUnknown) {
    var cc = catColors(config.category);
    var note = (extra && extra.note) || config.note || '';
    var subtitle = (extra && extra.subtitle) || '';
    var cdSection = buildCountdownSection(targetDate, isPast, isUnknown, note);

    /* Category border color derived from accent */
    var border = cc.soft.replace(/[\d.]+\)$/, '.3)');

    /* ── Optional article + FAQ section ── */
    var articleHTML = '';
    if (config.content || (config.faqs && config.faqs.length)) {
      articleHTML += '<div class="cd-article">';
      if (config.content) {
        articleHTML += '<p class="cd-article-body">' + config.content + '</p>';
      }
      if (config.faqs && config.faqs.length) {
        articleHTML += '<div class="cd-faq">';
        articleHTML += '<h2 class="cd-faq-title">Preguntas frecuentes</h2>';
        config.faqs.forEach(function (faq) {
          articleHTML += '<div class="cd-faq-item">';
          articleHTML += '<h3 class="cd-faq-q">' + faq.q + '</h3>';
          articleHTML += '<p class="cd-faq-a">' + faq.a + '</p>';
          articleHTML += '</div>';
        });
        articleHTML += '</div>';
      }
      articleHTML += '</div>';
    }

    return [
      '<div class="cd-page">',
      '  <div class="cd-hero" style="--cat-accent:' + cc.accent + ';--cat-soft:' + cc.soft + ';--cat-glow:' + cc.glow + ';--cat-border:' + border + '">',
      '    <div class="cd-breadcrumb">',
      '      <a href="/">Inicio</a> <span>›</span>',
      '      <a href="/countdowns/">Contadores</a> <span>›</span>',
      '      <span>' + config.category + '</span>',
      '    </div>',
      '    <div class="cd-badge"><span class="cd-badge-ico">' + config.emoji + '</span>' + config.category + '</div>',
      '    <h1 class="cd-title">' + config.name + '</h1>',
      subtitle ? '    <div class="cd-subtitle">' + subtitle + '</div>' : '',
      '    <p class="cd-desc">' + config.description + '</p>',
      '    ' + cdSection,
      '  </div>',
      '  <div class="cd-below">',
      note && !isUnknown ? '    <div class="cd-note-card">ℹ️ ' + note + '</div>' : '',
      '    <a href="/countdowns/" class="cd-back-link">← Ver todos los contadores</a>',
      '  </div>',
      articleHTML,
      '</div>',
    ].join('\n');
  }

  /* ─── TICKER ────────────────────────────────────────────────── */
  function startTicker(targetDate) {
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
    setInterval(tick, 1000);
  }

  /* ─── PUBLIC API ────────────────────────────────────────────── */
  window.CountdownEngine = {

    /* Render a full countdown page into rootId */
    render: function (rootId, config) {
      ensureCSS();
      var root = document.getElementById(rootId);
      if (!root) return;

      function init(targetDate, extra) {
        var isPast    = config.type === 'one-time' && targetDate && targetDate < new Date();
        var isUnknown = !targetDate;
        root.innerHTML = buildPage(config, targetDate, extra || {}, isPast, isUnknown);
        if (!isPast && !isUnknown) startTicker(targetDate);
      }

      if (config.type === 'auto') {
        var getter = AUTO[config.slug];
        if (!getter) { root.textContent = '[CountdownEngine] No auto getter for: ' + config.slug; return; }
        var res = getter();
        init(res.date, res);
      } else {
        /* variable or one-time → fetch JSON */
        loadData(function (data) {
          var ev = ((data || {}).events || {})[config.slug] || {};
          var date = ev.date ? new Date(ev.date) : null;
          init(date, { note: ev.note, subtitle: ev.raceName || '' });
        });
      }
    },

    /* For hub page: async get card data (days remaining + state) */
    getCardData: function (config, cb) {
      function resolve(date, isPast) {
        if (!date) { cb({ state: 'unknown' }); return; }
        if (isPast) { cb({ state: 'past', date: date }); return; }
        var days = daysUntil(date);
        cb({ state: days === 0 ? 'today' : 'future', days: days, date: date });
      }

      if (config.type === 'auto') {
        var getter = AUTO[config.slug];
        if (!getter) { cb({ state: 'unknown' }); return; }
        var res = getter();
        resolve(res.date, false);
      } else {
        loadData(function (data) {
          var ev = ((data || {}).events || {})[config.slug] || {};
          var date = ev.date ? new Date(ev.date) : null;
          resolve(date, config.type === 'one-time' && date && date < new Date());
        });
      }
    },

    /* Expose for hub use */
    _allEvents: null, /* set by hub */
  };

})();
