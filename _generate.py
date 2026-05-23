#!/usr/bin/env python3
"""
Generate individual countdown pages for countdowns.site
Run from repo root: python3 _generate.py
Generates /countdown/{slug}/ (EN) + /{lang}/countdown/{slug}/ for translated langs.
"""
import os, json
from datetime import date
from _translations import TRANSLATIONS

# ─── SEO: Multilingual keyword system ─────────────────────────────────────────
# Each phrase uses {name} (event name) and {year} (current/next occurrence year).
# This generates <meta name="keywords"> in 15 languages automatically for every page.
# Google ignores meta keywords, but Bing, Yandex, Baidu, DuckDuckGo use them.
# For Google: the English phrases are already in title/meta_desc/H1/FAQs.
#
# HOW TO ADD NEW EVENTS:
#   1. Add event dict to EVENTS with: slug, name, type, category, seo_title, meta_desc, hero_desc
#   2. Use seo_title pattern:  "How many days until {Name}? — {Name} Countdown {Year}"
#   3. Use meta_desc pattern:  "How many days until {name} {year}? Live countdown showing
#                               days, hours, minutes, seconds. When is {name} {year}?"
#   4. The keyword meta tag and multilingual phrases are auto-generated — nothing else needed.
#   5. If adding translations, add to _translations.py following existing pattern.

CURRENT_YEAR = date.today().year

# Keyword phrase templates per language (use {name} and {year} as placeholders)
KEYWORD_PHRASES = {
    'en': [
        'how many days until {name}',
        'how many days till {name}',
        'when is {name}',
        '{name} {year}',
        '{name} day',
        '{name} countdown',
        'days until {name}',
        'countdown to {name}',
        '{name} countdown {year}',
    ],
    'es': [
        'cuántos días faltan para {name}',
        'cuánto falta para {name}',
        'cuando es {name}',
        '{name} {year}',
        'cuenta regresiva {name}',
        'días para {name}',
        'cuántos días quedan para {name}',
    ],
    'pt': [
        'quantos dias faltam para {name}',
        'quando é {name}',
        '{name} {year}',
        'contagem regressiva {name}',
        'dias para {name}',
        'faltam quantos dias para {name}',
    ],
    'fr': [
        'combien de jours avant {name}',
        'quand est {name}',
        '{name} {year}',
        'compte à rebours {name}',
        'jours avant {name}',
        'dans combien de jours {name}',
    ],
    'de': [
        'wie viele tage bis {name}',
        'wann ist {name}',
        '{name} {year}',
        '{name} countdown',
        '{name} countdown {year}',
        'wie lange bis {name}',
    ],
    'it': [
        'quanti giorni mancano a {name}',
        'quando è {name}',
        '{name} {year}',
        'conto alla rovescia {name}',
        'giorni mancanti a {name}',
    ],
    'ar': [
        'كم يوم حتى {name}',
        'متى يكون {name}',
        '{name} {year}',
        'العد التنازلي {name}',
        'كم تبقى على {name}',
    ],
    'zh': [
        '距{name}还有多少天',
        '{name}倒计时',
        '{name}{year}',
        '还有几天到{name}',
        '{name}剩余天数',
    ],
    'ja': [
        '{name}まで何日',
        '{name}カウントダウン',
        '{name} {year}',
        '{name}までの日数',
        '{name}残り日数',
    ],
    'ko': [
        '{name}까지 며칠',
        '{name} 카운트다운',
        '{name} {year}',
        '{name}까지 남은 날',
        '{name} 날짜',
    ],
    'hi': [
        '{name} में कितने दिन बाकी हैं',
        '{name} काउंटडाउन',
        '{name} {year}',
        '{name} कब है',
    ],
    'ru': [
        'сколько дней до {name}',
        'когда {name}',
        '{name} {year}',
        'обратный отсчёт {name}',
        'дней до {name}',
    ],
    'nl': [
        'hoeveel dagen tot {name}',
        'wanneer is {name}',
        '{name} {year}',
        '{name} countdown',
        'nog hoeveel dagen tot {name}',
    ],
    'tr': [
        '{name} geri sayım',
        '{name} ne zaman',
        '{name} {year}',
        '{name} kaç gün kaldı',
    ],
    'pl': [
        'ile dni do {name}',
        'kiedy jest {name}',
        '{name} {year}',
        '{name} odliczanie',
    ],
}

def build_meta_keywords(name_en, year, name_by_lang=None):
    """Return comma-separated keywords in 15 languages for <meta name="keywords">.
    name_en     : English event name
    year        : Year of the event occurrence (int or str)
    name_by_lang: dict lang_code -> translated name (e.g. {'es': 'Navidad', 'fr': 'Noël'})
    """
    if name_by_lang is None:
        name_by_lang = {}
    seen = set()
    keywords = []
    for lang_code, phrases in KEYWORD_PHRASES.items():
        name = name_by_lang.get(lang_code, name_en)
        for phrase in phrases:
            kw = phrase.format(name=name, year=year)
            if kw not in seen:
                seen.add(kw)
                keywords.append(kw)
    return ', '.join(keywords)

# Merge auto-generated translations (manual entries in _translations.py always win)
try:
    from _translations_auto import TRANSLATIONS_AUTO as _AUTO
    for _lang, _ldata in _AUTO.items():
        if _lang not in TRANSLATIONS:
            TRANSLATIONS[_lang] = _ldata
            continue
        for _slug, _fields in _ldata.get('events', {}).items():
            _ev = TRANSLATIONS[_lang].setdefault('events', {}).setdefault(_slug, {})
            for _k, _v in _fields.items():
                if _k not in _ev:  # manual translation takes priority
                    _ev[_k] = _v
except ImportError:
    pass

BASE_URL = "https://countdowns.site"

# ─── Events ───────────────────────────────────────────────────────────────────
EVENTS = [
  # ── Releases ──────────────────────────────────────────────────────────────
  dict(
    slug="gta6", name="GTA VI", type="variable", category="Releases",
    regions=["global"],
    seo_title="GTA 6 Countdown — Days Until GTA VI Release 2026",
    meta_desc="Real-time countdown to GTA VI release date. Days, hours, minutes and seconds until Grand Theft Auto 6 launches on PS5 and Xbox Series X/S on November 19, 2026.",
    hero_desc="Real-time countdown to the release of Grand Theft Auto VI.",
    content="Grand Theft Auto VI is one of the most anticipated game releases in history. Developed by Rockstar Games, GTA VI is scheduled to launch on November 19, 2026 for PlayStation 5 and Xbox Series X/S. A PC release has not been officially confirmed but is expected to follow.",
    faqs=[
      ("When does GTA VI come out?", "GTA VI releases on November 19, 2026 for PS5 and Xbox Series X/S."),
      ("Will GTA VI be on PC?", "Rockstar has not yet announced a PC release date. GTA V arrived on PC about 18 months after the console launch."),
      ("What is GTA VI about?", "GTA VI is set in Leonida, a fictional version of Florida. It features the franchise's first female protagonist, Lucia, alongside Jason."),
      ("How long until GTA 6 comes out?", "Use the live counter above to see the exact days, hours, minutes and seconds remaining until the GTA VI release."),
    ]
  ),
  dict(
    slug="iphone", name="Next iPhone", type="variable", category="Releases",
    regions=["global"],
    seo_title="Next iPhone Countdown — Days Until the Next Apple iPhone Release",
    meta_desc="Live countdown to the next iPhone release. Apple typically unveils new iPhones in September each year. Track the exact days, hours and minutes.",
    hero_desc="Live countdown to Apple's next iPhone announcement and release.",
    content="Apple traditionally announces new iPhone models in September, with an event usually held in the first or second week of the month. Apple has maintained this annual release cadence since 2012, consistently launching new models each fall season.",
    faqs=[
      ("When will the next iPhone be released?", "Apple typically announces new iPhones in September, with release following a week or two later. The live countdown above shows the estimated time until the next launch."),
      ("What features will the next iPhone have?", "Apple does not pre-announce features. Leaks typically emerge several months before the September event and cover camera, chip, and design updates."),
      ("How do I pre-order the next iPhone?", "Apple opens pre-orders on the Friday following its September event, usually at apple.com and through carriers."),
    ]
  ),

  # ── Sports – Global ────────────────────────────────────────────────────────
  dict(
    slug="f1", name="F1 Next Race", type="variable", category="Sports",
    regions=["global"],
    seo_title="F1 Countdown — Days Until the Next Formula 1 Race",
    meta_desc="Real-time countdown to the next Formula 1 Grand Prix. See exactly how many days, hours and minutes until the next F1 race weekend.",
    hero_desc="Live countdown to the next Formula 1 Grand Prix.",
    content="Formula 1 holds around 24 Grands Prix per season, racing on circuits across five continents from March to December. The countdown above always shows the time remaining until the next scheduled race.",
    faqs=[
      ("When is the next F1 race?", "The countdown above shows the date of the next scheduled Grand Prix. The current race on the calendar is the Monaco Grand Prix on May 24."),
      ("How long is an F1 race weekend?", "A standard F1 weekend spans Thursday–Sunday, with practice on Thursday and Friday, qualifying on Saturday, and the race on Sunday."),
      ("Where can I watch F1?", "Formula 1 is broadcast on ESPN (USA), Sky Sports F1 (UK), Canal+ (France), DAZN (various countries), and F1 TV globally."),
    ]
  ),
  dict(
    slug="world-cup", name="2026 FIFA World Cup", type="variable", category="Sports",
    regions=["global"],
    seo_title="2026 FIFA World Cup Countdown — Days Until the World Cup",
    meta_desc="Live countdown to the 2026 FIFA World Cup opening match. The tournament is jointly hosted by the USA, Canada and Mexico starting June 11, 2026.",
    hero_desc="Countdown to the 2026 FIFA World Cup — USA, Canada & Mexico.",
    content="The 2026 FIFA World Cup is the first edition to feature 48 teams and will be co-hosted by the United States, Canada and Mexico. The tournament runs from June 11 to July 19, 2026, with the final at MetLife Stadium in New Jersey, near New York City.",
    faqs=[
      ("When does the 2026 World Cup start?", "The 2026 FIFA World Cup opens on June 11, 2026 and runs through the final on July 19, 2026."),
      ("Where is the 2026 World Cup?", "The tournament is hosted across 16 cities in the USA (11 venues), Canada (2) and Mexico (3)."),
      ("How many teams are in the 2026 World Cup?", "For the first time, 48 national teams compete at the World Cup, up from 32 in previous editions."),
      ("Who qualified for the 2026 World Cup?", "Qualification is ongoing across all confederations. The host nations (USA, Canada, Mexico) qualify automatically."),
    ]
  ),
  dict(
    slug="ucl-final", name="Champions League Final", type="variable", category="Sports",
    regions=["global"],
    seo_title="Champions League Final Countdown — Days Until the UCL Final",
    meta_desc="Live countdown to the UEFA Champions League Final — the most-watched annual club football match in the world. Days, hours, minutes and seconds.",
    hero_desc="Countdown to the UEFA Champions League Final.",
    content="The UEFA Champions League Final is the most-watched annual club football event in the world, drawing an estimated 500 million viewers globally. The final is held each May or June at a pre-selected host stadium, with the venue rotating across Europe each season.",
    faqs=[
      ("When is the Champions League Final?", "The UCL Final typically takes place in late May or early June. The live countdown above updates automatically each season."),
      ("Where is the Champions League Final held?", "The final venue rotates across European stadiums and is announced by UEFA each season, usually 3-4 years in advance."),
      ("How many teams are in the Champions League?", "The reformed format features 36 clubs in the league phase, with the top 8 advancing directly to the round of 16."),
    ]
  ),
  dict(
    slug="nba-finals", name="NBA Finals", type="variable", category="Sports",
    regions=["global"],
    seo_title="NBA Finals Countdown — Days Until the NBA Championship",
    meta_desc="Real-time countdown to the NBA Finals. Track the days until basketball's biggest series begins.",
    hero_desc="Countdown to the 2026 NBA Finals.",
    content="The NBA Finals is the annual championship series of the National Basketball Association, contested between the Eastern and Western Conference champions. The series typically begins in June following the conference finals.",
    faqs=[
      ("When are the 2026 NBA Finals?", "The exact dates are TBA — they depend on the conference finals schedule. The Finals typically begin in mid-June."),
      ("How many games are in the NBA Finals?", "The NBA Finals is a best-of-seven series. The team that wins 4 games first is crowned champion."),
      ("Where are the 2026 NBA Finals?", "Home-court advantage goes to the team with the better regular-season record. Games alternate between the two teams' arenas."),
    ]
  ),
  dict(
    slug="le-mans", name="24 Hours of Le Mans", type="variable", category="Sports",
    regions=["global"],
    seo_title="Le Mans 24h Countdown — Days Until the 24 Hours of Le Mans",
    meta_desc="Live countdown to the 24 Hours of Le Mans. The world's most prestigious endurance race starts June 13, 2026 at Circuit de la Sarthe.",
    hero_desc="Countdown to the 2026 24 Hours of Le Mans.",
    content="The 24 Hours of Le Mans is the world's oldest active sports car endurance race, held annually on the Circuit de la Sarthe near Le Mans, France. In 2026, the race starts on June 13 and runs continuously for 24 hours, featuring the top hypercar, LMP2 and GT classes.",
    faqs=[
      ("When is Le Mans?", "The 24 Hours of Le Mans 2026 starts on Saturday, June 13, 2026 at 16:00 local time (CET)."),
      ("Where is Le Mans held?", "Le Mans is held on the Circuit de la Sarthe, a 13.6 km circuit combining permanent track with closed public roads near Le Mans, France."),
      ("How can I watch Le Mans?", "Le Mans is broadcast live on Eurosport (Europe), MotorTrend (USA), and the FIA WEC streaming platform globally."),
    ]
  ),
  dict(
    slug="wimbledon", name="Wimbledon", type="variable", category="Sports",
    regions=["global"],
    seo_title="Wimbledon Countdown — Days Until Wimbledon Tennis",
    meta_desc="Live countdown to Wimbledon, the world's oldest and most prestigious tennis Grand Slam, starting June 29, 2026 at the All England Club.",
    hero_desc="Countdown to The Championships, Wimbledon.",
    content="Wimbledon is the oldest tennis Grand Slam in the world, held annually at the All England Lawn Tennis Club in London since 1877. The 2026 Championships begin on June 29, with the men's and women's singles finals held on the last two Sundays of the fortnight.",
    faqs=[
      ("When does Wimbledon 2026 start?", "Wimbledon 2026 begins on Monday, June 29, 2026 and runs for two weeks through mid-July."),
      ("Where is Wimbledon played?", "Wimbledon is held at the All England Lawn Tennis and Croquet Club in Wimbledon, southwest London."),
      ("How do I get Wimbledon tickets?", "Tickets are available via the annual public ballot (applications typically open in January) or through queue on the day."),
    ]
  ),
  dict(
    slug="tour-de-france", name="Tour de France", type="variable", category="Sports",
    regions=["global"],
    seo_title="Tour de France Countdown — Days Until the Tour de France",
    meta_desc="Live countdown to the Tour de France. The world's most famous cycling race starts in late June 2026 with 21 stages over three weeks.",
    hero_desc="Countdown to the 2026 Tour de France.",
    content="The Tour de France is the world's most prestigious cycling race, held annually since 1903. The 2026 edition features 21 stages over 23 days, covering approximately 3,400 km across France and neighboring countries, finishing on the Champs-Élysées in Paris.",
    faqs=[
      ("When does the Tour de France 2026 start?", "The Tour de France 2026 Grand Départ is estimated for late June 2026. The exact date and start city will be announced by ASO."),
      ("How long is the Tour de France?", "The race covers approximately 3,400 km across 21 stages over 23 days (including two rest days)."),
      ("Who won the last Tour de France?", "Check the Tour de France official site for the most recent race results."),
    ]
  ),
  dict(
    slug="olympics-2028", name="LA 2028 Olympics", type="auto", category="Sports",
    regions=["global"],
    seo_title="2028 Olympics Countdown — Days Until the Los Angeles Olympics",
    meta_desc="Live countdown to the 2028 Summer Olympic Games in Los Angeles. The Opening Ceremony is on July 14, 2028 at the LA Memorial Coliseum.",
    hero_desc="Countdown to the Los Angeles 2028 Summer Olympic Games.",
    content="The 2028 Summer Olympic Games will be held in Los Angeles, California from July 14 to July 30, 2028. Los Angeles previously hosted the Olympics in 1932 and 1984. The Opening Ceremony takes place at the historic LA Memorial Coliseum.",
    faqs=[
      ("When are the 2028 Olympics?", "The LA 2028 Olympics run from July 14 to July 30, 2028. The Opening Ceremony is on July 14, 2028."),
      ("Where are the 2028 Olympics?", "The 2028 Summer Olympics are hosted by Los Angeles, California, USA."),
      ("What new sports are in the 2028 Olympics?", "LA 2028 will include cricket, flag football, baseball/softball, lacrosse and squash as new sports."),
      ("How do I get 2028 Olympics tickets?", "Ticket sales are managed by LA28. Registration for priority access opens at la28.org."),
    ]
  ),
  dict(
    slug="super-bowl", name="Super Bowl", type="auto", category="Sports",
    regions=["en"],
    seo_title="Super Bowl Countdown — Days Until the Next Super Bowl",
    meta_desc="Live countdown to the next Super Bowl. The NFL championship game is played on the second Sunday of February each year. Days, hours, minutes and seconds.",
    hero_desc="Countdown to the next Super Bowl — the NFL Championship.",
    content="The Super Bowl is the annual championship game of the National Football League (NFL), and one of the most-watched television events in the world. Held on the second Sunday of February each year, the halftime show and commercials are as iconic as the game itself.",
    faqs=[
      ("When is the next Super Bowl?", "The Super Bowl is held on the second Sunday of February each year. The live countdown above shows the exact time remaining."),
      ("Where is the Super Bowl held?", "The Super Bowl host city rotates and is announced by the NFL several years in advance. It has been held in cities like Miami, New Orleans, Los Angeles, Las Vegas and Phoenix."),
      ("How much are Super Bowl tickets?", "Super Bowl tickets typically start at $900+ on the secondary market and often exceed $10,000 for premium seats."),
      ("When is the Super Bowl halftime show?", "The halftime show takes place between the second and third quarters, roughly 30–40 minutes into the game."),
    ]
  ),
  dict(
    slug="copa-libertadores", name="Copa Libertadores Final", type="variable", category="Sports",
    regions=["es", "pt"],
    seo_title="Copa Libertadores Final Countdown — Days Until the Final",
    meta_desc="Live countdown to the 2026 Copa Libertadores Final, South America's biggest club football match. Date and venue TBD by CONMEBOL.",
    hero_desc="Countdown to the 2026 Copa Libertadores Final.",
    content="The Copa Libertadores is South America's premier club football competition, organized by CONMEBOL. The annual final is one of the most watched football matches in the Americas. The 2026 final date and host city will be announced by CONMEBOL.",
    faqs=[
      ("When is the Copa Libertadores Final?", "The 2026 final date has not been confirmed yet. CONMEBOL usually holds the final in November."),
      ("Where is the Copa Libertadores Final held?", "CONMEBOL selects a neutral venue for the final, often in a major South American city such as Buenos Aires, Lima, Montevideo or Asunción."),
      ("Which teams have won the most Copa Libertadores titles?", "Independiente (Argentina) is the most successful club with 7 titles. Boca Juniors (Argentina) and Estudiantes (Argentina) are also among the top winners."),
      ("How many teams participate in the Copa Libertadores?", "The Copa Libertadores features 47 clubs from CONMEBOL's 10 member nations, competing across multiple knockout and group stage rounds."),
    ]
  ),

  # ── Holidays – Global ──────────────────────────────────────────────────────
  dict(
    slug="christmas", name="Christmas", type="auto", category="Holidays",
    regions=["global"],
    seo_title="Christmas Countdown — Days Until Christmas",
    meta_desc="How many days until Christmas? Live countdown showing exact days, hours, minutes and seconds until December 25.",
    hero_desc="How many days until Christmas?",
    content="Christmas is celebrated on December 25 each year across the world. As a public holiday in over 160 countries, it marks the culmination of the Advent season and is celebrated with gift-giving, family gatherings, and festive traditions.",
    faqs=[
      ("How many days until Christmas?", "The live counter above shows the exact days, hours, minutes and seconds until December 25."),
      ("What day is Christmas 2026?", "Christmas 2026 falls on a Friday, December 25."),
      ("How many weeks until Christmas?", "Divide the number of days shown above by 7 to get the weeks remaining until Christmas."),
      ("When is Christmas Eve?", "Christmas Eve is always December 24, the day before Christmas Day."),
      ("Is Christmas a public holiday?", "Christmas is a public holiday in over 160 countries, making it the most widely observed holiday in the world."),
    ]
  ),
  dict(
    slug="new-year", name="New Year", type="auto", category="Holidays",
    regions=["global"],
    seo_title="New Year Countdown — Days Until New Year's Eve",
    meta_desc="Live countdown to New Year. How many days, hours and seconds until January 1,? Watch the real-time counter.",
    hero_desc="Countdown to New Year.",
    content="New Year's Day is celebrated on January 1 and marks the start of the new calendar year. New Year's Eve on December 31 is famous for fireworks and celebrations in cities around the world, including Sydney, Dubai, London and New York.",
    faqs=[
      ("How many days until New Year?", "The live counter above shows the exact time remaining until January 1."),
      ("What day is New Year's Day 2027?", "New Year's Day 2027 falls on a Friday, January 1."),
      ("Where are the best New Year fireworks?", "Famous New Year fireworks displays include Sydney Harbour Bridge, Dubai, London's Thames, and New York's Times Square."),
      ("What time zone does New Year start first?", "New Year arrives first in Kiribati (UTC+14) and last in the Baker Island (UTC-12), about 26 hours apart."),
      ("When is New Year's Eve?", "New Year's Eve is December 31, the last day of the year, the night before January 1."),
    ]
  ),
  dict(
    slug="halloween", name="Halloween", type="auto", category="Holidays",
    regions=["global"],
    seo_title="Halloween Countdown — Days Until Halloween",
    meta_desc="How many days until Halloween? Live countdown to October 31. Watch the exact hours, minutes and seconds tick down.",
    hero_desc="How many days until Halloween?",
    content="Halloween is celebrated annually on October 31, primarily in the United States, Canada, the United Kingdom, Ireland and Australia. Traditions include trick-or-treating, costume parties, pumpkin carving and haunted house visits.",
    faqs=[
      ("How many days until Halloween?", "The live countdown above shows the exact time until October 31."),
      ("What day is Halloween 2026?", "Halloween 2026 falls on a Saturday."),
      ("When did Halloween originate?", "Halloween has roots in the ancient Celtic festival of Samhain, later influenced by the Christian feast of All Hallows' Eve on October 31."),
      ("What are popular Halloween costumes?", "Popular Halloween costumes include witches, vampires, skeletons, superheroes, and characters from current pop culture and movies."),
      ("Is Halloween celebrated outside the US?", "Yes. Halloween is widely celebrated in Canada, Ireland, the UK, Australia, and increasingly in many European and Latin American countries."),
    ]
  ),
  dict(
    slug="valentines", name="Valentine's Day", type="auto", category="Holidays",
    regions=["global"],
    seo_title="Valentine's Day Countdown — Days Until Valentine's Day",
    meta_desc="Live countdown to Valentine's Day. How many days until February 14? Watch the exact hours and minutes remaining.",
    hero_desc="Countdown to Valentine's Day, February 14.",
    content="Valentine's Day is observed on February 14 each year as a celebration of love and affection. It is one of the most commercially significant holidays globally, with traditions including sending cards, flowers, chocolates and gifts to romantic partners.",
    faqs=[
      ("How many days until Valentine's Day?", "The live counter above shows the exact time until February 14."),
      ("What day is Valentine's Day 2027?", "Valentine's Day 2027 falls on a Sunday, February 14."),
      ("What are popular Valentine's Day gifts?", "Classic gifts include roses, chocolates, jewelry, perfume and personalised cards."),
      ("Is Valentine's Day a public holiday?", "Valentine's Day is not a public holiday in most countries. It is a cultural observance celebrated with gifts and gestures of affection."),
      ("Who was Saint Valentine?", "Saint Valentine was a Christian martyr in ancient Rome. His association with romantic love developed in the Middle Ages, popularised by Geoffrey Chaucer and others."),
    ]
  ),
  dict(
    slug="easter", name="Easter", type="auto", category="Holidays",
    regions=["global"],
    seo_title="Easter Countdown — How Many Days Until Easter Sunday",
    meta_desc="Live countdown to Easter. Easter Sunday is a moveable feast — the countdown updates automatically each year.",
    hero_desc="Countdown to Easter Sunday.",
    content="Easter is a Christian holiday celebrating the resurrection of Jesus Christ. Easter Sunday falls on the first Sunday after the first full moon following the spring equinox (March 21), making it a moveable feast between March 22 and April 25.",
    faqs=[
      ("When is Easter?", "Easter 2027 falls on Sunday, March 28."),
      ("When is Easter?", "Easter 2026 falls on Sunday, April 5."),
      ("How is the date of Easter calculated?", "Easter falls on the first Sunday after the first full moon on or after March 21 (the ecclesiastical spring equinox). This is known as the computus."),
      ("What is Good Friday?", "Good Friday falls two days before Easter Sunday and marks the crucifixion of Jesus Christ. It is a public holiday in many countries."),
      ("What is Holy Week?", "Holy Week is the week leading up to Easter Sunday, beginning with Palm Sunday and including Maundy Thursday, Good Friday, and Holy Saturday."),
    ]
  ),
  dict(
    slug="mothers-day", name="Mother's Day", type="auto", category="Holidays",
    regions=["global"],
    seo_title="Mother's Day Countdown — Days Until Mother's Day",
    meta_desc="Live countdown to Mother's Day. Select your country — date varies by region. US, UK, Mexico, Argentina, France and more.",
    hero_desc="Countdown to Mother's Day. Date varies by country.",
    content="Mother's Day is celebrated on different dates around the world. The US, Canada, Australia and Brazil observe it on the second Sunday of May. The UK celebrates Mothering Sunday on the fourth Sunday of Lent (usually in March). Mexico always celebrates on May 10. Argentina marks it on the third Sunday of October. France holds it on the last Sunday of May. Use the selector below to find the date for your country.",
    faqs=[
      ("When is Mother's Day 2027 in the US?", "Mother's Day 2027 in the US, Canada and Australia falls on Sunday, May 9 (second Sunday of May)."),
      ("When is Mother's Day in Mexico?", "Mexico always celebrates Mother's Day on May 10, regardless of the day of the week."),
      ("When is Mother's Day in Argentina?", "Argentina celebrates Mother's Day on the third Sunday of October. In 2026 it falls on October 18; in 2027 on October 17."),
      ("When is Mothering Sunday in the UK?", "The UK observes Mothering Sunday on the fourth Sunday of Lent, which varies each year. In 2027 it falls on March 7."),
      ("Why is Mother's Day on different dates in different countries?", "Each country independently adopted the holiday at different times and chose a date tied to local tradition, religious calendars, or historic events."),
    ],
    country_variants=[
      {"code": "us",  "label": "US, Canada & Australia", "dates": ["2026-05-10", "2027-05-09"], "countries": ["US","CA","AU","NZ"]},
      {"code": "uk",  "label": "United Kingdom",         "dates": ["2026-03-15", "2027-03-07"], "countries": ["GB","IE"]},
      {"code": "mx",  "label": "México",                 "dates": ["2026-05-10", "2027-05-10"], "countries": ["MX"]},
      {"code": "ar",  "label": "Argentina",              "dates": ["2026-10-18", "2027-10-17"], "countries": ["AR","UY","CL","CO","PE","BO","EC","VE","PY","CR","GT","SV","HN","NI","DO","CU","PR"]},
      {"code": "fr",  "label": "France",                 "dates": ["2026-05-31", "2027-05-30"], "countries": ["FR","BE","LU","CH"]},
      {"code": "br",  "label": "Brasil / Brazil",        "dates": ["2026-05-10", "2027-05-09"], "countries": ["BR","PT"]},
    ],
    default_variant_by_lang={"en": 0, "es": 2, "pt": 5, "fr": 4},
  ),
  dict(
    slug="fathers-day", name="Father's Day", type="auto", category="Holidays",
    regions=["global"],
    seo_title="Father's Day Countdown — Days Until Father's Day",
    meta_desc="Live countdown to Father's Day. Select your country — date varies by region. US, Australia, Germany, Brazil and more.",
    hero_desc="Countdown to Father's Day. Date varies by country.",
    content="Father's Day is celebrated on different dates around the world. The US, Canada, UK and Mexico observe it on the third Sunday of June. Australia and New Zealand celebrate on the first Sunday of September. Germany and Austria mark it on Ascension Thursday (39 days after Easter). Brazil celebrates on the second Sunday of August. Select your country below to see the countdown for your region.",
    faqs=[
      ("When is Father's Day 2026 in the US?", "Father's Day 2026 in the US, Canada, UK and Mexico falls on Sunday, June 21 (third Sunday of June)."),
      ("When is Father's Day in Australia?", "Australia and New Zealand celebrate Father's Day on the first Sunday of September. In 2026 that is September 6."),
      ("When is Father's Day in Germany?", "Germany and Austria celebrate Father's Day on Ascension Thursday, 39 days after Easter. In 2026 that falls on May 14."),
      ("When is Father's Day in Brazil?", "Brazil celebrates Father's Day on the second Sunday of August. In 2026 that is August 9."),
      ("Why is Father's Day on different dates?", "Countries independently adopted the holiday and chose dates tied to local traditions. The US date (3rd Sunday of June) is the most widely followed internationally."),
    ],
    country_variants=[
      {"code": "us",  "label": "US, Canada, UK & Mexico", "dates": ["2026-06-21", "2027-06-20"], "countries": ["US","CA","GB","IE","MX","IN","ZA","SG"]},
      {"code": "au",  "label": "Australia & New Zealand",  "dates": ["2026-09-06", "2027-09-05"], "countries": ["AU","NZ"]},
      {"code": "de",  "label": "Germany & Austria",        "dates": ["2026-05-14", "2027-05-06"], "countries": ["DE","AT"]},
      {"code": "br",  "label": "Brasil / Brazil",          "dates": ["2026-08-09", "2027-08-08"], "countries": ["BR","PT"]},
      {"code": "fr",  "label": "France",                   "dates": ["2026-06-21", "2027-06-20"], "countries": ["FR","BE","LU","CH"]},
    ],
    default_variant_by_lang={"en": 0, "es": 0, "pt": 3, "fr": 4},
  ),
  dict(
    slug="thanksgiving", name="Thanksgiving", type="auto", category="Holidays",
    regions=["en"],
    seo_title="Thanksgiving Countdown — Days Until Thanksgiving",
    meta_desc="Live countdown to Thanksgiving. US Thanksgiving falls on the fourth Thursday of November.",
    hero_desc="Countdown to Thanksgiving — fourth Thursday of November.",
    content="Thanksgiving is a national holiday in the United States celebrated on the fourth Thursday of November. It is one of the most travelled holidays in the US, marked by large family gatherings, a traditional turkey meal and the start of the holiday shopping season.",
    faqs=[
      ("When is Thanksgiving?", "Thanksgiving 2026 falls on Thursday, November 26."),
      ("When is Black Friday?", "Black Friday always falls the day after Thanksgiving — November 27."),
      ("Is Thanksgiving a national holiday?", "Yes, Thanksgiving is a federal holiday in the United States. Canada also celebrates Thanksgiving, but on the second Monday of October."),
      ("When is Canadian Thanksgiving?", "Canadian Thanksgiving 2026 falls on Monday, October 12 (second Monday of October)."),
      ("What is the traditional Thanksgiving meal?", "The traditional US Thanksgiving meal typically includes roast turkey, stuffing, mashed potatoes, cranberry sauce, green bean casserole, and pumpkin pie."),
    ]
  ),
  dict(
    slug="independence-day", name="Independence Day", type="auto", category="Holidays",
    regions=["en"],
    seo_title="Independence Day Countdown — Days Until July 4th",
    meta_desc="Live countdown to US Independence Day, July 4. How many days until the 4th of July fireworks?",
    hero_desc="Countdown to US Independence Day — July 4.",
    content="Independence Day, commonly known as the Fourth of July, is a federal holiday in the United States commemorating the Declaration of Independence on July 4, 1776. Celebrations include fireworks, parades, barbecues and concerts across the country.",
    faqs=[
      ("When is Independence Day?", "Independence Day 2026 is on Saturday, July 4."),
      ("What day of the week is July 4, 2026?", "July 4, 2026 falls on a Saturday."),
      ("Why is Independence Day on July 4?", "The Continental Congress voted for independence on July 2, 1776, and the Declaration of Independence was formally adopted on July 4, 1776."),
    ]
  ),
  dict(
    slug="memorial-day", name="Memorial Day", type="auto", category="Holidays",
    regions=["en"],
    seo_title="Memorial Day Countdown — Days Until Memorial Day",
    meta_desc="Live countdown to Memorial Day. Memorial Day is the last Monday of May and marks the unofficial start of summer in the US.",
    hero_desc="Countdown to Memorial Day — last Monday of May.",
    content="Memorial Day is a United States federal holiday observed on the last Monday of May. It honours military personnel who have died in service. It is also widely regarded as the unofficial start of the summer season.",
    faqs=[
      ("When is Memorial Day?", "Memorial Day 2027 falls on Monday, May 31."),
      ("When is Memorial Day?", "Memorial Day 2026 falls on Monday, May 25 (last Monday of May)."),
      ("Is Memorial Day a federal holiday?", "Yes, Memorial Day is a federal holiday in the US. Banks, government offices and many businesses are closed."),
      ("What is the difference between Memorial Day and Veterans Day?", "Memorial Day (last Monday of May) honours military personnel who died in service. Veterans Day (November 11) honours all military veterans, living and deceased."),
      ("Does Memorial Day mark the start of summer?", "Yes. Memorial Day weekend is widely considered the unofficial start of summer in the United States, with many people opening pools and taking road trips."),
    ]
  ),
  dict(
    slug="labor-day", name="Labor Day", type="auto", category="Holidays",
    regions=["en"],
    seo_title="Labor Day Countdown — Days Until Labor Day",
    meta_desc="Live countdown to Labor Day. US Labor Day is the first Monday of September, marking the end of summer.",
    hero_desc="Countdown to US Labor Day — first Monday of September.",
    content="Labor Day in the United States and Canada is celebrated on the first Monday of September. It honors the labour movement and the contributions of workers. In the US, it also marks the unofficial end of summer.",
    faqs=[
      ("When is Labor Day?", "Labor Day 2026 falls on Monday, September 7."),
      ("Is Labor Day the same as International Workers' Day?", "No. International Workers' Day (May Day) is May 1. US/Canada Labor Day is the first Monday of September."),
      ("Is Labor Day a federal holiday?", "Yes, Labor Day is a federal holiday in both the United States and Canada. Most businesses, schools and government offices are closed."),
      ("Does Labor Day mark the end of summer?", "Yes. Labor Day weekend is considered the unofficial end of summer in the US, and many schools resume in the days following it."),
    ]
  ),
  dict(
    slug="st-patricks", name="St. Patrick's Day", type="auto", category="Holidays",
    regions=["global"],
    seo_title="St. Patrick's Day Countdown — Days Until March 17",
    meta_desc="Live countdown to St. Patrick's Day 2027, March 17. The Irish cultural holiday celebrated worldwide with parades, green beer and festivities.",
    hero_desc="Countdown to St. Patrick's Day — March 17.",
    content="St. Patrick's Day is a cultural and religious celebration held on March 17, the traditional death date of Saint Patrick, the patron saint of Ireland. It is a public holiday in Ireland and celebrated worldwide with parades, wearing of green, and Irish music and food.",
    faqs=[
      ("When is St. Patrick's Day?", "St. Patrick's Day 2027 falls on Wednesday, March 17."),
      ("When is St. Patrick's Day?", "St. Patrick's Day 2026 falls on Tuesday, March 17."),
      ("Where is the biggest St. Patrick's Day parade?", "New York City hosts one of the world's largest St. Patrick's Day parades, drawing millions of spectators along Fifth Avenue. Dublin also holds a major parade."),
      ("Is St. Patrick's Day a public holiday?", "St. Patrick's Day is a public holiday in the Republic of Ireland and Northern Ireland. It is a cultural observance (not a public holiday) in the US, Canada and Australia."),
      ("What colour is associated with St. Patrick's Day?", "Green is the iconic colour, symbolising Ireland's lush landscape. People around the world wear green and buildings are illuminated in green light on March 17."),
    ]
  ),
  dict(
    slug="dia-de-los-muertos", name="Día de los Muertos", type="auto", category="Holidays",
    regions=["es"],
    seo_title="Día de los Muertos Countdown — Days Until Day of the Dead",
    meta_desc="Live countdown to Día de los Muertos, celebrated November 1–2 in Mexico and Latin America.",
    hero_desc="Countdown to Día de los Muertos — November 1.",
    content="Día de los Muertos (Day of the Dead) is a Mexican and Latin American holiday celebrated on November 1–2, coinciding with the Catholic holy days of All Saints' Day and All Souls' Day. It honours deceased loved ones with colourful altars, marigolds, skull imagery and celebrations.",
    faqs=[
      ("When is Día de los Muertos?", "Día de los Muertos is celebrated November 1–2, 2026."),
      ("Is Día de los Muertos the same as Halloween?", "No. While they fall close together, Día de los Muertos is a distinct Mexican tradition honouring deceased loved ones through colour, food and altars — not a horror celebration."),
      ("What is an ofrenda?", "An ofrenda is a colourful altar built during Día de los Muertos to honour deceased loved ones. It typically holds photos, marigolds, candles, food and personal mementos."),
      ("Why are marigolds associated with Día de los Muertos?", "Marigolds (cempasúchil) are believed to guide the spirits of the dead back to the living world with their bright colour and strong scent."),
      ("Is Día de los Muertos celebrated outside Mexico?", "Yes. The holiday is celebrated in many Latin American countries and has grown in popularity worldwide, especially in the US and Central America."),
    ]
  ),
  dict(
    slug="cinco-de-mayo", name="Cinco de Mayo", type="auto", category="Holidays",
    regions=["es"],
    seo_title="Cinco de Mayo Countdown — Days Until May 5",
    meta_desc="Live countdown to Cinco de Mayo. The Mexican holiday celebrated on May 5 commemorating the Battle of Puebla.",
    hero_desc="Countdown to Cinco de Mayo — May 5.",
    content="Cinco de Mayo commemorates the Mexican army's victory over French forces at the Battle of Puebla on May 5, 1862. While it is a minor holiday in Mexico, it is widely celebrated in the United States as a celebration of Mexican-American culture.",
    faqs=[
      ("When is Cinco de Mayo?", "Cinco de Mayo 2027 falls on Tuesday, May 5."),
      ("Is Cinco de Mayo Mexican Independence Day?", "No. Mexican Independence Day is September 16. Cinco de Mayo commemorates the Mexican army's victory at the Battle of Puebla on May 5, 1862."),
      ("Is Cinco de Mayo a national holiday in Mexico?", "Cinco de Mayo is a regional holiday mainly observed in the state of Puebla, Mexico. It is not a federal public holiday. It is much more widely celebrated in the United States."),
      ("Why is Cinco de Mayo celebrated in the US?", "Cinco de Mayo became a celebration of Mexican-American culture and heritage in the US, popularised from the 1960s onward, particularly in states with large Mexican-American communities."),
    ]
  ),
  dict(
    slug="25-de-mayo", name="25 de Mayo — Día de la Patria", type="auto", category="Holidays",
    regions=["es"],
    seo_title="25 de Mayo — Cuenta Regresiva Día de la Patria Argentina",
    meta_desc="Cuenta regresiva en vivo para el 25 de mayo, Día de la Patria Argentina. La Revolución de Mayo de 1810 que dio origen a la nación.",
    hero_desc="Cuenta regresiva al 25 de Mayo — Día de la Patria Argentina.",
    content="El 25 de Mayo conmemora la Revolución de Mayo de 1810, cuando se estableció la Primera Junta de Gobierno en Buenos Aires, marcando el inicio del camino hacia la independencia argentina. Es uno de los feriados patrios más importantes de la Argentina, celebrado con actos escolares, desfiles y el tradicional locro.",
    faqs=[
      ("¿Qué se celebra el 25 de mayo en Argentina?", "Se conmemora la Revolución de Mayo de 1810, cuando se formó la Primera Junta de Gobierno en Buenos Aires, reemplazando al virrey español."),
      ("¿Es el 25 de mayo la Independencia Argentina?", "No exactamente. La Independencia argentina se declaró el 9 de julio de 1816. El 25 de mayo celebra la Revolución de Mayo de 1810, el primer paso hacia la independencia."),
      ("¿Qué día cae el 25 de mayo 2027?", "El 25 de mayo de 2027 cae en martes y es feriado nacional inamovible en Argentina."),
      ("¿Qué se come el 25 de mayo?", "La comida tradicional del 25 de mayo es el locro, un guiso de maíz, porotos, zapallo y carne, típico de las regiones andinas argentinas."),
      ("¿Cuándo es el otro feriado patrio argentino?", "El otro gran feriado patrio es el 9 de julio, que conmemora la Declaración de la Independencia Argentina de 1816."),
    ]
  ),
  dict(
    slug="fiestas-patrias", name="Fiestas Patrias Chile", type="auto", category="Holidays",
    regions=["es"],
    seo_title="Fiestas Patrias Chile Countdown — Days Until September 18",
    meta_desc="Cuenta regresiva en vivo para las Fiestas Patrias de Chile 2026, celebradas el 18 y 19 de septiembre.",
    hero_desc="Countdown to Chilean Independence Day — September 18.",
    content="Las Fiestas Patrias chilenas se celebran el 18 y 19 de septiembre, conmemorando la Primera Junta de Gobierno de 1810 y el Día de las Glorias del Ejército. Son los días festivos más importantes de Chile, celebrados con fondas, cueca, asados y fuegos artificiales.",
    faqs=[
      ("¿Cuándo son las Fiestas Patrias Chile 2026?", "Las Fiestas Patrias son el 18 y 19 de septiembre de 2026."),
      ("¿Qué se celebra el 18 de septiembre?", "Se conmemora la Primera Junta Nacional de Gobierno de Chile, formada el 18 de septiembre de 1810."),
      ("¿Qué se celebra el 19 de septiembre?", "El 19 de septiembre es el Día de las Glorias del Ejército, que conmemora la primera batalla del Ejército de Chile."),
      ("¿Qué es una fonda?", "Las fondas son carpas o locales festivos donde se baila cueca, se comen empanadas y anticuchos, y se celebra con chicha y vino durante las Fiestas Patrias."),
      ("When is Chilean Independence Day?", "Chile's national holiday (Fiestas Patrias) is on September 18–19 each year. The key date is September 18, commemorating the First National Government of 1810."),
    ]
  ),
  dict(
    slug="bastille-day", name="Bastille Day", type="auto", category="Holidays",
    regions=["fr"],
    seo_title="Bastille Day Countdown — Days Until July 14 (Fête Nationale)",
    meta_desc="Live countdown to Bastille Day. The French national holiday on July 14 marks the storming of the Bastille.",
    hero_desc="Countdown to Bastille Day — French National Holiday, July 14.",
    content="Bastille Day (La Fête Nationale) is France's national holiday, celebrated on July 14 to commemorate the Storming of the Bastille on July 14, 1789, a pivotal moment in the French Revolution. Celebrations include the military parade on the Champs-Élysées and a fireworks display at the Eiffel Tower.",
    faqs=[
      ("When is Bastille Day?", "Bastille Day 2026 falls on Tuesday, July 14."),
      ("What happens on Bastille Day?", "France celebrates with a military parade on the Champs-Élysées in Paris, a fireworks display at the Eiffel Tower, and balls and celebrations across the country."),
      ("What is the Storming of the Bastille?", "On July 14, 1789, Parisian revolutionaries stormed the Bastille prison, a symbol of royal tyranny. The event marked a turning point in the French Revolution."),
      ("Is Bastille Day a public holiday?", "Yes. July 14 is a national public holiday in France. Businesses, schools and government offices are closed."),
      ("Why is Bastille Day important outside France?", "Bastille Day is seen globally as a symbol of the ideals of the French Revolution — liberty, equality and fraternity — making it one of the most recognised national holidays in the world."),
    ]
  ),
  dict(
    slug="oktoberfest", name="Oktoberfest", type="auto", category="Holidays",
    regions=["global"],
    seo_title="Oktoberfest Countdown — Days Until Munich Oktoberfest",
    meta_desc="Live countdown to Oktoberfest 2026 in Munich. The world's largest beer festival runs from late September through early October.",
    hero_desc="Countdown to Oktoberfest 2026 — Munich.",
    content="Oktoberfest is the world's largest folk festival, held annually in Munich, Bavaria. The festival begins on a Saturday in late September and runs for 16–18 days, ending on the first Sunday of October. It attracts around 6 million visitors each year.",
    faqs=[
      ("When is Oktoberfest?", "Oktoberfest 2026 begins on Saturday, September 19, 2026, and runs until October 4."),
      ("Where is Oktoberfest held?", "Oktoberfest takes place at the Theresienwiese fairgrounds (known as the Wiesn) in Munich, Bavaria, Germany."),
      ("How many people attend Oktoberfest?", "Oktoberfest draws around 6 million visitors each year, making it the world's largest beer festival and folk event."),
      ("What is the most popular Oktoberfest tent?", "The Hofbräu-Festzelt (Hofbräu tent) is among the most famous. There are 17 large tents and 21 smaller ones, each run by a different Munich brewery."),
      ("Do I need reservations for Oktoberfest?", "Reservations are strongly recommended for the beer tents, especially on weekends. Many tables are booked months in advance by corporate groups and tour operators."),
    ]
  ),

  # ── Children's Day ────────────────────────────────────────────────────────
  dict(
    slug="dia-del-nino", name="Children's Day", type="fixed", category="Holidays",
    regions=["global", "es", "pt"],
    seo_title="Children's Day Countdown — Days Until Children's Day",
    meta_desc="Live countdown to Children's Day. Date varies by country — Mexico April 30, Argentina 2nd Sunday of August, Brazil October 12.",
    hero_desc="Countdown to Children's Day. Date varies by country.",
    content="Children's Day is celebrated on different dates around the world. Mexico observes it on April 30. Argentina celebrates on the second Sunday of August. Brazil marks it on October 12 (also a religious holiday, Nossa Senhora Aparecida). The United Nations' Universal Children's Day is November 20. Select your country below to see your local countdown.",
    faqs=[
      ("When is Children's Day in Mexico?", "Mexico celebrates Children's Day (Día del Niño) on April 30 every year."),
      ("When is Children's Day in Argentina?", "Argentina celebrates Children's Day (Día del Niño) on the second Sunday of August. In 2026 that is August 9; in 2027, August 8."),
      ("When is Children's Day in Brazil?", "Brazil celebrates Children's Day (Dia das Crianças) on October 12, which coincides with the national holiday for Nossa Senhora Aparecida."),
      ("When is International Children's Day?", "The United Nations' Universal Children's Day is November 20, marking the anniversary of the 1989 Convention on the Rights of the Child."),
      ("Is Children's Day a public holiday?", "It depends on the country. In Brazil, October 12 is a national public holiday. In Mexico and Argentina it is a cultural observance, not a public holiday."),
    ],
    country_variants=[
      {"code": "mx", "label": "México (30 de abril)",                 "dates": ["2026-04-30", "2027-04-30"], "countries": ["MX"]},
      {"code": "ar", "label": "Argentina (2.° dom. de agosto)",       "dates": ["2026-08-09", "2027-08-08"], "countries": ["AR","UY","CL","CO","PE","BO","EC","VE","PY","CR","GT","SV","HN","NI","DO","CU","PR"]},
      {"code": "br", "label": "Brasil / Brazil (12 de outubro)",      "dates": ["2026-10-12", "2027-10-12"], "countries": ["BR","PT"]},
      {"code": "un", "label": "International / Nov 20",               "dates": ["2026-11-20", "2027-11-20"], "countries": []},
    ],
    default_variant_by_lang={"en": 3, "es": 0, "pt": 2, "fr": 3},
  ),

  # ── Entertainment – Global ─────────────────────────────────────────────────
  dict(
    slug="oscars", name="Oscars", type="auto", category="Entertainment",
    regions=["global"],
    seo_title="Oscars Countdown — Days Until the Academy Awards",
    meta_desc="Live countdown to the 2027 Academy Awards (Oscars). The ceremony is held on the last Sunday of February at the Dolby Theatre, Hollywood.",
    hero_desc="Countdown to the 2027 Academy Awards.",
    content="The Academy Awards, known as the Oscars, are the most prestigious awards in the film industry. Hosted by the Academy of Motion Picture Arts and Sciences, the ceremony is held annually at the Dolby Theatre in Hollywood and broadcast to over 200 countries.",
    faqs=[
      ("When are the Oscars 2027?", "The 2027 Academy Awards are estimated for Sunday, February 28, 2027 (last Sunday of February)."),
      ("Where are the Oscars held?", "The Oscars ceremony is held at the Dolby Theatre in Hollywood, Los Angeles."),
      ("How are Oscar nominees chosen?", "Members of the Academy of Motion Picture Arts and Sciences vote to nominate and select winners in each category."),
    ]
  ),
  dict(
    slug="grammys", name="Grammy Awards", type="variable", category="Entertainment",
    regions=["global"],
    seo_title="Grammy Awards Countdown — Days Until the Grammys",
    meta_desc="Live countdown to the Grammy Awards. Music's biggest night — date TBA, usually held in January or February.",
    hero_desc="Countdown to the 2027 Grammy Awards.",
    content="The Grammy Awards are the most prestigious honours in the music industry, presented annually by the Recording Academy. The ceremony typically takes place in January or February and is broadcast live on CBS.",
    faqs=[
      ("When are the Grammys 2027?", "The 2027 Grammy dates have not yet been announced. The Grammys typically take place in January or February."),
      ("Where are the Grammys held?", "The Grammys rotate between venues in New York and Los Angeles, including Madison Square Garden and Crypto.com Arena."),
      ("How many Grammy categories are there?", "The Recording Academy presents awards in over 90 categories spanning all major genres of music, from pop and rock to classical and jazz."),
      ("Who has won the most Grammys?", "Beyoncé holds the record for the most Grammy wins in history with over 32 awards as of 2024."),
    ]
  ),
  dict(
    slug="met-gala", name="Met Gala", type="auto", category="Entertainment",
    regions=["global"],
    seo_title="Met Gala Countdown — Days Until the Met Gala",
    meta_desc="Live countdown to the Met Gala. Fashion's biggest night is held on the first Monday of May at the Metropolitan Museum of Art.",
    hero_desc="Countdown to the Met Gala — first Monday of May.",
    content="The Met Gala (formally the Costume Institute Benefit) is an annual fundraising gala for the Metropolitan Museum of Art's Costume Institute in New York City. Held on the first Monday of May, it is fashion's most glamorous and star-studded event of the year.",
    faqs=[
      ("When is the Met Gala?", "The Met Gala 2027 is on Monday, May 3, 2027 (first Monday of May)."),
      ("Who hosts the Met Gala?", "The Met Gala is chaired by Vogue editor-in-chief Anna Wintour, along with celebrity co-chairs who change each year."),
      ("Can anyone attend the Met Gala?", "Attendance is invitation-only. Tables are sold to fashion houses and corporations, with individual tickets reportedly costing $75,000+."),
    ]
  ),
  dict(
    slug="eurovision", name="Eurovision Song Contest", type="variable", category="Entertainment",
    regions=["global", "fr"],
    seo_title="Eurovision Countdown — Days Until the Eurovision Song Contest",
    meta_desc="Live countdown to Eurovision Song Contest. The Grand Final is held in May each year and is watched by over 160 million viewers.",
    hero_desc="Countdown to the Eurovision Song Contest.",
    content="The Eurovision Song Contest is Europe's (and the world's) biggest live music event, with over 160 million viewers tuning in annually. Held each May, it features competing songs from dozens of countries across Europe and beyond, with a combination of public and jury voting.",
    faqs=[
      ("When is Eurovision?", "The Eurovision 2027 Grand Final is estimated for Saturday, May 15. The exact date depends on the host country."),
      ("Who can participate in Eurovision?", "Any member country of the European Broadcasting Union (EBU) can participate, including non-European countries like Australia, Israel and Armenia."),
      ("How does Eurovision voting work?", "Each country awards points through a combination of national jury votes and public televote. 12 points goes to the favourite (douze points!)."),
    ]
  ),
  dict(
    slug="cannes", name="Cannes Film Festival", type="variable", category="Entertainment",
    regions=["global", "fr"],
    seo_title="Cannes Film Festival Countdown — Days Until Cannes",
    meta_desc="Live countdown to the 2026 Cannes Film Festival. The Palme d'Or competition opens May 13, 2026 on the French Riviera.",
    hero_desc="Countdown to the 2026 Cannes Film Festival.",
    content="The Cannes Film Festival is one of the world's most prestigious and publicised film festivals. Held annually in Cannes, France on the French Riviera, it presents and promotes films from around the world. The top prize, the Palme d'Or, is among the most coveted awards in cinema.",
    faqs=[
      ("When is the Cannes Film Festival?", "Cannes 2026 opens on May 13, 2026 and runs through May 24."),
      ("Where is the Cannes Film Festival?", "The festival is held at the Palais des Festivals et des Congrès in Cannes, on the French Riviera."),
      ("What is the Palme d'Or?", "The Palme d'Or is the highest prize awarded at Cannes, given to the best film in the main competition."),
    ]
  ),
  dict(
    slug="coachella", name="Coachella", type="variable", category="Entertainment",
    regions=["global"],
    seo_title="Coachella Countdown — Days Until Coachella Valley Music Festival",
    meta_desc="Live countdown to Coachella. The world's most famous music festival takes place in the California desert each April.",
    hero_desc="Countdown to Coachella.",
    content="The Coachella Valley Music and Arts Festival is held annually at the Empire Polo Club in Indio, California. It is one of the largest and most famous music festivals in the world, featuring top artists across two weekends in April.",
    faqs=[
      ("When is Coachella?", "Coachella 2027 Weekend 1 is estimated for April 9–11, 2027. Official dates are typically announced in late 2026."),
      ("Where is Coachella held?", "Coachella takes place at the Empire Polo Club in Indio, California, in the Coachella Valley desert."),
      ("How do I get Coachella tickets?", "Tickets go on sale on coachella.com, often selling out within hours. Passes include camping and shuttle options."),
    ]
  ),

  # ── Sales ──────────────────────────────────────────────────────────────────
  dict(
    slug="black-friday", name="Black Friday", type="auto", category="Sales",
    regions=["global"],
    seo_title="Black Friday Countdown — Days Until Black Friday",
    meta_desc="How many days until Black Friday? Live countdown to the biggest shopping day of the year, the fourth Friday of November.",
    hero_desc="Countdown to Black Friday — fourth Friday of November.",
    content="Black Friday is the Friday after Thanksgiving in the United States and has become the unofficial start of the Christmas shopping season. Retailers offer steep discounts, and the day has expanded globally with online deals that now extend over an entire week.",
    faqs=[
      ("When is Black Friday?", "Black Friday 2026 falls on Friday, November 27."),
      ("When does Black Friday start?", "Many retailers now start Black Friday deals a week early online. The main in-store event is always the Friday after US Thanksgiving."),
      ("When is Cyber Monday?", "Cyber Monday 2026 is on Monday, November 30, 2026 — three days after Black Friday."),
      ("Is Black Friday only in the US?", "No. Black Friday has spread globally and is now a major shopping event in the UK, Canada, Australia, Brazil, and most of Europe."),
      ("What are the best Black Friday deals?", "Electronics, appliances, clothing, toys and travel tend to offer the deepest discounts on Black Friday, both in-store and online."),
    ]
  ),
  dict(
    slug="cyber-monday", name="Cyber Monday", type="auto", category="Sales",
    regions=["global"],
    seo_title="Cyber Monday Countdown — Days Until Cyber Monday",
    meta_desc="Live countdown to Cyber Monday. The biggest online shopping day of the year falls on the Monday after Black Friday.",
    hero_desc="Countdown to Cyber Monday — the biggest online shopping day.",
    content="Cyber Monday is an online shopping holiday created by retailers in 2005 to encourage people to shop online. It falls on the Monday after US Thanksgiving (three days after Black Friday) and has grown into the biggest online shopping day of the year globally.",
    faqs=[
      ("When is Cyber Monday?", "Cyber Monday 2026 is on Monday, November 30."),
      ("Is Cyber Monday better than Black Friday?", "Both offer major deals. Cyber Monday focuses on online shopping and tech, while Black Friday traditionally includes both in-store and online offers. Many retailers now offer deals across the full Cyber Week."),
      ("What are the best Cyber Monday deals?", "Electronics, software, streaming services, laptops, and gaming gear typically see the deepest Cyber Monday discounts."),
      ("Is Cyber Monday only in the US?", "Originally a US event, Cyber Monday is now observed globally in the UK, Canada, Australia, and Latin America."),
    ]
  ),
  dict(
    slug="hot-sale", name="Hot Sale", type="variable", category="Sales",
    regions=["es"],
    seo_title="Hot Sale Argentina Countdown — Cuántos días faltan para el Hot Sale",
    meta_desc="Cuenta regresiva en vivo para el Hot Sale Argentina 2027. El evento de descuentos online más grande del país.",
    hero_desc="Countdown to Hot Sale Argentina — Argentina's biggest online sale event.",
    content="El Hot Sale es el evento de comercio electrónico más importante de Argentina, organizado por la Cámara Argentina de Comercio Electrónico (CACE). Se realiza anualmente en mayo y reúne a cientos de marcas con ofertas y descuentos exclusivos online.",
    faqs=[
      ("¿Cuándo es el Hot Sale 2027?", "Las fechas del Hot Sale Argentina 2027 aún no fueron confirmadas. Suele realizarse en mayo, alrededor del 18 al 20."),
      ("¿Qué marcas participan en el Hot Sale?", "Participan cientos de marcas incluyendo supermercados, electrónica, indumentaria, viajes y más. La lista se publica en hotsal.com.ar antes del evento."),
      ("¿Cómo aprovechar el Hot Sale?", "Conviene armar una lista de productos antes del evento, comparar precios con anterioridad y tener cuenta creada en las tiendas para poder comprar rápido."),
      ("¿El Hot Sale tiene descuentos en cuotas?", "Sí, muchas marcas ofrecen cuotas sin interés a través de tarjetas de crédito durante el Hot Sale, además de descuentos directos en el precio."),
    ]
  ),

  # ── Nature ─────────────────────────────────────────────────────────────────
  dict(
    slug="full-moon", name="Next Full Moon", type="auto", category="Nature",
    regions=["global"],
    seo_title="Full Moon Countdown — Days Until the Next Full Moon",
    meta_desc="Live countdown to the next full moon. Exact days, hours and seconds until the full moon, updated in real time.",
    hero_desc="Countdown to the next full moon.",
    content="A full moon occurs approximately every 29.5 days when the Moon is on the opposite side of the Earth from the Sun, illuminating the lunar surface as seen from Earth. The countdown above always shows the time remaining until the next full moon.",
    faqs=[
      ("When is the next full moon?", "The countdown above shows the exact date and time of the next full moon (accurate to within ±12 hours)."),
      ("How often is there a full moon?", "A full moon occurs approximately every 29.5 days (a synodic month), so there are roughly 12–13 full moons per year."),
      ("What is a supermoon?", "A supermoon occurs when a full moon coincides with the Moon's closest approach to Earth (perigee), making it appear larger and brighter."),
      ("What is a blue moon?", "A blue moon is the second full moon in a calendar month, or the third full moon in a season with four full moons. It happens roughly every 2.5 years."),
    ]
  ),
  dict(
    slug="eclipse", name="Solar Eclipse", type="variable", category="Nature",
    regions=["global"],
    seo_title="Solar Eclipse 2026 Countdown — Days Until the Total Solar Eclipse",
    meta_desc="Live countdown to the total solar eclipse on August 12, 2026. Visible from Spain, North Africa and parts of South America.",
    hero_desc="Countdown to the 2026 total solar eclipse.",
    content="The total solar eclipse of August 12, 2026 will be visible along a path stretching from Greenland across the North Atlantic, through the Iberian Peninsula (southern Spain, Gibraltar), and into North Africa. Partial phases will be visible across a much wider region including most of Europe and South America.",
    faqs=[
      ("When is the next solar eclipse?", "The next total solar eclipse is on August 12, 2026."),
      ("Where can I see the 2026 solar eclipse?", "The path of totality crosses southern Spain (including Málaga and Valencia) and northern Morocco. Partial eclipse visible across Europe and North Africa."),
      ("How long does totality last?", "The maximum duration of totality on August 12, 2026 is approximately 2 minutes 18 seconds, near the coast of Spain."),
      ("Is it safe to look at a solar eclipse?", "Never look directly at a partial eclipse without certified eclipse glasses (ISO 12312-2). During the brief totality phase, it is safe to look with the naked eye."),
    ]
  ),

  # ── Music ─────────────────────────────────────────────────────────────────
  dict(
    slug="lollapalooza-ar", name="Lollapalooza Argentina", type="variable", category="Music",
    regions=["es"],
    seo_title="Lollapalooza Argentina Countdown — Cuántos días faltan",
    meta_desc="Cuenta regresiva en vivo para el Lollapalooza Argentina 2027 en el Hipódromo de San Isidro, Buenos Aires.",
    hero_desc="Countdown to Lollapalooza Argentina.",
    content="Lollapalooza Argentina is one of the biggest music festivals in South America, held annually at the Hipódromo de San Isidro in Buenos Aires. The 2027 dates and lineup have not yet been announced.",
    faqs=[
      ("¿Cuándo es el Lollapalooza Argentina 2027?", "Las fechas aún no fueron anunciadas. El festival suele realizarse en marzo en el Hipódromo de San Isidro, Buenos Aires."),
      ("¿Dónde se hace el Lollapalooza Argentina?", "En el Hipódromo de San Isidro, ubicado en San Isidro, provincia de Buenos Aires, Argentina."),
      ("¿Cuántos días dura el Lollapalooza Argentina?", "El festival suele durar 3 días, con múltiples escenarios y artistas nacionales e internacionales en cada jornada."),
      ("¿Cómo comprar entradas para Lollapalooza Argentina?", "Las entradas se adquieren a través de la web oficial de Lollapalooza Argentina y plataformas como Ticketek. Los abonos suelen agotarse rápidamente."),
    ]
  ),
  dict(
    slug="lollapalooza-cl", name="Lollapalooza Chile", type="variable", category="Music",
    regions=["es"],
    seo_title="Lollapalooza Chile Countdown — Cuántos días faltan",
    meta_desc="Cuenta regresiva en vivo para el Lollapalooza Chile 2027 en el Parque Bicentenario Cerrillos, Santiago.",
    hero_desc="Countdown to Lollapalooza Chile.",
    content="Lollapalooza Chile is held annually at Parque Bicentenario Cerrillos in Santiago. It is one of the most important music festivals in Latin America, typically held in March. The 2027 lineup and dates are pending announcement.",
    faqs=[
      ("¿Cuándo es el Lollapalooza Chile 2027?", "Las fechas aún no fueron anunciadas. Suele realizarse en marzo en el Parque Bicentenario Cerrillos, Santiago."),
      ("¿Dónde se hace el Lollapalooza Chile?", "En el Parque Bicentenario Cerrillos, en la comuna de Cerrillos, Santiago de Chile."),
      ("¿Cuántos días dura el Lollapalooza Chile?", "El festival dura 3 días, con múltiples escenarios. Suele coincidir en fechas similares al Lollapalooza Argentina."),
      ("¿Cómo comprar entradas para Lollapalooza Chile?", "Las entradas se venden a través de Puntoticket y la web oficial del festival. Los abonos full pass suelen ser los primeros en agotarse."),
    ]
  ),
  dict(
    slug="cosquin-rock", name="Cosquín Rock", type="variable", category="Music",
    regions=["es"],
    seo_title="Cosquín Rock Countdown — Cuántos días faltan",
    meta_desc="Cuenta regresiva en vivo para el Cosquín Rock 2027 en Santa María de Punilla, Córdoba.",
    hero_desc="Countdown to Cosquín Rock.",
    content="El Cosquín Rock es uno de los festivales de rock más importantes de Argentina y América Latina, realizado en Santa María de Punilla, Córdoba. Suele celebrarse en febrero y reúne a artistas nacionales e internacionales. Las fechas de 2027 aún no fueron anunciadas.",
    faqs=[
      ("¿Cuándo es el Cosquín Rock 2027?", "Las fechas aún no fueron anunciadas. Suele realizarse en febrero en Santa María de Punilla, Córdoba."),
      ("¿Dónde se hace el Cosquín Rock?", "El festival se realiza en Santa María de Punilla, a pocos kilómetros de Cosquín, en las Sierras de Córdoba, Argentina."),
      ("¿Cómo comprar entradas para Cosquín Rock?", "Las entradas se venden a través de Ticketek Argentina y en la web oficial del festival. Se recomienda comprar con anticipación."),
      ("¿Cuántos escenarios tiene el Cosquín Rock?", "El festival cuenta con varios escenarios de diferentes tamaños, incluyendo el escenario principal y escenarios alternativos para bandas emergentes."),
    ]
  ),
  dict(
    slug="rock-in-rio", name="Rock in Rio Lisboa", type="variable", category="Music",
    regions=["pt"],
    seo_title="Rock in Rio Lisboa Countdown — Days Until Rock in Rio",
    meta_desc="Live countdown to Rock in Rio Lisboa 2026 at Parque da Bela Vista, Lisbon. Starts September 18, 2026.",
    hero_desc="Countdown to Rock in Rio Lisboa.",
    content="Rock in Rio Lisboa is one of the world's largest music festivals, held at Parque da Bela Vista in Lisbon, Portugal. The 2026 edition starts on September 18 and features international headliners across multiple stages.",
    faqs=[
      ("When is Rock in Rio Lisboa?", "Rock in Rio Lisboa 2026 starts on September 18, 2026 at Parque da Bela Vista, Lisbon."),
      ("How do I get Rock in Rio Lisboa tickets?", "Tickets (called Passports) are available at the official Rock in Rio Lisboa website. They often sell out within hours of going on sale."),
      ("How many days does Rock in Rio Lisboa last?", "Rock in Rio Lisboa typically runs over two consecutive weekends — 4 days of concerts spread across 8 days."),
      ("What stages does Rock in Rio Lisboa have?", "The main stage is the Palco Mundo (World Stage). Other stages include the Palco NOS and several smaller themed stages throughout the Cidade do Rock."),
    ]
  ),

  # ── Fashion ────────────────────────────────────────────────────────────────
  dict(
    slug="nyfw", name="New York Fashion Week", type="variable", category="Fashion",
    regions=["global"],
    seo_title="New York Fashion Week Countdown — Days Until NYFW",
    meta_desc="Live countdown to New York Fashion Week September 2026 (Spring/Summer 2027 collections).",
    hero_desc="Countdown to New York Fashion Week — September.",
    content="New York Fashion Week (NYFW) is held twice a year in New York City — in February (for Fall/Winter collections) and September (for Spring/Summer collections). It is the first of the four major fashion weeks, followed by London, Milan and Paris.",
    faqs=[
      ("When is New York Fashion Week?", "NYFW September 2026 starts on September 8, 2026 (Spring/Summer 2027 collections)."),
      ("Can I attend NYFW?", "NYFW shows are primarily industry-only events (buyers, press, stylists). Some designers hold open presentations or pop-up events — check nyfw.com for public programming."),
      ("How long does New York Fashion Week last?", "NYFW typically runs for about 7–9 days. It is held twice a year: February (Fall/Winter) and September (Spring/Summer)."),
      ("What is the order of the Big Four fashion weeks?", "The Big Four run in order: New York → London → Milan → Paris. The September season typically starts in early September and ends in late October."),
    ]
  ),
  dict(
    slug="paris-fw", name="Paris Fashion Week", type="variable", category="Fashion",
    regions=["global", "fr"],
    seo_title="Paris Fashion Week Countdown — Days Until PFW",
    meta_desc="Live countdown to Paris Fashion Week September 2026 — the final and most glamorous of the Big Four fashion weeks.",
    hero_desc="Countdown to Paris Fashion Week — September.",
    content="Paris Fashion Week closes the Big Four fashion weeks season. The September edition (Spring/Summer 2027 collections) features shows from Chanel, Dior, Louis Vuitton, Saint Laurent and more iconic French and international houses.",
    faqs=[
      ("When is Paris Fashion Week?", "Paris Fashion Week September 2026 starts on September 28, 2026 (Spring/Summer 2027 collections)."),
      ("What is the order of the Big Four Fashion Weeks?", "The Big Four run in order: New York (Sep 8) → London → Milan (Sep 16) → Paris (Sep 28)."),
      ("What brands show at Paris Fashion Week?", "Paris Fashion Week features shows from Chanel, Dior, Louis Vuitton, Balenciaga, Givenchy, Saint Laurent, Valentino and many other iconic houses."),
      ("Is Paris Fashion Week open to the public?", "Most runway shows are strictly invitation-only. However, some brands hold exhibitions, presentations and pop-up events open to a wider audience."),
    ]
  ),
  dict(
    slug="milan-fw", name="Milan Fashion Week", type="variable", category="Fashion",
    regions=["global"],
    seo_title="Milan Fashion Week Countdown — Days Until MFW",
    meta_desc="Live countdown to Milan Fashion Week September, featuring Prada, Gucci, Versace, Armani and more.",
    hero_desc="Countdown to Milan Fashion Week — September.",
    content="Milan Fashion Week is the third of the Big Four fashion weeks, held in September for Spring/Summer collections and February for Fall/Winter. The September 2026 edition features runway shows from Prada, Gucci, Versace, Bottega Veneta and many other iconic Italian houses.",
    faqs=[
      ("When is Milan Fashion Week?", "Milan Fashion Week September 2026 starts on September 16, 2026 (Spring/Summer 2027 collections)."),
      ("What brands show at Milan Fashion Week?", "Milan Fashion Week features shows from Prada, Gucci, Versace, Armani, Dolce & Gabbana, Bottega Veneta, Fendi and many other Italian and international houses."),
      ("How long does Milan Fashion Week last?", "Milan Fashion Week typically runs for about 7–8 days, with multiple shows each day across the city."),
      ("Is Milan Fashion Week open to the public?", "Most runway shows are invitation-only for buyers, press and VIPs. Some brands also hold open exhibitions or public events during the week."),
    ]
  ),
  dict(
    slug="bafweek", name="Buenos Aires Fashion Week", type="variable", category="Fashion",
    regions=["es"],
    seo_title="Buenos Aires Fashion Week Countdown — Cuántos días faltan",
    meta_desc="Cuenta regresiva en vivo para el Buenos Aires Fashion Week 2026, la semana de la moda más importante de Argentina.",
    hero_desc="Countdown to Buenos Aires Fashion Week.",
    content="Buenos Aires Fashion Week (BAFWeek) is Argentina's premier fashion week, held twice a year showcasing the best of Argentine and Latin American fashion design. The Spring/Summer edition takes place in October at various venues across Buenos Aires.",
    faqs=[
      ("¿Cuándo es el BAFWeek 2026?", "El Buenos Aires Fashion Week edición primavera-verano 2026 está estimado para octubre de 2026."),
      ("¿Dónde se realiza el BAFWeek?", "El BAFWeek se realiza en distintas sedes de Buenos Aires, incluyendo el Centro Metropolitano de Diseño y otros espacios culturales de la ciudad."),
      ("¿Se puede asistir al BAFWeek sin invitación?", "Algunos desfiles y presentaciones del BAFWeek son abiertos al público. Consultá la web oficial y las redes del evento para acceder a entradas o acreditaciones."),
      ("¿Quiénes participan en el BAFWeek?", "Participan los principales diseñadores y marcas de moda argentina, además de marcas regionales latinoamericanas invitadas."),
    ]
  ),


  # ── Months ────────────────────────────────────────────────────────────────────
  dict(
    slug="january", name="January", type="auto", category="Months",
    regions=["global"],
    seo_title="Countdown to January — Days Until January 1st",
    meta_desc="Live countdown to January 1st. See exactly how many days, hours, minutes and seconds until January begins.",
    hero_desc="Countdown to the start of January.",
    content="January is the first month of the year in the Gregorian calendar, with 31 days. Named after Janus, the Roman god of beginnings and doorways, January marks the start of a new year for most of the world. The countdown resets automatically each year.",
    faqs=[
      ("When does January start?", "January 1st is the first day of the new year in the Gregorian calendar, celebrated worldwide as New Year's Day."),
      ("How many days does January have?", "January has 31 days."),
      ("What are the main holidays in January?", "Key January dates include New Year's Day (Jan 1), Epiphany / Three Kings Day (Jan 6), and Martin Luther King Jr. Day in the US (third Monday)."),
    ]
  ),
  dict(
    slug="february", name="February", type="auto", category="Months",
    regions=["global"],
    seo_title="Countdown to February — Days Until February",
    meta_desc="Live countdown to February 1st. See exactly how many days, hours and minutes until February begins.",
    hero_desc="Countdown to the start of February.",
    content="February is the second month of the year and the shortest, with 28 days in common years and 29 in leap years. It hosts Valentine's Day on February 14th and Groundhog Day on February 2nd.",
    faqs=[
      ("How many days does February have?", "February has 28 days in common years and 29 in leap years."),
      ("When is the next leap year?", "Leap years occur every 4 years. The next leap year is 2028."),
      ("What holidays are in February?", "Valentine's Day (Feb 14), Groundhog Day (Feb 2), Presidents' Day in the USA (third Monday), and Carnival in many countries."),
    ]
  ),
  dict(
    slug="march", name="March", type="auto", category="Months",
    regions=["global"],
    seo_title="Countdown to March — Days Until March",
    meta_desc="Live countdown to March 1st. See exactly how many days, hours and minutes until March begins.",
    hero_desc="Countdown to the start of March.",
    content="March is the third month of the year with 31 days. It marks the beginning of spring in the Northern Hemisphere (around March 20) and the start of autumn in the Southern Hemisphere. St. Patrick's Day falls on March 17.",
    faqs=[
      ("When does spring start in March?", "The spring equinox in the Northern Hemisphere falls around March 20 or 21 each year."),
      ("How many days does March have?", "March has 31 days."),
      ("What are the main March holidays?", "St. Patrick's Day (Mar 17), International Women's Day (Mar 8), and the spring equinox."),
    ]
  ),
  dict(
    slug="april", name="April", type="auto", category="Months",
    regions=["global"],
    seo_title="Countdown to April — Days Until April",
    meta_desc="Live countdown to April 1st. See exactly how many days, hours and minutes until April begins.",
    hero_desc="Countdown to the start of April.",
    content="April is the fourth month of the year with 30 days. It is known for April Fools' Day on April 1st. Easter often falls in April. In the Southern Hemisphere, April signals the beginning of autumn.",
    faqs=[
      ("What is April Fools' Day?", "April 1st is a day traditionally marked by pranks and jokes. Its exact origin is uncertain."),
      ("How many days does April have?", "April has 30 days."),
      ("Does Easter always fall in April?", "Easter can fall between March 22 and April 25. It often lands in April."),
    ]
  ),
  dict(
    slug="may-month", name="May", type="auto", category="Months",
    regions=["global"],
    seo_title="Countdown to May — Days Until May",
    meta_desc="Live countdown to May 1st. See exactly how many days, hours and minutes until May begins.",
    hero_desc="Countdown to the start of May.",
    content="May is the fifth month of the year with 31 days. It includes International Labour Day on May 1st (celebrated in many countries as a public holiday), Mother's Day in many nations (second Sunday), and marks mid-spring in the Northern Hemisphere.",
    faqs=[
      ("When is Labour Day?", "International Labour Day (May Day) is celebrated on May 1st in most countries."),
      ("When is Mother's Day in May?", "In most countries, Mother's Day falls on the second Sunday of May."),
      ("How many days does May have?", "May has 31 days."),
    ]
  ),
  dict(
    slug="june-month", name="June", type="auto", category="Months",
    regions=["global"],
    seo_title="Countdown to June — Days Until June",
    meta_desc="Live countdown to June 1st. See exactly how many days, hours and minutes until June begins.",
    hero_desc="Countdown to the start of June.",
    content="June is the sixth month of the year with 30 days. The summer solstice in the Northern Hemisphere occurs around June 21, marking the longest day of the year. Pride Month is celebrated globally throughout June.",
    faqs=[
      ("When is the summer solstice?", "The summer solstice in the Northern Hemisphere falls around June 21, the longest day of the year."),
      ("What is celebrated in June?", "June hosts Pride Month, Father's Day (third Sunday in many countries), and the summer solstice."),
      ("How many days does June have?", "June has 30 days."),
    ]
  ),
  dict(
    slug="july-month", name="July", type="auto", category="Months",
    regions=["global"],
    seo_title="Countdown to July — Days Until July",
    meta_desc="Live countdown to July 1st. See exactly how many days, hours and minutes until July begins.",
    hero_desc="Countdown to the start of July.",
    content="July is the seventh month of the year with 31 days. It is named after Julius Caesar. Key July dates include US Independence Day (July 4), Canada Day (July 1), and Bastille Day in France (July 14).",
    faqs=[
      ("What happens on July 4th?", "July 4th is US Independence Day, commemorating the Declaration of Independence in 1776."),
      ("What is Bastille Day?", "Bastille Day on July 14th is France's national holiday, celebrating the storming of the Bastille in 1789."),
      ("How many days does July have?", "July has 31 days."),
    ]
  ),
  dict(
    slug="august", name="August", type="auto", category="Months",
    regions=["global"],
    seo_title="Countdown to August — Days Until August",
    meta_desc="Live countdown to August 1st. See exactly how many days, hours and minutes until August begins.",
    hero_desc="Countdown to the start of August.",
    content="August is the eighth month of the year with 31 days, named after Emperor Augustus. It is the peak of summer in the Northern Hemisphere and a popular holiday month. August also marks the last full month of summer before schools return in September.",
    faqs=[
      ("Why is August named August?", "August is named after Roman Emperor Augustus Caesar, who considered it his lucky month."),
      ("What holidays are in August?", "August includes India's Independence Day (Aug 15), National Day in many countries, and summer bank holidays in the UK."),
      ("How many days does August have?", "August has 31 days."),
    ]
  ),
  dict(
    slug="september", name="September", type="auto", category="Months",
    regions=["global"],
    seo_title="Countdown to September — Days Until September",
    meta_desc="Live countdown to September 1st. See exactly how many days, hours and minutes until September begins.",
    hero_desc="Countdown to the start of September.",
    content="September is the ninth month of the year with 30 days. The autumn equinox in the Northern Hemisphere falls around September 22 or 23. Schools typically resume in September across the Northern Hemisphere.",
    faqs=[
      ("When does autumn start in September?", "The autumn equinox in the Northern Hemisphere falls around September 22 or 23."),
      ("What is celebrated in September?", "Labor Day in the USA and Canada (first Monday), Mexican Independence Day (Sep 16), and the autumn equinox."),
      ("How many days does September have?", "September has 30 days."),
    ]
  ),
  dict(
    slug="october", name="October", type="auto", category="Months",
    regions=["global"],
    seo_title="Countdown to October — Days Until October",
    meta_desc="Live countdown to October 1st. See exactly how many days, hours and minutes until October begins.",
    hero_desc="Countdown to the start of October.",
    content="October is the tenth month of the year with 31 days. It is home to Halloween on October 31, Oktoberfest in Germany (late September through early October), and World Mental Health Day on October 10.",
    faqs=[
      ("When is Halloween?", "Halloween is on October 31 every year."),
      ("When is Oktoberfest?", "Oktoberfest typically runs from late September through the first weekend of October in Munich, Germany."),
      ("How many days does October have?", "October has 31 days."),
    ]
  ),
  dict(
    slug="november", name="November", type="auto", category="Months",
    regions=["global"],
    seo_title="Countdown to November — Days Until November",
    meta_desc="Live countdown to November 1st. See exactly how many days, hours and minutes until November begins.",
    hero_desc="Countdown to the start of November.",
    content="November is the eleventh month of the year with 30 days. It includes Dia de los Muertos (Nov 1-2), Veterans Day / Remembrance Day (Nov 11), and Thanksgiving in the USA (fourth Thursday). Black Friday follows Thanksgiving.",
    faqs=[
      ("When is Thanksgiving?", "In the USA, Thanksgiving falls on the fourth Thursday of November. In Canada, it is the second Monday of October."),
      ("When is Black Friday?", "Black Friday falls the day after US Thanksgiving, on the fourth Friday of November."),
      ("How many days does November have?", "November has 30 days."),
    ]
  ),
  dict(
    slug="december", name="December", type="auto", category="Months",
    regions=["global"],
    seo_title="Countdown to December — Days Until December",
    meta_desc="Live countdown to December 1st. See exactly how many days, hours and minutes until December begins.",
    hero_desc="Countdown to the start of December.",
    content="December is the twelfth and final month of the year with 31 days. It hosts the winter solstice (around December 21), Christmas (December 25), Hanukkah (dates vary), Kwanzaa (Dec 26), and New Year's Eve (Dec 31).",
    faqs=[
      ("When is the winter solstice?", "The winter solstice in the Northern Hemisphere falls around December 21, the shortest day of the year."),
      ("What holidays are in December?", "Christmas (Dec 25), Hanukkah (dates vary), Kwanzaa (Dec 26-Jan 1), New Year's Eve (Dec 31), and the winter solstice."),
      ("How many days does December have?", "December has 31 days."),
    ]
  ),

  # ── Time ──────────────────────────────────────────────────────────────────────
  dict(
    slug="midnight", name="Midnight", type="auto", category="Time",
    regions=["global"],
    seo_title="Countdown to Midnight — Time Until Tonight's Midnight",
    meta_desc="Live countdown to midnight tonight in your timezone. See exactly how many hours, minutes and seconds until the clock strikes 12:00 AM.",
    hero_desc="Countdown to midnight tonight in your local timezone.",
    content="Midnight marks the transition between one calendar day and the next, occurring at exactly 12:00:00 AM. The countdown above resets automatically every day, always showing the time remaining until the next midnight in your selected country's timezone.",
    faqs=[
      ("What time is midnight?", "Midnight is 12:00:00 AM, the moment when one day ends and the next begins."),
      ("Is midnight 12 AM or 12 PM?", "Midnight is 12:00 AM (ante meridiem — before noon). Noon is 12:00 PM."),
      ("Does the countdown adjust for my timezone?", "Yes. The countdown uses the timezone of your selected country to show the correct local midnight."),
    ]
  ),

  # ── Seasons ───────────────────────────────────────────────────────────────────
  dict(
    slug="spring", name="Spring", type="auto", category="Seasons",
    regions=["global"],
    seo_title="Countdown to Spring — Days Until the First Day of Spring",
    meta_desc="Live countdown to the first day of spring. The spring equinox marks the astronomical start of the season — adapts to your hemisphere.",
    hero_desc="Countdown to the first day of spring in your hemisphere.",
    content="Spring begins at the vernal equinox, when day and night are approximately equal in length. In the Northern Hemisphere this falls around March 20; in the Southern Hemisphere around September 23. The countdown automatically adapts to the hemisphere of your selected country.",
    faqs=[
      ("When does spring start?", "Spring begins at the vernal equinox: around March 20 in the Northern Hemisphere and around September 23 in the Southern Hemisphere."),
      ("Does the countdown show my hemisphere?", "Yes. Select your country and the countdown will show the correct spring start date for your hemisphere."),
      ("What is the vernal equinox?", "The vernal equinox is the moment when the sun crosses the celestial equator heading north, giving roughly equal day and night everywhere on Earth."),
    ]
  ),
  dict(
    slug="summer", name="Summer", type="auto", category="Seasons",
    regions=["global"],
    seo_title="Countdown to Summer — Days Until the First Day of Summer",
    meta_desc="Live countdown to the first day of summer. The summer solstice is the longest day of the year — adapts to your hemisphere.",
    hero_desc="Countdown to the first day of summer in your hemisphere.",
    content="Summer begins at the summer solstice, the longest day of the year. In the Northern Hemisphere this falls around June 21; in the Southern Hemisphere around December 21. The countdown automatically adapts to the hemisphere of your selected country.",
    faqs=[
      ("When does summer start?", "Summer begins at the summer solstice: around June 21 in the Northern Hemisphere and around December 21 in the Southern Hemisphere."),
      ("What is the summer solstice?", "The summer solstice is the day with the most hours of daylight. The sun reaches its highest point in the sky at noon."),
      ("Does the countdown adapt to my hemisphere?", "Yes. Select your country and the countdown will show the correct summer start date for your hemisphere."),
    ]
  ),
  dict(
    slug="autumn", name="Autumn / Fall", type="auto", category="Seasons",
    regions=["global"],
    seo_title="Countdown to Autumn — Days Until the First Day of Fall",
    meta_desc="Live countdown to the first day of autumn (fall). The autumnal equinox marks the start of the season — adapts to your hemisphere.",
    hero_desc="Countdown to the first day of autumn in your hemisphere.",
    content="Autumn (also called fall) begins at the autumnal equinox. In the Northern Hemisphere this falls around September 23; in the Southern Hemisphere around March 20. The countdown automatically adapts to the hemisphere of your selected country.",
    faqs=[
      ("When does autumn start?", "Autumn begins at the autumnal equinox: around September 23 in the Northern Hemisphere and around March 20 in the Southern Hemisphere."),
      ("Why is autumn also called fall?", "The word 'fall' comes from the phrase 'fall of the leaf,' describing when deciduous trees shed their leaves."),
      ("Does the countdown adapt to my hemisphere?", "Yes. Select your country and the countdown will show the correct autumn start date for your hemisphere."),
    ]
  ),
  dict(
    slug="winter-season", name="Winter", type="auto", category="Seasons",
    regions=["global"],
    seo_title="Countdown to Winter — Days Until the First Day of Winter",
    meta_desc="Live countdown to the first day of winter. The winter solstice is the shortest day of the year — adapts to your hemisphere.",
    hero_desc="Countdown to the first day of winter in your hemisphere.",
    content="Winter begins at the winter solstice, the shortest day of the year. In the Northern Hemisphere this falls around December 21; in the Southern Hemisphere around June 21. The countdown automatically adapts to the hemisphere of your selected country.",
    faqs=[
      ("When does winter start?", "Winter begins at the winter solstice: around December 21 in the Northern Hemisphere and around June 21 in the Southern Hemisphere."),
      ("What is the winter solstice?", "The winter solstice is the day with the fewest hours of daylight. It marks the official start of winter and the return of longer days."),
      ("Does the countdown adapt to my hemisphere?", "Yes. Select your country and the countdown will show the correct winter start date for your hemisphere."),
    ]
  ),

  # ── School ────────────────────────────────────────────────────────────────────
  dict(
    slug="back-to-school", name="Back to School", type="auto", category="School",
    regions=["global"],
    seo_title="Back to School Countdown — Days Until School Starts",
    meta_desc="Live countdown to back-to-school day. The date automatically adapts to the school year calendar of your selected country.",
    hero_desc="Countdown to the first day of school in your country.",
    content="The back-to-school date varies widely around the world. In the Northern Hemisphere most schools resume in late August or early September. In the Southern Hemisphere — countries like Argentina, Chile, Brazil and Australia — schools typically restart in late January or early February. The countdown automatically adapts to your selected country.",
    faqs=[
      ("When does school start?", "School start dates vary by country. In the USA it is typically late August. In Argentina and Chile it is around early March. Select your country for the exact date."),
      ("Does the countdown adapt to my country?", "Yes. The countdown uses the approximate first day of school for your selected country."),
      ("Why do Southern Hemisphere countries start school in February?", "Because their seasons are reversed. Summer vacation coincides with December-January, so the school year starts in February or March."),
    ]
  ),
  dict(
    slug="summer-vacation", name="Summer Vacation", type="auto", category="School",
    regions=["global"],
    seo_title="Summer Vacation Countdown — Days Until Summer Break",
    meta_desc="Live countdown to the start of summer vacation. The date adapts to your hemisphere's school calendar.",
    hero_desc="Countdown to the start of summer school vacation.",
    content="Summer vacation marks the long school break that coincides with the warmest months of the year. In the Northern Hemisphere this typically begins in June, while in the Southern Hemisphere it starts in December. The countdown adapts to your selected country.",
    faqs=[
      ("When does summer vacation start?", "Roughly mid-June in the Northern Hemisphere and mid-December in the Southern Hemisphere, varying by country."),
      ("How long is summer vacation?", "Summer break typically lasts 6 to 12 weeks depending on the country."),
      ("Does the countdown adapt to my hemisphere?", "Yes. Select your country and the countdown will show the approximate start of summer vacation for your region."),
    ]
  ),
  dict(
    slug="winter-vacation", name="Winter Vacation", type="auto", category="School",
    regions=["global"],
    seo_title="Winter Vacation Countdown — Days Until Winter Break",
    meta_desc="Live countdown to the start of winter school vacation. The date adapts to your hemisphere.",
    hero_desc="Countdown to the start of winter school vacation.",
    content="Winter vacation is the school break that coincides with the winter holidays. In the Northern Hemisphere it typically falls in late December. In the Southern Hemisphere (Argentina, Chile, etc.) it falls in July. The countdown adapts to your selected country.",
    faqs=[
      ("When is winter vacation?", "In the Northern Hemisphere, winter break is typically late December. In the Southern Hemisphere it falls around July."),
      ("How long is winter vacation?", "Winter break is usually 2 to 4 weeks, covering the winter holiday period."),
      ("Does the countdown adapt to my country?", "Yes. The countdown uses your selected country to determine the correct winter vacation period."),
    ]
  ),

  # ── National Days ─────────────────────────────────────────────────────────────
  dict(
    slug="independence", name="Independence Day", type="auto", category="National Days",
    regions=["global"],
    seo_title="Independence Day Countdown — Days Until Your Country's Independence Day",
    meta_desc="Live countdown to Independence Day. The date automatically changes based on your selected country — USA, Argentina, Mexico, France, and 50+ more.",
    hero_desc="Countdown to your country's Independence Day.",
    content="Independence Day is the national holiday commemorating the date a country declared or achieved independence from colonial or foreign rule. The date varies by country: July 4 in the USA, July 9 in Argentina, September 16 in Mexico, July 14 in France (Bastille Day), and many more. Select your country above to see your national independence day.",
    faqs=[
      ("When is US Independence Day?", "US Independence Day is July 4, commemorating the Declaration of Independence in 1776."),
      ("Does this countdown adapt to my country?", "Yes. Select your country and the countdown will automatically show the correct independence or national day for your nation."),
      ("What if my country is not listed?", "If your country is not in the list, the countdown defaults to July 4 (US Independence Day) as a reference date."),
      ("What is celebrated on independence day?", "Each country celebrates its own historical milestone: a declaration of independence, a revolution, a liberation, or the founding of the nation."),
    ]
  ),
  dict(
    slug="canada-day", name="Canada Day", type="auto", category="National Days",
    regions=["global"],
    seo_title="Canada Day Countdown — Days Until July 1st",
    meta_desc="Live countdown to Canada Day on July 1st. Celebrate the anniversary of Canadian Confederation.",
    hero_desc="Countdown to Canada Day — July 1st.",
    content="Canada Day, celebrated on July 1st every year, marks the anniversary of Canadian Confederation. On July 1, 1867, the British North America Act came into effect, uniting the provinces of Canada, Nova Scotia and New Brunswick into a single dominion within the British Empire.",
    faqs=[
      ("When is Canada Day?", "Canada Day is on July 1st every year."),
      ("What does Canada Day celebrate?", "Canada Day marks the anniversary of the Constitution Act (1867), which united three provinces into the Dominion of Canada."),
      ("What do Canadians do on Canada Day?", "Canadians celebrate with fireworks, parades, outdoor concerts, barbecues, and public ceremonies across the country."),
    ]
  ),
  dict(
    slug="australia-day", name="Australia Day", type="auto", category="National Days",
    regions=["global"],
    seo_title="Australia Day Countdown — Days Until January 26th",
    meta_desc="Live countdown to Australia Day on January 26th. Australia's national day commemorating the 1788 arrival of the First Fleet.",
    hero_desc="Countdown to Australia Day — January 26th.",
    content="Australia Day is observed on January 26th each year, marking the anniversary of the 1788 arrival of the First Fleet of British ships at Port Jackson, New South Wales. It is Australia's national day, though it remains a topic of ongoing national discussion regarding its date and meaning.",
    faqs=[
      ("When is Australia Day?", "Australia Day is on January 26th every year."),
      ("What does Australia Day commemorate?", "It marks the 1788 arrival of the First Fleet at Port Jackson, the beginning of British colonisation of the continent."),
      ("What happens on Australia Day?", "Celebrations include fireworks, outdoor events, citizenship ceremonies, and the Australian of the Year awards."),
    ]
  ),
  dict(
    slug="waitangi-day", name="Waitangi Day", type="auto", category="National Days",
    regions=["global"],
    seo_title="Waitangi Day Countdown — Days Until February 6th",
    meta_desc="Live countdown to Waitangi Day on February 6th — New Zealand's national day commemorating the Treaty of Waitangi.",
    hero_desc="Countdown to Waitangi Day — February 6th.",
    content="Waitangi Day is New Zealand's national day, observed on February 6th each year. It commemorates the signing of the Treaty of Waitangi on February 6, 1840, between the British Crown and Maori chiefs. The treaty is considered the founding document of New Zealand.",
    faqs=[
      ("When is Waitangi Day?", "Waitangi Day is February 6th every year."),
      ("What is the Treaty of Waitangi?", "The Treaty of Waitangi, signed in 1840, is a founding document of New Zealand establishing a relationship between the Crown and Maori."),
      ("Is Waitangi Day a public holiday?", "Yes, Waitangi Day is a public holiday in New Zealand."),
    ]
  ),
  dict(
    slug="syttende-mai", name="Norwegian Constitution Day", type="auto", category="National Days",
    regions=["global"],
    seo_title="Norwegian Constitution Day Countdown — Syttende Mai, May 17th",
    meta_desc="Live countdown to Syttende Mai — Norway's Constitution Day on May 17th.",
    hero_desc="Countdown to Norway's Constitution Day — May 17th.",
    content="Syttende mai (the 17th of May) is Norway's Constitution Day, celebrating the signing of the Norwegian Constitution on May 17, 1814. It is one of the world's most festive national days, characterized by school parades, traditional folk costumes (bunad), and celebrations in towns across the country.",
    faqs=[
      ("When is Norway's Constitution Day?", "Syttende mai is May 17th every year."),
      ("What is the bunad?", "The bunad is a traditional Norwegian folk costume worn during national celebrations, varying by region."),
      ("Why is May 17 special in Norway?", "On May 17, 1814, Norway signed its Constitution at Eidsvoll, asserting its independence."),
    ]
  ),
  dict(
    slug="german-unity-day", name="German Unity Day", type="auto", category="National Days",
    regions=["global"],
    seo_title="German Unity Day Countdown — Tag der Deutschen Einheit, October 3rd",
    meta_desc="Live countdown to German Unity Day on October 3rd, celebrating the reunification of Germany.",
    hero_desc="Countdown to German Unity Day — October 3rd.",
    content="German Unity Day (Tag der Deutschen Einheit) is Germany's national holiday, celebrated on October 3rd. It commemorates the reunification of East and West Germany on October 3, 1990, following the fall of the Berlin Wall in November 1989.",
    faqs=[
      ("When is German Unity Day?", "German Unity Day is October 3rd every year."),
      ("What does October 3rd commemorate?", "It marks the reunification of East Germany (GDR) and West Germany (FRG) in 1990."),
      ("When did the Berlin Wall fall?", "The Berlin Wall fell on November 9, 1989, leading to German reunification less than a year later."),
    ]
  ),
  dict(
    slug="festa-della-repubblica", name="Italian Republic Day", type="auto", category="National Days",
    regions=["global"],
    seo_title="Italian Republic Day Countdown — Festa della Repubblica, June 2nd",
    meta_desc="Live countdown to Italian Republic Day (Festa della Repubblica) on June 2nd.",
    hero_desc="Countdown to Italian Republic Day — June 2nd.",
    content="The Festa della Repubblica is Italy's national holiday, held on June 2nd each year. It commemorates the institutional referendum of June 2, 1946, when Italians voted to abolish the monarchy and establish a republic. The day is marked by a military parade on Via dei Fori Imperiali in Rome.",
    faqs=[
      ("When is Italian Republic Day?", "Festa della Repubblica is June 2nd every year."),
      ("What happened on June 2, 1946?", "Italy held a referendum in which citizens chose a republic over the monarchy, ending the reign of the House of Savoy."),
      ("What are the main celebrations?", "The main event is a military parade in Rome along Via dei Fori Imperiali, attended by the President of the Republic."),
    ]
  ),
  dict(
    slug="national-day-sg", name="Singapore National Day", type="auto", category="National Days",
    regions=["global"],
    seo_title="Singapore National Day Countdown — Days Until August 9th",
    meta_desc="Live countdown to Singapore National Day on August 9th, celebrating independence since 1965.",
    hero_desc="Countdown to Singapore National Day — August 9th.",
    content="Singapore's National Day is celebrated on August 9th every year, marking the country's independence from Malaysia on August 9, 1965. The highlight is the National Day Parade, featuring military displays, civilian performances, and a fireworks finale.",
    faqs=[
      ("When is Singapore National Day?", "Singapore's National Day is August 9th every year."),
      ("What does August 9th commemorate?", "It marks Singapore's separation from Malaysia and declaration of independence on August 9, 1965."),
      ("What is the National Day Parade?", "The NDP is Singapore's annual celebration featuring military contingents, cultural performances, and spectacular fireworks."),
    ]
  ),
  dict(
    slug="freedom-day-za", name="South Africa Freedom Day", type="auto", category="National Days",
    regions=["global"],
    seo_title="South Africa Freedom Day Countdown — Days Until April 27th",
    meta_desc="Live countdown to South Africa's Freedom Day on April 27th, celebrating the first democratic elections.",
    hero_desc="Countdown to South Africa Freedom Day — April 27th.",
    content="Freedom Day is South Africa's national holiday observed on April 27th. It commemorates the country's first fully democratic elections held on April 27, 1994, which ended apartheid and resulted in Nelson Mandela becoming the first democratically elected president.",
    faqs=[
      ("When is South Africa Freedom Day?", "Freedom Day is April 27th every year."),
      ("What does Freedom Day celebrate?", "It marks the date of South Africa's first democratic elections in 1994, ending the apartheid era."),
      ("Who became president after the 1994 elections?", "Nelson Mandela was elected president, serving from 1994 to 1999."),
    ]
  ),
  dict(
    slug="dia-de-la-hispanidad", name="Dia de la Hispanidad", type="auto", category="National Days",
    regions=["global"],
    seo_title="Dia de la Hispanidad Countdown — Spain's National Day, October 12th",
    meta_desc="Live countdown to Spain's Dia de la Hispanidad (National Day) on October 12th.",
    hero_desc="Countdown to Dia de la Hispanidad — October 12th.",
    content="El Dia de la Hispanidad (also Fiesta Nacional de Espana) is Spain's national holiday, celebrated on October 12th. The date commemorates Christopher Columbus's arrival in the Americas on October 12, 1492. In many Latin American countries the same date is observed as Dia de la Raza or Columbus Day.",
    faqs=[
      ("When is Dia de la Hispanidad?", "Spain's national holiday is October 12th every year."),
      ("What does October 12th commemorate?", "It marks Christopher Columbus's arrival in the Americas on October 12, 1492, sailing under the Spanish crown."),
      ("How is it celebrated in Spain?", "A military parade takes place in Madrid attended by the royal family and senior government officials."),
    ]
  ),
  dict(
    slug="dia-de-la-raza", name="Dia de la Raza", type="auto", category="National Days",
    regions=["global"],
    seo_title="Dia de la Raza Countdown — Days Until October 12th",
    meta_desc="Live countdown to Dia de la Raza on October 12th, celebrated across Latin America.",
    hero_desc="Countdown to Dia de la Raza — October 12th.",
    content="El Dia de la Raza is commemorated on October 12th across many Latin American countries, marking the anniversary of Christopher Columbus's arrival in the Americas in 1492. The holiday is known by different names in different countries: Dia de la Hispanidad in Spain, Columbus Day in the USA, and Dia de la Resistencia Indigena in Venezuela.",
    faqs=[
      ("When is Dia de la Raza?", "Dia de la Raza is October 12th every year."),
      ("What is the significance of October 12th?", "It marks the date Christopher Columbus first sighted the Americas in 1492."),
      ("What is it called in different countries?", "Dia de la Hispanidad (Spain), Columbus Day (USA), Dia de la Raza (Mexico, many Latin American countries), Dia de la Resistencia Indigena (Venezuela)."),
    ]
  ),
  dict(
    slug="dia-de-la-bandera", name="Dia de la Bandera (Argentina)", type="auto", category="National Days",
    regions=["global"],
    seo_title="Dia de la Bandera Countdown — Argentina Flag Day, June 20th",
    meta_desc="Live countdown to Argentina's Dia de la Bandera (Flag Day) on June 20th.",
    hero_desc="Countdown to Argentina's Dia de la Bandera — June 20th.",
    content="El Dia de la Bandera (Flag Day) is one of Argentina's most important national holidays, observed on June 20th. It commemorates the death of Manuel Belgrano, the Argentine general who designed the national flag. The main ceremony takes place in Rosario, Santa Fe, the city where Belgrano raised the flag for the first time on February 27, 1812.",
    faqs=[
      ("When is Dia de la Bandera in Argentina?", "Flag Day in Argentina is June 20th every year."),
      ("Who created the Argentine flag?", "Manuel Belgrano created and raised the Argentine flag for the first time on February 27, 1812, in Rosario."),
      ("Why is June 20th significant?", "June 20th is the anniversary of Manuel Belgrano's death in 1820."),
    ]
  ),
  dict(
    slug="dia-de-la-revolucion", name="Dia de la Revolucion (Mexico)", type="auto", category="National Days",
    regions=["global"],
    seo_title="Dia de la Revolucion Countdown — Mexican Revolution Day, November 20th",
    meta_desc="Live countdown to Mexico's Dia de la Revolucion on November 20th, commemorating the Mexican Revolution of 1910.",
    hero_desc="Countdown to Mexico's Dia de la Revolucion — November 20th.",
    content="El Dia de la Revolucion is a Mexican national holiday celebrated on the third Monday of November (closest to November 20th) to commemorate the start of the Mexican Revolution in 1910. The revolution began as a movement against the dictatorship of Porfirio Diaz and transformed into a decade-long civil conflict that reshaped Mexico.",
    faqs=[
      ("When is Dia de la Revolucion in Mexico?", "Revolution Day in Mexico is observed on the third Monday of November (around November 20th)."),
      ("What does Dia de la Revolucion celebrate?", "It commemorates the start of the Mexican Revolution on November 20, 1910, led by Francisco I. Madero against Porfirio Diaz."),
      ("How is it celebrated?", "Celebrations include military and civic parades, school ceremonies, and cultural events throughout Mexico."),
    ]
  ),
  dict(
    slug="dia-de-la-constitucion", name="Dia de la Constitucion (Mexico)", type="auto", category="National Days",
    regions=["global"],
    seo_title="Dia de la Constitucion Countdown — Mexican Constitution Day, February 5th",
    meta_desc="Live countdown to Mexico's Dia de la Constitucion on February 5th, celebrating the 1917 Constitution.",
    hero_desc="Countdown to Mexico's Dia de la Constitucion — February 5th.",
    content="El Dia de la Constitucion (Constitution Day) is a Mexican national holiday observed on the first Monday of February (closest to February 5th). It commemorates the promulgation of the Political Constitution of Mexico on February 5, 1917, one of the most progressive constitutions of its time.",
    faqs=[
      ("When is Dia de la Constitucion in Mexico?", "Constitution Day in Mexico is observed on the first Monday of February (around February 5th)."),
      ("What does it celebrate?", "It commemorates the promulgation of the Mexican Constitution on February 5, 1917."),
      ("Why is the 1917 constitution significant?", "It was one of the world's first constitutions to include social rights such as land reform, labor rights, and limits on the power of the Catholic Church."),
    ]
  ),
  dict(
    slug="proclamacao-da-republica", name="Proclamacao da Republica (Brazil)", type="auto", category="National Days",
    regions=["global"],
    seo_title="Proclamacao da Republica Countdown — Brazil Republic Day, November 15th",
    meta_desc="Live countdown to Brazil's Proclamacao da Republica on November 15th.",
    hero_desc="Countdown to Brazil's Proclamacao da Republica — November 15th.",
    content="A Proclamacao da Republica is a Brazilian national holiday observed on November 15th, commemorating the proclamation of the republic on November 15, 1889. On that day, a military coup led by Marshal Deodoro da Fonseca ended the Brazilian Empire and established the Republic of Brazil.",
    faqs=[
      ("When is Brazil's Republic Day?", "Proclamacao da Republica is November 15th every year."),
      ("What happened on November 15, 1889?", "Marshal Deodoro da Fonseca proclaimed the Republic of Brazil, ending Emperor Pedro II's reign."),
      ("Is November 15th a public holiday in Brazil?", "Yes, it is a national public holiday in Brazil."),
    ]
  ),
  dict(
    slug="tiradentes", name="Tiradentes (Brazil)", type="auto", category="National Days",
    regions=["global"],
    seo_title="Tiradentes Countdown — Brazil National Holiday, April 21st",
    meta_desc="Live countdown to Tiradentes Day in Brazil on April 21st.",
    hero_desc="Countdown to Tiradentes Day — April 21st.",
    content="Tiradentes is a Brazilian national holiday on April 21st, honoring Joaquim Jose da Silva Xavier (nicknamed Tiradentes, meaning 'tooth puller'), a leading figure in the Inconfidencia Mineira, Brazil's first major independence movement. He was executed on April 21, 1792, and is celebrated as a national hero and martyr.",
    faqs=[
      ("When is Tiradentes Day?", "Tiradentes Day is April 21st every year in Brazil."),
      ("Who was Tiradentes?", "Tiradentes was a Brazilian revolutionary who led the Inconfidencia Mineira, an early independence movement. He was executed in 1792."),
      ("Is Tiradentes Day a public holiday?", "Yes, April 21st is a national public holiday in Brazil."),
    ]
  ),
  dict(
    slug="proclamacion-independencia-ar", name="25 de Mayo (Argentina)", type="auto", category="National Days",
    regions=["global"],
    seo_title="25 de Mayo Countdown — Argentina Revolution Day, May 25th",
    meta_desc="Live countdown to Argentina's 25 de Mayo (May Revolution Day) on May 25th.",
    hero_desc="Countdown to Argentina's 25 de Mayo — May 25th.",
    content="El 25 de Mayo es el Dia de la Revolucion de Mayo en Argentina, commemorating the May Revolution of 1810 when the Viceroyalty of the Rio de la Plata formed its first independent government, the Primera Junta, on May 25, 1810. This is considered the beginning of Argentina's independence process, culminating in formal independence on July 9, 1816.",
    faqs=[
      ("When is 25 de Mayo in Argentina?", "Argentina's May Revolution Day is May 25th every year."),
      ("What happened on May 25, 1810?", "The Primera Junta was established in Buenos Aires, replacing the Spanish Viceroy and beginning Argentina's path to independence."),
      ("What is the difference between May 25 and July 9 in Argentina?", "May 25 marks the start of the independence process (1810), while July 9 is the formal declaration of independence (1816)."),
    ]
  ),

  # ── Jewish Holidays ───────────────────────────────────────────────────────────
  dict(
    slug="rosh-hashana", name="Rosh Hashanah", type="auto", category="Jewish Holidays",
    regions=["global"],
    seo_title="Rosh Hashanah Countdown — Days Until the Jewish New Year",
    meta_desc="Live countdown to Rosh Hashanah, the Jewish New Year. Date follows the Hebrew calendar and varies each year.",
    hero_desc="Countdown to Rosh Hashanah — the Jewish New Year.",
    content="Rosh Hashanah (Hebrew: head of the year) is the Jewish New Year, observed on the 1st and 2nd of Tishrei in the Hebrew calendar. It marks the beginning of the High Holy Days (Yamim Noraim), a 10-day period of reflection ending with Yom Kippur. Rosh Hashanah traditions include blowing the shofar (ram's horn), eating apples dipped in honey, and attending synagogue services.",
    faqs=[
      ("When is Rosh Hashanah?", "Rosh Hashanah falls on the 1st and 2nd of Tishrei in the Hebrew calendar, typically in September or October."),
      ("What does Rosh Hashanah celebrate?", "Rosh Hashanah is the Jewish New Year, celebrating the anniversary of creation and beginning a period of reflection and repentance."),
      ("What is the shofar?", "The shofar is a ram's horn blown during Rosh Hashanah services as a call to repentance and spiritual awakening."),
      ("Why eat apples and honey on Rosh Hashanah?", "Dipping apples in honey symbolizes the wish for a sweet new year."),
    ]
  ),
  dict(
    slug="yom-kipur", name="Yom Kippur", type="auto", category="Jewish Holidays",
    regions=["global"],
    seo_title="Yom Kippur Countdown — Days Until the Day of Atonement",
    meta_desc="Live countdown to Yom Kippur, the Jewish Day of Atonement. The holiest day of the Jewish year.",
    hero_desc="Countdown to Yom Kippur — the Day of Atonement.",
    content="Yom Kippur (Hebrew: Day of Atonement) is the holiest day in Judaism, observed on the 10th of Tishrei. It is a day of fasting, prayer, and repentance, marking the conclusion of the Ten Days of Repentance that begin with Rosh Hashanah. The fast lasts approximately 25 hours.",
    faqs=[
      ("When is Yom Kippur?", "Yom Kippur falls on the 10th of Tishrei in the Hebrew calendar, 9 days after Rosh Hashanah."),
      ("What is Yom Kippur?", "Yom Kippur is the Day of Atonement, the holiest day in Judaism. Jews fast for approximately 25 hours and attend synagogue services."),
      ("Why do Jews fast on Yom Kippur?", "Fasting on Yom Kippur is a form of self-denial commanded in the Torah, symbolizing repentance and seeking forgiveness."),
      ("What is Kol Nidre?", "Kol Nidre is the prayer that opens the Yom Kippur eve service. The haunting melody is one of the most recognizable in Jewish liturgy."),
    ]
  ),
  dict(
    slug="januca", name="Hanukkah", type="auto", category="Jewish Holidays",
    regions=["global"],
    seo_title="Hanukkah Countdown — Days Until Chanukah",
    meta_desc="Live countdown to Hanukkah (Chanukah), the Jewish Festival of Lights. Eight nights of candle-lighting.",
    hero_desc="Countdown to Hanukkah — the Festival of Lights.",
    content="Hanukkah (also Chanukah) is a Jewish festival lasting eight nights, beginning on the 25th of Kislev in the Hebrew calendar. It commemorates the rededication of the Holy Temple in Jerusalem during the Maccabean Revolt (2nd century BCE). The main ritual is lighting the hanukkiah (menorah) — one candle on the first night, adding one each night until all eight are lit.",
    faqs=[
      ("When does Hanukkah start?", "Hanukkah begins on the 25th of Kislev in the Hebrew calendar, typically in November or December."),
      ("How long does Hanukkah last?", "Hanukkah lasts eight nights and days."),
      ("What is the hanukkiah?", "The hanukkiah is a special nine-branched menorah used during Hanukkah. Eight branches hold the Hanukkah candles, and the ninth (the shamash) is used to light the others."),
      ("What is the story of Hanukkah?", "Hanukkah commemorates the Maccabees' victory over the Seleucid Empire and the miracle of a small amount of oil lasting eight days in the rededicated Temple."),
    ]
  ),
  dict(
    slug="purim", name="Purim", type="auto", category="Jewish Holidays",
    regions=["global"],
    seo_title="Purim Countdown — Days Until Purim",
    meta_desc="Live countdown to Purim, the joyful Jewish holiday of costumes, gifts, and celebration.",
    hero_desc="Countdown to Purim — the Festival of Lots.",
    content="Purim is a joyous Jewish holiday observed on the 14th of Adar in the Hebrew calendar. It celebrates the salvation of the Jewish people as recorded in the Book of Esther. Traditions include reading the Megillah (Book of Esther), wearing costumes, exchanging food gifts (mishloach manot), giving charity, and enjoying festive meals.",
    faqs=[
      ("When is Purim?", "Purim falls on the 14th of Adar in the Hebrew calendar, typically in February or March."),
      ("What is the story of Purim?", "Purim commemorates the story of Esther and Mordecai, who foiled the plot of Haman to destroy the Jewish people in ancient Persia."),
      ("Why do people wear costumes on Purim?", "Wearing costumes is a Purim tradition with several explanations, including celebrating the hidden miracles of the Purim story."),
      ("What are mishloach manot?", "Mishloach manot are food gift packages exchanged between friends and family on Purim, typically including ready-to-eat foods or drinks."),
    ]
  ),
  dict(
    slug="pesaj", name="Passover (Pesach)", type="auto", category="Jewish Holidays",
    regions=["global"],
    seo_title="Passover Countdown — Days Until Pesach (Seder Night)",
    meta_desc="Live countdown to Passover (Pesach), the Jewish festival of freedom. The Seder is held on the first night.",
    hero_desc="Countdown to Passover (Pesach) — the Seder night.",
    content="Passover (Hebrew: Pesach) is one of the most widely observed Jewish holidays, lasting 7 days in Israel and 8 days in the diaspora. It commemorates the Exodus from Egypt, when the Israelites were liberated from slavery. The highlight is the Seder meal, held on the first (and often second) night, where the Haggadah is read and symbolic foods are eaten.",
    faqs=[
      ("When is Passover?", "Passover begins on the 15th of Nisan in the Hebrew calendar, typically in March or April."),
      ("What is the Seder?", "The Seder is the ritual Passover meal where the story of the Exodus is retold through the Haggadah, and symbolic foods such as matzah and bitter herbs are eaten."),
      ("What is matzah?", "Matzah is unleavened flatbread eaten during Passover, symbolizing the hasty departure from Egypt when there was no time for bread to rise."),
      ("How long does Passover last?", "Passover lasts 7 days in Israel and 8 days in the diaspora."),
    ]
  ),
  dict(
    slug="shavuot", name="Shavuot", type="auto", category="Jewish Holidays",
    regions=["global"],
    seo_title="Shavuot Countdown — Days Until Shavuot",
    meta_desc="Live countdown to Shavuot, the Jewish holiday marking the giving of the Torah at Mount Sinai.",
    hero_desc="Countdown to Shavuot — the Festival of Weeks.",
    content="Shavuot (Hebrew: weeks) is a Jewish holiday observed 49 days after Passover, on the 6th of Sivan. It marks the giving of the Torah to Moses at Mount Sinai and also celebrates the spring wheat harvest. Traditions include all-night Torah study, synagogue services decorated with flowers and plants, and eating dairy foods.",
    faqs=[
      ("When is Shavuot?", "Shavuot falls on the 6th of Sivan, exactly 50 days (7 weeks) after the second day of Passover."),
      ("What does Shavuot celebrate?", "Shavuot commemorates the giving of the Torah to Moses and the Israelites at Mount Sinai."),
      ("Why do Jews eat dairy on Shavuot?", "One explanation is that before receiving the Torah's dietary laws, the Israelites had not yet set up separate meat and dairy utensils, so they ate dairy foods."),
      ("What is the tradition of staying up all night on Shavuot?", "Many Jewish communities study Torah through the entire night of Shavuot (Tikkun Leil Shavuot), preparing spiritually to receive the Torah again."),
    ]
  ),

  # ── Holidays (additional) ─────────────────────────────────────────────────────
  dict(
    slug="epiphany", name="Epiphany / Three Kings Day", type="auto", category="Holidays",
    regions=["global"],
    seo_title="Three Kings Day Countdown — Days Until Epiphany, January 6th",
    meta_desc="Live countdown to Epiphany (Three Kings Day) on January 6th. One of the most celebrated holidays in Spain and Latin America.",
    hero_desc="Countdown to Epiphany — Three Kings Day, January 6th.",
    content="Epiphany (also called Three Kings Day or Dia de Reyes) is celebrated on January 6th, commemorating the visit of the Magi to the newborn Jesus. In Spain and many Latin American countries it is one of the most important holidays of the Christmas season, traditionally when children receive gifts. In many Western churches it also marks the official end of the Christmas season.",
    faqs=[
      ("When is Epiphany / Three Kings Day?", "Epiphany is January 6th every year."),
      ("What is Three Kings Day?", "Three Kings Day (Dia de Reyes) celebrates the arrival of the Biblical Magi who brought gifts to baby Jesus. In many countries children receive gifts on this day."),
      ("Is January 6th a public holiday?", "Yes, January 6th is a public holiday in Spain, many Latin American countries, Italy, Poland, and several other nations."),
      ("What is the Roscon de Reyes?", "The Roscon de Reyes is a ring-shaped sweet bread eaten in Spain on Three Kings Day. A small figurine hidden inside brings good luck to whoever finds it."),
    ]
  ),

  # ── Music / Festivals ──────────────────────────────────────────────────────────
  dict(
    slug="rio-carnival", name="Rio Carnival", type="auto", category="Entertainment",
    regions=["global"],
    seo_title="Rio Carnival Countdown — Days Until Carnaval do Rio",
    meta_desc="Live countdown to Rio de Janeiro Carnival. The world's biggest party starts on the Friday before Ash Wednesday.",
    hero_desc="Countdown to Rio Carnival — the world's biggest party.",
    content="The Rio de Janeiro Carnival (Carnaval do Rio) is the world's largest carnival, attracting over two million visitors to the streets of Rio each day during the festivities. It takes place in the days leading up to Ash Wednesday, typically in February or early March. The highlight is the Sambadrome parade, where samba schools compete for the championship title.",
    faqs=[
      ("When is Rio Carnival?", "Rio Carnival always starts on the Friday before Ash Wednesday and runs through Shrove Tuesday (Fat Tuesday). The date changes each year based on Easter."),
      ("How long does Rio Carnival last?", "The official carnival lasts 5 days, from Friday to Carnival Tuesday, but street parties (blocos) begin weeks before."),
      ("What is the Sambodrome?", "The Sambadrome (Sambodromo) is a purpose-built parade ground in Rio where samba schools compete during the carnival championship nights."),
      ("How many people attend Rio Carnival?", "Rio Carnival draws an estimated 2 million people to the streets each day, making it one of the world's largest public events."),
    ]
  ),
  dict(
    slug="lollapalooza-us", name="Lollapalooza Chicago", type="variable", category="Music",
    regions=["global"],
    seo_title="Lollapalooza Countdown — Days Until Lollapalooza Chicago",
    meta_desc="Live countdown to Lollapalooza 2026 at Grant Park, Chicago. July 30 - August 2, 2026.",
    hero_desc="Countdown to Lollapalooza 2026 — Grant Park, Chicago.",
    content="Lollapalooza is one of the world's premier music festivals, held annually in Grant Park, Chicago. The 2026 edition runs from July 30 to August 2 and typically features over 170 acts across multiple stages. Founded in 1991, Lollapalooza has also expanded internationally to cities including Berlin, Paris, Buenos Aires, and Sao Paulo.",
    faqs=[
      ("When is Lollapalooza 2026 in Chicago?", "Lollapalooza 2026 runs from July 30 to August 2, 2026 at Grant Park, Chicago."),
      ("How do I get Lollapalooza tickets?", "Tickets are available at lollapalooza.com. Four-day passes and single-day tickets are usually offered."),
      ("What kind of music is played at Lollapalooza?", "Lollapalooza features a wide range of genres: rock, hip-hop, EDM, pop, alternative, and more."),
    ]
  ),
  dict(
    slug="lollapalooza-de", name="Lollapalooza Berlin", type="variable", category="Music",
    regions=["global"],
    seo_title="Lollapalooza Berlin Countdown — Days Until Lolla Berlin",
    meta_desc="Live countdown to Lollapalooza Berlin 2026 at Tempelhof Field. July 18-19, 2026.",
    hero_desc="Countdown to Lollapalooza Berlin 2026 — Tempelhof Field.",
    content="Lollapalooza Berlin is the European flagship of the Lollapalooza festival franchise, held at the historic Tempelhof Field in Berlin. The 2026 edition takes place on July 18-19, drawing top international acts to one of Europe's most iconic outdoor venues.",
    faqs=[
      ("When is Lollapalooza Berlin?", "Lollapalooza Berlin 2026 is July 18-19, 2026 at Tempelhof Field, Berlin."),
      ("Where is Lollapalooza Berlin held?", "At Tempelhof Field (Tempelhofer Feld), the former airport turned public park in central Berlin."),
      ("How do I get tickets for Lollapalooza Berlin?", "Tickets are sold at lollapalooza.de."),
    ]
  ),
  dict(
    slug="lollapalooza-fr", name="Lollapalooza Paris", type="variable", category="Music",
    regions=["global"],
    seo_title="Lollapalooza Paris Countdown — Days Until Lolla Paris",
    meta_desc="Live countdown to Lollapalooza Paris. The upcoming edition was cancelled; 2027 dates are estimated.",
    hero_desc="Countdown to Lollapalooza Paris.",
    content="Lollapalooza Paris has been held at the Hippodrome de Longchamp in the Bois de Boulogne. The 2026 edition was cancelled, with the next edition expected in 2027. The estimated date is mid-July 2027.",
    faqs=[
      ("When is Lollapalooza Paris?", "The 2026 edition was cancelled. The next expected edition is estimated for July 2027."),
      ("Where is Lollapalooza Paris held?", "At the Hippodrome de Longchamp in the Bois de Boulogne, Paris."),
      ("Why was Lollapalooza Paris 2026 cancelled?", "The organizers cancelled the 2026 edition due to scheduling and logistical issues."),
    ]
  ),
  dict(
    slug="primavera-sound-es", name="Primavera Sound Barcelona", type="variable", category="Music",
    regions=["global"],
    seo_title="Primavera Sound Barcelona Countdown — Days Until Primavera Sound",
    meta_desc="Live countdown to Primavera Sound Barcelona 2026 at Parc del Forum. June 4-6, 2026.",
    hero_desc="Countdown to Primavera Sound Barcelona.",
    content="Primavera Sound is one of the most acclaimed music festivals in Europe, held annually at Parc del Forum in Barcelona. Known for its eclectic lineup spanning indie, electronic, rock, and pop, the 2026 edition runs June 4-6 with a pre-festival week in late May.",
    faqs=[
      ("When is Primavera Sound Barcelona?", "The main weekend is June 4-6, 2026 at Parc del Forum, Barcelona."),
      ("What genres are featured?", "Primavera Sound is known for indie rock, electronic music, alternative pop, and experimental artists."),
      ("Are there other Primavera Sound editions?", "Yes. Primavera Sound also takes place in Madrid and has international editions in Buenos Aires and Sao Paulo."),
    ]
  ),
  dict(
    slug="primavera-sound-ar", name="Primavera Sound Buenos Aires", type="variable", category="Music",
    regions=["global"],
    seo_title="Primavera Sound Buenos Aires Countdown",
    meta_desc="Live countdown to Primavera Sound Buenos Aires 2026 at Hipodromo de Palermo. November 28-29, 2026.",
    hero_desc="Countdown to Primavera Sound Buenos Aires.",
    content="Primavera Sound Buenos Aires brings the iconic Barcelona festival to Argentina, held at the Hipodromo de Palermo. The 2026 edition is scheduled for November 28-29, featuring international and local artists across multiple stages.",
    faqs=[
      ("When is Primavera Sound Buenos Aires?", "November 28-29, 2026 at Hipodromo de Palermo, Buenos Aires."),
      ("What artists perform at Primavera Sound Buenos Aires?", "The lineup mirrors Primavera Sound's signature blend of indie, electronic, and alternative music, featuring both international headliners and local South American acts."),
      ("How do I get tickets?", "Tickets are available at primaverasound.com.ar."),
    ]
  ),
  dict(
    slug="primavera-sound-br", name="Primavera Sound Sao Paulo", type="variable", category="Music",
    regions=["global"],
    seo_title="Primavera Sound Sao Paulo Countdown",
    meta_desc="Live countdown to Primavera Sound Sao Paulo 2026 at Interlagos. December 5-6, 2026.",
    hero_desc="Countdown to Primavera Sound Sao Paulo.",
    content="Primavera Sound Sao Paulo is held at the Autodromo de Interlagos, the iconic Formula 1 venue. The 2026 edition is scheduled for December 5-6, featuring the same eclectic international lineup as the Barcelona and Buenos Aires editions.",
    faqs=[
      ("When is Primavera Sound Sao Paulo?", "December 5-6, 2026 at Autodromo de Interlagos, Sao Paulo."),
      ("Where is Primavera Sound Sao Paulo held?", "At the Autodromo Jose Carlos Pace (Interlagos), also home to the Brazilian Formula 1 Grand Prix."),
      ("How do I get tickets?", "Tickets are available at primaverasound.com.br."),
    ]
  ),
  dict(
    slug="tomorrowland", name="Tomorrowland", type="variable", category="Music",
    regions=["global"],
    seo_title="Tomorrowland Countdown — Days Until Tomorrowland",
    meta_desc="Live countdown to Tomorrowland 2026 at De Schorre, Boom, Belgium. July 17-26, 2026.",
    hero_desc="Countdown to Tomorrowland 2026 — Boom, Belgium.",
    content="Tomorrowland is the world's leading electronic music festival, held at De Schorre nature reserve in Boom, Belgium. The 2026 edition spans two weekends: July 17-19 and July 24-26, featuring hundreds of DJs across dozens of elaborately themed stages.",
    faqs=[
      ("When is Tomorrowland?", "Tomorrowland 2026 takes place on July 17-19 and July 24-26, 2026 at De Schorre, Boom, Belgium."),
      ("What music is played at Tomorrowland?", "Tomorrowland focuses on electronic dance music (EDM), house, techno, trance, and related genres."),
      ("How do I get tickets for Tomorrowland?", "Tomorrowland tickets sell out very quickly. They are available at tomorrowland.com through a registration and lottery system."),
      ("How many people attend Tomorrowland?", "Each weekend of Tomorrowland attracts around 200,000 festival-goers, with attendees from over 200 countries."),
    ]
  ),

  # ── Sports (additional) ────────────────────────────────────────────────────────
  dict(
    slug="world-cup-final", name="2026 World Cup Final", type="variable", category="Sports",
    regions=["global"],
    seo_title="2026 World Cup Final Countdown — Days Until the FIFA World Cup Final",
    meta_desc="Live countdown to the 2026 FIFA World Cup Final on July 19, 2026 at MetLife Stadium, New Jersey.",
    hero_desc="Countdown to the 2026 FIFA World Cup Final.",
    content="The 2026 FIFA World Cup Final will be played on July 19, 2026 at MetLife Stadium in East Rutherford, New Jersey (near New York City). It will be the most-watched sporting event in the world, expected to be seen by over 1.5 billion viewers globally. The 2026 edition is the first with 48 teams.",
    faqs=[
      ("When is the 2026 World Cup Final?", "The 2026 FIFA World Cup Final is on July 19, 2026."),
      ("Where is the 2026 World Cup Final?", "The final is at MetLife Stadium in East Rutherford, New Jersey — the largest stadium in the host nations."),
      ("What time does the 2026 World Cup Final start?", "Kickoff is at 3:00 PM Eastern Time (19:00 UTC) on July 19, 2026."),
    ]
  ),
  dict(
    slug="copa-america-2028", name="Copa America 2028", type="variable", category="Sports",
    regions=["global"],
    seo_title="Copa America 2028 Countdown — Days Until Copa America",
    meta_desc="Live countdown to Copa America 2028. Estimated start: June 1, 2028. Host country TBD.",
    hero_desc="Countdown to Copa America.",
    content="Copa America 2028 is the next edition of South America's premier international football tournament, organized by CONMEBOL. The host country is yet to be confirmed. The tournament typically takes place every four years and features the 10 CONMEBOL member nations plus 6 invited CONCACAF teams. The estimated start is June 2028.",
    faqs=[
      ("When is Copa America 2028?", "Copa America 2028 is estimated to start in June 2028. The exact dates and host country are yet to be confirmed."),
      ("Who plays in Copa America?", "Copa America features the 10 CONMEBOL national teams (South America) plus invited CONCACAF (North America) teams."),
      ("Who won Copa America 2024?", "Argentina won Copa America 2024, defeating Colombia 1-0 after extra time in the final in Miami."),
    ]
  ),
  dict(
    slug="copa-america-2028-final", name="Copa America 2028 Final", type="variable", category="Sports",
    regions=["global"],
    seo_title="Copa America 2028 Final Countdown — Days Until the Final",
    meta_desc="Live countdown to the Copa America 2028 Final. Estimated date: July 1, 2028. Venue TBD.",
    hero_desc="Countdown to the Copa America 2028 Final.",
    content="The Copa America 2028 Final will be the decisive match of the 2028 edition of South America's premier international tournament. The host country and venue are yet to be confirmed. The final is estimated to take place in early July 2028.",
    faqs=[
      ("When is the Copa America 2028 Final?", "The Copa America 2028 Final is estimated for early July 2028. Exact date and venue TBD."),
      ("Where will the 2028 Copa America Final be held?", "The host country and venue for Copa America 2028 have not yet been announced."),
    ]
  ),
  dict(
    slug="euro-2028", name="UEFA Euro 2028", type="variable", category="Sports",
    regions=["global"],
    seo_title="Euro 2028 Countdown — Days Until UEFA European Championship 2028",
    meta_desc="Live countdown to UEFA Euro 2028, hosted by the UK and Republic of Ireland. Opening match estimated June 9, 2028.",
    hero_desc="Countdown to UEFA Euro 2028 — UK and Ireland.",
    content="UEFA Euro 2028 will be hosted jointly by the United Kingdom and the Republic of Ireland. It is the first time the UK has hosted a major UEFA tournament since Euro 1996. The tournament is expected to open in early June 2028 and conclude with the final at Wembley Stadium in London in July 2028.",
    faqs=[
      ("When is Euro 2028?", "Euro 2028 is estimated to run from early June to mid-July 2028, hosted by the UK and Republic of Ireland."),
      ("Where is Euro 2028?", "Stadiums across England, Scotland, Wales, Northern Ireland, and the Republic of Ireland will host matches."),
      ("Where is the Euro 2028 final?", "The final is expected to be held at Wembley Stadium in London."),
      ("How many teams are in Euro 2028?", "UEFA Euro 2028 will feature 24 national teams."),
    ]
  ),
  dict(
    slug="euro-2028-final", name="UEFA Euro 2028 Final", type="variable", category="Sports",
    regions=["global"],
    seo_title="Euro 2028 Final Countdown — Days Until the UEFA Euro Final",
    meta_desc="Live countdown to the UEFA Euro 2028 Final at Wembley Stadium, London. Estimated July 9, 2028.",
    hero_desc="Countdown to the UEFA Euro 2028 Final — Wembley Stadium.",
    content="The UEFA Euro 2028 Final is expected to take place on July 9, 2028 at Wembley Stadium in London, England. Wembley, with a capacity of 90,000, hosted the Euro 2020 final (played in 2021) and will once again be the stage for Europe's most prestigious international football match.",
    faqs=[
      ("When is the Euro 2028 Final?", "The Euro 2028 Final is estimated to be on July 9, 2028 at Wembley Stadium, London."),
      ("Where is the Euro 2028 Final?", "At Wembley Stadium in London, England, with a capacity of approximately 90,000."),
      ("Who hosted Euro 2028?", "Euro 2028 is jointly hosted by England, Scotland, Wales, Northern Ireland, and the Republic of Ireland."),
    ]
  ),

  # ── Technology / Awards ────────────────────────────────────────────────────────
  dict(
    slug="ces", name="CES Las Vegas", type="auto", category="Technology",
    regions=["global"],
    seo_title="CES Las Vegas Countdown — Days Until ",
    meta_desc="Live countdown to CES (Consumer Electronics Show) in Las Vegas. The world's largest tech trade show, held every January.",
    hero_desc="Countdown to CES — Consumer Electronics Show, Las Vegas.",
    content="CES (Consumer Electronics Show) is the world's most influential technology trade show, held annually in early January in Las Vegas, Nevada. Organized by the Consumer Technology Association, CES hosts over 4,000 exhibiting companies and attracts around 170,000 attendees from 160+ countries. Major announcements in TVs, cars, AI, robotics, and consumer gadgets are made every year.",
    faqs=[
      ("When is CES?", "CES takes place in early January in Las Vegas, typically the first or second week of the month."),
      ("What is CES?", "CES is the Consumer Electronics Show, the world's largest tech trade show where companies unveil new products and technologies."),
      ("Who can attend CES?", "CES is a trade show, primarily open to industry professionals. Some events are open to the public; check the official CES website for registration."),
      ("What major brands exhibit at CES?", "Samsung, LG, Sony, Intel, NVIDIA, Ford, GM, and thousands of other technology and consumer electronics companies exhibit every year."),
    ]
  ),
  dict(
    slug="balon-de-oro", name="Balon de Oro", type="auto", category="Entertainment",
    regions=["global"],
    seo_title="Balon de Oro Countdown — Days Until the Ballon d'Or Ceremony",
    meta_desc="Live countdown to the Ballon d'Or ceremony. Awarded annually to the world's best football player, typically in October.",
    hero_desc="Countdown to the Balon de Oro ceremony.",
    content="The Ballon d'Or (Golden Ball) is the most prestigious individual award in football (soccer), awarded annually by France Football magazine since 1956. The ceremony typically takes place in Paris in October. Winners are selected by international journalists and national team coaches and captains.",
    faqs=[
      ("When is the Balon de Oro ceremony?", "The Ballon d'Or ceremony typically takes place in Paris in late October."),
      ("Who has won the most Ballons d'Or?", "Lionel Messi holds the record with 8 Ballons d'Or (2009, 2010, 2011, 2012, 2015, 2019, 2021, 2023)."),
      ("How is the Ballon d'Or winner chosen?", "Votes are cast by sports journalists from around the world, as well as national team coaches and captains."),
      ("Is there a women's Ballon d'Or?", "Yes. The women's Ballon d'Or (Ballon d'Or Feminin) has been awarded since 2018."),
    ]
  ),
  dict(
    slug="mr-olympia", name="Mr. Olympia", type="auto", category="Sports",
    regions=["global"],
    seo_title="Mr. Olympia Countdown — Days Until Mr. Olympia Competition",
    meta_desc="Live countdown to Mr. Olympia, the most prestigious bodybuilding competition in the world, held in Las Vegas each fall.",
    hero_desc="Countdown to Mr. Olympia — the world's top bodybuilding competition.",
    content="Mr. Olympia is the most prestigious professional bodybuilding competition in the world, organized by the International Federation of Bodybuilding and Fitness (IFBB). Founded by Joe Weider in 1965, the competition is held annually in Las Vegas in the fall. The Mr. Olympia title is considered the pinnacle of professional bodybuilding.",
    faqs=[
      ("When is Mr. Olympia?", "Mr. Olympia is typically held in late September or early October in Las Vegas, Nevada."),
      ("Who has won Mr. Olympia the most times?", "Lee Haney and Ronnie Coleman share the record with 8 consecutive Mr. Olympia titles each."),
      ("What is the prize for Mr. Olympia?", "The Mr. Olympia winner receives a substantial prize purse; in recent editions the overall prize money exceeded $1 million."),
      ("Is Mr. Olympia only for men?", "No. Mr. Olympia weekend includes multiple divisions for women, including Women's Physique, Bikini, Figure, and Fitness."),
    ]
  ),
  dict(
    slug="arnold-classic", name="Arnold Classic", type="auto", category="Sports",
    regions=["global"],
    seo_title="Arnold Classic Countdown — Days Until the Arnold Sports Festival",
    meta_desc="Live countdown to the Arnold Classic (Arnold Sports Festival) in Columbus, Ohio. Held every March.",
    hero_desc="Countdown to the Arnold Classic — Columbus, Ohio.",
    content="The Arnold Classic is a prestigious bodybuilding and fitness competition held annually in Columbus, Ohio, as part of the Arnold Sports Festival. Founded in 1989 by Arnold Schwarzenegger and Jim Lorimer, it is considered the second most important bodybuilding competition after Mr. Olympia and also hosts over 80 sports disciplines.",
    faqs=[
      ("When is the Arnold Classic?", "The Arnold Classic is held in early March in Columbus, Ohio, typically the first weekend of the month."),
      ("What is the Arnold Sports Festival?", "The Arnold Sports Festival is a multi-sport event spanning a full weekend, hosting over 80 sports and featuring the Arnold Classic bodybuilding competition."),
      ("Who founded the Arnold Classic?", "The Arnold Classic was founded in 1989 by Arnold Schwarzenegger and promoter Jim Lorimer."),
    ]
  ),


  # ── Politics ───────────────────────────────────────────────────────────────
  dict(
    slug="elecciones-ar", name="Argentine Elections 2027", type="auto", category="Politics",
    regions=["es"],
    seo_title="Argentine Elections 2027 Countdown — Días para las Elecciones",
    meta_desc="Cuenta regresiva para las Elecciones Generales Argentina 2027, estimadas para el 26 de octubre de 2027.",
    hero_desc="Countdown to the Argentine General Elections.",
    content="Argentina celebrará elecciones generales en octubre de 2027, cuando se renovará la composición del Congreso Nacional y se elegirá al próximo presidente y vicepresidente de la Nación para el período 2027–2031.",
    faqs=[
      ("¿Cuándo son las elecciones en Argentina 2027?", "Las elecciones generales Argentina 2027 están estimadas para el 26 de octubre de 2027."),
      ("¿Qué se vota en las elecciones 2027?", "Se elige presidente, vicepresidente, y se renuevan parcialmente los cargos legislativos nacionales (diputados y senadores)."),
      ("¿Habrá PASO en 2027?", "Las Primarias Abiertas Simultáneas y Obligatorias (PASO) suelen celebrarse aproximadamente dos meses antes de las elecciones generales, en agosto de 2027."),
      ("¿Quiénes pueden votar en Argentina?", "Pueden votar los ciudadanos argentinos nativos o naturalizados mayores de 16 años. El voto es obligatorio para los mayores de 18 y optativo para los de 16 y 17 años."),
    ]
  ),

  # ── Awards / Entertainment ─────────────────────────────────────────────────
  dict(
    slug="bafta", name="BAFTA Film Awards 2027", type="variable", category="Entertainment",
    regions=["global"],
    seo_title="BAFTA Film Awards 2027 Countdown — Days Until the BAFTAs",
    meta_desc="Live countdown to the 80th BAFTA Film Awards on Sunday, February 21, 2027 at the Royal Festival Hall, Southbank Centre, London.",
    hero_desc="Countdown to the 80th BAFTA Film Awards — February 21, 2027, London.",
    content="The BAFTA Film Awards are presented annually by the British Academy of Film and Television Arts to honor the best in cinema. First held in 1948, the BAFTAs are one of the world's most prestigious film awards and often serve as a strong predictor of Oscar outcomes. The 80th BAFTA Film Awards ceremony takes place on Sunday, February 21, 2027 at the Royal Festival Hall, Southbank Centre, London.",
    faqs=[
      ("When are the BAFTA Film Awards 2027?", "The 80th BAFTA Film Awards take place on Sunday, February 21, 2027 at the Royal Festival Hall, Southbank Centre, London."),
      ("Where are the BAFTAs held?", "The BAFTA Film Awards are held at the Royal Festival Hall, Southbank Centre, London."),
      ("What does BAFTA stand for?", "BAFTA stands for British Academy of Film and Television Arts."),
      ("What time do the BAFTA Awards start?", "The BAFTA Film Awards ceremony begins at 7:00 PM GMT at the Royal Festival Hall in London."),
      ("How many days until the BAFTA Awards?", "Use the live countdown above to see the exact days, hours, minutes and seconds until the BAFTA Film Awards 2027."),
    ]
  ),

  # ── Sports – Draft & National Days ────────────────────────────────────────
  dict(
    slug="nba-draft", name="NBA Draft 2026", type="variable", category="Sports",
    regions=["global"],
    seo_title="NBA Draft 2026 Countdown — Days Until the NBA Draft",
    meta_desc="Live countdown to the 2026 NBA Draft — Round 1 on June 23, 2026 at the Barclays Center, Brooklyn. The Washington Wizards hold the No. 1 overall pick.",
    hero_desc="Countdown to the 2026 NBA Draft — Round 1 on June 23 at the Barclays Center, Brooklyn.",
    content="The NBA Draft is the annual event where the 30 NBA teams select eligible players to join the league. The 2026 NBA Draft takes place on June 23 (Round 1) and June 24 (Round 2) at the Barclays Center in Brooklyn, New York. Round 1 airs live on ABC and ESPN at 8:00 PM ET. The Washington Wizards hold the No. 1 overall pick, with the Utah Jazz at No. 2 and the Memphis Grizzlies at No. 3.",
    faqs=[
      ("When is the NBA Draft 2026?", "The 2026 NBA Draft Round 1 is on Tuesday, June 23, 2026. Round 2 follows on Wednesday, June 24, at the Barclays Center in Brooklyn, New York."),
      ("Where is the NBA Draft 2026 held?", "The 2026 NBA Draft takes place at the Barclays Center in Brooklyn, New York."),
      ("Who has the No. 1 pick in the 2026 NBA Draft?", "The Washington Wizards hold the No. 1 overall pick in the 2026 NBA Draft."),
      ("How does the NBA Draft work?", "30 NBA teams select players in 2 rounds (60 picks total). Teams that missed the playoffs enter the Draft Lottery, with the worst records getting the best odds for top picks."),
      ("What time does the NBA Draft 2026 start?", "The 2026 NBA Draft Round 1 begins at 8:00 PM ET on Tuesday, June 23, 2026, airing on ABC and ESPN."),
    ]
  ),
  dict(
    slug="koningsdag", name="King's Day (Netherlands)", type="variable", category="National Days",
    regions=["global"],
    seo_title="King's Day 2027 Countdown — Days Until Koningsdag Netherlands",
    meta_desc="Live countdown to King's Day 2027 on April 27 — the Netherlands' largest national celebration, with the whole country turning orange for King Willem-Alexander's birthday.",
    hero_desc="Countdown to King's Day 2027 (Koningsdag) — April 27 in the Netherlands.",
    content="King's Day (Koningsdag) is celebrated every April 27 in the Netherlands — or April 26 if April 27 falls on a Sunday. The entire country dresses in orange, takes to the streets, canals, and outdoor markets, and celebrates the birthday of King Willem-Alexander. Amsterdam is completely transformed: its canals fill with boats, free markets (vrijmarkten) pop up everywhere, and live music fills every square.",
    faqs=[
      ("When is King's Day 2027?", "King's Day 2027 falls on Tuesday, April 27, 2027. It celebrates the birthday of King Willem-Alexander of the Netherlands."),
      ("Why do people wear orange on King's Day?", "Orange is the color of the Dutch Royal Family — the House of Orange-Nassau. Wearing orange on King's Day is a national tradition expressing pride and loyalty to the monarchy."),
      ("What happens on King's Day in Amsterdam?", "Amsterdam hosts the world's largest outdoor flea market (vrijmarkt), canal boat parties, live music on every street, and orange-clad crowds celebrating throughout the city."),
      ("Is King's Day always on April 27?", "King's Day is celebrated on April 27 every year. If April 27 falls on a Sunday, the celebration moves to April 26."),
      ("How many days until King's Day?", "Use the live countdown above to see the exact number of days, hours, minutes, and seconds until King's Day 2027."),
    ]
  ),

  # ── Gaming Releases ───────────────────────────────────────────────────────
  dict(
    slug="ps6", name="PlayStation 6", type="variable", category="Releases",
    regions=["global"],
    seo_title="PlayStation 6 (PS6) Release Date Countdown — When Does PS6 Come Out?",
    meta_desc="Countdown to the PlayStation 6 release date. Sony has not yet announced an official date, but rumors and patents suggest a PS6 launch in 2027–2028. Stay tuned for updates.",
    hero_desc="Counting down to the PlayStation 6 launch — date not yet confirmed.",
    content="Sony has not announced an official PlayStation 6 release date. Based on the PS4 and PS5 release cycles, industry analysts and leaks suggest a PS6 launch window of 2027 or 2028. Sony's patent filings and job listings provide some hints about the next-gen hardware, but no official launch date has been set. This page will update automatically once Sony confirms the date.",
    faqs=[
      ("When will PlayStation 6 come out?", "Sony has not officially announced a PS6 release date. Analyst estimates and rumors point to a 2027–2028 window, following the PS5's 2020 launch."),
      ("What do we know about PS6 specs?", "Sony has shared little official information. Leaks and patents suggest major improvements in GPU performance, AI-driven processing, and potentially advanced VR capabilities."),
      ("Will PS6 be backwards compatible with PS5?", "Sony has not confirmed backwards compatibility, but given the PS5's strong support for PS4 games, backwards compatibility with PS5 titles is widely expected."),
      ("How much will PS6 cost?", "No pricing has been confirmed. Given the PS5's $499 launch price and inflation, the PS6 is expected to launch at $599–$699."),
      ("How do I get notified of the PS6 release date?", "Bookmark this page — it will update automatically with a live countdown the moment Sony confirms the PS6 release date."),
    ]
  ),

  # ── Calendar Countdowns ───────────────────────────────────────────────────
  dict(
    slug="weekend", name="Next Weekend", type="auto", category="Time",
    regions=["global"],
    seo_title="Countdown to the Weekend — How Many Days Until the Weekend?",
    meta_desc="Live countdown to the next weekend. See the exact days, hours, minutes and seconds until Saturday arrives. Auto-updates every week.",
    hero_desc="Live countdown to the next weekend — Saturday is coming.",
    content="Whether you're counting down to a well-earned rest, a trip, or just two days away from work, this live countdown shows exactly how long until the weekend starts. The timer counts to the next Saturday at midnight local time and resets automatically every week.",
    faqs=[
      ("How many days until the weekend?", "Use the live countdown above to see the exact days, hours, minutes and seconds until Saturday. It updates automatically based on your local time."),
      ("What day does the weekend start?", "This countdown uses Saturday at midnight (00:00) as the start of the weekend."),
      ("Does the countdown use my local time?", "Yes — the countdown uses your device's local timezone, so it's accurate wherever you are in the world."),
      ("How many hours until Friday?", "If you want a countdown specifically to Friday, use the custom countdown feature on this site to set your own target date and time."),
    ]
  ),
  dict(
    slug="next-year", name="Next Year", type="auto", category="Time",
    regions=["global"],
    seo_title="How Many Days Until Next Year? — Live Countdown to 2027",
    meta_desc="Live countdown to January 1, 2027 — the start of next year. See the exact days, hours, minutes and seconds remaining. Auto-resets each year.",
    hero_desc="Live countdown to the start of next year.",
    content="How far away is next year? This live countdown shows the exact time remaining until January 1 of the next year arrives. Whether you're planning for the year ahead, counting down to a fresh start, or just curious, this timer keeps you updated to the second. It resets automatically every year on January 1.",
    faqs=[
      ("How many days until next year?", "Use the live countdown above for the exact number of days, hours, minutes and seconds until January 1 of next year."),
      ("What year is next year?", "Next year is 2027. This countdown targets January 1, 2027 at midnight local time."),
      ("Is this the same as the New Year countdown?", "Yes — both this and the New Year countdown point to January 1. This page is focused on the 'days until next year' search intent."),
      ("Does the timer use my local timezone?", "Yes — the countdown uses your device's local time, so it accurately reflects your local New Year midnight."),
    ]
  ),

  # ── Festivals & Awards ────────────────────────────────────────────────────
  dict(
    slug="mardi-gras", name="Mardi Gras 2027", type="variable", category="Holidays",
    regions=["global"],
    seo_title="Mardi Gras 2027 Countdown — Days Until Fat Tuesday",
    meta_desc="Live countdown to Mardi Gras 2027 on Tuesday, February 9, 2027 — the legendary Fat Tuesday celebration in New Orleans and around the world.",
    hero_desc="Countdown to Mardi Gras 2027 — Fat Tuesday, February 9, 2027.",
    content="Mardi Gras (French for 'Fat Tuesday') is the last day of Carnival season, celebrated on the Tuesday before Ash Wednesday. Known for its vibrant parades, costumes, music, and beads, the biggest celebration takes place in New Orleans, Louisiana. Mardi Gras 2027 falls on Tuesday, February 9 — 47 days before Easter Sunday (March 28, 2027).",
    faqs=[
      ("When is Mardi Gras 2027?", "Mardi Gras 2027 falls on Tuesday, February 9, 2027. It is always the Tuesday before Ash Wednesday, 47 days before Easter."),
      ("Where is Mardi Gras celebrated?", "The most famous celebration takes place in New Orleans, Louisiana. It is also celebrated in Mobile, Alabama, Rio de Janeiro (as Carnaval), Venice, and many cities worldwide."),
      ("What does 'Mardi Gras' mean?", "'Mardi Gras' means 'Fat Tuesday' in French. It refers to the tradition of eating rich foods before the fasting of Lent begins on Ash Wednesday."),
      ("Is Mardi Gras a public holiday?", "Mardi Gras is a public holiday in parts of Louisiana, including New Orleans and surrounding parishes."),
      ("How many days until Mardi Gras?", "Use the live countdown above to see the exact days, hours, minutes and seconds until Mardi Gras 2027."),
    ]
  ),
  dict(
    slug="bonnaroo", name="Bonnaroo 2026", type="variable", category="Music",
    regions=["en"],
    seo_title="Bonnaroo 2026 Countdown — Days Until Bonnaroo Music Festival",
    meta_desc="Live countdown to Bonnaroo 2026, June 11–14, 2026 at Great Stage Park, Manchester, Tennessee. One of America's premier multi-genre music festivals.",
    hero_desc="Countdown to Bonnaroo 2026 — June 11–14, Manchester, Tennessee.",
    content="Bonnaroo Music and Arts Festival is an annual multi-genre music and camping festival held at Great Stage Park in Manchester, Tennessee. Founded in 2002, it features hundreds of artists across multiple stages over four days. Bonnaroo 2026 runs from Thursday, June 11 to Sunday, June 14, 2026.",
    faqs=[
      ("When is Bonnaroo 2026?", "Bonnaroo 2026 takes place June 11–14, 2026 at Great Stage Park in Manchester, Tennessee."),
      ("Where is Bonnaroo held?", "Bonnaroo is held at Great Stage Park in Manchester, Tennessee, about an hour south of Nashville."),
      ("How many people attend Bonnaroo?", "Bonnaroo typically draws around 65,000–80,000 attendees per year, making it one of the largest music festivals in the United States."),
      ("Can you camp at Bonnaroo?", "Yes — camping is a core part of the Bonnaroo experience. Attendees can camp on-site for the full four-day festival."),
      ("How many days until Bonnaroo 2026?", "Use the live countdown above to see the exact days, hours, minutes and seconds until Bonnaroo 2026."),
    ]
  ),
  dict(
    slug="glastonbury", name="Glastonbury Festival 2027", type="variable", category="Music",
    regions=["global"],
    seo_title="Glastonbury Festival 2027 Countdown — Days Until Glastonbury",
    meta_desc="Live countdown to Glastonbury Festival 2027, June 23–27 at Worthy Farm, Somerset, UK. There is no Glastonbury in 2026 — it is a fallow year.",
    hero_desc="Countdown to Glastonbury Festival 2027 — June 23–27, Worthy Farm, Somerset.",
    content="Glastonbury Festival is the world's most iconic outdoor music and arts festival, held at Worthy Farm in Pilton, Somerset, UK. The 2027 festival runs from Wednesday, June 23 to Sunday, June 27. Note: there is no Glastonbury in 2026 — the festival observes a fallow year every few years to allow the farmland to recover.",
    faqs=[
      ("When is Glastonbury 2027?", "Glastonbury Festival 2027 runs Wednesday, June 23 to Sunday, June 27, 2027 at Worthy Farm in Pilton, Somerset, UK."),
      ("Is there a Glastonbury in 2026?", "No — there is no Glastonbury Festival in 2026. The festival observes a fallow year to allow the farmland and cows to recover. The next Glastonbury is in 2027."),
      ("How do I get Glastonbury tickets?", "Glastonbury tickets are sold through an annual registration and ballot system. Registration is free but demand far exceeds supply."),
      ("Who has headlined Glastonbury?", "Past headliners include Beyoncé, Paul McCartney, Coldplay, Radiohead, Adele, David Bowie, The Rolling Stones, and Stormzy."),
      ("How many days until Glastonbury 2027?", "Use the live countdown above to see the exact days, hours, minutes and seconds until Glastonbury Festival 2027."),
    ]
  ),
  dict(
    slug="mtv-vmas", name="MTV VMAs 2026", type="variable", category="Entertainment",
    regions=["global"],
    seo_title="MTV VMAs 2026 Countdown — Days Until the MTV Video Music Awards",
    meta_desc="Live countdown to the MTV Video Music Awards 2026 on Sunday, September 27, 2026 in Los Angeles, CA. Live on CBS and Paramount+.",
    hero_desc="Countdown to the MTV VMAs 2026 — September 27, 2026, Los Angeles.",
    content="The MTV Video Music Awards (VMAs) celebrate the best in music videos and pop culture. The 2026 MTV VMAs take place on Sunday, September 27, 2026 in Los Angeles, California — the event's first return to LA since 2017. The ceremony airs live on CBS and streams on Paramount+, beginning at 8:00 PM ET / 7:00 PM CT.",
    faqs=[
      ("When are the MTV VMAs 2026?", "The 2026 MTV VMAs air live on Sunday, September 27, 2026 at 8:00 PM ET in Los Angeles, California."),
      ("Where are the MTV VMAs 2026 held?", "The 2026 MTV VMAs are held in Los Angeles, California — the first return to LA since 2017."),
      ("How to watch the MTV VMAs 2026?", "The MTV VMAs 2026 air live on CBS and stream on Paramount+."),
      ("What is the MTV VMA Moonperson trophy?", "The MTV VMA trophy, known as the Moonperson, depicts an astronaut planting an MTV flag on the moon. It is one of the most recognizable trophies in music."),
      ("How many days until the MTV VMAs?", "Use the live countdown above to see the exact days, hours, minutes and seconds until the MTV VMAs 2026."),
    ]
  ),
  dict(
    slug="elecciones-usa-midterms", name="US Midterm Elections 2026", type="variable", category="Politics",
    regions=["en"],
    seo_title="US Midterm Elections 2026 Countdown — Days Until Election Day",
    meta_desc="Live countdown to the 2026 US Midterm Elections on November 3, 2026. All 435 House seats and 34 Senate seats are up for election.",
    hero_desc="Countdown to the 2026 US Midterm Elections — November 3, 2026.",
    content="The 2026 United States midterm elections are scheduled for Tuesday, November 3, 2026. All 435 seats in the House of Representatives and 34 of the 100 Senate seats will be contested. Midterm elections are held two years into a presidential term and often serve as a referendum on the sitting president's performance.",
    faqs=[
      ("When are the 2026 US Midterm Elections?", "The 2026 US Midterm Elections take place on Tuesday, November 3, 2026."),
      ("What is decided in the 2026 Midterms?", "All 435 House seats and 34 Senate seats are up for election, along with numerous state governors and local offices."),
      ("How do US Midterm elections work?", "Every two years, all 435 House seats come up for election. Senate seats are staggered — about a third per cycle. The President is not on the ballot."),
      ("When can I register to vote for the 2026 Midterms?", "Voter registration deadlines vary by state. Most states require registration 15–30 days before the election. Check requirements at vote.gov."),
      ("How many days until the 2026 Midterms?", "Use the live countdown above to see the exact days, hours, minutes and seconds until the 2026 US Midterm Elections."),
    ]
  ),
]

# ─── Category colours ──────────────────────────────────────────────────────────
CAT_COLORS = {
  'Releases':      ('#C084FC', 'rgba(192,132,252,.25)', 'rgba(192,132,252,.1)'),
  'Sports':        ('#FB923C', 'rgba(251,146,60,.25)',  'rgba(251,146,60,.1)'),
  'Holidays':      ('#4ADE80', 'rgba(74,222,128,.2)',   'rgba(74,222,128,.08)'),
  'Entertainment': ('#FBBF24', 'rgba(251,191,36,.2)',   'rgba(251,191,36,.08)'),
  'Sales':         ('#60A5FA', 'rgba(96,165,250,.2)',   'rgba(96,165,250,.08)'),
  'Nature':        ('#22D3EE', 'rgba(34,211,238,.2)',   'rgba(34,211,238,.08)'),
  'Music':         ('#F472B6', 'rgba(244,114,182,.2)',  'rgba(244,114,182,.08)'),
  'Politics':      ('#94A3B8', 'rgba(148,163,184,.2)',  'rgba(148,163,184,.08)'),
  'Fashion':       ('#FDA4AF', 'rgba(253,164,175,.2)',  'rgba(253,164,175,.08)'),
  'Technology':    ('#34D399', 'rgba(52,211,153,.2)',   'rgba(52,211,153,.08)'),
  'Months':        ('#A78BFA', 'rgba(167,139,250,.2)',  'rgba(167,139,250,.08)'),
  'Seasons':       ('#6EE7B7', 'rgba(110,231,183,.2)',  'rgba(110,231,183,.08)'),
  'School':        ('#FCD34D', 'rgba(252,211,77,.2)',   'rgba(252,211,77,.08)'),
  'National Days': ('#F87171', 'rgba(248,113,113,.2)',  'rgba(248,113,113,.08)'),
  'Jewish Holidays':('#E9D5A1','rgba(233,213,161,.2)',  'rgba(233,213,161,.08)'),
  'Time':          ('#67E8F9', 'rgba(103,232,249,.2)',  'rgba(103,232,249,.08)'),
}

# ─── Pre-compute which (lang, slug) pages to generate ─────────────────────────
def compute_lang_pages():
    pages = {}  # slug -> set of langs
    for ev in EVENTS:
        slug = ev["slug"]
        langs = {"en"}
        for region in ev.get("regions", ["global"]):
            if region == "global":
                for lang in ["es", "pt", "fr"]:
                    if slug in TRANSLATIONS.get(lang, {}).get("events", {}):
                        langs.add(lang)
            elif region in ("es", "pt", "fr"):
                if slug in TRANSLATIONS.get(region, {}).get("events", {}):
                    langs.add(region)
        pages[slug] = langs
    return pages

SLUG_LANGS = compute_lang_pages()

# ─── Helpers ───────────────────────────────────────────────────────────────────
def faq_json_ld(slug, name, faqs):
    items = []
    for q, a in faqs:
        items.append(f'''    {{
      "@type": "Question",
      "name": "{q.replace('"', '&quot;')}",
      "acceptedAnswer": {{ "@type": "Answer", "text": "{a.replace('"', '&quot;')}" }}
    }}''')
    return "[\n" + ",\n".join(items) + "\n  ]"

# ─── Page generator ────────────────────────────────────────────────────────────
def generate_page(ev, lang="en"):
    slug      = ev["slug"]
    category  = ev["category"]
    ev_type   = ev["type"]
    cat_color, cat_glow, cat_soft = CAT_COLORS.get(
        category, ('#818CF8', 'rgba(129,140,248,.2)', 'rgba(129,140,248,.08)')
    )

    # Translation lookup
    t         = TRANSLATIONS.get(lang, {}).get("events", {}).get(slug, {}) if lang != "en" else {}
    html_lang = TRANSLATIONS.get(lang, {}).get("html_lang", "en") if lang != "en" else "en"
    faq_title = TRANSLATIONS.get(lang, {}).get("faq_title", "Frequently Asked Questions")

    name      = t.get("name",      ev["name"])
    seo_title = t.get("seo_title", ev["seo_title"])
    meta_desc = t.get("meta_desc", ev["meta_desc"])
    hero_desc = t.get("hero_desc", ev["hero_desc"])
    content   = t.get("content",   ev.get("content", ""))
    faqs      = t.get("faqs",      ev.get("faqs", []))

    # Collect translated event names for multilingual keywords
    name_by_lang = {}
    for _lc in ("es", "pt", "fr"):
        _tname = TRANSLATIONS.get(_lc, {}).get("events", {}).get(slug, {}).get("name")
        if _tname:
            name_by_lang[_lc] = _tname
    meta_keywords = build_meta_keywords(ev["name"], CURRENT_YEAR, name_by_lang)

    # OG image — use event-specific if available, else generic
    _og_jpg = os.path.join("og-images", f"{slug}.jpg")
    _og_png = os.path.join("og-images", f"{slug}.png")
    if os.path.exists(_og_jpg):
        og_image_url = f"https://countdowns.site/og-images/{slug}.jpg"
    elif os.path.exists(_og_png):
        og_image_url = f"https://countdowns.site/og-images/{slug}.png"
    else:
        og_image_url = "https://countdowns.site/og-image.png"

    # URLs
    en_url   = f"{BASE_URL}/countdown/{slug}/"
    page_url = en_url if lang == "en" else f"{BASE_URL}/{lang}/countdown/{slug}/"

    # Language button links
    def lang_href(btn_lang):
        if btn_lang == "en":
            return f"/countdown/{slug}/"
        elif btn_lang in SLUG_LANGS.get(slug, set()):
            return f"/{btn_lang}/countdown/{slug}/"
        else:
            return f"/{btn_lang}/"

    def lang_btn(btn_lang, label):
        active = ' active' if btn_lang == lang else ''
        if btn_lang == lang:
            return f'<button class="lang-btn{active}">{label}</button>'
        return f'<button class="lang-btn{active}" onclick="localStorage.setItem(\'cd_lang_override\',\'{btn_lang}\');location.href=\'{lang_href(btn_lang)}\'">{label}</button>'

    lang_buttons = (
        lang_btn("en", "EN") +
        lang_btn("es", "ES") +
        lang_btn("pt", "PT") +
        lang_btn("fr", "FR")
    )

    # hreflang tags
    hreflang = f'<link rel="alternate" hreflang="en" href="{en_url}">\n'
    hreflang += f'<link rel="alternate" hreflang="x-default" href="{en_url}">\n'
    for alt_lang, alt_hl in [("es","es"), ("pt","pt-BR"), ("fr","fr")]:
        if alt_lang in SLUG_LANGS.get(slug, set()):
            hreflang += f'<link rel="alternate" hreflang="{alt_hl}" href="{BASE_URL}/{alt_lang}/countdown/{slug}/">\n'

    # FAQ HTML
    faq_items_html = "".join(
        f'<div class="cd-faq-item"><h3 class="cd-faq-q">{q}</h3><p class="cd-faq-a">{a}</p></div>'
        for q, a in faqs
    )
    faq_section = f'''<div class="cd-article">
  <p class="cd-article-body">{content}</p>
  <div class="cd-faq"><h2 class="cd-faq-title">{faq_title}</h2>{faq_items_html}</div>
</div>''' if (content or faqs) else ""

    faq_json = faq_json_ld(slug, name, faqs) if faqs else "[]"

    # Country picker
    country_variants = ev.get("country_variants", [])
    default_variant_by_lang = ev.get("default_variant_by_lang", {})

    if country_variants:
        default_idx = default_variant_by_lang.get(lang, 0)
        cv_js = json.dumps([
            {"code": v["code"], "label": v["label"], "dates": v["dates"], "countries": v.get("countries", [])}
            for v in country_variants
        ])
        country_picker_html = f'''<div class="cd-country-picker">
  <p class="cd-cpicker-label">Date varies by country — select yours:</p>
  <div class="cd-cpicker-grid" id="cd-cpicker-grid"></div>
</div>'''
        render_script = f'''(function() {{
  var VARIANTS = {cv_js};
  var DEFAULT_IDX = {default_idx};
  var _cfg = {{
    slug: {json.dumps(slug)},
    type: 'fixed',
    name: {json.dumps(name)},
    category: {json.dumps(category)},
    description: {json.dumps(hero_desc)}
  }};
  function nextDate(dates) {{
    var now = new Date();
    for (var i = 0; i < dates.length; i++) {{
      if (new Date(dates[i]) > now) return new Date(dates[i]);
    }}
    return new Date(dates[dates.length - 1]);
  }}
  // Auto-select variant based on saved country
  var _savedC = (typeof localStorage !== 'undefined' ? localStorage.getItem('cd_country') : null) || '';
  var activeIdx = DEFAULT_IDX;
  if (_savedC) {{
    for (var _i = 0; _i < VARIANTS.length; _i++) {{
      if (VARIANTS[_i].countries && VARIANTS[_i].countries.indexOf(_savedC) >= 0) {{
        activeIdx = _i; break;
      }}
    }}
  }}
  var grid = document.getElementById('cd-cpicker-grid');
  VARIANTS.forEach(function(v, idx) {{
    var btn = document.createElement('button');
    btn.className = 'cd-cpicker-btn' + (idx === activeIdx ? ' active' : '');
    btn.textContent = v.label;
    btn.onclick = function() {{
      document.querySelectorAll('.cd-cpicker-btn').forEach(function(b) {{ b.classList.remove('active'); }});
      btn.classList.add('active');
      CountdownEngine.render('root', Object.assign({{}}, _cfg, {{ date: nextDate(v.dates) }}));
    }};
    grid.appendChild(btn);
  }});
  CountdownEngine.render('root', Object.assign({{}}, _cfg, {{ date: nextDate(VARIANTS[activeIdx].dates) }}));
}})();'''
    else:
        country_picker_html = ""
        render_script = f'''CountdownEngine.render('root', {{
  slug: {json.dumps(slug)},
  type: {json.dumps(ev_type)},
  name: {json.dumps(name)},
  category: {json.dumps(category)},
  description: {json.dumps(hero_desc)}
}});'''

    return f'''<!DOCTYPE html>
<html lang="{html_lang}">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{seo_title} | countdowns.site</title>
<meta name="description" content="{meta_desc}">
<meta name="keywords" content="{meta_keywords}">
<meta name="robots" content="index, follow">
<link rel="canonical" href="{en_url}">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="icon" href="/favicon.png" type="image/png" sizes="256x256">
<link rel="apple-touch-icon" href="/favicon.png">
<meta property="og:type" content="article">
<meta property="og:url" content="{page_url}">
<meta property="og:title" content="{seo_title}">
<meta property="og:description" content="{meta_desc}">
<meta property="og:image" content="{og_image_url}">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{seo_title}">
<meta name="twitter:description" content="{meta_desc}">
<meta name="twitter:image" content="{og_image_url}">
{hreflang}<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/countdown.css">
<style>:root{{--cat-color:{cat_color};--cat-glow:{cat_glow};--cat-soft:{cat_soft};}}</style>
<script>if(localStorage.getItem('cd_theme')==='light')document.documentElement.setAttribute('data-theme','light');</script>
<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@graph": [
    {{
      "@type": "WebPage",
      "@id": "{page_url}#webpage",
      "url": "{page_url}",
      "name": "{seo_title}",
      "description": "{meta_desc}",
      "inLanguage": "{html_lang}"
    }},
    {{
      "@type": "Event",
      "name": "{name}",
      "description": "{meta_desc}",
      "url": "{page_url}",
      "organizer": {{
        "@type": "Organization",
        "name": "countdowns.site",
        "url": "https://countdowns.site"
      }}
    }},
    {{
      "@type": "FAQPage",
      "mainEntity": {faq_json}
    }}
  ]
}}
</script>
</head>
<body>
<header class="site-header">
  <a href="/" class="logo">countdowns<span class="logo-tld">.site</span></a>
  <div class="header-right">
    <a href="/favorites/" class="hub-fav-header-link" id="hub-fav-header-link" title="My Favorites">☆&nbsp;Favorites <span id="hub-fav-badge" class="hub-fav-badge" style="display:none"></span></a>
    <button class="theme-btn" id="theme-toggle">Light</button>
    <div class="lang-seg" role="group" aria-label="Language">
      {lang_buttons}
    </div>
    <button class="country-flag-btn" id="country-flag-btn" title="Select country" aria-label="Select country">🌍</button>
  </div>
</header>
<div id="root"><div style="min-height:100vh;background:#080812"></div></div>
{country_picker_html}
{faq_section}
<footer class="site-footer">
  countdowns<span class="logo-tld">.site</span> · <a href="/privacy/" style="color:inherit;opacity:.6;font-size:.85rem">Privacy Policy</a>
</footer>
<script src="/countdown-engine.js"></script>
<script>
{render_script}
// ── Theme toggle ──────────────────────────────────────────────────────
(function() {{
  var btn = document.getElementById('theme-toggle');
  var saved = localStorage.getItem('cd_theme');
  if (saved === 'light') {{ document.documentElement.setAttribute('data-theme', 'light'); btn.textContent = 'Dark'; }}
  btn.addEventListener('click', function() {{
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
// ── Country flag ──────────────────────────────────────────────────────
(function(){{
  var fb=document.getElementById('country-flag-btn');
  if(!fb)return;
  var saved=typeof localStorage!=='undefined'?localStorage.getItem('cd_country'):null;
  if(saved&&CountdownEngine.FLAG_MAP)fb.textContent=CountdownEngine.FLAG_MAP[saved]||'🌍';
  fb.addEventListener('click',function(){{
    CountdownEngine.openCountryPicker(function(code){{
      localStorage.setItem('cd_country',code);
      location.reload();
    }});
  }});
}})();
</script>
</body>
</html>'''

# ─── Embed page generator ──────────────────────────────────────────────────────
def generate_embed_page(ev, lang="en"):
    slug      = ev["slug"]
    category  = ev["category"]
    ev_type   = ev["type"]
    cat_color, cat_glow, cat_soft = CAT_COLORS.get(
        category, ('#818CF8', 'rgba(129,140,248,.2)', 'rgba(129,140,248,.08)')
    )

    t         = TRANSLATIONS.get(lang, {}).get("events", {}).get(slug, {}) if lang != "en" else {}
    html_lang = TRANSLATIONS.get(lang, {}).get("html_lang", "en") if lang != "en" else "en"
    name      = t.get("name", ev["name"])
    hero_desc = t.get("hero_desc", ev["hero_desc"])

    lang_pfx  = "" if lang == "en" else f"/{lang}"
    page_url  = f"https://countdowns.site{lang_pfx}/countdown/{slug}/"

    # render script — same patterns as generate_page but calling renderEmbed
    country_variants = ev.get("country_variants", [])
    default_variant_by_lang = ev.get("default_variant_by_lang", {})

    if country_variants:
        default_idx = default_variant_by_lang.get(lang, 0)
        cv_js = json.dumps([
            {"code": v["code"], "label": v["label"], "dates": v["dates"], "countries": v.get("countries", [])}
            for v in country_variants
        ])
        render_script = f'''(function() {{
  var VARIANTS = {cv_js};
  var DEFAULT_IDX = {default_idx};
  var _cfg = {{
    slug: {json.dumps(slug)},
    type: 'fixed',
    name: {json.dumps(name)},
    category: {json.dumps(category)},
    description: {json.dumps(hero_desc)},
    pageUrl: {json.dumps(page_url)}
  }};
  function nextDate(dates) {{
    var now = new Date();
    for (var i = 0; i < dates.length; i++) {{
      if (new Date(dates[i]) > now) return new Date(dates[i]);
    }}
    return new Date(dates[dates.length - 1]);
  }}
  var _savedC = (typeof localStorage !== 'undefined' ? localStorage.getItem('cd_country') : null) || '';
  var activeIdx = DEFAULT_IDX;
  if (_savedC) {{
    for (var _i = 0; _i < VARIANTS.length; _i++) {{
      if (VARIANTS[_i].countries && VARIANTS[_i].countries.indexOf(_savedC) >= 0) {{
        activeIdx = _i; break;
      }}
    }}
  }}
  CountdownEngine.renderEmbed('root', Object.assign({{}}, _cfg, {{ date: nextDate(VARIANTS[activeIdx].dates) }}));
}})();'''
    else:
        render_script = f'''CountdownEngine.renderEmbed('root', {{
  slug: {json.dumps(slug)},
  type: {json.dumps(ev_type)},
  name: {json.dumps(name)},
  category: {json.dumps(category)},
  description: {json.dumps(hero_desc)},
  pageUrl: {json.dumps(page_url)}
}});'''

    return f'''<!DOCTYPE html>
<html lang="{html_lang}">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{name} — countdowns.site</title>
<meta name="robots" content="noindex">
<style>
*,*::before,*::after{{box-sizing:border-box;margin:0;padding:0}}
html,body{{width:100%;height:100%;background:transparent;overflow:hidden}}
:root{{--cat:{cat_color};--cat-glow:{cat_glow};--cat-soft:{cat_soft};}}
</style>
</head>
<body>
<div id="root"></div>
<script src="/countdown-engine.js"></script>
<script>
{render_script}
</script>
</body>
</html>'''

# ─── Custom countdown page generator ──────────────────────────────────────────
def generate_custom_page(lang="en"):
    html_lang_map = {"en":"en","es":"es","pt":"pt-BR","fr":"fr"}
    html_lang = html_lang_map.get(lang, "en")
    lang_pfx  = "" if lang == "en" else f"/{lang}"
    en_url    = "https://countdowns.site/custom/"
    page_url  = en_url if lang == "en" else f"https://countdowns.site/{lang}/custom/"

    def lang_href(btn_lang):
        return "/custom/" if btn_lang == "en" else f"/{btn_lang}/custom/"
    def lang_btn(btn_lang, label):
        active = ' active' if btn_lang == lang else ''
        if btn_lang == lang:
            return f'<button class="lang-btn{active}">{label}</button>'
        return f'<button class="lang-btn{active}" onclick="localStorage.setItem(\'cd_lang_override\',\'{btn_lang}\');location.href=\'{lang_href(btn_lang)}\'">{label}</button>'
    lang_buttons = lang_btn("en","EN") + lang_btn("es","ES") + lang_btn("pt","PT") + lang_btn("fr","FR")

    hreflang = f'<link rel="alternate" hreflang="en" href="{en_url}">\n'
    hreflang += f'<link rel="alternate" hreflang="x-default" href="{en_url}">\n'
    for alt_lang, alt_hl in [("es","es"),("pt","pt-BR"),("fr","fr")]:
        hreflang += f'<link rel="alternate" hreflang="{alt_hl}" href="https://countdowns.site/{alt_lang}/custom/">\n'

    seo_titles = {"en":"Create Your Own Countdown — Free Shareable Timer",
                  "es":"Crea Tu Cuenta Regresiva Gratis — Compártela al Instante",
                  "pt":"Crie Sua Contagem Regressiva Grátis — Compartilhe Agora",
                  "fr":"Créez Votre Compte à Rebours Gratuit — Partagez en Un Clic"}
    meta_descs = {"en":"Create a free custom countdown timer for any event. Just pick a name, date and optional time — get a shareable link instantly. No sign-up needed.",
                  "es":"Crea un contador regresivo gratis para cualquier evento. Elegí nombre, fecha y hora opcional — obtenés un enlace para compartir al instante. Sin registro.",
                  "pt":"Crie uma contagem regressiva grátis para qualquer evento. Escolha nome, data e hora opcional — obtenha um link compartilhável na hora. Sem cadastro.",
                  "fr":"Créez un compte à rebours gratuit pour n'importe quel événement. Choisissez un nom, une date et une heure optionnelle — obtenez un lien à partager instantanément."}

    seo_title = seo_titles.get(lang, seo_titles["en"])
    meta_desc = meta_descs.get(lang, meta_descs["en"])

    # All UI strings and logic live in embedded JS
    # Build the UI i18n object as a Python dict so json.dumps handles all
    # apostrophes / special chars correctly — no manual escaping needed.
    ui_obj = {
        "en": {
            "hero": "Create your countdown",
            "heroSub": "Pick a date — get a free shareable link. No sign-up needed.",
            "nameLabel": "Event name", "namePlaceholder": "My wedding, Graduation, Trip to Japan…",
            "dateLabel": "Date", "timeLabel": "Time", "timePlaceholder": "Optional",
            "msgLabel": "Note", "msgPlaceholder": "Optional — shown below the timer",
            "createBtn": "Create countdown →", "editBtn": "← Edit",
            "saveFav": "Save to favorites", "savedFav": "Saved",
            "copyLink": "Copy link", "copied": "✓ Copied!", "share": "Share", "wa": "WhatsApp",
            "shareMsg": "Check out this countdown: ",
            "pastBadge": "This event already happened",
            "faqTitle": "How it works",
            "faqs": [
                ["Is it free?", "Yes, 100% free. No account or sign-up needed. Ever."],
                ["How do I share my countdown?", "After creating it, click “Copy link” and send the URL to anyone. Opening that link shows the countdown directly."],
                ["Does my link expire?", "No. All the data is encoded in the URL itself, so it works forever without any server."],
                ["Can I set an exact time?", "Yes — the time field is optional. Leave it blank and the countdown goes to midnight on the chosen date."],
                ["Can I edit it later?", "Click “Edit” on any countdown page to change the name, date, or note."],
            ]
        },
        "es": {
            "hero": "Crea tu cuenta regresiva",
            "heroSub": "Elegí una fecha y compartí el enlace con quien quieras. Gratis, sin registro.",
            "nameLabel": "Nombre del evento", "namePlaceholder": "Mi boda, Graduación, Viaje a Japón…",
            "dateLabel": "Fecha", "timeLabel": "Hora", "timePlaceholder": "Opcional",
            "msgLabel": "Nota", "msgPlaceholder": "Opcional — se muestra bajo el temporizador",
            "createBtn": "Crear cuenta regresiva →", "editBtn": "← Editar",
            "saveFav": "Guardar en favoritos", "savedFav": "Guardado",
            "copyLink": "Copiar enlace", "copied": "✓ ¡Copiado!", "share": "Compartir", "wa": "WhatsApp",
            "shareMsg": "Mirá esta cuenta regresiva: ",
            "pastBadge": "Este evento ya ocurrió",
            "faqTitle": "Cómo funciona",
            "faqs": [
                ["¿Es gratis?", "Sí, 100% gratis. Sin cuenta ni registro. Siempre."],
                ["¿Cómo lo comparto?", "Después de crear tu cuenta regresiva, hacé clic en “Copiar enlace” y mandáselo a quien quieras."],
                ["¿El enlace caduca?", "No. Todos los datos están en la URL, así que funciona para siempre sin ningún servidor."],
                ["¿Puedo poner una hora exacta?", "Sí — el campo de hora es opcional. Si lo dejás vacío, cuenta hasta la medianoche de la fecha elegida."],
                ["¿Puedo editarlo después?", "Hacé clic en “Editar” en cualquier página de cuenta regresiva para cambiar el nombre, fecha o nota."],
            ]
        },
        "pt": {
            "hero": "Crie sua contagem regressiva",
            "heroSub": "Escolha uma data e compartilhe o link com quem quiser. Grátis, sem cadastro.",
            "nameLabel": "Nome do evento", "namePlaceholder": "Meu casamento, Formatura, Viagem ao Japão…",
            "dateLabel": "Data", "timeLabel": "Hora", "timePlaceholder": "Opcional",
            "msgLabel": "Nota", "msgPlaceholder": "Opcional — exibida abaixo do timer",
            "createBtn": "Criar contagem regressiva →", "editBtn": "← Editar",
            "saveFav": "Salvar nos favoritos", "savedFav": "Salvo",
            "copyLink": "Copiar link", "copied": "✓ Copiado!", "share": "Compartilhar", "wa": "WhatsApp",
            "shareMsg": "Veja esta contagem regressiva: ",
            "pastBadge": "Este evento já aconteceu",
            "faqTitle": "Como funciona",
            "faqs": [
                ["É gratuito?", "Sim, 100% gratuito. Sem cadastro ou conta. Sempre."],
                ["Como compartilho?", "Após criar sua contagem, clique em “Copiar link” e envie para quem quiser."],
                ["O link expira?", "Não. Todos os dados ficam na URL, então funciona para sempre sem servidor."],
                ["Posso definir um horário exato?", "Sim — o campo de hora é opcional. Se deixar em branco, conta até a meia-noite da data escolhida."],
                ["Posso editar depois?", "Clique em “Editar” em qualquer página para mudar o nome, data ou nota."],
            ]
        },
        "fr": {
            "hero": "Créez votre compte à rebours",
            "heroSub": "Choisissez une date et partagez le lien avec qui vous voulez. Gratuit, sans inscription.",
            "nameLabel": "Événement", "namePlaceholder": "Mon mariage, Diplôme, Voyage au Japon…",
            "dateLabel": "Date", "timeLabel": "Heure", "timePlaceholder": "Optionnel",
            "msgLabel": "Note", "msgPlaceholder": "Optionnel — affichée sous le minuteur",
            "createBtn": "Créer le compte à rebours →", "editBtn": "← Modifier",
            "saveFav": "Sauvegarder en favoris", "savedFav": "Sauvegardé",
            "copyLink": "Copier le lien", "copied": "✓ Copié !", "share": "Partager", "wa": "WhatsApp",
            "shareMsg": "Regardez ce compte à rebours : ",
            "pastBadge": "Cet événement a déjà eu lieu",
            "faqTitle": "Comment ça marche",
            "faqs": [
                ["C’est gratuit ?", "Oui, 100 % gratuit. Sans inscription ni compte. Toujours."],
                ["Comment le partager ?", "Après avoir créé votre compte à rebours, cliquez sur “Copier le lien” et envoyez-le à qui vous voulez."],
                ["Le lien expire-t-il ?", "Non. Toutes les données sont dans l’URL, donc il fonctionne indéfiniment sans serveur."],
                ["Puis-je définir une heure précise ?", "Oui — le champ heure est optionnel. Si vous le laissez vide, le compte à rebours va jusqu’à minuit à la date choisie."],
                ["Puis-je modifier après ?", "Cliquez sur “Modifier” sur n’importe quelle page pour changer le nom, la date ou la note."],
            ]
        },
    }

    return f'''<!DOCTYPE html>
<html lang="{html_lang}">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{seo_title} | countdowns.site</title>
<meta name="description" content="{meta_desc}">
<meta name="robots" content="index, follow">
<link rel="canonical" href="{page_url}">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="icon" href="/favicon.png" type="image/png" sizes="256x256">
<link rel="apple-touch-icon" href="/favicon.png">
<meta property="og:type" content="website">
<meta property="og:url" content="{page_url}">
<meta property="og:title" content="{seo_title}">
<meta property="og:description" content="{meta_desc}">
{hreflang}<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/countdown.css">
<script src="/countdown-engine.js"></script>
<style>:root{{--cat-color:#818CF8;--cat-glow:rgba(129,140,248,.2);--cat-soft:rgba(129,140,248,.08);}}</style>
<script>if(localStorage.getItem('cd_theme')==='light')document.documentElement.setAttribute('data-theme','light');</script>
</head>
<body>
<header class="site-header">
  <a href="/" class="logo">countdowns<span class="logo-tld">.site</span></a>
  <div class="header-right">
    <a href="/favorites/" class="hub-fav-header-link" id="hub-fav-header-link" title="My Favorites">☆&nbsp;Favorites <span id="hub-fav-badge" class="hub-fav-badge" style="display:none"></span></a>
    <button class="theme-btn" id="theme-toggle" title="Toggle theme"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="5"/><line x1="12" y1="1" x2="12" y2="3"/><line x1="12" y1="21" x2="12" y2="23"/><line x1="4.22" y1="4.22" x2="5.64" y2="5.64"/><line x1="18.36" y1="18.36" x2="19.78" y2="19.78"/><line x1="1" y1="12" x2="3" y2="12"/><line x1="21" y1="12" x2="23" y2="12"/><line x1="4.22" y1="19.78" x2="5.64" y2="18.36"/><line x1="18.36" y1="5.64" x2="19.78" y2="4.22"/></svg></button>
    <div class="lang-seg" role="group" aria-label="Language">
      {lang_buttons}
    </div>
    <button class="country-flag-btn" id="country-flag-btn" title="Select country" aria-label="Select country">🌍</button>
  </div>
</header>

<div id="cc-root"></div>

<footer class="site-footer">
  countdowns<span class="logo-tld">.site</span> · <a href="/privacy/" style="color:inherit;opacity:.6;font-size:.85rem">Privacy Policy</a>
</footer>

<script>
(function(){{
'use strict';
var LANG={json.dumps(lang)};
var UI={json.dumps(ui_obj, ensure_ascii=False)};
var T=UI[LANG]||UI.en;
var root=document.getElementById('cc-root');
var _ticker=null;

function pad(n){{return n<10?'0'+n:''+n;}}

function getParams(){{
  var hash=location.hash.replace(/^#/,'');
  var p={{}};
  if(!hash)return p;
  hash.split('&').forEach(function(part){{
    var eq=part.indexOf('=');
    if(eq>0){{
      var k=decodeURIComponent(part.slice(0,eq));
      var v=decodeURIComponent(part.slice(eq+1).replace(/\\+/g,' '));
      p[k]=v;
    }}
  }});
  return p;
}}

function buildHash(n,d,t,m){{
  var parts=['n='+encodeURIComponent(n),'d='+encodeURIComponent(d)];
  if(t)parts.push('t='+encodeURIComponent(t));
  if(m)parts.push('m='+encodeURIComponent(m));
  return parts.join('&');
}}

function startTicker(target){{
  if(_ticker)clearInterval(_ticker);
  function tick(){{
    var now=new Date();
    var diff=target-now;
    if(diff<=0){{clearInterval(_ticker);return;}}
    var d=Math.floor(diff/86400000);
    var h=Math.floor((diff%86400000)/3600000);
    var m=Math.floor((diff%3600000)/60000);
    var s=Math.floor((diff%60000)/1000);
    var el;
    el=document.getElementById('cc-d');if(el)el.textContent=d;
    el=document.getElementById('cc-h');if(el)el.textContent=pad(h);
    el=document.getElementById('cc-m');if(el)el.textContent=pad(m);
    el=document.getElementById('cc-s');if(el)el.textContent=pad(s);
  }}
  tick();
  _ticker=setInterval(tick,1000);
}}

function formatDate(d,t){{
  var parts=d.split('-');
  var dt=new Date(+parts[0],+parts[1]-1,+parts[2],0,0,0);
  var opts={{weekday:'long',year:'numeric',month:'long',day:'numeric'}};
  var locale=LANG==='en'?'en-US':LANG==='es'?'es-ES':LANG==='pt'?'pt-BR':'fr-FR';
  var str=dt.toLocaleDateString(locale,opts);
  if(t)str+=' · '+t;
  return str;
}}

function esc(s){{return s.replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;').replace(/"/g,'&quot;');}}

function buildForm(prefill){{
  prefill=prefill||{{}};
  return '<div class="cc-wrap">'+
    '<h1 class="cc-hero-title">'+T.hero+'</h1>'+
    '<p class="cc-hero-sub">'+T.heroSub+'</p>'+
    '<form id="cc-form" class="cc-form" autocomplete="off">'+
      '<div class="cc-field">'+
        '<label class="cc-label">'+T.nameLabel+' <span class="cc-required">*</span></label>'+
        '<input class="cc-input" id="cc-name" type="text" placeholder="'+T.namePlaceholder+'" maxlength="80" value="'+esc(prefill.n||'')+'" required>'+
      '</div>'+
      '<div class="cc-field cc-row">'+
        '<div class="cc-field-half">'+
          '<label class="cc-label">'+T.dateLabel+' <span class="cc-required">*</span></label>'+
          '<input class="cc-input" id="cc-date" type="date" value="'+(prefill.d||'')+'" required>'+
        '</div>'+
        '<div class="cc-field-half">'+
          '<label class="cc-label">'+T.timeLabel+'</label>'+
          '<input class="cc-input" id="cc-time" type="time" value="'+(prefill.t||'')+'">'+
        '</div>'+
      '</div>'+
      '<div class="cc-field">'+
        '<label class="cc-label">'+T.msgLabel+'</label>'+
        '<input class="cc-input" id="cc-msg" type="text" placeholder="'+T.msgPlaceholder+'" maxlength="200" value="'+esc(prefill.m||'')+'">'+
      '</div>'+
      '<button class="cc-create-btn" type="submit">'+T.createBtn+'</button>'+
    '</form>'+
    buildFaq()+
  '</div>';
}}

// ── Custom favorites helpers ──────────────────────────────────────────────────
function getCustomFavs(){{try{{return JSON.parse(localStorage.getItem('cd_custom_favs')||'[]');}}catch(e){{return [];}}}}
function setCustomFavs(arr){{try{{localStorage.setItem('cd_custom_favs',JSON.stringify(arr));}}catch(e){{}}}}
function customFavKey(p){{return (p.n||'')+'|'+(p.d||'')+'|'+(p.t||'');}}
function isCustomFav(p){{var key=customFavKey(p);return getCustomFavs().some(function(f){{return f.key===key;}});}}
function addCustomFav(p){{var key=customFavKey(p);var favs=getCustomFavs().filter(function(f){{return f.key!==key;}});favs.unshift({{key:key,name:p.n,date:p.d,time:p.t||'',note:p.m||'',url:location.href,savedAt:Date.now()}});setCustomFavs(favs);}}
function removeCustomFav(p){{var key=customFavKey(p);setCustomFavs(getCustomFavs().filter(function(f){{return f.key!==key;}}));}}

function buildCountdown(p){{
  var target=new Date(p.d+(p.t?'T'+p.t+':00':'T00:00:00'));
  var now=new Date();
  var isPast=target<=now;
  var timerHtml=isPast
    ?('<div class="cd-past" style="padding:32px 0 16px">'+
        '<div class="cd-past-badge">'+T.pastBadge+'</div>'+
        '<p class="cd-past-date">'+formatDate(p.d,p.t||'')+'</p>'+
      '</div>')
    :('<div class="cd-grid">'+
        '<div class="cd-box"><span class="cd-num" id="cc-d">0</span><span class="cd-lbl">'+(LANG==='en'?'days':LANG==='es'?'días':LANG==='pt'?'dias':'jours')+'</span></div>'+
        '<span class="cd-sep">:</span>'+
        '<div class="cd-box"><span class="cd-num" id="cc-h">00</span><span class="cd-lbl">'+(LANG==='en'?'hours':LANG==='es'?'horas':LANG==='pt'?'horas':'heures')+'</span></div>'+
        '<span class="cd-sep">:</span>'+
        '<div class="cd-box"><span class="cd-num" id="cc-m">00</span><span class="cd-lbl">min</span></div>'+
        '<span class="cd-sep">:</span>'+
        '<div class="cd-box"><span class="cd-num" id="cc-s">00</span><span class="cd-lbl">sec</span></div>'+
      '</div>'+
      '<p class="cd-date-label">'+formatDate(p.d,p.t||'')+'</p>');
  var noteHtml=p.m?'<div class="cd-note-card">'+esc(p.m)+'</div>':'';
  var shareUrl=location.href;
  var waUrl='https://wa.me/?text='+encodeURIComponent((T.shareMsg)+shareUrl);
  var xUrl='https://twitter.com/intent/tweet?text='+encodeURIComponent((T.shareMsg)+shareUrl);
  var shareBar=
    '<div class="cd-share-bar">'+
      '<button class="cd-share-btn" id="cc-copy" title="'+T.copyLink+'">'+
        '<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="9" y="9" width="13" height="13" rx="2"/><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"/></svg>'+
        T.copyLink+
      '</button>'+
      (navigator.share?'<button class="cd-share-btn" id="cc-native">'+
        '<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 12v8a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2v-8"/><polyline points="16 6 12 2 8 6"/><line x1="12" y1="2" x2="12" y2="15"/></svg>'+
        T.share+'</button>':'')+
      '<a class="cd-share-btn" href="'+waUrl+'" target="_blank" rel="noopener">'+
        '<svg width="14" height="14" viewBox="0 0 24 24" fill="currentColor"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51a12.8 12.8 0 0 0-.57-.01c-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 0 1-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 0 1-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 0 1 2.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0 0 12.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 0 0 5.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 0 0-3.48-8.413Z"/></svg>'+
        T.wa+
      '</a>'+
      '<a class="cd-share-btn" href="'+xUrl+'" target="_blank" rel="noopener">'+
        '<svg width="14" height="14" viewBox="0 0 24 24" fill="currentColor"><path d="M18.244 2.25h3.308l-7.227 8.26 8.502 11.24H16.17l-4.714-6.231-5.401 6.231H2.746l7.73-8.835L1.254 2.25H8.08l4.253 5.622zm-1.161 17.52h1.833L7.084 4.126H5.117z"/></svg>'+
        'X'+
      '</a>'+
    '</div>';
  var isSaved=isCustomFav(p);
  var favBtnLabel=isSaved?'★ '+T.savedFav:'☆ '+T.saveFav;
  var favBtnStyle=isSaved?'color:#FBBF24':'';
  return '<div class="cc-countdown-wrap">'+
    '<div class="cc-edit-row">'+
      '<button class="cc-edit-btn" id="cc-edit">'+
        '<svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M11 4H4a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2v-7"/><path d="M18.5 2.5a2.121 2.121 0 0 1 3 3L12 15l-4 1 1-4 9.5-9.5z"/></svg>'+
        T.editBtn+
      '</button>'+
      '<button class="cc-edit-btn" id="cc-fav-btn" style="'+favBtnStyle+'">'+favBtnLabel+'</button>'+
    '</div>'+
    '<div class="cd-hero" style="padding-top:32px">'+
      '<div class="cd-category-badge" style="margin-bottom:18px">EVENT</div>'+
      '<h1 class="cd-title">'+esc(p.n)+'</h1>'+
      timerHtml+
    '</div>'+
    '<div class="cd-below">'+
      noteHtml+
      shareBar+
    '</div>'+
    buildFaq()+
  '</div>';
}}

function buildFaq(){{
  var items=T.faqs.map(function(f){{
    return '<div class="cd-faq-item"><h3 class="cd-faq-q">'+f[0]+'</h3><p class="cd-faq-a">'+f[1]+'</p></div>';
  }}).join('');
  return '<div class="cd-article" style="max-width:540px;margin:0 auto;padding:0 20px 40px">'+
    '<div class="cd-faq"><h2 class="cd-faq-title">'+T.faqTitle+'</h2>'+items+'</div>'+
  '</div>';
}}

function bindForm(){{
  var form=document.getElementById('cc-form');
  if(!form)return;
  form.addEventListener('submit',function(e){{
    e.preventDefault();
    var n=document.getElementById('cc-name').value.trim();
    var d=document.getElementById('cc-date').value;
    var t=document.getElementById('cc-time').value;
    var m=document.getElementById('cc-msg').value.trim();
    if(!n||!d)return;
    location.hash=buildHash(n,d,t,m);
  }});
}}

function bindCountdown(p){{
  var isPast=new Date(p.d+(p.t?'T'+p.t+':00':'T00:00:00'))<=new Date();
  if(!isPast)startTicker(new Date(p.d+(p.t?'T'+p.t+':00':'T00:00:00')));
  // Edit
  var editBtn=document.getElementById('cc-edit');
  if(editBtn)editBtn.addEventListener('click',function(){{location.hash='';render();}});
  // Save to favorites
  var favBtn=document.getElementById('cc-fav-btn');
  if(favBtn)favBtn.addEventListener('click',function(){{
    if(isCustomFav(p)){{
      removeCustomFav(p);
      favBtn.textContent='☆ '+T.saveFav;
      favBtn.style.color='';
    }}else{{
      addCustomFav(p);
      favBtn.textContent='★ '+T.savedFav;
      favBtn.style.color='#FBBF24';
    }}
  }});
  // Copy
  var copyBtn=document.getElementById('cc-copy');
  if(copyBtn)copyBtn.addEventListener('click',function(){{
    navigator.clipboard.writeText(location.href).then(function(){{
      copyBtn.textContent=T.copied;
      setTimeout(function(){{copyBtn.innerHTML='<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="9" y="9" width="13" height="13" rx="2"/><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"/></svg>'+T.copyLink;}},2000);
    }}).catch(function(){{
      var ta=document.createElement('textarea');
      ta.value=location.href;document.body.appendChild(ta);ta.select();document.execCommand('copy');document.body.removeChild(ta);
      copyBtn.textContent=T.copied;
    }});
  }});
  // Native share
  var nativeBtn=document.getElementById('cc-native');
  if(nativeBtn)nativeBtn.addEventListener('click',function(){{
    navigator.share({{title:p.n,url:location.href}}).catch(function(){{}});
  }});
}}

function render(){{
  var p=getParams();
  if(p.n&&p.d){{
    root.innerHTML=buildCountdown(p);
    bindCountdown(p);
  }}else{{
    root.innerHTML=buildForm(p);
    bindForm();
    var nameEl=document.getElementById('cc-name');
    if(nameEl)nameEl.focus();
  }}
}}

window.addEventListener('hashchange',render);
render();

// Theme toggle
(function(){{
  var SUN='<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="5"/><line x1="12" y1="1" x2="12" y2="3"/><line x1="12" y1="21" x2="12" y2="23"/><line x1="4.22" y1="4.22" x2="5.64" y2="5.64"/><line x1="18.36" y1="18.36" x2="19.78" y2="19.78"/><line x1="1" y1="12" x2="3" y2="12"/><line x1="21" y1="12" x2="23" y2="12"/><line x1="4.22" y1="19.78" x2="5.64" y2="18.36"/><line x1="18.36" y1="5.64" x2="19.78" y2="4.22"/></svg>';
  var MOON='<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"/></svg>';
  var btn=document.getElementById('theme-toggle');
  var saved=localStorage.getItem('cd_theme');
  if(saved==='light'){{document.documentElement.setAttribute('data-theme','light');btn.innerHTML=MOON;}}
  btn.addEventListener('click',function(){{
    var isLight=document.documentElement.getAttribute('data-theme')==='light';
    if(isLight){{document.documentElement.removeAttribute('data-theme');localStorage.setItem('cd_theme','dark');btn.innerHTML=SUN;}}
    else{{document.documentElement.setAttribute('data-theme','light');localStorage.setItem('cd_theme','light');btn.innerHTML=MOON;}}
  }});
}})();
// ── Country flag ──────────────────────────────────────────────────────
(function(){{
  var fb=document.getElementById('country-flag-btn');
  if(!fb)return;
  var saved=typeof localStorage!=='undefined'?localStorage.getItem('cd_country'):null;
  if(saved&&CountdownEngine.FLAG_MAP)fb.textContent=CountdownEngine.FLAG_MAP[saved]||'🌍';
  fb.addEventListener('click',function(){{
    CountdownEngine.openCountryPicker(function(code){{
      localStorage.setItem('cd_country',code);
      location.reload();
    }});
  }});
}})();
}})();
</script>
</body>
</html>'''

# ─── Daily countdown helpers ──────────────────────────────────────────────────
MONTH_NAMES_DAILY = {
  'en': ['January','February','March','April','May','June',
         'July','August','September','October','November','December'],
  'es': ['enero','febrero','marzo','abril','mayo','junio',
         'julio','agosto','septiembre','octubre','noviembre','diciembre'],
  'pt': ['janeiro','fevereiro','março','abril','maio','junho',
         'julho','agosto','setembro','outubro','novembro','dezembro'],
  'fr': ['janvier','février','mars','avril','mai','juin',
         'juillet','août','septembre','octobre','novembre','décembre'],
}
MONTH_DAYS_DAILY = [31,28,31,30,31,30,31,31,30,31,30,31]

def day_ord_en(n):
  s = 'th' if 10 <= n%100 <= 20 else {1:'st',2:'nd',3:'rd'}.get(n%10,'th')
  return f"{n}{s}"

def get_daily_ev(month, day):
  month_en = MONTH_NAMES_DAILY['en'][month-1]
  slug     = f"{month_en.lower()}-{day}"
  ord_en   = day_ord_en(day)
  name_en  = f"{month_en} {ord_en}"
  return dict(
    slug=slug, name=name_en, type="annual", category="Months",
    regions=["global"],
    seo_title=f"How Many Days Until {month_en} {ord_en}? — Live Countdown",
    meta_desc=f"Live countdown to {month_en} {ord_en}. Exact days, hours, minutes and seconds. Resets automatically every year.",
    hero_desc=f"Live countdown to {month_en} {ord_en}.",
    content=f"{month_en} {ord_en} recurs every year. This live countdown shows the exact time remaining until the next {month_en} {day}. The timer resets automatically once the date arrives.",
    faqs=[
      (f"How many days until {month_en} {ord_en}?",
       f"Use the live countdown above to see the exact days, hours, minutes and seconds until {month_en} {ord_en}."),
      ("Does the countdown reset each year?",
       f"Yes — once {month_en} {day} arrives, the countdown automatically resets to next year's {month_en} {day}."),
      (f"Is {month_en} {day} a holiday?",
       f"It depends on the country. Use the live countdown above to count down to {month_en} {day}, regardless of whether it is a public holiday."),
    ]
  )

def inject_daily_translations(slug, month, day):
  for lang in ['es','pt','fr']:
    mn = MONTH_NAMES_DAILY[lang][month-1]
    if lang == 'fr':
      ds = f"1er {mn}" if day == 1 else f"{day} {mn}"
      t = dict(
        name=ds,
        seo_title=f"Dans combien de jours c'est le {ds} ? — Compte à Rebours",
        meta_desc=f"Compte à rebours en direct pour le {ds}. Jours, heures, minutes et secondes exactes. Se réinitialise chaque année.",
        hero_desc=f"Compte à rebours pour le {ds}.",
        content=f"Le {ds} est une date qui revient chaque année. Ce compteur montre le temps exact jusqu'au prochain {ds}. Le compteur se réinitialise automatiquement.",
        faqs=[
          (f"Dans combien de jours est le {ds} ?",
           f"Utilisez le compte à rebours ci-dessus pour voir les jours, heures, minutes et secondes exacts jusqu'au {ds}."),
          ("Le compte à rebours se réinitialise-t-il chaque année ?",
           f"Oui — lorsque le {ds} arrive, le compteur se réinitialise automatiquement pour l'année suivante."),
        ]
      )
    elif lang == 'es':
      t = dict(
        name=f"{day} de {mn}",
        seo_title=f"¿Cuántos días faltan para el {day} de {mn}? — Cuenta Regresiva",
        meta_desc=f"Cuenta regresiva en vivo para el {day} de {mn}. Días, horas, minutos y segundos exactos. Se reinicia automáticamente cada año.",
        hero_desc=f"Cuenta regresiva para el {day} de {mn}.",
        content=f"El {day} de {mn} es una fecha que se repite cada año. Este contador muestra el tiempo exacto restante hasta el próximo {day} de {mn}. Se reinicia automáticamente.",
        faqs=[
          (f"¿Cuántos días faltan para el {day} de {mn}?",
           f"Usa la cuenta regresiva de arriba para ver los días, horas, minutos y segundos exactos hasta el {day} de {mn}."),
          ("¿El contador se reinicia cada año?",
           f"Sí — cuando llega el {day} de {mn}, el contador se reinicia automáticamente para el año siguiente."),
        ]
      )
    else:  # pt
      t = dict(
        name=f"{day} de {mn}",
        seo_title=f"Quantos dias faltam para {day} de {mn}? — Contagem Regressiva",
        meta_desc=f"Contagem regressiva ao vivo para {day} de {mn}. Dias, horas, minutos e segundos exatos. Reinicia automaticamente todo ano.",
        hero_desc=f"Contagem regressiva para {day} de {mn}.",
        content=f"{day} de {mn} é uma data que se repete todo ano. Este contador mostra o tempo exato até o próximo {day} de {mn}. Reinicia automaticamente.",
        faqs=[
          (f"Quantos dias faltam para {day} de {mn}?",
           f"Use a contagem regressiva acima para ver os dias, horas, minutos e segundos exatos até {day} de {mn}."),
          ("A contagem regressiva reinicia todo ano?",
           f"Sim — quando chega {day} de {mn}, o contador reinicia automaticamente para o ano seguinte."),
        ]
      )
    TRANSLATIONS.setdefault(lang,{}).setdefault('events',{})[slug] = t

def cleanup_daily_translations(slug):
  for lang in ['es','pt','fr']:
    TRANSLATIONS.get(lang,{}).get('events',{}).pop(slug,None)

# ─── Generate all pages ────────────────────────────────────────────────────────
generated = 0
for ev in EVENTS:
    slug = ev["slug"]
    langs_for_slug = SLUG_LANGS[slug]

    # EN page → /countdown/{slug}/
    en_dir = os.path.join("countdown", slug)
    os.makedirs(en_dir, exist_ok=True)
    with open(os.path.join(en_dir, "index.html"), "w", encoding="utf-8") as f:
        f.write(generate_page(ev, "en"))
    print(f"  ✓  /countdown/{slug}/")
    generated += 1

    # Translated pages → /{lang}/countdown/{slug}/
    for lang in ["es", "pt", "fr"]:
        if lang in langs_for_slug:
            out_dir = os.path.join(lang, "countdown", slug)
            os.makedirs(out_dir, exist_ok=True)
            with open(os.path.join(out_dir, "index.html"), "w", encoding="utf-8") as f:
                f.write(generate_page(ev, lang))
            print(f"  ✓  /{lang}/countdown/{slug}/")
            generated += 1

    # EN embed page → /embed/{slug}/
    embed_en_dir = os.path.join("embed", slug)
    os.makedirs(embed_en_dir, exist_ok=True)
    with open(os.path.join(embed_en_dir, "index.html"), "w", encoding="utf-8") as f:
        f.write(generate_embed_page(ev, "en"))
    print(f"  ✓  /embed/{slug}/")
    generated += 1

    # Translated embed pages → /{lang}/embed/{slug}/
    for lang in ["es", "pt", "fr"]:
        if lang in langs_for_slug:
            out_dir = os.path.join(lang, "embed", slug)
            os.makedirs(out_dir, exist_ok=True)
            with open(os.path.join(out_dir, "index.html"), "w", encoding="utf-8") as f:
                f.write(generate_embed_page(ev, lang))
            print(f"  ✓  /{lang}/embed/{slug}/")
            generated += 1

print(f"\nGenerated {generated} pages.")

# ─── Generate 365 daily countdown pages (not shown on hub) ────────────────────
print("\nGenerating 365 daily countdown pages...")
daily_count = 0
for m_idx, days_in_month in enumerate(MONTH_DAYS_DAILY):
  month = m_idx + 1
  for day in range(1, days_in_month + 1):
    month_en = MONTH_NAMES_DAILY['en'][m_idx]
    slug     = f"{month_en.lower()}-{day}"
    ev       = get_daily_ev(month, day)
    inject_daily_translations(slug, month, day)

    # EN page
    en_dir = os.path.join("countdown", slug)
    os.makedirs(en_dir, exist_ok=True)
    with open(os.path.join(en_dir, "index.html"), "w", encoding="utf-8") as f:
      f.write(generate_page(ev, "en"))
    daily_count += 1

    # ES / PT / FR pages
    for lang in ["es", "pt", "fr"]:
      out_dir = os.path.join(lang, "countdown", slug)
      os.makedirs(out_dir, exist_ok=True)
      with open(os.path.join(out_dir, "index.html"), "w", encoding="utf-8") as f:
        f.write(generate_page(ev, lang))
      daily_count += 1

    cleanup_daily_translations(slug)

print(f"Generated {daily_count} daily pages ({daily_count//4} dates × 4 languages).")

# ─── Generate custom countdown pages ──────────────────────────────────────────
os.makedirs("custom", exist_ok=True)
with open(os.path.join("custom", "index.html"), "w", encoding="utf-8") as f:
    f.write(generate_custom_page("en"))
print("  ✓  /custom/")

for lang in ["es", "pt", "fr"]:
    out_dir = os.path.join(lang, "custom")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "index.html"), "w", encoding="utf-8") as f:
        f.write(generate_custom_page(lang))
    print(f"  ✓  /{lang}/custom/")

print("\nDone.")
