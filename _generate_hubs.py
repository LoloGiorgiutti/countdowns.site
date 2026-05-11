#!/usr/bin/env python3
"""
Generate language hub pages: /es/, /pt/, /fr/
Run from repo root: python3 _generate_hubs.py
"""
import os, sys
# Import translated slug map so hub cards link to /{lang}/countdown/{slug}/ when available
try:
    from _generate import SLUG_LANGS
except Exception:
    SLUG_LANGS = {}

BASE_URL = "https://countdowns.site"

LANGS = [
  dict(
    code="en", html_lang="en",
    dir="",
    canonical=f"{BASE_URL}/",
    og_locale="en_US",
    title="Countdowns — Every countdown that matters",
    meta_desc="Real-time countdowns for sports, releases, holidays, sales and more. Free, live, no ads.",
    og_title="Countdowns — Every countdown that matters",
    og_desc="Real-time countdowns for every event the world is waiting for.",
    hero_label="Live · updated in real time",
    h1="Every countdown<br>that <em>matters</em>",
    hero_sub="Sports, releases, holidays, sales — every event the world is counting down to.",
    sort_chrono="Soonest first",
    sort_cat="By category",
    bucket_today="Today",
    bucket_week="This week",
    bucket_month="This month",
    bucket_soon="Coming soon",
    bucket_year="Later this year",
    bucket_future="Next year +",
    bucket_tba="Date TBA",
    card_tba="Date TBA",
    card_today="Today",
    card_days="days",
    lang_btn_active="EN",
    names={},
    json_ld_name="Countdowns",
    json_ld_desc="Real-time countdowns for every event that matters",
  ),
  dict(
    code="es", html_lang="es",
    dir="es",
    canonical=f"{BASE_URL}/es/",
    og_locale="es_ES",
    title="Countdowns — Cada cuenta regresiva que importa",
    meta_desc="Contadores en tiempo real para deportes, lanzamientos, feriados, ventas y más. Gratis, en vivo, sin anuncios.",
    og_title="Countdowns — Cada cuenta regresiva que importa",
    og_desc="Contadores en tiempo real para todos los eventos que el mundo está esperando.",
    hero_label="En vivo · actualizado en tiempo real",
    h1="Cada cuenta regresiva<br>que <em>importa</em>",
    hero_sub="Deportes, lanzamientos, feriados, ventas — cada evento del mundo.",
    sort_chrono="Más próximos",
    sort_cat="Por categoría",
    bucket_today="Hoy",
    bucket_week="Esta semana",
    bucket_month="Este mes",
    bucket_soon="Muy pronto",
    bucket_year="Este año",
    bucket_future="Año próximo +",
    bucket_tba="Fecha por confirmar",
    card_tba="Fecha TBA",
    card_today="Hoy",
    card_days="días",
    lang_btn_active="ES",
    # Translated event names (override)
    names={
      'gta6':              'GTA VI',
      'iphone':            'Próximo iPhone',
      'f1':                'Próxima Carrera F1',
      'world-cup':         'Copa del Mundo 2026',
      'ucl-final':         'Final Champions League',
      'nba-finals':        'Finales NBA',
      'le-mans':           '24h de Le Mans',
      'wimbledon':         'Wimbledon',
      'tour-de-france':    'Tour de France',
      'olympics-2028':     'Olimpiadas LA 2028',
      'copa-libertadores': 'Final Copa Libertadores',
      'christmas':         'Navidad',
      'new-year':          'Año Nuevo',
      'halloween':         'Halloween',
      'valentines':        'Día de San Valentín',
      'easter':            'Pascua',
      'mothers-day':       'Día de la Madre',
      'fathers-day':       'Día del Padre',
      'dia-de-los-muertos':'Día de los Muertos',
      'cinco-de-mayo':     'Cinco de Mayo',
      'fiestas-patrias':   'Fiestas Patrias Chile',
      'oscars':            'Premios Oscar',
      'grammys':           'Grammy Awards',
      'met-gala':          'Met Gala',
      'eurovision':        'Eurovisión',
      'cannes':            'Festival de Cannes',
      'black-friday':      'Black Friday',
      'cyber-monday':      'Cyber Monday',
      'hot-sale':          'Hot Sale Argentina',
      'full-moon':         'Próxima Luna Llena',
      'eclipse':           'Eclipse Solar',
      'lollapalooza-ar':   'Lollapalooza Argentina',
      'lollapalooza-cl':   'Lollapalooza Chile',
      'cosquin-rock':      'Cosquín Rock',
      'nyfw':              'Semana Moda NY',
      'paris-fw':          'Semana Moda París',
      'milan-fw':          'Semana Moda Milán',
      'bafweek':           'BAFWeek Buenos Aires',
      'elecciones-ar':     'Elecciones Argentina 2027',
      '25-de-mayo':        '25 de Mayo — Día de la Patria',
      'dia-del-nino':      'Día del Niño',
    },
    json_ld_name="Countdowns en Español",
    json_ld_desc="Contadores en tiempo real para cada evento que importa",
  ),
  dict(
    code="pt", html_lang="pt-BR",
    dir="pt",
    canonical=f"{BASE_URL}/pt/",
    og_locale="pt_BR",
    title="Countdowns — Cada contagem regressiva que importa",
    meta_desc="Contagens regressivas em tempo real para esportes, lançamentos, feriados, promoções e mais. Grátis, ao vivo, sem anúncios.",
    og_title="Countdowns — Cada contagem regressiva que importa",
    og_desc="Contagens regressivas em tempo real para todos os eventos que o mundo está esperando.",
    hero_label="Ao vivo · atualizado em tempo real",
    h1="Cada contagem regressiva<br>que <em>importa</em>",
    hero_sub="Esportes, lançamentos, feriados, promoções — cada evento do mundo.",
    sort_chrono="Mais próximos",
    sort_cat="Por categoria",
    bucket_today="Hoje",
    bucket_week="Esta semana",
    bucket_month="Este mês",
    bucket_soon="Em breve",
    bucket_year="Este ano",
    bucket_future="Próximo ano +",
    bucket_tba="Data a confirmar",
    card_tba="Data TBA",
    card_today="Hoje",
    card_days="dias",
    lang_btn_active="PT",
    names={
      'gta6':           'GTA VI',
      'iphone':         'Próximo iPhone',
      'f1':             'Próxima Corrida F1',
      'world-cup':      'Copa do Mundo 2026',
      'ucl-final':      'Final da Champions',
      'nba-finals':     'Finais da NBA',
      'le-mans':        '24h de Le Mans',
      'wimbledon':      'Wimbledon',
      'tour-de-france': 'Tour de France',
      'olympics-2028':  'Olimpíadas LA 2028',
      'christmas':      'Natal',
      'new-year':       'Ano Novo',
      'halloween':      'Halloween',
      'valentines':     'Dia dos Namorados',
      'easter':         'Páscoa',
      'mothers-day':    'Dia das Mães',
      'fathers-day':    'Dia dos Pais',
      'oscars':         'Oscar',
      'grammys':        'Grammy Awards',
      'met-gala':       'Met Gala',
      'eurovision':     'Eurovision',
      'cannes':         'Festival de Cannes',
      'black-friday':   'Black Friday',
      'cyber-monday':   'Cyber Monday',
      'full-moon':      'Próxima Lua Cheia',
      'eclipse':        'Eclipse Solar',
      'rock-in-rio':    'Rock in Rio Lisboa',
      'dia-del-nino':   'Dia das Crianças',
      'nyfw':           'Semana de Moda NY',
      'paris-fw':       'Semana de Moda Paris',
      'milan-fw':       'Semana de Moda Milão',
    },
    json_ld_name="Countdowns em Português",
    json_ld_desc="Contagens regressivas em tempo real para cada evento que importa",
  ),
  dict(
    code="fr", html_lang="fr",
    dir="fr",
    canonical=f"{BASE_URL}/fr/",
    og_locale="fr_FR",
    title="Countdowns — Chaque compte à rebours qui compte",
    meta_desc="Comptes à rebours en temps réel pour le sport, les sorties, les fêtes, les soldes et plus. Gratuit, en direct, sans publicités.",
    og_title="Countdowns — Chaque compte à rebours qui compte",
    og_desc="Comptes à rebours en temps réel pour tous les événements que le monde attend.",
    hero_label="En direct · mis à jour en temps réel",
    h1="Chaque compte à rebours<br>qui <em>compte</em>",
    hero_sub="Sport, sorties, fêtes, soldes — chaque événement que le monde attend.",
    sort_chrono="Les plus proches",
    sort_cat="Par catégorie",
    bucket_today="Aujourd'hui",
    bucket_week="Cette semaine",
    bucket_month="Ce mois-ci",
    bucket_soon="Bientôt",
    bucket_year="Plus tard cette année",
    bucket_future="L'année prochaine +",
    bucket_tba="Date à confirmer",
    card_tba="Date TBA",
    card_today="Aujourd'hui",
    card_days="jours",
    lang_btn_active="FR",
    names={
      'gta6':           'GTA VI',
      'iphone':         'Prochain iPhone',
      'f1':             'Prochain Grand Prix F1',
      'world-cup':      'Coupe du Monde 2026',
      'ucl-final':      'Finale Champions League',
      'nba-finals':     'Finales NBA',
      'le-mans':        '24h du Mans',
      'wimbledon':      'Wimbledon',
      'tour-de-france': 'Tour de France',
      'olympics-2028':  'JO Los Angeles 2028',
      'christmas':      'Noël',
      'new-year':       'Nouvel An',
      'halloween':      'Halloween',
      'valentines':     'Saint-Valentin',
      'easter':         'Pâques',
      'mothers-day':    'Fête des Mères',
      'fathers-day':    'Fête des Pères',
      'bastille-day':   'Fête Nationale (14 Juillet)',
      'oscars':         'Oscars',
      'grammys':        'Grammy Awards',
      'met-gala':       'Met Gala',
      'eurovision':     'Eurovision',
      'cannes':         'Festival de Cannes',
      'black-friday':   'Black Friday',
      'cyber-monday':   'Cyber Monday',
      'full-moon':      'Prochaine Pleine Lune',
      'eclipse':        'Éclipse Solaire',
      'nyfw':           'Semaine Mode NY',
      'paris-fw':       'Semaine Mode Paris',
      'milan-fw':       'Semaine Mode Milan',
      'dia-del-nino':   'Journée des Enfants',
    },
    json_ld_name="Countdowns en Français",
    json_ld_desc="Comptes à rebours en temps réel pour chaque événement qui compte",
  ),
]

EVENTS_JS = """    /* ── Releases ── */
    { slug:'gta6',       name:'GTA VI',                        type:'variable', countries:['global'], regions:['global'], cat:'Releases',      url:'/countdown/gta6/'       },
    { slug:'iphone',     name:'Next iPhone',                   type:'variable', countries:['global'], regions:['global'], cat:'Releases',      url:'/countdown/iphone/'     },
    /* ── Sports – Global ── */
    { slug:'f1',         name:'F1 Next Race',                  type:'variable', countries:['global'], regions:['global'], cat:'Sports',        url:'/countdown/f1/'         },
    { slug:'world-cup',  name:'2026 FIFA World Cup',           type:'variable', countries:['global'], regions:['global'], cat:'Sports',        url:'/countdown/world-cup/'  },
    { slug:'ucl-final',  name:'Champions League Final',        type:'variable', countries:['global'], regions:['global'], cat:'Sports',        url:'/countdown/ucl-final/'  },
    { slug:'nba-finals', name:'NBA Finals',                    type:'variable', countries:['global'], regions:['global'], cat:'Sports',        url:'/countdown/nba-finals/' },
    { slug:'le-mans',    name:'24h Le Mans',                   type:'variable', countries:['global'], regions:['global'], cat:'Sports',        url:'/countdown/le-mans/'    },
    { slug:'wimbledon',  name:'Wimbledon',                     type:'variable', countries:['global'], regions:['global'], cat:'Sports',        url:'/countdown/wimbledon/'  },
    { slug:'tour-de-france', name:'Tour de France',            type:'variable', countries:['global'], regions:['global'], cat:'Sports',        url:'/countdown/tour-de-france/' },
    { slug:'olympics-2028',  name:'LA 2028 Olympics',          type:'auto',     countries:['global'], regions:['global'], cat:'Sports',        url:'/countdown/olympics-2028/'  },
    { slug:'super-bowl',     name:'Super Bowl',                type:'auto',     countries:['US','CA','MX','GB','AU'],     regions:['en'],      cat:'Sports',        url:'/countdown/super-bowl/'         },
    { slug:'copa-libertadores', name:'Copa Libertadores Final',type:'variable', countries:LATAM,      regions:['es'],     cat:'Sports',        url:'/countdown/copa-libertadores/' },
    /* ── Holidays – Global ── */
    { slug:'christmas',   name:'Christmas',                    type:'auto',     countries:['global'], regions:['global'], cat:'Holidays',      url:'/countdown/christmas/'   },
    { slug:'new-year',    name:'New Year',                     type:'auto',     countries:['global'], regions:['global'], cat:'Holidays',      url:'/countdown/new-year/'    },
    { slug:'halloween',   name:'Halloween',                    type:'auto',     countries:['US','CA','GB','AU','IE','MX','AR','CL','CO','PE','UY','BR','FR','ES','PT','DE','BE','NZ'], regions:['global'], cat:'Holidays', url:'/countdown/halloween/' },
    { slug:'valentines',  name:"Valentine's Day",              type:'auto',     countries:['global'], regions:['global'], cat:'Holidays',      url:'/countdown/valentines/'  },
    { slug:'easter',      name:'Easter',                       type:'auto',     countries:['global'], regions:['global'], cat:'Holidays',      url:'/countdown/easter/'      },
    { slug:'mothers-day', name:"Mother's Day",                 type:'auto',     countries:['global'], regions:['global'], cat:'Holidays',      url:'/countdown/mothers-day/' },
    { slug:'fathers-day', name:"Father's Day",                 type:'auto',     countries:['global'], regions:['global'], cat:'Holidays',      url:'/countdown/fathers-day/' },
    { slug:'thanksgiving',     name:'Thanksgiving',            type:'auto',     countries:['US','CA'],                   regions:['en'],      cat:'Holidays',      url:'/countdown/thanksgiving/'     },
    { slug:'independence-day', name:'Independence Day (USA)',  type:'auto',     countries:['US'],                        regions:['en'],      cat:'Holidays',      url:'/countdown/independence-day/' },
    { slug:'memorial-day',     name:'Memorial Day',            type:'auto',     countries:['US'],                        regions:['en'],      cat:'Holidays',      url:'/countdown/memorial-day/'     },
    { slug:'labor-day',        name:'Labor Day',               type:'auto',     countries:['US','CA'],                   regions:['en'],      cat:'Holidays',      url:'/countdown/labor-day/'        },
    { slug:'st-patricks',      name:"St. Patrick's Day",       type:'auto',     countries:['US','IE','GB','AU','CA','AR','MX'], regions:['en'], cat:'Holidays',   url:'/countdown/st-patricks/'      },
    { slug:'dia-de-los-muertos', name:'Dia de los Muertos',    type:'auto',     countries:['MX','GT','SV','HN','NI','CR','CO','AR','CL','PE','UY'], regions:['es'], cat:'Holidays', url:'/countdown/dia-de-los-muertos/' },
    { slug:'cinco-de-mayo',   name:'Cinco de Mayo',            type:'auto',     countries:['MX','US'],                   regions:['es'],      cat:'Holidays',      url:'/countdown/cinco-de-mayo/'    },
    { slug:'fiestas-patrias', name:'Fiestas Patrias Chile',    type:'auto',     countries:['CL'],                        regions:['es'],      cat:'Holidays',      url:'/countdown/fiestas-patrias/'  },
    { slug:'bastille-day',    name:'Bastille Day',             type:'auto',     countries:['FR','BE','CH','LU'],          regions:['fr'],      cat:'Holidays',      url:'/countdown/bastille-day/'     },
    { slug:'oktoberfest',     name:'Oktoberfest',              type:'variable', countries:['DE','AT','CH','US','CA','AU','BR'], regions:['global'], cat:'Holidays', url:'/countdown/oktoberfest/'  },
    { slug:'25-de-mayo',      name:'25 de Mayo',               type:'auto',     countries:['AR'],                        regions:['es'],      cat:'Holidays',      url:'/countdown/25-de-mayo/'       },
    { slug:'dia-del-nino', name:"Children's Day",              type:'auto',     countries:['MX','AR','BR','CO','CL','PE','UY','VE','BO','EC','CR','PA','GT','SV','DO','PY'], regions:['global','es','pt'], cat:'Holidays', url:'/countdown/dia-del-nino/' },
    { slug:'epiphany',    name:'Epiphany / Three Kings Day',   type:'auto',     countries:['ES','MX','AR','CL','CO','IT','DE','AT','PL','GR','FR','BE','BR','UY','BO','PY','PE','EC','VE','CR','PA','GT','SV','HN','NI','DO','CU'], regions:['global'], cat:'Holidays', url:'/countdown/epiphany/' },
    /* ── Entertainment – Global ── */
    { slug:'oscars',      name:'Oscars',                       type:'auto',     countries:['global'], regions:['global'], cat:'Entertainment', url:'/countdown/oscars/'     },
    { slug:'grammys',     name:'Grammy Awards',                type:'variable', countries:['global'], regions:['global'], cat:'Entertainment', url:'/countdown/grammys/'    },
    { slug:'met-gala',    name:'Met Gala',                     type:'auto',     countries:['global'], regions:['global'], cat:'Entertainment', url:'/countdown/met-gala/'   },
    { slug:'cannes',      name:'Cannes Film Festival',         type:'variable', countries:['global'], regions:['global'], cat:'Entertainment', url:'/countdown/cannes/'     },
    { slug:'eurovision',  name:'Eurovision',                   type:'variable', countries:['FR','BE','CH','ES','PT','GB','IE','AU','DE','AT','SE','NO','FI','NL','IT','GR'], regions:['global','fr'], cat:'Entertainment', url:'/countdown/eurovision/' },
    { slug:'coachella',   name:'Coachella',                    type:'variable', countries:['US','MX','CA','GB'],          regions:['en'],      cat:'Entertainment', url:'/countdown/coachella/'  },
    { slug:'rio-carnival',name:'Rio Carnival',                 type:'auto',     countries:['BR','AR','UY','CO','BO','PE'], regions:['global'], cat:'Entertainment', url:'/countdown/rio-carnival/'},
    { slug:'balon-de-oro',name:"Ballon d'Or",                  type:'auto',     countries:['global'], regions:['global'], cat:'Entertainment', url:'/countdown/balon-de-oro/' },
    /* ── Sales – Global ── */
    { slug:'black-friday', name:'Black Friday',                type:'auto',     countries:['global'], regions:['global'], cat:'Sales',         url:'/countdown/black-friday/' },
    { slug:'cyber-monday', name:'Cyber Monday',                type:'auto',     countries:['global'], regions:['global'], cat:'Sales',         url:'/countdown/cyber-monday/' },
    { slug:'hot-sale',     name:'Hot Sale',                    type:'variable', countries:['AR','MX'],                   regions:['es'],      cat:'Sales',         url:'/countdown/hot-sale/'     },
    /* ── Nature – Global ── */
    { slug:'full-moon',   name:'Next Full Moon',               type:'auto',     countries:['global'], regions:['global'], cat:'Nature',        url:'/countdown/full-moon/'  },
    { slug:'eclipse',     name:'Solar Eclipse',                type:'variable', countries:['global'], regions:['global'], cat:'Nature',        url:'/countdown/eclipse/'    },
    /* ── Music ── */
    { slug:'lollapalooza-ar', name:'Lollapalooza Argentina',   type:'variable', countries:['AR','UY'],                   regions:['es'],      cat:'Music',         url:'/countdown/lollapalooza-ar/' },
    { slug:'lollapalooza-cl', name:'Lollapalooza Chile',       type:'variable', countries:['CL','AR'],                   regions:['es'],      cat:'Music',         url:'/countdown/lollapalooza-cl/' },
    { slug:'cosquin-rock',    name:'Cosquin Rock',             type:'variable', countries:['AR'],                        regions:['es'],      cat:'Music',         url:'/countdown/cosquin-rock/'    },
    { slug:'rock-in-rio',     name:'Rock in Rio',              type:'variable', countries:['BR','PT'],                   regions:['pt'],      cat:'Music',         url:'/countdown/rock-in-rio/'     },
    { slug:'lollapalooza-us', name:'Lollapalooza Chicago',     type:'variable', countries:['US','CA','MX'],              regions:['global'],  cat:'Music',         url:'/countdown/lollapalooza-us/' },
    { slug:'lollapalooza-de', name:'Lollapalooza Berlin',      type:'variable', countries:['DE','AT','CH','NL','BE','FR','ES','PL','SE','DK','NO','FI'], regions:['global'], cat:'Music', url:'/countdown/lollapalooza-de/' },
    { slug:'lollapalooza-fr', name:'Lollapalooza Paris',       type:'variable', countries:['FR','BE','CH','ES','DE'],    regions:['global'],  cat:'Music',         url:'/countdown/lollapalooza-fr/' },
    { slug:'primavera-sound-es',name:'Primavera Sound Barcelona', type:'variable', countries:['ES','FR','DE','GB','IT','PT','NL','BE','SE','NO','DK'], regions:['global'], cat:'Music', url:'/countdown/primavera-sound-es/'},
    { slug:'primavera-sound-ar',name:'Primavera Sound Buenos Aires', type:'variable', countries:['AR','UY','CL','BO','PY','PE'], regions:['global'], cat:'Music', url:'/countdown/primavera-sound-ar/'},
    { slug:'primavera-sound-br',name:'Primavera Sound Sao Paulo',    type:'variable', countries:['BR','AR','UY'],        regions:['global'],  cat:'Music',         url:'/countdown/primavera-sound-br/'},
    { slug:'tomorrowland',    name:'Tomorrowland',              type:'variable', countries:['global'],                   regions:['global'],  cat:'Music',         url:'/countdown/tomorrowland/'     },
    /* ── Fashion – Global ── */
    { slug:'nyfw',     name:'New York Fashion Week',           type:'variable', countries:['global'], regions:['global'], cat:'Fashion',      url:'/countdown/nyfw/'     },
    { slug:'paris-fw', name:'Paris Fashion Week',              type:'variable', countries:['global'], regions:['global'], cat:'Fashion',      url:'/countdown/paris-fw/' },
    { slug:'milan-fw', name:'Milan Fashion Week',              type:'variable', countries:['global'], regions:['global'], cat:'Fashion',      url:'/countdown/milan-fw/' },
    { slug:'bafweek',  name:'Buenos Aires Fashion Week',       type:'variable', countries:['AR'],                        regions:['es'],      cat:'Fashion',      url:'/countdown/bafweek/'  },
    /* ── Sports (additional) ── */
    { slug:'world-cup-final',        name:'2026 World Cup Final',    type:'variable', countries:['global'], regions:['global'], cat:'Sports', url:'/countdown/world-cup-final/'        },
    { slug:'copa-america-2028',      name:'Copa America 2028',       type:'variable', countries:['global'], regions:['global'], cat:'Sports', url:'/countdown/copa-america-2028/'      },
    { slug:'copa-america-2028-final',name:'Copa America 2028 Final', type:'variable', countries:['global'], regions:['global'], cat:'Sports', url:'/countdown/copa-america-2028-final/'},
    { slug:'euro-2028',              name:'UEFA Euro 2028',          type:'variable', countries:['global'], regions:['global'], cat:'Sports', url:'/countdown/euro-2028/'              },
    { slug:'euro-2028-final',        name:'UEFA Euro 2028 Final',    type:'variable', countries:['global'], regions:['global'], cat:'Sports', url:'/countdown/euro-2028-final/'        },
    { slug:'mr-olympia',             name:'Mr. Olympia',             type:'auto',     countries:['global'], regions:['global'], cat:'Sports', url:'/countdown/mr-olympia/'             },
    { slug:'arnold-classic',         name:'Arnold Classic',          type:'auto',     countries:['global'], regions:['global'], cat:'Sports', url:'/countdown/arnold-classic/'         },
    /* ── Technology ── */
    { slug:'ces',          name:'CES Las Vegas',               type:'auto',     countries:['global'], regions:['global'], cat:'Technology',    url:'/countdown/ces/'          },
    /* ── Months ── */
    { slug:'january',   name:'January',   type:'auto', countries:['global'], regions:['global'], cat:'Months', url:'/countdown/january/'   },
    { slug:'february',  name:'February',  type:'auto', countries:['global'], regions:['global'], cat:'Months', url:'/countdown/february/'  },
    { slug:'march',     name:'March',     type:'auto', countries:['global'], regions:['global'], cat:'Months', url:'/countdown/march/'     },
    { slug:'april',     name:'April',     type:'auto', countries:['global'], regions:['global'], cat:'Months', url:'/countdown/april/'     },
    { slug:'may-month', name:'May',       type:'auto', countries:['global'], regions:['global'], cat:'Months', url:'/countdown/may-month/' },
    { slug:'june-month',name:'June',      type:'auto', countries:['global'], regions:['global'], cat:'Months', url:'/countdown/june-month/'},
    { slug:'july-month',name:'July',      type:'auto', countries:['global'], regions:['global'], cat:'Months', url:'/countdown/july-month/'},
    { slug:'august',    name:'August',    type:'auto', countries:['global'], regions:['global'], cat:'Months', url:'/countdown/august/'    },
    { slug:'september', name:'September', type:'auto', countries:['global'], regions:['global'], cat:'Months', url:'/countdown/september/' },
    { slug:'october',   name:'October',   type:'auto', countries:['global'], regions:['global'], cat:'Months', url:'/countdown/october/'   },
    { slug:'november',  name:'November',  type:'auto', countries:['global'], regions:['global'], cat:'Months', url:'/countdown/november/'  },
    { slug:'december',  name:'December',  type:'auto', countries:['global'], regions:['global'], cat:'Months', url:'/countdown/december/'  },
    /* ── Time ── */
    { slug:'midnight',  name:'Midnight',  type:'auto', countries:['global'], regions:['global'], cat:'Time',   url:'/countdown/midnight/'  },
    /* ── Seasons ── */
    { slug:'spring',        name:'Spring', type:'auto', countries:['global'], regions:['global'], cat:'Seasons', url:'/countdown/spring/'        },
    { slug:'summer',        name:'Summer', type:'auto', countries:['global'], regions:['global'], cat:'Seasons', url:'/countdown/summer/'        },
    { slug:'autumn',        name:'Autumn', type:'auto', countries:['global'], regions:['global'], cat:'Seasons', url:'/countdown/autumn/'        },
    { slug:'winter-season', name:'Winter', type:'auto', countries:['global'], regions:['global'], cat:'Seasons', url:'/countdown/winter-season/' },
    /* ── School ── */
    { slug:'back-to-school',  name:'Back to School',  type:'auto', countries:['global'], regions:['global'], cat:'School', url:'/countdown/back-to-school/'  },
    { slug:'summer-vacation', name:'Summer Vacation', type:'auto', countries:['global'], regions:['global'], cat:'School', url:'/countdown/summer-vacation/' },
    { slug:'winter-vacation', name:'Winter Vacation', type:'auto', countries:['global'], regions:['global'], cat:'School', url:'/countdown/winter-vacation/' },
    /* ── National Days ── */
    { slug:'independence',    name:'Independence Day',            type:'auto', countries:['global'], regions:['global'], cat:'National Days', url:'/countdown/independence/'    },
    { slug:'canada-day',      name:'Canada Day',                  type:'auto', countries:['CA'],     regions:['global'], cat:'National Days', url:'/countdown/canada-day/'      },
    { slug:'australia-day',   name:'Australia Day',               type:'auto', countries:['AU'],     regions:['global'], cat:'National Days', url:'/countdown/australia-day/'   },
    { slug:'waitangi-day',    name:'Waitangi Day',                type:'auto', countries:['NZ'],     regions:['global'], cat:'National Days', url:'/countdown/waitangi-day/'    },
    { slug:'syttende-mai',    name:'Norwegian Constitution Day',  type:'auto', countries:['NO'],     regions:['global'], cat:'National Days', url:'/countdown/syttende-mai/'    },
    { slug:'german-unity-day',name:'German Unity Day',            type:'auto', countries:['DE','AT'],regions:['global'], cat:'National Days', url:'/countdown/german-unity-day/'},
    { slug:'festa-della-repubblica', name:'Italian Republic Day', type:'auto', countries:['IT'],    regions:['global'], cat:'National Days', url:'/countdown/festa-della-repubblica/' },
    { slug:'national-day-sg', name:'Singapore National Day',      type:'auto', countries:['SG'],     regions:['global'], cat:'National Days', url:'/countdown/national-day-sg/' },
    { slug:'freedom-day-za',  name:'South Africa Freedom Day',    type:'auto', countries:['ZA'],     regions:['global'], cat:'National Days', url:'/countdown/freedom-day-za/'  },
    { slug:'dia-de-la-hispanidad', name:'Dia de la Hispanidad',   type:'auto', countries:['ES','MX','AR','CL','CO','PE','UY','BO','EC','PY','VE','CR','PA','GT','SV','HN','NI','DO','CU','PR'], regions:['global'], cat:'National Days', url:'/countdown/dia-de-la-hispanidad/' },
    { slug:'dia-de-la-raza',  name:'Dia de la Raza',              type:'auto', countries:LATAM,      regions:['global'], cat:'National Days', url:'/countdown/dia-de-la-raza/'  },
    { slug:'dia-de-la-bandera',name:'Dia de la Bandera',          type:'auto', countries:['AR'],     regions:['global'], cat:'National Days', url:'/countdown/dia-de-la-bandera/'},
    { slug:'dia-de-la-revolucion',   name:'Dia de la Revolucion', type:'auto', countries:['MX'],    regions:['global'], cat:'National Days', url:'/countdown/dia-de-la-revolucion/'   },
    { slug:'dia-de-la-constitucion', name:'Dia de la Constitucion',type:'auto',countries:['MX'],    regions:['global'], cat:'National Days', url:'/countdown/dia-de-la-constitucion/' },
    { slug:'proclamacao-da-republica', name:'Proclamacao da Republica', type:'auto', countries:['BR','PT'], regions:['global'], cat:'National Days', url:'/countdown/proclamacao-da-republica/' },
    { slug:'tiradentes',      name:'Tiradentes',                  type:'auto', countries:['BR'],     regions:['global'], cat:'National Days', url:'/countdown/tiradentes/'      },
    { slug:'proclamacion-independencia-ar', name:'25 de Mayo (Argentina)', type:'auto', countries:['AR'], regions:['global'], cat:'National Days', url:'/countdown/proclamacion-independencia-ar/' },
    /* ── Jewish Holidays ── */
    { slug:'rosh-hashana', name:'Rosh Hashanah', type:'auto', countries:['global'], regions:['global'], cat:'Jewish Holidays', url:'/countdown/rosh-hashana/' },
    { slug:'yom-kipur',    name:'Yom Kippur',    type:'auto', countries:['global'], regions:['global'], cat:'Jewish Holidays', url:'/countdown/yom-kipur/'    },
    { slug:'januca',       name:'Hanukkah',      type:'auto', countries:['global'], regions:['global'], cat:'Jewish Holidays', url:'/countdown/januca/'       },
    { slug:'purim',        name:'Purim',         type:'auto', countries:['global'], regions:['global'], cat:'Jewish Holidays', url:'/countdown/purim/'        },
    { slug:'pesaj',        name:'Passover',      type:'auto', countries:['global'], regions:['global'], cat:'Jewish Holidays', url:'/countdown/pesaj/'        },
    { slug:'shavuot',      name:'Shavuot',       type:'auto', countries:['global'], regions:['global'], cat:'Jewish Holidays', url:'/countdown/shavuot/'      },
    /* ── Politics ── */
    { slug:'elecciones-ar', name:'Argentine Elections', type:'auto', countries:['AR'], regions:['es'], cat:'Politics', url:'/countdown/elecciones-ar/' },
"""


def generate_hub(lang):
    c = lang["code"]
    names_js = "{\n" + "".join(
        f"      '{k}': '{v}',\n" for k, v in lang["names"].items()
    ) + "    }"
    # Build LANG_URLS: slug -> /{lang}/countdown/{slug}/ for slugs with translated pages
    # For EN (code="en"), the canonical pages live at /countdown/{slug}/ (no prefix)
    lang_urls_items = ""
    for slug, langs in SLUG_LANGS.items():
        if c in langs:
            prefix = "" if c == "en" else f"/{c}"
            lang_urls_items += f"      '{slug}': '{prefix}/countdown/{slug}/',\n"
    lang_urls_js = "{\n" + lang_urls_items + "    }"

    return f'''<!DOCTYPE html>
<html lang="{lang['html_lang']}">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{lang['title']}</title>
<meta name="description" content="{lang['meta_desc']}">
<meta name="robots" content="index, follow">
<link rel="canonical" href="{lang['canonical']}">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">

<meta property="og:type" content="website">
<meta property="og:url" content="{lang['canonical']}">
<meta property="og:title" content="{lang['og_title']}">
<meta property="og:description" content="{lang['og_desc']}">
<meta property="og:locale" content="{lang['og_locale']}">

<link rel="alternate" hreflang="en" href="https://countdowns.site/">
<link rel="alternate" hreflang="es" href="https://countdowns.site/es/">
<link rel="alternate" hreflang="pt" href="https://countdowns.site/pt/">
<link rel="alternate" hreflang="fr" href="https://countdowns.site/fr/">
<link rel="alternate" hreflang="x-default" href="https://countdowns.site/">

<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/countdown.css">
<script>if(localStorage.getItem('cd_theme')==='light')document.documentElement.setAttribute('data-theme','light');</script>

<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "WebSite",
  "@id": "{lang['canonical']}#website",
  "url": "{lang['canonical']}",
  "name": "{lang['json_ld_name']}",
  "description": "{lang['json_ld_desc']}",
  "inLanguage": "{lang['html_lang']}"
}}
</script>
</head>
<body>

<header class="site-header">
  <a href="/" class="logo">countdowns<span class="logo-tld">.site</span></a>
  <div class="header-right">
    <button class="theme-btn" id="theme-toggle">Light</button>
    <div class="lang-seg" role="group" aria-label="Language">
      <button class="lang-btn" onclick="location.href='/'">EN</button>
      <button class="lang-btn{' active' if c == 'es' else ''}" onclick="location.href='/es/'">ES</button>
      <button class="lang-btn{' active' if c == 'pt' else ''}" onclick="location.href='/pt/'">PT</button>
      <button class="lang-btn{' active' if c == 'fr' else ''}" onclick="location.href='/fr/'">FR</button>
    </div>
    <button class="country-flag-btn" id="country-flag-btn" title="Select country" aria-label="Select country">🌍</button>
  </div>
</header>

<div class="hub-hero">
  <div class="hub-hero-label"><span></span>{lang['hero_label']}</div>
  <h1>{lang['h1']}</h1>
  <p class="hub-hero-sub">{lang['hero_sub']}</p>
  <div id="country-detected" class="country-detected hidden"></div>
  <div class="hub-hero-actions">
    <div class="sort-toggle" role="group" aria-label="Sort order">
      <button class="sort-btn active" data-sort="chrono">{lang['sort_chrono']}</button>
      <button class="sort-btn" data-sort="category">{lang['sort_cat']}</button>
    </div>
    <a href="/custom/" class="hub-create-btn">✦ Create your own countdown</a>
  </div>
</div>

<main class="hub-body" id="hub-body">
  <div id="hub-content"></div>
</main>

<footer class="site-footer">
  countdowns<span class="logo-tld">.site</span>
</footer>

<script src="/countdown-engine.js"></script>
<script>
(function () {{
  'use strict';

  var CAT_COLOR = {{
    'Releases':       {{ color:'#C084FC', glow:'rgba(192,132,252,.25)' }},
    'Sports':         {{ color:'#FB923C', glow:'rgba(251,146,60,.25)'  }},
    'Holidays':       {{ color:'#4ADE80', glow:'rgba(74,222,128,.2)'   }},
    'Entertainment':  {{ color:'#FBBF24', glow:'rgba(251,191,36,.2)'   }},
    'Sales':          {{ color:'#60A5FA', glow:'rgba(96,165,250,.2)'   }},
    'Nature':         {{ color:'#22D3EE', glow:'rgba(34,211,238,.2)'   }},
    'Music':          {{ color:'#F472B6', glow:'rgba(244,114,182,.2)'  }},
    'Politics':       {{ color:'#94A3B8', glow:'rgba(148,163,184,.2)'  }},
    'Fashion':        {{ color:'#FDA4AF', glow:'rgba(253,164,175,.2)'  }},
    'Technology':     {{ color:'#34D399', glow:'rgba(52,211,153,.2)'   }},
    'Months':         {{ color:'#A78BFA', glow:'rgba(167,139,250,.2)'  }},
    'Seasons':        {{ color:'#6EE7B7', glow:'rgba(110,231,183,.2)'  }},
    'School':         {{ color:'#FCD34D', glow:'rgba(252,211,77,.2)'   }},
    'National Days':  {{ color:'#F87171', glow:'rgba(248,113,113,.2)'  }},
    'Jewish Holidays':{{ color:'#E9D5A1', glow:'rgba(233,213,161,.2)'  }},
    'Time':           {{ color:'#67E8F9', glow:'rgba(103,232,249,.2)'  }},
  }};
  function cc(cat) {{ return CAT_COLOR[cat] || {{ color:'#818CF8', glow:'rgba(129,140,248,.2)' }}; }}

  var LATAM = ['AR','BR','CL','CO','PE','UY','VE','BO','PY','EC','CR','PA','GT','SV','HN','NI','DO','CU','MX'];

  var NAMES = {names_js};
  var LANG_URLS = {lang_urls_js};

  var EVENTS = [
{EVENTS_JS}
  ];

  var currentLang = '{c}';
  var currentSort = 'chrono';

  function filteredEvents() {{
    var country = (typeof localStorage !== 'undefined' ? localStorage.getItem('cd_country') : null) || 'global';
    return EVENTS.filter(function (e) {{
      var langOk = e.regions.indexOf('global') >= 0 || e.regions.indexOf(currentLang) >= 0;
      if (!langOk) return false;
      if (country === 'global' || !e.countries) return true;
      var cs = e.countries;
      if (cs.indexOf('global') >= 0) return true;
      // handle LATAM reference (passed as array by the time JS runs)
      return cs.indexOf(country) >= 0;
    }});
  }}

  var BUCKETS = [
    {{ key:'today',  label:'{lang['bucket_today']}',  test: function(d){{ return d<=0; }} }},
    {{ key:'week',   label:'{lang['bucket_week']}',   test: function(d){{ return d<=7; }} }},
    {{ key:'month',  label:'{lang['bucket_month']}',  test: function(d){{ return d<=30; }} }},
    {{ key:'soon',   label:'{lang['bucket_soon']}',   test: function(d){{ return d<=90; }} }},
    {{ key:'year',   label:'{lang['bucket_year']}',   test: function(d){{ return d<=365; }} }},
    {{ key:'future', label:'{lang['bucket_future']}', test: function(d){{ return d>365; }} }},
  ];

  function bucket(days) {{
    for (var i = 0; i < BUCKETS.length; i++) {{
      if (BUCKETS[i].test(days)) return BUCKETS[i].key;
    }}
    return 'future';
  }}

  function displayName(ev) {{
    return NAMES[ev.slug] || ev.name;
  }}

  function cardHTML(ev, data) {{
    var c = cc(ev.cat);
    var style = 'style="--cat-color:' + c.color + ';--cat-glow:' + c.glow + '"';
    var n = displayName(ev);
    var inner = '';
    if (data.state === 'unknown') {{
      inner = '<div class="cd-card-name">' + n + '</div>' +
              '<div class="cd-card-unknown">{lang['card_tba']}</div>';
    }} else if (data.state === 'today') {{
      inner = '<div class="cd-card-name">' + n + '</div>' +
              '<div class="cd-card-today">{lang['card_today']}</div>';
    }} else {{
      inner = '<div class="cd-card-name">' + n + '</div>' +
              '<div class="cd-card-num">' + data.days + '</div>' +
              '<div class="cd-card-lbl">{lang['card_days']}</div>';
    }}
    var cardUrl = LANG_URLS[ev.slug] || ev.url;
    return '<a href="' + cardUrl + '" class="cd-card" ' + style + '>' + inner + '</a>';
  }}

  function renderHub(results) {{
    var container = document.getElementById('hub-content');
    if (!container) return;
    var html = '';

    if (currentSort === 'chrono') {{
      results.sort(function (a, b) {{
        function rank(r) {{
          if (r.data.state === 'today')   return -1;
          if (r.data.state === 'future')  return r.data.days;
          if (r.data.state === 'unknown') return 99999;
          return 99998;
        }}
        return rank(a) - rank(b);
      }});

      var lastBucket = null;
      results.forEach(function (r) {{
        if (r.data.state === 'future' || r.data.state === 'today') {{
          var b = bucket(r.data.state === 'today' ? 0 : r.data.days);
          if (b !== lastBucket) {{
            if (lastBucket !== null) html += '</div>';
            var label = BUCKETS.filter(function(x){{ return x.key===b; }})[0].label;
            html += '<div class="time-bucket-hdr">' + label + '</div>';
            html += '<div class="cards-grid">';
            lastBucket = b;
          }}
          html += cardHTML(r.ev, r.data);
        }}
      }});
      if (lastBucket !== null) html += '</div>';

      var tba = results.filter(function (r) {{ return r.data.state === 'unknown'; }});
      if (tba.length) {{
        html += '<div class="time-bucket-hdr">{lang['bucket_tba']}</div>';
        html += '<div class="cards-grid">';
        tba.forEach(function (r) {{ html += cardHTML(r.ev, r.data); }});
        html += '</div>';
      }}
    }} else {{
      var grouped = {{}}, catOrder = [];
      results.forEach(function (r) {{
        var cat = r.ev.cat;
        if (!grouped[cat]) {{ grouped[cat] = []; catOrder.push(cat); }}
        grouped[cat].push(r);
      }});
      catOrder.forEach(function (cat) {{
        var c = cc(cat);
        html += '<div class="hub-section">';
        html += '<div class="section-hdr" style="--cat-color:' + c.color + ';--cat-glow:' + c.glow + '">';
        html += '<span class="section-hdr-label">' + cat + '</span></div>';
        html += '<div class="cards-grid">';
        grouped[cat].forEach(function (r) {{ html += cardHTML(r.ev, r.data); }});
        html += '</div></div>';
      }});
    }}

    container.innerHTML = html;
  }}

  function loadHub() {{
    var container = document.getElementById('hub-content');
    var evs = filteredEvents();
    var skeletons = '';
    for (var s = 0; s < Math.min(evs.length, 12); s++) {{
      skeletons += '<div class="cd-card-skeleton"></div>';
    }}
    container.innerHTML = '<div class="cards-grid">' + skeletons + '</div>';

    var results = new Array(evs.length);
    var loaded = 0;
    evs.forEach(function (ev, i) {{
      CountdownEngine.getCardData({{ slug: ev.slug, type: ev.type }}, function (data) {{
        results[i] = {{ ev: ev, data: data }};
        loaded++;
        if (loaded === evs.length) renderHub(results);
      }});
    }});
  }}

  document.querySelectorAll('.sort-btn').forEach(function (btn) {{
    btn.addEventListener('click', function () {{
      document.querySelectorAll('.sort-btn').forEach(function (b) {{ b.classList.remove('active'); }});
      btn.classList.add('active');
      currentSort = btn.dataset.sort;
      renderHub(window._hubResults || []);
    }});
  }});

  loadHub();

  var _origRender = renderHub;
  renderHub = function (results) {{
    window._hubResults = results;
    _origRender(results);
  }};

  // Theme toggle
  (function () {{
    var btn = document.getElementById('theme-toggle');
    var saved = localStorage.getItem('cd_theme');
    if (saved === 'light') {{ document.documentElement.setAttribute('data-theme', 'light'); btn.textContent = 'Dark'; }}
    btn.addEventListener('click', function () {{
      var isLight = document.documentElement.getAttribute('data-theme') === 'light';
      if (isLight) {{
        document.documentElement.removeAttribute('data-theme');
        localStorage.setItem('cd_theme', 'dark');
        btn.textContent = 'Light';
      }} else {{
        document.documentElement.setAttribute('data-theme', 'light');
        localStorage.setItem('cd_theme', 'light');
        btn.textContent = 'Dark';
      }}
    }});
  }})();

  // Country selector + auto geo-detection
  (function(){{
    var fb = document.getElementById('country-flag-btn');
    var det = document.getElementById('country-detected');
    var savedC = typeof localStorage !== 'undefined' ? localStorage.getItem('cd_country') : null;

    function applyCountry(code, reload) {{
      localStorage.setItem('cd_country', code);
      if (fb && CountdownEngine.FLAG_MAP) fb.textContent = CountdownEngine.FLAG_MAP[code] || '🌍';
      if (reload) {{ loadHub(); }}
    }}

    // Restore saved flag
    if (savedC && CountdownEngine.FLAG_MAP) fb.textContent = CountdownEngine.FLAG_MAP[savedC] || '🌍';

    if (fb) {{
      fb.addEventListener('click', function(){{
        CountdownEngine.openCountryPicker(function(code){{
          if (det) det.classList.add('hidden');
          applyCountry(code, true);
        }});
      }});
    }}

    // First visit: auto-detect via IP
    if (!savedC) {{
      fetch('https://ipapi.co/json/?fields=country_code')
        .then(function(r) {{ return r.json(); }})
        .then(function(data) {{
          var code = ((data && data.country_code) || 'global').toUpperCase();
          applyCountry(code, true);
          if (det && code !== 'global' && CountdownEngine.FLAG_MAP) {{
            det.innerHTML = '<span class="country-detected-dot"></span>Auto-detected: ' + (CountdownEngine.FLAG_MAP[code] || '') + ' ' + code;
            det.classList.remove('hidden');
          }}
        }})
        .catch(function() {{ loadHub(); }});
    }}
  }})();

}})();
</script>
</body>
</html>'''


for lang in LANGS:
    out_dir = lang["dir"]
    if out_dir:
        os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "index.html") if out_dir else "index.html"
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(generate_hub(lang))
    print(f"  ✓  /{out_dir}/" if out_dir else "  ✓  /")

print(f"\nGenerated {len(LANGS)} hub pages.")
