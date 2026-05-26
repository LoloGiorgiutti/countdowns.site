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
      elapsed: 'Time elapsed since this event',
      since: 'Since',
      backLink: '← All countdowns',
      faqTitle: 'Frequently Asked Questions',
copyLink: 'Copy link', copied: '✓ Copied!',
      shareBtn: 'Share', whatsapp: 'WhatsApp',
      screenshot: 'Save image', embed: 'Embed',
      embedTitle: 'Embed this countdown',
      embedNote: 'Paste this code on any website:',
      close: 'Close',
      shareMsg: 'Countdown to ',    },
    es: {
      days: 'días', hours: 'horas', min: 'min', sec: 'seg',
      dateTBC: 'Fecha por confirmar',
      alreadyHappened: 'Ya ocurrió',
      elapsed: 'Tiempo transcurrido desde este evento',
      since: 'Desde el',
      backLink: '← Todos los countdowns',
      faqTitle: 'Preguntas Frecuentes',
copyLink: 'Copiar enlace', copied: '✓ ¡Copiado!',
      shareBtn: 'Compartir', whatsapp: 'WhatsApp',
      screenshot: 'Guardar imagen', embed: 'Insertar',
      embedTitle: 'Insertar este countdown',
      embedNote: 'Pegá este código en cualquier sitio:',
      close: 'Cerrar',
      shareMsg: 'Countdown para ',    },
    pt: {
      days: 'dias', hours: 'horas', min: 'min', sec: 's',
      dateTBC: 'Data a confirmar',
      alreadyHappened: 'Já aconteceu',
      elapsed: 'Tempo decorrido desde este evento',
      since: 'Desde',
      backLink: '← Todos os countdowns',
      faqTitle: 'Perguntas Frequentes',
copyLink: 'Copiar link', copied: '✓ Copiado!',
      shareBtn: 'Compartilhar', whatsapp: 'WhatsApp',
      screenshot: 'Salvar imagem', embed: 'Incorporar',
      embedTitle: 'Incorporar este countdown',
      embedNote: 'Cole este código em qualquer site:',
      close: 'Fechar',
      shareMsg: 'Countdown para ',    },
    fr: {
      days: 'jours', hours: 'heures', min: 'min', sec: 's',
      dateTBC: 'Date à confirmer',
      alreadyHappened: 'Déjà passé',
      elapsed: 'Temps écoulé depuis cet événement',
      since: 'Depuis le',
      backLink: '← Tous les comptes à rebours',
      faqTitle: 'Questions Fréquentes',
copyLink: 'Copier le lien', copied: '✓ Copié !',
      shareBtn: 'Partager', whatsapp: 'WhatsApp',
      screenshot: 'Enregistrer', embed: 'Intégrer',
      embedTitle: 'Intégrer ce countdown',
      embedNote: 'Collez ce code sur n\'importe quel site :',
      close: 'Fermer',
      shareMsg: 'Compte à rebours : ',    },
  };
  var T = UI[_pageLang] || UI.en;

  /* ─── FEEDBACK WIDGET TRANSLATIONS ─────────────────────────── */
  var FB = ({
    en: { title:'Anything to improve?',
          sub:'Missing something? Have an idea? Every suggestion helps.',
          love:'😍 Love it', add:"💡 I'd add something",
          broken:"🐛 Something's broken", question:'❓ I have a question',
          ph:"Tell us what you'd add or what's not working. Every suggestion counts!",
          send:'Send feedback →', thanks:'✓ Thanks for your feedback!' },
    es: { title:'¿Algo para mejorar?',
          sub:'¿Le falta algo? ¿Tenés una idea? Cada sugerencia nos ayuda a mejorar.',
          love:'😍 Me encanta', add:'💡 Le agregaría algo',
          broken:'🐛 Algo no funciona', question:'❓ Tengo una pregunta',
          ph:'Contanos qué le agregarías o qué no funciona. ¡Cada sugerencia cuenta!',
          send:'Enviar sugerencia →', thanks:'✓ ¡Gracias por tu sugerencia!' },
    pt: { title:'Algo para melhorar?',
          sub:'Falta algo? Tem uma ideia? Cada sugestão nos ajuda.',
          love:'😍 Adorei', add:'💡 Adicionaria algo',
          broken:'🐛 Algo não funciona', question:'❓ Tenho uma pergunta',
          ph:'Conta o que adicionarias ou o que não está funcionando. Toda sugestão conta!',
          send:'Enviar sugestão →', thanks:'✓ Obrigado pelo seu feedback!' },
    fr: { title:'Quelque chose à améliorer ?',
          sub:'Il manque quelque chose ? Une idée ? Chaque suggestion nous aide.',
          love:"😍 J'adore", add:"💡 J'ajouterais quelque chose",
          broken:'🐛 Quelque chose ne fonctionne pas', question:"❓ J'ai une question",
          ph:"Dites-nous ce que vous ajouteriez ou ce qui ne fonctionne pas.",
          send:'Envoyer →', thanks:'✓ Merci pour votre retour !' },
  })[_pageLang] || ({
    title:'Anything to improve?',
    sub:'Missing something? Have an idea? Every suggestion helps.',
    love:'😍 Love it', add:"💡 I'd add something",
    broken:"🐛 Something's broken", question:'❓ I have a question',
    ph:"Tell us what you'd add or what's not working.",
    send:'Send feedback →', thanks:'✓ Thanks for your feedback!' });

  /* ─── CATEGORY NAME TRANSLATIONS ───────────────────────────── */
  var CAT_I18N = {
    es: { Releases:'Lanzamientos', Sports:'Deportes', Holidays:'Feriados',
          Entertainment:'Entretenimiento', Sales:'Ofertas', Nature:'Naturaleza',
          Music:'Música', Politics:'Política', Fashion:'Moda', Technology:'Tecnología',
          Months:'Meses', Seasons:'Estaciones', School:'Escuela',
          'National Days':'Días Nacionales', 'Jewish Holidays':'Fiestas Judías' },
    pt: { Releases:'Lançamentos', Sports:'Esportes', Holidays:'Feriados',
          Entertainment:'Entretenimento', Sales:'Promoções', Nature:'Natureza',
          Music:'Música', Politics:'Política', Fashion:'Moda', Technology:'Tecnologia',
          Months:'Meses', Seasons:'Estações', School:'Escola',
          'National Days':'Datas Nacionais', 'Jewish Holidays':'Feriados Judaicos' },
    fr: { Releases:'Sorties', Sports:'Sports', Holidays:'Jours Fériés',
          Entertainment:'Divertissement', Sales:'Promotions', Nature:'Nature',
          Music:'Musique', Politics:'Politique', Fashion:'Mode', Technology:'Technologie',
          Months:'Mois', Seasons:'Saisons', School:'École',
          'National Days':'Jours Nationaux', 'Jewish Holidays':'Fêtes Juives' },
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

  /* ─── COUNTRY → TIMEZONE MAP ────────────────────────────────── */
  var COUNTRY_TZ = {
    US:'America/New_York',  GB:'Europe/London',    CA:'America/Toronto',
    AU:'Australia/Sydney',  IE:'Europe/Dublin',    NZ:'Pacific/Auckland',
    SG:'Asia/Singapore',    AE:'Asia/Dubai',       IN:'Asia/Kolkata',
    PH:'Asia/Manila',       ZA:'Africa/Johannesburg',
    AR:'America/Argentina/Buenos_Aires', MX:'America/Mexico_City',
    CL:'America/Santiago',  CO:'America/Bogota',   PE:'America/Lima',
    UY:'America/Montevideo',VE:'America/Caracas',  BO:'America/La_Paz',
    PY:'America/Asuncion',  EC:'America/Guayaquil',CR:'America/Costa_Rica',
    PA:'America/Panama',    DO:'America/Santo_Domingo', PR:'America/Puerto_Rico',
    GT:'America/Guatemala', SV:'America/El_Salvador',  HN:'America/Tegucigalpa',
    NI:'America/Managua',   CU:'America/Havana',
    ES:'Europe/Madrid',     FR:'Europe/Paris',     BE:'Europe/Brussels',
    CH:'Europe/Zurich',     PT:'Europe/Lisbon',    DE:'Europe/Berlin',
    AT:'Europe/Vienna',     SE:'Europe/Stockholm', NO:'Europe/Oslo',
    DK:'Europe/Copenhagen', FI:'Europe/Helsinki',  NL:'Europe/Amsterdam',
    IT:'Europe/Rome',       GR:'Europe/Athens',
    BR:'America/Sao_Paulo', AO:'Africa/Luanda',    MZ:'Africa/Maputo',
  };

  /* ─── COUNTRY LIST (for picker UI) ─────────────────────────── */
  var COUNTRY_LIST = [
    {code:'global',flag:'🌍',name:'Global'},
    {code:'US',flag:'🇺🇸',name:'USA'},          {code:'GB',flag:'🇬🇧',name:'UK'},
    {code:'CA',flag:'🇨🇦',name:'Canada'},       {code:'AU',flag:'🇦🇺',name:'Australia'},
    {code:'IE',flag:'🇮🇪',name:'Ireland'},      {code:'NZ',flag:'🇳🇿',name:'New Zealand'},
    {code:'SG',flag:'🇸🇬',name:'Singapore'},    {code:'AE',flag:'🇦🇪',name:'UAE'},
    {code:'AR',flag:'🇦🇷',name:'Argentina'},    {code:'MX',flag:'🇲🇽',name:'México'},
    {code:'CL',flag:'🇨🇱',name:'Chile'},        {code:'CO',flag:'🇨🇴',name:'Colombia'},
    {code:'PE',flag:'🇵🇪',name:'Perú'},         {code:'UY',flag:'🇺🇾',name:'Uruguay'},
    {code:'VE',flag:'🇻🇪',name:'Venezuela'},    {code:'EC',flag:'🇪🇨',name:'Ecuador'},
    {code:'BO',flag:'🇧🇴',name:'Bolivia'},      {code:'PY',flag:'🇵🇾',name:'Paraguay'},
    {code:'CR',flag:'🇨🇷',name:'Costa Rica'},   {code:'PA',flag:'🇵🇦',name:'Panamá'},
    {code:'DO',flag:'🇩🇴',name:'Rep. Dominicana'},{code:'PR',flag:'🇵🇷',name:'Puerto Rico'},
    {code:'GT',flag:'🇬🇹',name:'Guatemala'},    {code:'SV',flag:'🇸🇻',name:'El Salvador'},
    {code:'HN',flag:'🇭🇳',name:'Honduras'},     {code:'NI',flag:'🇳🇮',name:'Nicaragua'},
    {code:'CU',flag:'🇨🇺',name:'Cuba'},         {code:'ES',flag:'🇪🇸',name:'España'},
    {code:'BR',flag:'🇧🇷',name:'Brasil'},       {code:'PT',flag:'🇵🇹',name:'Portugal'},
    {code:'FR',flag:'🇫🇷',name:'France'},       {code:'BE',flag:'🇧🇪',name:'Belgique'},
    {code:'CH',flag:'🇨🇭',name:'Schweiz'},      {code:'DE',flag:'🇩🇪',name:'Deutschland'},
    {code:'AT',flag:'🇦🇹',name:'Österreich'},   {code:'SE',flag:'🇸🇪',name:'Sverige'},
    {code:'NO',flag:'🇳🇴',name:'Norge'},        {code:'DK',flag:'🇩🇰',name:'Danmark'},
    {code:'FI',flag:'🇫🇮',name:'Finland'},      {code:'NL',flag:'🇳🇱',name:'Nederland'},
    {code:'IT',flag:'🇮🇹',name:'Italia'},       {code:'GR',flag:'🇬🇷',name:'Ελλάδα'},
  ];
  var FLAG_MAP = {};
  COUNTRY_LIST.forEach(function(c){FLAG_MAP[c.code]=c.flag;});

  function getCountryTZ() {
    var code = (typeof localStorage !== 'undefined' ? localStorage.getItem('cd_country') : null) || 'global';
    return COUNTRY_TZ[code] || null; /* null → use browser local time */
  }

  /* Compute midnight on year/month/day in the given IANA timezone.
     Falls back to browser local time if tz is null or Intl not available. */
  function midnightInTZ(tz, year, month, day) {
    if (!tz) return new Date(year, month, day);
    try {
      /* Reference: noon UTC on target day — safe from DST boundary issues */
      var ref = new Date(Date.UTC(year, month, day, 12));
      var parts = new Intl.DateTimeFormat('en-US', {
        timeZone: tz, hour12: false,
        year:'numeric', month:'2-digit', day:'2-digit',
        hour:'2-digit', minute:'2-digit'
      }).formatToParts(ref);
      var h = parseInt(parts.find(function(p){return p.type==='hour';}).value, 10);
      var m = parseInt(parts.find(function(p){return p.type==='minute';}).value, 10);
      var d = parseInt(parts.find(function(p){return p.type==='day';}).value, 10);
      /* Determine if tz shows a different day than `day` (east/west extremes) */
      var dayDiff = 0;
      if (d !== day) {
        if      (d > day  && d - day  <= 1)  dayDiff =  1;
        else if (d < day  && day - d  <= 1)  dayDiff = -1;
        else if (d === 1  && day >= 28)       dayDiff =  1;
        else if (d >= 28  && day === 1)       dayDiff = -1;
      }
      var adjH      = h + dayDiff * 24;
      var offsetMin = (adjH - 12) * 60 + m;
      return new Date(Date.UTC(year, month, day) - offsetMin * 60000);
    } catch (e) {
      return new Date(year, month, day);
    }
  }

  /* Convert a date returned by nthWeekday/lastWeekday to TZ-aware midnight */
  function tzDay(tz, date) {
    if (!tz) return date;
    return midnightInTZ(tz, date.getFullYear(), date.getMonth(), date.getDate());
  }

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

  /* ─── HEMISPHERE / NATIONAL DAYS / BACK-TO-SCHOOL / JEWISH ──── */
  var SOUTHERN_HEMISPHERE = {
    AR:1,BR:1,CL:1,BO:1,PY:1,PE:1,UY:1,ZA:1,AU:1,NZ:1,AO:1,MZ:1,EC:1
  };
  function isSouthern() {
    var c=(typeof localStorage!=='undefined'?localStorage.getItem('cd_country'):null)||'global';
    return !!SOUTHERN_HEMISPHERE[c];
  }
  function getCurrentCountry() {
    return (typeof localStorage!=='undefined'?localStorage.getItem('cd_country'):null)||'global';
  }

  /* Main national/independence day per country */
  var COUNTRY_NATIONAL_DATES = {
    US:{m:6,d:4},  CA:{m:6,d:1},  MX:{m:8,d:16}, GT:{m:8,d:15}, SV:{m:8,d:15},
    HN:{m:8,d:15}, NI:{m:8,d:15}, CR:{m:8,d:15},  PA:{m:10,d:3}, DO:{m:1,d:27},
    CU:{m:0,d:1},  PR:{m:6,d:4},  AR:{m:6,d:9},   CL:{m:8,d:18}, CO:{m:6,d:20},
    PE:{m:6,d:28}, EC:{m:7,d:10}, BO:{m:7,d:6},   PY:{m:4,d:14}, UY:{m:7,d:25},
    VE:{m:6,d:5},  BR:{m:8,d:7},  ES:{m:9,d:12},  FR:{m:6,d:14}, PT:{m:5,d:10},
    GB:{m:5,d:2},  IE:{m:2,d:17}, DE:{m:9,d:3},   IT:{m:5,d:2},  BE:{m:6,d:21},
    CH:{m:7,d:1},  AT:{m:9,d:26}, SE:{m:5,d:6},   NO:{m:4,d:17}, DK:{m:5,d:5},
    FI:{m:11,d:6}, NL:{m:3,d:27}, GR:{m:2,d:25},  AU:{m:0,d:26}, NZ:{m:1,d:6},
    SG:{m:7,d:9},  AE:{m:11,d:2}, IN:{m:7,d:15},  PH:{m:5,d:12}, ZA:{m:3,d:27},
    AO:{m:10,d:11},MZ:{m:5,d:25},
  };

  /* Typical first day back to school per country (month 0-indexed) */
  var COUNTRY_BACK_TO_SCHOOL = {
    AR:{m:2,d:2},  CL:{m:2,d:4},  UY:{m:2,d:2},  PY:{m:1,d:23}, BO:{m:1,d:2},
    PE:{m:2,d:16}, BR:{m:1,d:2},  AU:{m:0,d:28}, NZ:{m:1,d:2},  ZA:{m:0,d:14},
    AO:{m:0,d:15}, MZ:{m:0,d:15}, EC:{m:4,d:4},  VE:{m:8,d:15},
    US:{m:7,d:18}, CA:{m:8,d:8},  MX:{m:7,d:31}, ES:{m:8,d:7},  FR:{m:8,d:1},
    GB:{m:8,d:3},  DE:{m:8,d:15}, IT:{m:8,d:15}, PT:{m:8,d:14}, BE:{m:7,d:31},
    NL:{m:7,d:24}, IE:{m:8,d:1},  AT:{m:8,d:7},  CH:{m:7,d:17}, SE:{m:7,d:21},
    NO:{m:7,d:19}, DK:{m:7,d:13}, FI:{m:7,d:13}, GR:{m:8,d:8},
    IN:{m:5,d:11}, PH:{m:5,d:8},  SG:{m:0,d:2},  CO:{m:0,d:26}, DO:{m:7,d:25},
  };

  /* Start of winter/mid-year school break per country (month 0-indexed) */
  var COUNTRY_WINTER_VACATION = {
    /* Southern Hemisphere — mid-year break start (0-indexed months) */
    AR:{m:6,d:20}, CL:{m:5,d:22}, UY:{m:5,d:29}, PY:{m:6,d:13}, BO:{m:6,d:6},
    BR:{m:6,d:7},  PE:{m:6,d:27}, CO:{m:5,d:22}, AU:{m:6,d:6},  NZ:{m:6,d:4},
    ZA:{m:5,d:27},
    /* Northern Hemisphere — Christmas break */
    US:{m:11,d:20}, CA:{m:11,d:21}, MX:{m:11,d:20}, GB:{m:11,d:18},
    FR:{m:11,d:19}, DE:{m:11,d:23}, ES:{m:11,d:21}, IT:{m:11,d:23},
    PT:{m:11,d:16}, NL:{m:11,d:19}, BE:{m:11,d:21}, AT:{m:11,d:24},
  };

  /* Start of summer/end-of-year school break per country (month 0-indexed) */
  var COUNTRY_SUMMER_VACATION = {
    /* Southern Hemisphere — long summer break start (0-indexed months) */
    AR:{m:11,d:18}, CL:{m:11,d:18}, UY:{m:11,d:18}, PY:{m:10,d:30}, BO:{m:11,d:2},
    BR:{m:11,d:18}, PE:{m:11,d:18}, CO:{m:10,d:29}, AU:{m:11,d:17}, NZ:{m:11,d:18},
    ZA:{m:11,d:11},
    /* Northern Hemisphere — summer break start */
    US:{m:5,d:15}, CA:{m:5,d:26}, MX:{m:6,d:15}, GB:{m:6,d:22}, FR:{m:6,d:4},
    DE:{m:7,d:3},  ES:{m:5,d:19}, IT:{m:5,d:10}, PT:{m:5,d:12}, NL:{m:6,d:12},
    BE:{m:6,d:6},  AT:{m:6,d:4},
  };

  /* Jewish holiday dates — [year, month(0-based), day] when the holiday begins.
     Using the evening/sundown convention (when candles/fast begin). */
  var JEWISH_TABLE = {
    'rosh-hashana': [[2025,8,22],[2026,8,12],[2027,9,1],[2028,8,20]],
    'yom-kipur':    [[2025,9,1], [2026,8,21],[2027,9,10],[2028,8,29]],
    'januca':       [[2025,11,14],[2026,11,3],[2027,11,24],[2028,11,12]],
    'purim':        [[2026,2,3], [2027,2,22],[2028,2,11]],
    'pesaj':        [[2026,3,1], [2027,3,21],[2028,3,9]],
    'shavuot':      [[2026,4,21],[2027,5,10],[2028,4,29]],
  };

  function nextJewishHoliday(key) {
    var now=new Date(), tz=getCountryTZ(), entries=JEWISH_TABLE[key]||[];
    for(var i=0;i<entries.length;i++){
      var e=entries[i];
      var d=tz?midnightInTZ(tz,e[0],e[1],e[2]):new Date(e[0],e[1],e[2]);
      if(d>now)return d;
    }
    return null;
  }

  /* ─── AUTO DATE GETTERS ─────────────────────────────────────── */
  var AUTO = {
    /* ── Holidays ── */
    'christmas':        function () { var tz=getCountryTZ(); return { date: nextOccurrence(function (y) { return midnightInTZ(tz,y,11,25); }) }; },
    'new-year':         function () { var tz=getCountryTZ(); return { date: nextOccurrence(function (y) { return midnightInTZ(tz,y+1,0,1); }) }; },
    'next-year':        function () { var tz=getCountryTZ(); return { date: nextOccurrence(function (y) { return midnightInTZ(tz,y+1,0,1); }) }; },
    'halloween':        function () { var tz=getCountryTZ(); return { date: nextOccurrence(function (y) { return midnightInTZ(tz,y,9,31); }) }; },
    'valentines':       function () { var tz=getCountryTZ(); return { date: nextOccurrence(function (y) { return midnightInTZ(tz,y,1,14); }) }; },
    'easter':           function () { var tz=getCountryTZ(); return { date: nextOccurrence(function (y) { return tzDay(tz,easterDate(y)); }) }; },
    'st-patricks':      function () { var tz=getCountryTZ(); return { date: nextOccurrence(function (y) { return midnightInTZ(tz,y,2,17); }) }; },
    'dia-de-los-muertos': function () { var tz=getCountryTZ(); return { date: nextOccurrence(function (y) { return midnightInTZ(tz,y,10,1); }) }; },
    'cinco-de-mayo':    function () { var tz=getCountryTZ(); return { date: nextOccurrence(function (y) { return midnightInTZ(tz,y,4,5); }) }; },
    'fiestas-patrias':  function () { var tz=getCountryTZ(); return { date: nextOccurrence(function (y) { return midnightInTZ(tz,y,8,18); }) }; },
    'bastille-day':     function () { var tz=getCountryTZ(); return { date: nextOccurrence(function (y) { return midnightInTZ(tz,y,6,14); }) }; },
    'oktoberfest':      function () { var tz=getCountryTZ(); return { date: nextOccurrence(function (y) { return midnightInTZ(tz,y,8,19); }) }; },
    'dia-del-nino': function () {
      var tz = getCountryTZ();
      var country = (typeof localStorage !== 'undefined' ? localStorage.getItem('cd_country') : null) || 'global';
      return { date: nextOccurrence(function (y) {
        if (country === 'AE') return midnightInTZ(tz, y, 2, 15);
        if (country === 'NZ') return tzDay(tz, nthWeekday(y, 2, 1, 0));
        if (country === 'BO') return midnightInTZ(tz, y, 3, 12);
        if (country === 'ES') return midnightInTZ(tz, y, 3, 15);
        if (country === 'CO') return tzDay(tz, lastWeekday(y, 3, 6));
        if (country === 'MX') return midnightInTZ(tz, y, 3, 30);
        if (['EC','NI','PT','BE'].indexOf(country) >= 0) return midnightInTZ(tz, y, 5, 1);
        if (country === 'US') return tzDay(tz, nthWeekday(y, 5, 2, 0));
        if (['VE','PA','CU'].indexOf(country) >= 0) return tzDay(tz, nthWeekday(y, 6, 3, 0));
        if (country === 'PR') return tzDay(tz, nthWeekday(y, 7, 2, 0));
        if (['AR','UY','PE'].indexOf(country) >= 0) return tzDay(tz, nthWeekday(y, 7, 3, 0));
        if (country === 'PY') return midnightInTZ(tz, y, 7, 16);
        if (country === 'CR') return midnightInTZ(tz, y, 8, 9);
        if (country === 'HN') return midnightInTZ(tz, y, 8, 10);
        if (['DE','AT'].indexOf(country) >= 0) return midnightInTZ(tz, y, 8, 20);
        if (country === 'DO') return midnightInTZ(tz, y, 8, 29);
        if (['GT','SV'].indexOf(country) >= 0) return midnightInTZ(tz, y, 9, 1);
        if (country === 'SG') return tzDay(tz, nthWeekday(y, 9, 1, 5));
        if (country === 'BR') return midnightInTZ(tz, y, 9, 12);
        if (country === 'CL') return tzDay(tz, nthWeekday(y, 9, 4, 0));
        if (country === 'AU') return tzDay(tz, nthWeekday(y, 9, 4, 3));
        return midnightInTZ(tz, y, 10, 20);
      }) };
    },

    /* ── US Holidays ── */
    'thanksgiving': function () {
      var tz = getCountryTZ();
      var country = (typeof localStorage !== 'undefined' ? localStorage.getItem('cd_country') : null) || 'global';
      if (country === 'CA') {
        /* Canada: 2nd Monday of October */
        return { date: nextOccurrence(function (y) { return tzDay(tz, nthWeekday(y, 9, 2, 1)); }) };
      }
      /* US (default): 4th Thursday of November */
      return { date: nextOccurrence(function (y) { return tzDay(tz, nthWeekday(y, 10, 4, 4)); }) };
    },
    'independence-day': function () { var tz=getCountryTZ(); return { date: nextOccurrence(function (y) { return midnightInTZ(tz,y,6,4); }) }; },
    'memorial-day':     function () { var tz=getCountryTZ(); return { date: nextOccurrence(function (y) { return tzDay(tz,lastWeekday(y,4,1)); }) }; },
    'labor-day':        function () { var tz=getCountryTZ(); return { date: nextOccurrence(function (y) { return tzDay(tz,nthWeekday(y,8,1,1)); }) }; },
    'mothers-day': function () {
      var tz = getCountryTZ();
      var country = getCurrentCountry();
      var getDate;
      if (country === 'AR') {
        getDate = function (y) { return tzDay(tz, nthWeekday(y, 9, 3, 0)); };         /* 3rd Sun Oct */
      } else if (['MX','GT','SV'].indexOf(country) >= 0) {
        getDate = function (y) { return midnightInTZ(tz, y, 4, 10); };               /* May 10 fixed */
      } else if (country === 'GB' || country === 'IE') {
        getDate = function (y) {                                                        /* Mothering Sunday = Easter − 21 days */
          var e = easterDate(y);
          return tzDay(tz, new Date(e.getFullYear(), e.getMonth(), e.getDate() - 21));
        };
      } else if (country === 'FR' || country === 'SE' || country === 'DO') {
        getDate = function (y) { return tzDay(tz, lastWeekday(y, 4, 0)); };            /* Last Sun May */
      } else if (country === 'PT' || country === 'ES') {
        getDate = function (y) { return tzDay(tz, nthWeekday(y, 4, 1, 0)); };         /* 1st Sun May */
      } else if (country === 'BO') {
        getDate = function (y) { return midnightInTZ(tz, y, 4, 27); };               /* May 27 fixed */
      } else if (country === 'PY') {
        getDate = function (y) { return midnightInTZ(tz, y, 4, 15); };               /* May 15 fixed */
      } else if (country === 'NI') {
        getDate = function (y) { return midnightInTZ(tz, y, 4, 30); };               /* May 30 fixed */
      } else if (country === 'CR') {
        getDate = function (y) { return midnightInTZ(tz, y, 7, 15); };               /* Aug 15 fixed */
      } else if (country === 'PA') {
        getDate = function (y) { return midnightInTZ(tz, y, 11, 8); };               /* Dec 8 fixed */
      } else if (country === 'NO') {
        getDate = function (y) { return tzDay(tz, nthWeekday(y, 1, 2, 0)); };         /* 2nd Sun Feb */
      } else {
        getDate = function (y) { return tzDay(tz, nthWeekday(y, 4, 2, 0)); };         /* 2nd Sun May default */
      }
      return { date: nextOccurrence(getDate) };
    },
    'fathers-day': function () {
      var tz = getCountryTZ();
      var country = getCurrentCountry();
      var getDate;
      if (country === 'ES' || country === 'BO' || country === 'HN') {
        getDate = function (y) { return midnightInTZ(tz, y, 2, 19); };          /* March 19 */
      } else if (country === 'BR' || country === 'PT') {
        getDate = function (y) { return tzDay(tz, nthWeekday(y, 7, 2, 0)); };  /* 2nd Sun Aug */
      } else if (country === 'AU' || country === 'NZ') {
        getDate = function (y) { return tzDay(tz, nthWeekday(y, 8, 1, 0)); };  /* 1st Sun Sep */
      } else if (country === 'DE' || country === 'AT') {
        getDate = function (y) {                                                  /* Ascension Thu = Easter + 39 days */
          var e = easterDate(y);
          return tzDay(tz, new Date(e.getFullYear(), e.getMonth(), e.getDate() + 39));
        };
      } else if (country === 'UY') {
        getDate = function (y) { return tzDay(tz, nthWeekday(y, 6, 2, 0)); };  /* 2nd Sun Jul */
      } else if (country === 'GT' || country === 'SV') {
        getDate = function (y) { return midnightInTZ(tz, y, 5, 17); };         /* Jun 17 fixed */
      } else if (country === 'NI') {
        getDate = function (y) { return midnightInTZ(tz, y, 5, 23); };         /* Jun 23 fixed */
      } else if (country === 'DO') {
        getDate = function (y) { return tzDay(tz, lastWeekday(y, 6, 0)); };    /* Last Sun Jul */
      } else if (country === 'FI') {
        getDate = function (y) { return tzDay(tz, nthWeekday(y, 10, 2, 0)); }; /* 2nd Sun Nov */
      } else {
        getDate = function (y) { return tzDay(tz, nthWeekday(y, 5, 3, 0)); };  /* 3rd Sun Jun default */
      }
      return { date: nextOccurrence(getDate) };
    },

    /* ── Sports (recurring) ── */
    'super-bowl':       function () { var tz=getCountryTZ(); return { date: nextOccurrence(function (y) { return tzDay(tz,nthWeekday(y,1,2,0)); }), note: '2nd Sunday of February' }; },
    'oscars':           function () { var tz=getCountryTZ(); return { date: nextOccurrence(function (y) { return tzDay(tz,nthWeekday(y,1,4,0)); }), note: '~Last Sunday of February (estimated)' }; },
    'met-gala':         function () { var tz=getCountryTZ(); return { date: nextOccurrence(function (y) { return tzDay(tz,nthWeekday(y,4,1,1)); }) }; },

    /* ── Sales ── */
    'black-friday':     function () { var tz=getCountryTZ(); return { date: nextOccurrence(function (y) { return tzDay(tz,nthWeekday(y,10,4,5)); }) }; },
    'cyber-monday':     function () {
      var tz = getCountryTZ();
      return {
        date: nextOccurrence(function (y) {
          var bf = nthWeekday(y, 10, 4, 5);
          return tzDay(tz, new Date(bf.getFullYear(), bf.getMonth(), bf.getDate() + 3));
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
    '25-de-mayo':       function () { var tz=getCountryTZ(); return { date: nextOccurrence(function (y) { return midnightInTZ(tz,y,4,25); }) }; },
    'dia-del-nino': function () {
      var tz = getCountryTZ();
      var country = getCurrentCountry();
      if (country === 'MX') {
        return { date: nextOccurrence(function (y) { return midnightInTZ(tz, y, 3, 30); }) };   /* Apr 30 */
      } else if (country === 'AE') {
        return { date: nextOccurrence(function (y) { return midnightInTZ(tz, y, 2, 15); }) };   /* Mar 15 */
      } else if (country === 'BO') {
        return { date: nextOccurrence(function (y) { return midnightInTZ(tz, y, 3, 12); }) };   /* Apr 12 */
      } else if (country === 'ES') {
        return { date: nextOccurrence(function (y) { return midnightInTZ(tz, y, 3, 15); }) };   /* Apr 15 */
      } else if (country === 'CO') {
        return { date: nextOccurrence(function (y) { return tzDay(tz, lastWeekday(y, 3, 6)); }) }; /* Last Sat Apr */
      } else if (country === 'EC' || country === 'NI' || country === 'PT' || country === 'BE') {
        return { date: nextOccurrence(function (y) { return midnightInTZ(tz, y, 5, 1); }) };    /* Jun 1 */
      } else if (country === 'US') {
        return { date: nextOccurrence(function (y) { return tzDay(tz, nthWeekday(y, 5, 2, 0)); }) }; /* 2nd Sun Jun */
      } else if (country === 'VE' || country === 'PA' || country === 'CU') {
        return { date: nextOccurrence(function (y) { return tzDay(tz, nthWeekday(y, 6, 3, 0)); }) }; /* 3rd Sun Jul */
      } else if (country === 'AR' || country === 'UY' || country === 'PE') {
        return { date: nextOccurrence(function (y) { return tzDay(tz, nthWeekday(y, 7, 3, 0)); }) }; /* 3rd Sun Aug */
      } else if (country === 'PY') {
        return { date: nextOccurrence(function (y) { return midnightInTZ(tz, y, 7, 16); }) };   /* Aug 16 */
      } else if (country === 'PR') {
        return { date: nextOccurrence(function (y) { return tzDay(tz, nthWeekday(y, 7, 2, 0)); }) }; /* 2nd Sun Aug */
      } else if (country === 'CR') {
        return { date: nextOccurrence(function (y) { return midnightInTZ(tz, y, 8, 9); }) };    /* Sep 9 */
      } else if (country === 'HN') {
        return { date: nextOccurrence(function (y) { return midnightInTZ(tz, y, 8, 10); }) };   /* Sep 10 */
      } else if (country === 'DO') {
        return { date: nextOccurrence(function (y) { return midnightInTZ(tz, y, 8, 29); }) };   /* Sep 29 */
      } else if (country === 'DE' || country === 'AT') {
        return { date: nextOccurrence(function (y) { return midnightInTZ(tz, y, 8, 20); }) };   /* Sep 20 */
      } else if (country === 'GT' || country === 'SV') {
        return { date: nextOccurrence(function (y) { return midnightInTZ(tz, y, 9, 1); }) };    /* Oct 1 */
      } else if (country === 'SG') {
        return { date: nextOccurrence(function (y) { return tzDay(tz, nthWeekday(y, 9, 1, 5)); }) }; /* 1st Fri Oct */
      } else if (country === 'AU') {
        return { date: nextOccurrence(function (y) { return tzDay(tz, nthWeekday(y, 9, 4, 3)); }) }; /* 4th Wed Oct */
      } else if (country === 'CL') {
        return { date: nextOccurrence(function (y) { return tzDay(tz, nthWeekday(y, 9, 4, 0)); }) }; /* 4th Sun Oct */
      } else if (country === 'BR') {
        return { date: nextOccurrence(function (y) { return midnightInTZ(tz, y, 9, 12); }) };   /* Oct 12 */
      } else if (country === 'NZ') {
        return { date: nextOccurrence(function (y) { return tzDay(tz, nthWeekday(y, 2, 1, 0)); }) }; /* 1st Sun Mar */
      } else {
        return { date: nextOccurrence(function (y) { return midnightInTZ(tz, y, 10, 20); }) };  /* Nov 20 UN Day */
      }
    },

    /* ── One-time political ── */
    'elecciones-ar':    function () { return { date: new Date(2027, 9, 26, 8, 0, 0), note: 'Estimated date. Argentine general elections 2027.' }; },

    /* ── LA 2028 Olympics ── */
    'olympics-2028':    function () { return { date: new Date(2028, 6, 14, 20, 0, 0), note: 'Los Angeles 2028 — Opening Ceremony' }; },

    /* ── Months (always next occurrence of the 1st of that month) ── */
    'january':   function(){var tz=getCountryTZ();return{date:nextOccurrence(function(y){return midnightInTZ(tz,y,0,1);})};},
    'february':  function(){var tz=getCountryTZ();return{date:nextOccurrence(function(y){return midnightInTZ(tz,y,1,1);})};},
    'march':     function(){var tz=getCountryTZ();return{date:nextOccurrence(function(y){return midnightInTZ(tz,y,2,1);})};},
    'april':     function(){var tz=getCountryTZ();return{date:nextOccurrence(function(y){return midnightInTZ(tz,y,3,1);})};},
    'may-month': function(){var tz=getCountryTZ();return{date:nextOccurrence(function(y){return midnightInTZ(tz,y,4,1);})};},
    'june-month':function(){var tz=getCountryTZ();return{date:nextOccurrence(function(y){return midnightInTZ(tz,y,5,1);})};},
    'july-month':function(){var tz=getCountryTZ();return{date:nextOccurrence(function(y){return midnightInTZ(tz,y,6,1);})};},
    'august':    function(){var tz=getCountryTZ();return{date:nextOccurrence(function(y){return midnightInTZ(tz,y,7,1);})};},
    'september': function(){var tz=getCountryTZ();return{date:nextOccurrence(function(y){return midnightInTZ(tz,y,8,1);})};},
    'october':   function(){var tz=getCountryTZ();return{date:nextOccurrence(function(y){return midnightInTZ(tz,y,9,1);})};},
    'november':  function(){var tz=getCountryTZ();return{date:nextOccurrence(function(y){return midnightInTZ(tz,y,10,1);})};},
    'december':  function(){var tz=getCountryTZ();return{date:nextOccurrence(function(y){return midnightInTZ(tz,y,11,1);})};},

    /* ── Midnight (next midnight in selected country's timezone) ── */
    'midnight': function(){
      var tz=getCountryTZ(), now=new Date();
      var cursor=new Date(now), midnight, attempts=0;
      do {
        midnight=midnightInTZ(tz,cursor.getFullYear(),cursor.getMonth(),cursor.getDate());
        if(midnight<=now){ cursor.setDate(cursor.getDate()+1); }
        attempts++;
      } while(midnight<=now && attempts<4);
      return{date:midnight};
    },

    /* ── Seasons (hemisphere-aware via selected country) ── */
    'spring': function(){
      var tz=getCountryTZ(),s=isSouthern();
      /* Northern: Mar 20 | Southern: Sep 23 */
      return{date:nextOccurrence(function(y){return midnightInTZ(tz,y,s?8:2,s?23:20);})};
    },
    'summer': function(){
      var tz=getCountryTZ(),s=isSouthern();
      /* Northern: Jun 21 | Southern: Dec 21 */
      return{date:nextOccurrence(function(y){return midnightInTZ(tz,y,s?11:5,21);})};
    },
    'autumn': function(){
      var tz=getCountryTZ(),s=isSouthern();
      /* Northern: Sep 23 | Southern: Mar 20 */
      return{date:nextOccurrence(function(y){return midnightInTZ(tz,y,s?2:8,s?20:23);})};
    },
    'winter-season': function(){
      var tz=getCountryTZ(),s=isSouthern();
      /* Northern: Dec 21 | Southern: Jun 21 */
      return{date:nextOccurrence(function(y){return midnightInTZ(tz,y,s?5:11,21);})};
    },

    /* ── School (country-aware) ── */
    'back-to-school': function(){
      var tz=getCountryTZ(),c=getCurrentCountry();
      var def=isSouthern()?{m:2,d:4}:{m:7,d:25};
      var dt=COUNTRY_BACK_TO_SCHOOL[c]||def;
      return{date:nextOccurrence(function(y){return midnightInTZ(tz,y,dt.m,dt.d);})};
    },
    'summer-vacation': function(){
      var tz=getCountryTZ(),s=isSouthern(),c=getCurrentCountry();
      var def=s?{m:11,d:15}:{m:5,d:15};
      var dt=COUNTRY_SUMMER_VACATION[c]||def;
      return{date:nextOccurrence(function(y){return midnightInTZ(tz,y,dt.m,dt.d);})};
    },
    'winter-vacation': function(){
      var tz=getCountryTZ(),s=isSouthern(),c=getCurrentCountry();
      var def=s?{m:6,d:20}:{m:11,d:20};
      var dt=COUNTRY_WINTER_VACATION[c]||def;
      return{date:nextOccurrence(function(y){return midnightInTZ(tz,y,dt.m,dt.d);})};
    },

    /* ── Independence Day (adaptive: changes with selected country) ── */
    'independence': function(){
      var tz=getCountryTZ(),c=getCurrentCountry();
      var dt=COUNTRY_NATIONAL_DATES[c]||{m:6,d:4};
      return{date:nextOccurrence(function(y){return midnightInTZ(tz,y,dt.m,dt.d);})};
    },

    /* ── Other country-specific national dates ── */
    'dia-de-la-bandera':     function(){var tz=getCountryTZ();return{date:nextOccurrence(function(y){return midnightInTZ(tz,y,5,20);})};},  /* Jun 20 AR */
    'dia-de-la-revolucion':  function(){var tz=getCountryTZ();return{date:nextOccurrence(function(y){return midnightInTZ(tz,y,10,20);})};}, /* Nov 20 MX */
    'dia-de-la-constitucion':function(){var tz=getCountryTZ();return{date:nextOccurrence(function(y){return midnightInTZ(tz,y,1,5);})};},   /* Feb 5 MX */
    'proclamacao-da-republica':function(){var tz=getCountryTZ();return{date:nextOccurrence(function(y){return midnightInTZ(tz,y,10,15);})};},/* Nov 15 BR */
    'tiradentes':            function(){var tz=getCountryTZ();return{date:nextOccurrence(function(y){return midnightInTZ(tz,y,3,21);})};},   /* Apr 21 BR */
    'proclamacion-independencia-ar':function(){var tz=getCountryTZ();return{date:nextOccurrence(function(y){return midnightInTZ(tz,y,4,25);})};},/* May 25 AR */
    'dia-de-la-hispanidad':  function(){var tz=getCountryTZ();return{date:nextOccurrence(function(y){return midnightInTZ(tz,y,9,12);})};},   /* Oct 12 ES */
    'german-unity-day':      function(){var tz=getCountryTZ();return{date:nextOccurrence(function(y){return midnightInTZ(tz,y,9,3);})};},    /* Oct 3 DE */
    'australia-day':         function(){var tz=getCountryTZ();return{date:nextOccurrence(function(y){return midnightInTZ(tz,y,0,26);})};},   /* Jan 26 AU */
    'canada-day':            function(){var tz=getCountryTZ();return{date:nextOccurrence(function(y){return midnightInTZ(tz,y,6,1);})};},    /* Jul 1 CA */
    'syttende-mai':          function(){var tz=getCountryTZ();return{date:nextOccurrence(function(y){return midnightInTZ(tz,y,4,17);})};},   /* May 17 NO */
    'festa-della-repubblica':function(){var tz=getCountryTZ();return{date:nextOccurrence(function(y){return midnightInTZ(tz,y,5,2);})};},    /* Jun 2 IT */
    'waitangi-day':          function(){var tz=getCountryTZ();return{date:nextOccurrence(function(y){return midnightInTZ(tz,y,1,6);})};},    /* Feb 6 NZ */
    'national-day-sg':       function(){var tz=getCountryTZ();return{date:nextOccurrence(function(y){return midnightInTZ(tz,y,7,9);})};},    /* Aug 9 SG */
    'dia-de-la-raza':        function(){var tz=getCountryTZ();return{date:nextOccurrence(function(y){return midnightInTZ(tz,y,9,12);})};},   /* Oct 12 CO/LA */
    'freedom-day-za':        function(){var tz=getCountryTZ();return{date:nextOccurrence(function(y){return midnightInTZ(tz,y,3,27);})};},   /* Apr 27 ZA */

    /* ── Epiphany / Three Kings Day ── */
    'epiphany': function(){var tz=getCountryTZ();return{date:nextOccurrence(function(y){return midnightInTZ(tz,y,0,6);})};},

    /* ── Rio Carnival (Mardi Gras = Easter − 47 days) ── */
    'rio-carnival': function(){
      var tz=getCountryTZ();
      return{date:nextOccurrence(function(y){
        var e=easterDate(y);
        var fat=new Date(e.getFullYear(),e.getMonth(),e.getDate()-47);
        return tzDay(tz,fat);
      })};
    },

    /* ── CES Las Vegas (~Jan 6 each year) ── */
    'ces': function(){var tz=getCountryTZ();return{date:nextOccurrence(function(y){return midnightInTZ(tz,y,0,6);})};},

    /* ── Balón de Oro (last Monday of October) ── */
    'balon-de-oro': function(){var tz=getCountryTZ();return{date:nextOccurrence(function(y){return tzDay(tz,lastWeekday(y,9,1));})};},

    /* ── Mr. Olympia (4th Thursday of September, Las Vegas) ── */
    'mr-olympia': function(){var tz=getCountryTZ();return{date:nextOccurrence(function(y){return tzDay(tz,nthWeekday(y,8,4,4));})};},

    /* ── Arnold Classic (1st Thursday of March) ── */
    'arnold-classic': function(){var tz=getCountryTZ();return{date:nextOccurrence(function(y){return tzDay(tz,nthWeekday(y,2,1,4));})};},

    /* ── Jewish Holidays ── */
    'rosh-hashana': function(){return{date:nextJewishHoliday('rosh-hashana'),note:'Rosh Hashanah — Jewish New Year'};},
    'yom-kipur':    function(){return{date:nextJewishHoliday('yom-kipur'),   note:'Yom Kippur — Day of Atonement'};},
    'januca':       function(){return{date:nextJewishHoliday('januca'),       note:'Hanukkah — first candle'};},
    'purim':        function(){return{date:nextJewishHoliday('purim')};},
    'pesaj':        function(){return{date:nextJewishHoliday('pesaj'),        note:'Passover — first seder night'};},
    'shavuot':      function(){return{date:nextJewishHoliday('shavuot')};},
  };

  /* ─── COUNTRY PICKER (shared modal for all pages) ───────────── */
  function openCountryPicker(onSelect) {
    var overlay = document.createElement('div');
    overlay.className = 'cd-cpicker-overlay';
    var saved = (typeof localStorage !== 'undefined' ? localStorage.getItem('cd_country') : null) || 'global';
    overlay.innerHTML =
      '<div class="cd-cpicker-modal">' +
        '<h2 class="cd-cpicker-title">Select your country</h2>' +
        '<input class="cd-cpicker-search" id="cd-cpicker-q" type="text" placeholder="Search…" autocomplete="off" spellcheck="false">' +
        '<div class="cd-cpicker-grid" id="cd-cpicker-items"></div>' +
      '</div>';
    document.body.appendChild(overlay);
    document.body.style.overflow = 'hidden';

    var grid = document.getElementById('cd-cpicker-items');

    function renderItems(filter) {
      grid.innerHTML = COUNTRY_LIST.filter(function(c) {
        if (!filter) return true;
        return c.name.toLowerCase().indexOf(filter) >= 0 ||
               c.code.toLowerCase().indexOf(filter) >= 0;
      }).map(function(c) {
        return '<button class="cd-cpicker-item' + (c.code === saved ? ' selected' : '') +
               '" data-code="' + c.code + '">' +
               '<span class="cd-cpicker-flag">' + c.flag + '</span>' + c.name + '</button>';
      }).join('');
      grid.querySelectorAll('.cd-cpicker-item').forEach(function(btn) {
        btn.addEventListener('click', function() {
          document.body.removeChild(overlay);
          document.body.style.overflow = '';
          onSelect(btn.dataset.code);
        });
      });
    }

    renderItems('');
    var searchEl = document.getElementById('cd-cpicker-q');
    if (searchEl) {
      searchEl.oninput = function() { renderItems(this.value.toLowerCase()); };
      setTimeout(function() { searchEl.focus(); }, 80);
    }
    overlay.addEventListener('click', function(e) {
      if (e.target === overlay) { document.body.removeChild(overlay); document.body.style.overflow = ''; }
    });
  }

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

  function fmtDate(d, lang, tz) {
    var locale = lang === 'es' ? 'es' : lang === 'pt' ? 'pt-BR' : lang === 'fr' ? 'fr' : lang === 'de' ? 'de' : 'en-US';
    var opts = { weekday: 'long', year: 'numeric', month: 'long', day: 'numeric' };
    if (tz) { try { opts.timeZone = tz; } catch(e) {} }
    return d.toLocaleDateString(locale, opts);
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
      if (diff <= 0) {
        clearInterval(_tickerHandle); _tickerHandle = null;
        // Switch to elapsed (counting-up) mode
        var desc = document.querySelector('.cd-desc');
        if (desc) desc.textContent = T.elapsed;
        var grid = document.querySelector('.cd-grid');
        if (grid) {
          grid.classList.add('cd-grid--elapsed');
          var dateLabel = document.querySelector('.cd-date-label');
          if (dateLabel) {
            dateLabel.className = 'cd-elapsed-label';
            dateLabel.textContent = T.since + ' ' + fmtDate(targetDate, _pageLang);
          }
        }
        startElapsedTicker(targetDate);
        return;
      }
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

  /* ─── ELAPSED TICKER (counts up after event) ───────────────── */
  function startElapsedTicker(targetDate) {
    if (_tickerHandle) { clearInterval(_tickerHandle); _tickerHandle = null; }
    function tick() {
      var elapsed = new Date() - targetDate;
      var days  = Math.floor(elapsed / 86400000);
      var hours = Math.floor((elapsed % 86400000) / 3600000);
      var mins  = Math.floor((elapsed % 3600000) / 60000);
      var secs  = Math.floor((elapsed % 60000) / 1000);
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
    var embedBase = 'https://countdowns.site' + (_pageLang !== 'en' ? '/' + _pageLang : '');
    var embedSrc = embedBase + '/embed/' + slug + '/';
    var pageLink = 'https://countdowns.site' + (_pageLang !== 'en' ? '/' + _pageLang : '') + '/countdown/' + slug + '/';
    var iframeCode = '<iframe src="' + embedSrc + '" width="320" height="200" frameborder="0" style="border-radius:16px;overflow:hidden" allowtransparency="true"></iframe>\n<p style="font-size:11px;text-align:center;margin:4px 0;font-family:sans-serif"><a href="' + pageLink + '" style="color:#888;text-decoration:none" target="_blank">countdowns.site</a></p>';
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
  function buildCountdownSection(targetDate, isPast, isUnknown, note, isElapsed) {
    if (isUnknown) {
      return '<div class="cd-unknown"><div class="cd-unknown-text">' + T.dateTBC + '</div>' +
             (note ? '<div class="cd-unknown-sub">' + note + '</div>' : '') + '</div>';
    }
    if (isPast) {
      return '<div class="cd-past"><div class="cd-past-badge">' + T.alreadyHappened + '</div>' +
             '<div class="cd-past-date">' + fmtDate(targetDate, _pageLang) + '</div></div>';
    }
    var gridClass = isElapsed ? 'cd-grid cd-grid--elapsed' : 'cd-grid';
    var bottomLabel = isElapsed
      ? '<div class="cd-elapsed-label">' + T.since + ' ' + fmtDate(targetDate, _pageLang) + '</div>'
      : '<div class="cd-date-label">' + fmtDate(targetDate, _pageLang, getCountryTZ()) + '</div>';
    return [
      '<div class="' + gridClass + '">',
      '<div class="cd-box"><div class="cd-num" id="cd-d">—</div><div class="cd-lbl">' + T.days + '</div></div>',
      '<div class="cd-sep">:</div>',
      '<div class="cd-box"><div class="cd-num" id="cd-h">—</div><div class="cd-lbl">' + T.hours + '</div></div>',
      '<div class="cd-sep">:</div>',
      '<div class="cd-box"><div class="cd-num" id="cd-m">—</div><div class="cd-lbl">' + T.min + '</div></div>',
      '<div class="cd-sep">:</div>',
      '<div class="cd-box"><div class="cd-num" id="cd-s">—</div><div class="cd-lbl">' + T.sec + '</div></div>',
      '</div>',
      bottomLabel,
    ].join('');
  }

  function buildPage(config, targetDate, extra, isPast, isUnknown, isElapsed) {
    var cc = catColors(config.category);
    var note     = (extra && extra.note) || config.note || '';
    var subtitle = (extra && extra.subtitle) || '';
    var cdSection = buildCountdownSection(targetDate, isPast, isUnknown, note, isElapsed);

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
      '<p class="cd-desc">' + (isElapsed ? T.elapsed : (config.description || '')) + '</p>',
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

  /* ─── EMBED WIDGET ─────────────────────────────────────────── */
  function buildEmbedWidget(config, targetDate, extra, isPast, isUnknown) {
    var cc       = catColors(config.category);
    var subtitle = (extra && extra.subtitle) || '';
    var dispName = config.name + (subtitle ? ' — ' + subtitle : '');
    var langPfx  = _pageLang !== 'en' ? '/' + _pageLang : '';
    var pageUrl  = config.pageUrl || ('https://countdowns.site' + langPfx + '/countdown/' + (config.slug || '') + '/');

    var timerHTML;
    if (isUnknown) {
      timerHTML = '<div class="wd-tbc">' + T.dateTBC + '</div>';
    } else if (isPast) {
      timerHTML = '<div class="wd-tbc">' + T.alreadyHappened + '</div>';
    } else {
      timerHTML = [
        '<div class="wd-grid">',
        '<div class="wd-box"><span class="cd-num" id="cd-d">—</span><span class="wd-lbl">' + T.days + '</span></div>',
        '<span class="wd-sep">:</span>',
        '<div class="wd-box"><span class="cd-num" id="cd-h">—</span><span class="wd-lbl">' + T.hours + '</span></div>',
        '<span class="wd-sep">:</span>',
        '<div class="wd-box"><span class="cd-num" id="cd-m">—</span><span class="wd-lbl">' + T.min + '</span></div>',
        '<span class="wd-sep">:</span>',
        '<div class="wd-box"><span class="cd-num" id="cd-s">—</span><span class="wd-lbl">' + T.sec + '</span></div>',
        '</div>',
        '<div class="wd-date">' + fmtDate(targetDate, _pageLang) + '</div>',
      ].join('');
    }

    return [
      '<div class="wd-widget" style="--cat:' + cc.color + ';--cat-glow:' + cc.glow + '">',
      '<div class="wd-badge">' + tCat(config.category || '') + '</div>',
      '<div class="wd-name">' + dispName + '</div>',
      timerHTML,
      '<a href="' + pageUrl + '" class="wd-brand" target="_blank" rel="noopener">countdowns.site</a>',
      '</div>',
    ].join('');
  }

  /* ─── PUBLIC API ────────────────────────────────────────────── */
  window.CountdownEngine = {

    render: function (rootId, config) {
      var root = document.getElementById(rootId);
      if (!root) return;

      function patchEventSchema(targetDate) {
        if (!targetDate) return;
        try {
          var scripts = document.querySelectorAll('script[type="application/ld+json"]');
          for (var i = 0; i < scripts.length; i++) {
            var text = scripts[i].textContent || '';
            if (text.indexOf('"Event"') === -1) continue;
            var data = JSON.parse(text);
            var nodes = data['@graph'] ? data['@graph'] : [data];
            var changed = false;
            for (var j = 0; j < nodes.length; j++) {
              var node = nodes[j];
              if (node['@type'] !== 'Event') continue;
              if (!node.startDate)   { node.startDate   = targetDate.toISOString(); changed = true; }
              if (!node.endDate)     { node.endDate     = targetDate.toISOString(); changed = true; }
              if (!node.location)    { node.location    = { '@type': 'Place', 'name': 'Worldwide' }; changed = true; }
              if (!node.eventStatus) { node.eventStatus = 'https://schema.org/EventScheduled'; changed = true; }
            }
            if (changed) scripts[i].textContent = JSON.stringify(data);
            break;
          }
        } catch (e) {}
      }

      function init(targetDate, extra) {
        var now       = new Date();
        var isElapsed = !!(targetDate && targetDate < now &&
                          config.type !== 'auto' && config.type !== 'annual' && config.type !== 'schedule');
        var isPast    = false; // legacy static badge — superseded by elapsed ticker
        var isUnknown = !targetDate;
        root.innerHTML = buildPage(config, targetDate, extra || {}, isPast, isUnknown, isElapsed);
        setupShare(config);
        if (!isUnknown) {
          if (isElapsed) {
            startElapsedTicker(targetDate);
          } else {
            startTicker(targetDate);
          }
        }
        patchEventSchema(targetDate);
      }

      if (config.type === 'fixed') {
        init(config.date || null, {});
      } else if (config.type === 'auto') {
        var getter = AUTO[config.slug];
        if (!getter) { root.textContent = '[Engine] No auto getter for: ' + config.slug; return; }
        var res = getter();
        init(res.date, res);
      } else if (config.type === 'annual') {
        loadData(function (data) {
          var ev   = ((data || {}).events || {})[config.slug] || {};
          var _lang = (window.location.pathname.match(/^\/(es|pt|fr)\//) || [])[1] || 'en';
          var _note = (_lang !== 'en' && ev['note_' + _lang]) || ev.note || '';
          var date = null;
          if (ev.date) {
            var dp = ev.date.split('T')[0].split('-');
            var mo = parseInt(dp[1], 10) - 1;
            var dy = parseInt(dp[2], 10);
            var tz = getCountryTZ();
            date = nextOccurrence(function (y) { return midnightInTZ(tz, y, mo, dy); });
          }
          init(date, { note: _note });
        });
      } else if (config.type === 'schedule') {
        loadData(function (data) {
          var ev = ((data || {}).events || {})[config.slug] || {};
          var schedule = ev.schedule || [];
          var _lang = (window.location.pathname.match(/^\/(es|pt|fr)\//) || [])[1] || 'en';
          function findNext() {
            var now = new Date();
            for (var i = 0; i < schedule.length; i++) {
              if (new Date(schedule[i].date) > now) return schedule[i];
            }
            return null;
          }
          var race = findNext();
          if (race) {
            var _note = race['note_' + _lang] || race.note || '';
            var targetDate = new Date(race.date);
            init(targetDate, { note: _note, subtitle: race.raceName || '' });
            /* Auto-advance: when this race passes, re-init with next */
            var _advGuard = setInterval(function() {
              if (new Date() > targetDate) {
                clearInterval(_advGuard);
                setTimeout(function() {
                  var next = findNext();
                  if (next) {
                    var n = next['note_' + _lang] || next.note || '';
                    init(new Date(next.date), { note: n, subtitle: next.raceName || '' });
                  }
                }, 3000);
              }
            }, 15000);
          } else {
            var _note2 = ev['note_' + _lang] || ev.note || '';
            init(null, { note: _note2 });
          }
        });
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
        if (days < 0) { cb({ state: 'unknown' }); return; } // recurring past date (>1 day ago) → TBC
        cb({ state: days === 0 ? 'today' : 'future', days: days, date: date });
      }

      if (config.type === 'auto') {
        var getter = AUTO[config.slug];
        if (!getter) { cb({ state: 'unknown' }); return; }
        var res = getter();
        resolve(res.date, false);
      } else if (config.type === 'annual') {
        loadData(function (data) {
          var ev   = ((data || {}).events || {})[config.slug] || {};
          var date = null;
          if (ev.date) {
            var dp = ev.date.split('T')[0].split('-');
            var mo = parseInt(dp[1], 10) - 1;
            var dy = parseInt(dp[2], 10);
            var tz = getCountryTZ();
            date = nextOccurrence(function (y) { return midnightInTZ(tz, y, mo, dy); });
          }
          resolve(date, false);
        });
      } else if (config.type === 'schedule') {
        loadData(function (data) {
          var ev = ((data || {}).events || {})[config.slug] || {};
          var schedule = ev.schedule || [];
          var now = new Date();
          var nextDate = null;
          for (var i = 0; i < schedule.length; i++) {
            var d = new Date(schedule[i].date);
            if (d > now) { nextDate = d; break; }
          }
          resolve(nextDate, false);
        });
      } else {
        loadData(function (data) {
          var ev   = ((data || {}).events || {})[config.slug] || {};
          var date = ev.date ? new Date(ev.date) : null;
          // Fallback: if no JSON data found, try AUTO getter (handles recurring events)
          if (!date && AUTO[config.slug]) {
            var res = AUTO[config.slug]();
            resolve(res.date, false);
            return;
          }
          var _isPastType = config.type === 'one-time' || config.type === 'variable' || config.type === 'fixed';
          resolve(date, !!(_isPastType && date && date < new Date()));
        });
      }
    },

    renderEmbed: function (rootId, config) {
      var root = document.getElementById(rootId);
      if (!root) return;

      function initEmbed(targetDate, extra) {
        var isPast    = config.type === 'one-time' && targetDate && targetDate < new Date();
        var isUnknown = !targetDate;
        root.innerHTML = buildEmbedWidget(config, targetDate, extra || {}, isPast, isUnknown);
        if (!isPast && !isUnknown) startTicker(targetDate);
      }

      if (config.type === 'fixed') {
        initEmbed(config.date || null, {});
      } else if (config.type === 'auto') {
        var getter = AUTO[config.slug];
        if (!getter) { root.textContent = '—'; return; }
        var res = getter();
        initEmbed(res.date, res);
      } else if (config.type === 'annual') {
        loadData(function (data) {
          var ev   = ((data || {}).events || {})[config.slug] || {};
          var _note = (_pageLang !== 'en' && ev['note_' + _pageLang]) || ev.note || '';
          var date = null;
          if (ev.date) {
            var dp = ev.date.split('T')[0].split('-');
            var mo = parseInt(dp[1], 10) - 1;
            var dy = parseInt(dp[2], 10);
            var tz = getCountryTZ();
            date = nextOccurrence(function (y) { return midnightInTZ(tz, y, mo, dy); });
          }
          initEmbed(date, { note: _note });
        });
      } else if (config.type === 'schedule') {
        loadData(function (data) {
          var ev = ((data || {}).events || {})[config.slug] || {};
          var schedule = ev.schedule || [];
          var _lang2 = (window.location.pathname.match(/^\/(es|pt|fr)\//) || [])[1] || 'en';
          function findNextEmbed() {
            var now = new Date();
            for (var i = 0; i < schedule.length; i++) {
              if (new Date(schedule[i].date) > now) return schedule[i];
            }
            return null;
          }
          var race2 = findNextEmbed();
          if (race2) {
            var _n2 = race2['note_' + _lang2] || race2.note || '';
            initEmbed(new Date(race2.date), { note: _n2, subtitle: race2.raceName || '' });
          } else {
            initEmbed(null, {});
          }
        });
      } else {
        loadData(function (data) {
          var ev   = ((data || {}).events || {})[config.slug] || {};
          var date = ev.date ? new Date(ev.date) : null;
          var _lang = _pageLang;
          var _note = (_lang !== 'en' && ev['note_' + _lang]) || ev.note || '';
          initEmbed(date, { note: _note, subtitle: ev.raceName || '' });
        });
      }
    },

    catColors: catColors,
    fmtDate:   fmtDate,
    openCountryPicker: openCountryPicker,
    FLAG_MAP:          FLAG_MAP,
    COUNTRY_LIST:      COUNTRY_LIST,
    getCurrentFlag:    function() {
      var code = (typeof localStorage !== 'undefined' ? localStorage.getItem('cd_country') : null) || 'global';
      return FLAG_MAP[code] || '🌍';
    },
  };

  /* ─── THEME TOGGLE (sun/moon icons) ────────────────────────────── */
  function initThemeToggle() {
    var oldBtn = document.getElementById('theme-toggle');
    if (!oldBtn) return;
    /* Apply saved theme early */
    if (typeof localStorage !== 'undefined' && localStorage.getItem('cd_theme') === 'light') {
      document.documentElement.setAttribute('data-theme', 'light');
    }
    var SUN  = '<svg xmlns="http://www.w3.org/2000/svg" width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="4"/><line x1="12" y1="2" x2="12" y2="5"/><line x1="12" y1="19" x2="12" y2="22"/><line x1="4.22" y1="4.22" x2="6.34" y2="6.34"/><line x1="17.66" y1="17.66" x2="19.78" y2="19.78"/><line x1="2" y1="12" x2="5" y2="12"/><line x1="19" y1="12" x2="22" y2="12"/><line x1="4.22" y1="19.78" x2="6.34" y2="17.66"/><line x1="17.66" y1="6.34" x2="19.78" y2="4.22"/></svg>';
    var MOON = '<svg xmlns="http://www.w3.org/2000/svg" width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"/></svg>';
    /* Clone to remove any prior click handlers from inline page scripts */
    var btn = oldBtn.cloneNode(false);
    oldBtn.parentNode.replaceChild(btn, oldBtn);
    function updateIcon() {
      var light = document.documentElement.getAttribute('data-theme') === 'light';
      btn.innerHTML = light ? MOON : SUN;
      btn.setAttribute('aria-label', light ? 'Switch to dark mode' : 'Switch to light mode');
    }
    updateIcon();
    btn.addEventListener('click', function () {
      var light = document.documentElement.getAttribute('data-theme') === 'light';
      if (light) {
        document.documentElement.removeAttribute('data-theme');
        if (typeof localStorage !== 'undefined') localStorage.setItem('cd_theme', 'dark');
      } else {
        document.documentElement.setAttribute('data-theme', 'light');
        if (typeof localStorage !== 'undefined') localStorage.setItem('cd_theme', 'light');
      }
      updateIcon();
    });
  }

  document.addEventListener('DOMContentLoaded', initThemeToggle);

  /* ─── FEEDBACK WIDGET ────────────────────────────────────────── */
  function renderFeedback() {
    if (!document.querySelector('.cd-article')) return; // individual countdown pages only

    var ENDPOINT = 'https://formspree.io/f/xkoegbgy';

    var wrap = document.createElement('div');
    wrap.className = 'cd-feedback';
    wrap.innerHTML =
      '<p class="cd-fb-title">' + FB.title + '</p>' +
      '<p class="cd-fb-sub">' + FB.sub + '</p>' +
      '<div class="cd-fb-btns">' +
        '<button class="cd-fb-btn" data-cat="love">'    + FB.love     + '</button>' +
        '<button class="cd-fb-btn" data-cat="add">'     + FB.add      + '</button>' +
        '<button class="cd-fb-btn" data-cat="broken">'  + FB.broken   + '</button>' +
        '<button class="cd-fb-btn" data-cat="question">' + FB.question + '</button>' +
      '</div>' +
      '<div class="cd-fb-form" style="display:none">' +
        '<textarea class="cd-fb-ta" rows="3" placeholder="' + FB.ph + '"></textarea>' +
        '<button class="cd-fb-send">' + FB.send + '</button>' +
      '</div>' +
      '<p class="cd-fb-thanks" style="display:none">' + FB.thanks + '</p>';

    var footer = document.querySelector('.site-footer');
    if (footer) footer.parentNode.insertBefore(wrap, footer);
    else document.body.appendChild(wrap);

    var selected = null;
    var btns  = wrap.querySelectorAll('.cd-fb-btn');
    var form  = wrap.querySelector('.cd-fb-form');
    var ta    = wrap.querySelector('.cd-fb-ta');
    var send  = wrap.querySelector('.cd-fb-send');
    var thanks = wrap.querySelector('.cd-fb-thanks');

    btns.forEach(function(btn) {
      btn.addEventListener('click', function() {
        btns.forEach(function(b) { b.classList.remove('cd-fb-btn--active'); });
        btn.classList.add('cd-fb-btn--active');
        selected = btn.getAttribute('data-cat');
        form.style.display = '';
        ta.focus();
      });
    });

    send.addEventListener('click', function() {
      var msg = ta.value.trim();
      if (!msg && !selected) return;

      var payload = {
        category: selected || '',
        message:  msg,
        page:     window.location.href
      };

      if (ENDPOINT === 'REPLACE_WITH_FORMSPREE_ENDPOINT') {
        // No endpoint yet — just show thanks locally
        form.style.display = 'none';
        wrap.querySelector('.cd-fb-btns').style.display = 'none';
        wrap.querySelector('.cd-fb-title').style.display = 'none';
        wrap.querySelector('.cd-fb-sub').style.display = 'none';
        thanks.style.display = '';
        return;
      }

      send.disabled = true;
      fetch(ENDPOINT, {
        method: 'POST',
        headers: { 'Accept': 'application/json', 'Content-Type': 'application/json' },
        body: JSON.stringify(payload)
      }).then(function(r) {
        form.style.display = 'none';
        wrap.querySelector('.cd-fb-btns').style.display = 'none';
        wrap.querySelector('.cd-fb-title').style.display = 'none';
        wrap.querySelector('.cd-fb-sub').style.display = 'none';
        thanks.style.display = '';
      }).catch(function() {
        send.disabled = false;
      });
    });
  }

  /* ─── FAVORITES BADGE (header link on all pages) ─────────────── */
  function updateHeaderFavBadge() {
    var badge = document.getElementById('hub-fav-badge');
    if (!badge) return;
    try {
      var favs    = JSON.parse(localStorage.getItem('cd_favorites')  || '[]');
      var customs = JSON.parse(localStorage.getItem('cd_custom_favs') || '[]');
      var n = favs.length + customs.length;
      badge.textContent = n;
      badge.style.display = n > 0 ? 'inline-flex' : 'none';
    } catch(e) {}
  }

  document.addEventListener('DOMContentLoaded', function() {
    renderFeedback();
    updateHeaderFavBadge();
  });

})();
