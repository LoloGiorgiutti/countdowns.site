#!/usr/bin/env python3
"""
Generate individual countdown pages for countdowns.site
Run from repo root: python3 _generate.py
"""
import os, json

BASE_URL = "https://countdowns.site"

EVENTS = [
  # ── Releases ──────────────────────────────────────────────────────────
  dict(
    slug="gta6", name="GTA VI", type="variable", category="Releases",
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
    seo_title="Next iPhone Countdown — Days Until iPhone 18 Release 2026",
    meta_desc="Live countdown to the next iPhone release. Apple typically unveils new iPhones in September. Track the exact days until iPhone 18 launch.",
    hero_desc="Live countdown to Apple's next iPhone announcement and release.",
    content="Apple traditionally announces new iPhone models in September, with an event usually held in the first or second week of the month. The iPhone 18 lineup is expected to be unveiled in September 2026, following the same annual release cadence Apple has maintained since 2012.",
    faqs=[
      ("When will the next iPhone be released?", "Apple typically announces new iPhones in September. The next iPhone (iPhone 18) is estimated to launch around September 9, 2026."),
      ("What will iPhone 18 feature?", "Apple has not officially revealed iPhone 18 specs yet. Leaks suggest significant camera improvements, a new A20 chip, and potential design changes."),
      ("How do I pre-order the next iPhone?", "Apple opens pre-orders on the Friday following its September event, usually at apple.com and through carriers."),
    ]
  ),

  # ── Sports – Global ────────────────────────────────────────────────────
  dict(
    slug="f1", name="F1 Next Race", type="variable", category="Sports",
    seo_title="F1 Countdown — Days Until the Next Formula 1 Race",
    meta_desc="Real-time countdown to the next Formula 1 Grand Prix. See exactly how many days, hours and minutes until the next F1 race weekend.",
    hero_desc="Live countdown to the next Formula 1 Grand Prix.",
    content="Formula 1 holds around 24 Grands Prix per season, racing on circuits across five continents from March to December. The countdown above always shows the time remaining until the next scheduled race.",
    faqs=[
      ("When is the next F1 race?", "The countdown above shows the date of the next scheduled Grand Prix. The current race on the calendar is the Monaco Grand Prix on May 24, 2026."),
      ("How long is an F1 race weekend?", "A standard F1 weekend spans Thursday–Sunday, with practice on Thursday and Friday, qualifying on Saturday, and the race on Sunday."),
      ("Where can I watch F1?", "Formula 1 is broadcast on ESPN (USA), Sky Sports F1 (UK), Canal+ (France), DAZN (various countries), and F1 TV globally."),
    ]
  ),
  dict(
    slug="world-cup", name="2026 FIFA World Cup", type="variable", category="Sports",
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
    seo_title="Champions League Final Countdown 2026 — Days Until UCL Final",
    meta_desc="Live countdown to the UEFA Champions League 2025–26 Final at Puskás Aréna, Budapest on May 30, 2026.",
    hero_desc="Countdown to the 2026 UEFA Champions League Final.",
    content="The UEFA Champions League 2025–26 Final takes place at Puskás Aréna in Budapest, Hungary on May 30, 2026. The final is the most-watched annual club football event in the world, drawing an estimated 500 million viewers globally.",
    faqs=[
      ("When is the Champions League Final 2026?", "The UCL Final 2026 is on May 30, 2026 at Puskás Aréna, Budapest."),
      ("Where is the 2026 Champions League Final?", "The final is held at Puskás Aréna in Budapest, Hungary, with a capacity of around 68,000."),
      ("How many teams are in the Champions League?", "The 2024–25 reformed format features 36 clubs in the league phase, with the top 8 advancing directly to the round of 16."),
    ]
  ),
  dict(
    slug="nba-finals", name="NBA Finals", type="variable", category="Sports",
    seo_title="NBA Finals Countdown 2026 — Days Until the NBA Championship",
    meta_desc="Real-time countdown to the 2026 NBA Finals. Track the days until basketball's biggest series begins.",
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
    seo_title="Le Mans 24h Countdown 2026 — Days Until the 24 Hours of Le Mans",
    meta_desc="Live countdown to the 24 Hours of Le Mans 2026. The world's most prestigious endurance race starts June 13, 2026 at Circuit de la Sarthe.",
    hero_desc="Countdown to the 2026 24 Hours of Le Mans.",
    content="The 24 Hours of Le Mans is the world's oldest active sports car endurance race, held annually on the Circuit de la Sarthe near Le Mans, France. In 2026, the race starts on June 13 and runs continuously for 24 hours, featuring the top hypercar, LMP2 and GT classes.",
    faqs=[
      ("When is Le Mans 2026?", "The 24 Hours of Le Mans 2026 starts on Saturday, June 13, 2026 at 16:00 local time (CET)."),
      ("Where is Le Mans held?", "Le Mans is held on the Circuit de la Sarthe, a 13.6 km circuit combining permanent track with closed public roads near Le Mans, France."),
      ("How can I watch Le Mans?", "Le Mans is broadcast live on Eurosport (Europe), MotorTrend (USA), and the FIA WEC streaming platform globally."),
    ]
  ),
  dict(
    slug="wimbledon", name="Wimbledon", type="variable", category="Sports",
    seo_title="Wimbledon 2026 Countdown — Days Until Wimbledon Tennis",
    meta_desc="Live countdown to Wimbledon 2026, the world's oldest and most prestigious tennis Grand Slam, starting June 29, 2026 at the All England Club.",
    hero_desc="Countdown to The Championships, Wimbledon 2026.",
    content="Wimbledon is the oldest tennis Grand Slam in the world, held annually at the All England Lawn Tennis Club in London since 1877. The 2026 Championships begin on June 29, with the men's and women's singles finals held on the last two Sundays of the fortnight.",
    faqs=[
      ("When does Wimbledon 2026 start?", "Wimbledon 2026 begins on Monday, June 29, 2026 and runs for two weeks through mid-July."),
      ("Where is Wimbledon played?", "Wimbledon is held at the All England Lawn Tennis and Croquet Club in Wimbledon, southwest London."),
      ("How do I get Wimbledon tickets?", "Tickets are available via the annual public ballot (applications typically open in January) or through queue on the day."),
    ]
  ),
  dict(
    slug="tour-de-france", name="Tour de France", type="variable", category="Sports",
    seo_title="Tour de France 2026 Countdown — Days Until the Tour de France",
    meta_desc="Live countdown to the Tour de France 2026. The world's most famous cycling race starts in late June 2026 with 21 stages over three weeks.",
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
    seo_title="Super Bowl Countdown — Days Until Super Bowl LXI 2027",
    meta_desc="Live countdown to Super Bowl LXI in 2027. The NFL championship game is played on the second Sunday of February each year.",
    hero_desc="Countdown to Super Bowl LXI — the NFL Championship.",
    content="The Super Bowl is the annual championship game of the National Football League (NFL), and one of the most-watched television events in the world. Super Bowl LXI takes place on the second Sunday of February 2027. The halftime show and commercials are as iconic as the game itself.",
    faqs=[
      ("When is the next Super Bowl?", "Super Bowl LXI will be held on Sunday, February 7, 2027 (second Sunday of February)."),
      ("Where is Super Bowl LXI?", "The host city for Super Bowl LXI has not yet been announced by the NFL."),
      ("How much are Super Bowl tickets?", "Super Bowl tickets typically start at $900+ on the secondary market and often exceed $10,000 for premium seats."),
      ("When is the Super Bowl halftime show?", "The halftime show takes place between the second and third quarters, roughly 30–40 minutes into the game."),
    ]
  ),
  dict(
    slug="copa-libertadores", name="Copa Libertadores Final", type="variable", category="Sports",
    seo_title="Copa Libertadores Final 2026 Countdown — Days Until the Final",
    meta_desc="Live countdown to the 2026 Copa Libertadores Final, South America's biggest club football match. Date and venue TBD by CONMEBOL.",
    hero_desc="Countdown to the 2026 Copa Libertadores Final.",
    content="The Copa Libertadores is South America's premier club football competition, organized by CONMEBOL. The annual final is one of the most watched football matches in the Americas. The 2026 final date and host city will be announced by CONMEBOL.",
    faqs=[
      ("When is the Copa Libertadores Final 2026?", "The 2026 final date has not been confirmed yet. CONMEBOL usually holds the final in November."),
      ("Where is the Copa Libertadores Final held?", "CONMEBOL selects a neutral venue for the final, often in a major South American city such as Buenos Aires, Lima, Montevideo or Asunción."),
      ("Which teams have won the most Copa Libertadores titles?", "Independiente (Argentina) is the most successful club with 7 titles. Boca Juniors (Argentina) and Estudiantes (Argentina) are also among the top winners."),
      ("How many teams participate in the Copa Libertadores?", "The Copa Libertadores features 47 clubs from CONMEBOL's 10 member nations, competing across multiple knockout and group stage rounds."),
    ]
  ),

  # ── Holidays – Global ──────────────────────────────────────────────────
  dict(
    slug="christmas", name="Christmas", type="auto", category="Holidays",
    seo_title="Christmas Countdown 2026 — Days Until Christmas",
    meta_desc="How many days until Christmas 2026? Live countdown showing exact days, hours, minutes and seconds until December 25.",
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
    seo_title="New Year Countdown 2027 — Days Until New Year's Eve",
    meta_desc="Live countdown to New Year 2027. How many days, hours and seconds until January 1, 2027? Watch the real-time counter.",
    hero_desc="Countdown to New Year 2027.",
    content="New Year's Day is celebrated on January 1 and marks the start of the new calendar year. New Year's Eve on December 31 is famous for fireworks and celebrations in cities around the world, including Sydney, Dubai, London and New York.",
    faqs=[
      ("How many days until New Year 2027?", "The live counter above shows the exact time remaining until January 1, 2027."),
      ("What day is New Year's Day 2027?", "New Year's Day 2027 falls on a Friday, January 1."),
      ("Where are the best New Year fireworks?", "Famous New Year fireworks displays include Sydney Harbour Bridge, Dubai, London's Thames, and New York's Times Square."),
      ("What time zone does New Year start first?", "New Year arrives first in Kiribati (UTC+14) and last in the Baker Island (UTC-12), about 26 hours apart."),
      ("When is New Year's Eve?", "New Year's Eve is December 31, the last day of the year, the night before January 1."),
    ]
  ),
  dict(
    slug="halloween", name="Halloween", type="auto", category="Holidays",
    seo_title="Halloween Countdown 2026 — Days Until Halloween",
    meta_desc="How many days until Halloween 2026? Live countdown to October 31. Watch the exact hours, minutes and seconds tick down.",
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
    seo_title="Valentine's Day Countdown 2027 — Days Until Valentine's Day",
    meta_desc="Live countdown to Valentine's Day 2027. How many days until February 14? Watch the exact hours and minutes remaining.",
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
    seo_title="Easter 2027 Countdown — How Many Days Until Easter Sunday",
    meta_desc="Live countdown to Easter 2027. Easter Sunday is a moveable feast — the countdown updates automatically each year.",
    hero_desc="Countdown to Easter Sunday.",
    content="Easter is a Christian holiday celebrating the resurrection of Jesus Christ. Easter Sunday falls on the first Sunday after the first full moon following the spring equinox (March 21), making it a moveable feast between March 22 and April 25.",
    faqs=[
      ("When is Easter 2027?", "Easter 2027 falls on Sunday, March 28, 2027."),
      ("When is Easter 2026?", "Easter 2026 falls on Sunday, April 5, 2026."),
      ("How is the date of Easter calculated?", "Easter falls on the first Sunday after the first full moon on or after March 21 (the ecclesiastical spring equinox). This is known as the computus."),
      ("What is Good Friday?", "Good Friday falls two days before Easter Sunday and marks the crucifixion of Jesus Christ. It is a public holiday in many countries."),
      ("What is Holy Week?", "Holy Week is the week leading up to Easter Sunday, beginning with Palm Sunday and including Maundy Thursday, Good Friday, and Holy Saturday."),
    ]
  ),
  dict(
    slug="mothers-day", name="Mother's Day", type="auto", category="Holidays",
    seo_title="Mother's Day Countdown 2027 — Days Until Mother's Day",
    meta_desc="Live countdown to Mother's Day. Select your country — date varies by region. US, UK, Mexico, Argentina, France and more.",
    hero_desc="Countdown to Mother's Day. Date varies by country.",
    content="Mother's Day is celebrated on different dates around the world. The US, Canada, Australia and Brazil observe it on the second Sunday of May. The UK celebrates Mothering Sunday on the fourth Sunday of Lent (usually in March). Mexico always celebrates on May 10. Argentina marks it on the third Sunday of October. France holds it on the last Sunday of May. Use the selector below to find the date for your country.",
    faqs=[
      ("When is Mother's Day 2027 in the US?", "Mother's Day 2027 in the US, Canada and Australia falls on Sunday, May 9, 2027 (second Sunday of May)."),
      ("When is Mother's Day in Mexico?", "Mexico always celebrates Mother's Day on May 10, regardless of the day of the week."),
      ("When is Mother's Day in Argentina?", "Argentina celebrates Mother's Day on the third Sunday of October. In 2026 it falls on October 18; in 2027 on October 17."),
      ("When is Mothering Sunday in the UK?", "The UK observes Mothering Sunday on the fourth Sunday of Lent, which varies each year. In 2027 it falls on March 7."),
      ("Why is Mother's Day on different dates in different countries?", "Each country independently adopted the holiday at different times and chose a date tied to local tradition, religious calendars, or historic events."),
    ],
    country_variants=[
      {"code": "us",  "label": "US, Canada & Australia", "dates": ["2026-05-10", "2027-05-09"]},
      {"code": "uk",  "label": "United Kingdom",         "dates": ["2026-03-15", "2027-03-07"]},
      {"code": "mx",  "label": "Mexico",                 "dates": ["2026-05-10", "2027-05-10"]},
      {"code": "ar",  "label": "Argentina",              "dates": ["2026-10-18", "2027-10-17"]},
      {"code": "fr",  "label": "France",                 "dates": ["2026-05-31", "2027-05-30"]},
      {"code": "br",  "label": "Brazil",                 "dates": ["2026-05-10", "2027-05-09"]},
    ]
  ),
  dict(
    slug="fathers-day", name="Father's Day", type="auto", category="Holidays",
    seo_title="Father's Day Countdown 2026 — Days Until Father's Day",
    meta_desc="Live countdown to Father's Day. Select your country — date varies by region. US, Australia, Germany, Brazil and more.",
    hero_desc="Countdown to Father's Day. Date varies by country.",
    content="Father's Day is celebrated on different dates around the world. The US, Canada, UK and Mexico observe it on the third Sunday of June. Australia and New Zealand celebrate on the first Sunday of September. Germany and Austria mark it on Ascension Thursday (39 days after Easter). Brazil celebrates on the second Sunday of August. Select your country below to see the countdown for your region.",
    faqs=[
      ("When is Father's Day 2026 in the US?", "Father's Day 2026 in the US, Canada, UK and Mexico falls on Sunday, June 21, 2026 (third Sunday of June)."),
      ("When is Father's Day in Australia?", "Australia and New Zealand celebrate Father's Day on the first Sunday of September. In 2026 that is September 6."),
      ("When is Father's Day in Germany?", "Germany and Austria celebrate Father's Day on Ascension Thursday, 39 days after Easter. In 2026 that falls on May 14."),
      ("When is Father's Day in Brazil?", "Brazil celebrates Father's Day on the second Sunday of August. In 2026 that is August 9."),
      ("Why is Father's Day on different dates?", "Countries independently adopted the holiday and chose dates tied to local traditions. The US date (3rd Sunday of June) is the most widely followed internationally."),
    ],
    country_variants=[
      {"code": "us",  "label": "US, Canada, UK & Mexico", "dates": ["2026-06-21", "2027-06-20"]},
      {"code": "au",  "label": "Australia & New Zealand",  "dates": ["2026-09-06", "2027-09-05"]},
      {"code": "de",  "label": "Germany & Austria",        "dates": ["2026-05-14", "2027-05-06"]},
      {"code": "br",  "label": "Brazil",                   "dates": ["2026-08-09", "2027-08-08"]},
    ]
  ),
  dict(
    slug="thanksgiving", name="Thanksgiving", type="auto", category="Holidays",
    seo_title="Thanksgiving Countdown 2026 — Days Until Thanksgiving",
    meta_desc="Live countdown to Thanksgiving 2026. US Thanksgiving falls on the fourth Thursday of November.",
    hero_desc="Countdown to Thanksgiving — fourth Thursday of November.",
    content="Thanksgiving is a national holiday in the United States celebrated on the fourth Thursday of November. It is one of the most travelled holidays in the US, marked by large family gatherings, a traditional turkey meal and the start of the holiday shopping season.",
    faqs=[
      ("When is Thanksgiving 2026?", "Thanksgiving 2026 falls on Thursday, November 26, 2026."),
      ("When is Black Friday 2026?", "Black Friday always falls the day after Thanksgiving — November 27, 2026."),
      ("Is Thanksgiving a national holiday?", "Yes, Thanksgiving is a federal holiday in the United States. Canada also celebrates Thanksgiving, but on the second Monday of October."),
      ("When is Canadian Thanksgiving 2026?", "Canadian Thanksgiving 2026 falls on Monday, October 12, 2026 (second Monday of October)."),
      ("What is the traditional Thanksgiving meal?", "The traditional US Thanksgiving meal typically includes roast turkey, stuffing, mashed potatoes, cranberry sauce, green bean casserole, and pumpkin pie."),
    ]
  ),
  dict(
    slug="independence-day", name="Independence Day", type="auto", category="Holidays",
    seo_title="Independence Day Countdown 2026 — Days Until July 4th",
    meta_desc="Live countdown to US Independence Day 2026, July 4. How many days until the 4th of July fireworks?",
    hero_desc="Countdown to US Independence Day — July 4.",
    content="Independence Day, commonly known as the Fourth of July, is a federal holiday in the United States commemorating the Declaration of Independence on July 4, 1776. Celebrations include fireworks, parades, barbecues and concerts across the country.",
    faqs=[
      ("When is Independence Day 2026?", "Independence Day 2026 is on Saturday, July 4, 2026."),
      ("What day of the week is July 4, 2026?", "July 4, 2026 falls on a Saturday."),
      ("Why is Independence Day on July 4?", "The Continental Congress voted for independence on July 2, 1776, and the Declaration of Independence was formally adopted on July 4, 1776."),
    ]
  ),
  dict(
    slug="memorial-day", name="Memorial Day", type="auto", category="Holidays",
    seo_title="Memorial Day Countdown 2027 — Days Until Memorial Day",
    meta_desc="Live countdown to Memorial Day 2027. Memorial Day is the last Monday of May and marks the unofficial start of summer in the US.",
    hero_desc="Countdown to Memorial Day — last Monday of May.",
    content="Memorial Day is a United States federal holiday observed on the last Monday of May. It honours military personnel who have died in service. It is also widely regarded as the unofficial start of the summer season.",
    faqs=[
      ("When is Memorial Day 2027?", "Memorial Day 2027 falls on Monday, May 31, 2027."),
      ("When is Memorial Day 2026?", "Memorial Day 2026 falls on Monday, May 25, 2026 (last Monday of May)."),
      ("Is Memorial Day a federal holiday?", "Yes, Memorial Day is a federal holiday in the US. Banks, government offices and many businesses are closed."),
      ("What is the difference between Memorial Day and Veterans Day?", "Memorial Day (last Monday of May) honours military personnel who died in service. Veterans Day (November 11) honours all military veterans, living and deceased."),
      ("Does Memorial Day mark the start of summer?", "Yes. Memorial Day weekend is widely considered the unofficial start of summer in the United States, with many people opening pools and taking road trips."),
    ]
  ),
  dict(
    slug="labor-day", name="Labor Day", type="auto", category="Holidays",
    seo_title="Labor Day Countdown 2026 — Days Until Labor Day",
    meta_desc="Live countdown to Labor Day 2026. US Labor Day is the first Monday of September, marking the end of summer.",
    hero_desc="Countdown to US Labor Day — first Monday of September.",
    content="Labor Day in the United States and Canada is celebrated on the first Monday of September. It honors the labour movement and the contributions of workers. In the US, it also marks the unofficial end of summer.",
    faqs=[
      ("When is Labor Day 2026?", "Labor Day 2026 falls on Monday, September 7, 2026."),
      ("Is Labor Day the same as International Workers' Day?", "No. International Workers' Day (May Day) is May 1. US/Canada Labor Day is the first Monday of September."),
      ("Is Labor Day a federal holiday?", "Yes, Labor Day is a federal holiday in both the United States and Canada. Most businesses, schools and government offices are closed."),
      ("Does Labor Day mark the end of summer?", "Yes. Labor Day weekend is considered the unofficial end of summer in the US, and many schools resume in the days following it."),
    ]
  ),
  dict(
    slug="st-patricks", name="St. Patrick's Day", type="auto", category="Holidays",
    seo_title="St. Patrick's Day Countdown 2027 — Days Until March 17",
    meta_desc="Live countdown to St. Patrick's Day 2027, March 17. The Irish cultural holiday celebrated worldwide with parades, green beer and festivities.",
    hero_desc="Countdown to St. Patrick's Day — March 17.",
    content="St. Patrick's Day is a cultural and religious celebration held on March 17, the traditional death date of Saint Patrick, the patron saint of Ireland. It is a public holiday in Ireland and celebrated worldwide with parades, wearing of green, and Irish music and food.",
    faqs=[
      ("When is St. Patrick's Day 2027?", "St. Patrick's Day 2027 falls on Wednesday, March 17, 2027."),
      ("When is St. Patrick's Day 2026?", "St. Patrick's Day 2026 falls on Tuesday, March 17, 2026."),
      ("Where is the biggest St. Patrick's Day parade?", "New York City hosts one of the world's largest St. Patrick's Day parades, drawing millions of spectators along Fifth Avenue. Dublin also holds a major parade."),
      ("Is St. Patrick's Day a public holiday?", "St. Patrick's Day is a public holiday in the Republic of Ireland and Northern Ireland. It is a cultural observance (not a public holiday) in the US, Canada and Australia."),
      ("What colour is associated with St. Patrick's Day?", "Green is the iconic colour, symbolising Ireland's lush landscape. People around the world wear green and buildings are illuminated in green light on March 17."),
    ]
  ),
  dict(
    slug="dia-de-los-muertos", name="Día de los Muertos", type="auto", category="Holidays",
    seo_title="Día de los Muertos Countdown 2026 — Days Until Day of the Dead",
    meta_desc="Live countdown to Día de los Muertos 2026, celebrated November 1–2 in Mexico and Latin America.",
    hero_desc="Countdown to Día de los Muertos — November 1.",
    content="Día de los Muertos (Day of the Dead) is a Mexican and Latin American holiday celebrated on November 1–2, coinciding with the Catholic holy days of All Saints' Day and All Souls' Day. It honours deceased loved ones with colourful altars, marigolds, skull imagery and celebrations.",
    faqs=[
      ("When is Día de los Muertos 2026?", "Día de los Muertos is celebrated November 1–2, 2026."),
      ("Is Día de los Muertos the same as Halloween?", "No. While they fall close together, Día de los Muertos is a distinct Mexican tradition honouring deceased loved ones through colour, food and altars — not a horror celebration."),
      ("What is an ofrenda?", "An ofrenda is a colourful altar built during Día de los Muertos to honour deceased loved ones. It typically holds photos, marigolds, candles, food and personal mementos."),
      ("Why are marigolds associated with Día de los Muertos?", "Marigolds (cempasúchil) are believed to guide the spirits of the dead back to the living world with their bright colour and strong scent."),
      ("Is Día de los Muertos celebrated outside Mexico?", "Yes. The holiday is celebrated in many Latin American countries and has grown in popularity worldwide, especially in the US and Central America."),
    ]
  ),
  dict(
    slug="cinco-de-mayo", name="Cinco de Mayo", type="auto", category="Holidays",
    seo_title="Cinco de Mayo Countdown 2027 — Days Until May 5",
    meta_desc="Live countdown to Cinco de Mayo 2027. The Mexican holiday celebrated on May 5 commemorating the Battle of Puebla in 1862.",
    hero_desc="Countdown to Cinco de Mayo — May 5.",
    content="Cinco de Mayo commemorates the Mexican army's victory over French forces at the Battle of Puebla on May 5, 1862. While it is a minor holiday in Mexico, it is widely celebrated in the United States as a celebration of Mexican-American culture.",
    faqs=[
      ("When is Cinco de Mayo 2027?", "Cinco de Mayo 2027 falls on Tuesday, May 5, 2027."),
      ("Is Cinco de Mayo Mexican Independence Day?", "No. Mexican Independence Day is September 16. Cinco de Mayo commemorates the Mexican army's victory at the Battle of Puebla on May 5, 1862."),
      ("Is Cinco de Mayo a national holiday in Mexico?", "Cinco de Mayo is a regional holiday mainly observed in the state of Puebla, Mexico. It is not a federal public holiday. It is much more widely celebrated in the United States."),
      ("Why is Cinco de Mayo celebrated in the US?", "Cinco de Mayo became a celebration of Mexican-American culture and heritage in the US, popularised from the 1960s onward, particularly in states with large Mexican-American communities."),
    ]
  ),
  dict(
    slug="fiestas-patrias", name="Fiestas Patrias Chile", type="auto", category="Holidays",
    seo_title="Fiestas Patrias Chile 2026 Countdown — Days Until September 18",
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
    seo_title="Bastille Day Countdown 2026 — Days Until July 14 (Fête Nationale)",
    meta_desc="Live countdown to Bastille Day 2026. The French national holiday on July 14 marks the storming of the Bastille in 1789.",
    hero_desc="Countdown to Bastille Day — French National Holiday, July 14.",
    content="Bastille Day (La Fête Nationale) is France's national holiday, celebrated on July 14 to commemorate the Storming of the Bastille on July 14, 1789, a pivotal moment in the French Revolution. Celebrations include the military parade on the Champs-Élysées and a fireworks display at the Eiffel Tower.",
    faqs=[
      ("When is Bastille Day 2026?", "Bastille Day 2026 falls on Tuesday, July 14, 2026."),
      ("What happens on Bastille Day?", "France celebrates with a military parade on the Champs-Élysées in Paris, a fireworks display at the Eiffel Tower, and balls and celebrations across the country."),
      ("What is the Storming of the Bastille?", "On July 14, 1789, Parisian revolutionaries stormed the Bastille prison, a symbol of royal tyranny. The event marked a turning point in the French Revolution."),
      ("Is Bastille Day a public holiday?", "Yes. July 14 is a national public holiday in France. Businesses, schools and government offices are closed."),
      ("Why is Bastille Day important outside France?", "Bastille Day is seen globally as a symbol of the ideals of the French Revolution — liberty, equality and fraternity — making it one of the most recognised national holidays in the world."),
    ]
  ),
  dict(
    slug="oktoberfest", name="Oktoberfest", type="auto", category="Holidays",
    seo_title="Oktoberfest 2026 Countdown — Days Until Munich Oktoberfest",
    meta_desc="Live countdown to Oktoberfest 2026 in Munich. The world's largest beer festival runs from late September through early October.",
    hero_desc="Countdown to Oktoberfest 2026 — Munich.",
    content="Oktoberfest is the world's largest folk festival, held annually in Munich, Bavaria. The festival begins on a Saturday in late September and runs for 16–18 days, ending on the first Sunday of October. It attracts around 6 million visitors each year.",
    faqs=[
      ("When is Oktoberfest 2026?", "Oktoberfest 2026 begins on Saturday, September 19, 2026, and runs until October 4, 2026."),
      ("Where is Oktoberfest held?", "Oktoberfest takes place at the Theresienwiese fairgrounds (known as the Wiesn) in Munich, Bavaria, Germany."),
      ("How many people attend Oktoberfest?", "Oktoberfest draws around 6 million visitors each year, making it the world's largest beer festival and folk event."),
      ("What is the most popular Oktoberfest tent?", "The Hofbräu-Festzelt (Hofbräu tent) is among the most famous. There are 17 large tents and 21 smaller ones, each run by a different Munich brewery."),
      ("Do I need reservations for Oktoberfest?", "Reservations are strongly recommended for the beer tents, especially on weekends. Many tables are booked months in advance by corporate groups and tour operators."),
    ]
  ),

  # ── Entertainment – Global ─────────────────────────────────────────────
  dict(
    slug="oscars", name="Oscars", type="auto", category="Entertainment",
    seo_title="Oscars 2027 Countdown — Days Until the Academy Awards",
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
    seo_title="Grammy Awards 2027 Countdown — Days Until the Grammys",
    meta_desc="Live countdown to the Grammy Awards 2027. Music's biggest night — date TBA, usually held in January or February.",
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
    seo_title="Met Gala 2027 Countdown — Days Until the Met Gala",
    meta_desc="Live countdown to the Met Gala 2027. Fashion's biggest night is held on the first Monday of May at the Metropolitan Museum of Art.",
    hero_desc="Countdown to the Met Gala — first Monday of May.",
    content="The Met Gala (formally the Costume Institute Benefit) is an annual fundraising gala for the Metropolitan Museum of Art's Costume Institute in New York City. Held on the first Monday of May, it is fashion's most glamorous and star-studded event of the year.",
    faqs=[
      ("When is the Met Gala 2027?", "The Met Gala 2027 is on Monday, May 3, 2027 (first Monday of May)."),
      ("Who hosts the Met Gala?", "The Met Gala is chaired by Vogue editor-in-chief Anna Wintour, along with celebrity co-chairs who change each year."),
      ("Can anyone attend the Met Gala?", "Attendance is invitation-only. Tables are sold to fashion houses and corporations, with individual tickets reportedly costing $75,000+."),
    ]
  ),
  dict(
    slug="eurovision", name="Eurovision Song Contest", type="variable", category="Entertainment",
    seo_title="Eurovision 2027 Countdown — Days Until the Eurovision Song Contest",
    meta_desc="Live countdown to Eurovision Song Contest 2027. The Grand Final is held in May each year and is watched by over 160 million viewers.",
    hero_desc="Countdown to the Eurovision Song Contest 2027.",
    content="The Eurovision Song Contest is Europe's (and the world's) biggest live music event, with over 160 million viewers tuning in annually. Held each May, it features competing songs from dozens of countries across Europe and beyond, with a combination of public and jury voting.",
    faqs=[
      ("When is Eurovision 2027?", "The Eurovision 2027 Grand Final is estimated for Saturday, May 15, 2027. The exact date depends on the host country."),
      ("Who can participate in Eurovision?", "Any member country of the European Broadcasting Union (EBU) can participate, including non-European countries like Australia, Israel and Armenia."),
      ("How does Eurovision voting work?", "Each country awards points through a combination of national jury votes and public televote. 12 points goes to the favourite (douze points!)."),
    ]
  ),
  dict(
    slug="cannes", name="Cannes Film Festival", type="variable", category="Entertainment",
    seo_title="Cannes Film Festival 2026 Countdown — Days Until Cannes",
    meta_desc="Live countdown to the 2026 Cannes Film Festival. The Palme d'Or competition opens May 13, 2026 on the French Riviera.",
    hero_desc="Countdown to the 2026 Cannes Film Festival.",
    content="The Cannes Film Festival is one of the world's most prestigious and publicised film festivals. Held annually in Cannes, France on the French Riviera, it presents and promotes films from around the world. The top prize, the Palme d'Or, is among the most coveted awards in cinema.",
    faqs=[
      ("When is the Cannes Film Festival 2026?", "Cannes 2026 opens on May 13, 2026 and runs through May 24."),
      ("Where is the Cannes Film Festival?", "The festival is held at the Palais des Festivals et des Congrès in Cannes, on the French Riviera."),
      ("What is the Palme d'Or?", "The Palme d'Or is the highest prize awarded at Cannes, given to the best film in the main competition."),
    ]
  ),
  dict(
    slug="coachella", name="Coachella", type="variable", category="Entertainment",
    seo_title="Coachella 2027 Countdown — Days Until Coachella Valley Music Festival",
    meta_desc="Live countdown to Coachella 2027. The world's most famous music festival takes place in the California desert each April.",
    hero_desc="Countdown to Coachella 2027.",
    content="The Coachella Valley Music and Arts Festival is held annually at the Empire Polo Club in Indio, California. It is one of the largest and most famous music festivals in the world, featuring top artists across two weekends in April.",
    faqs=[
      ("When is Coachella 2027?", "Coachella 2027 Weekend 1 is estimated for April 9–11, 2027. Official dates are typically announced in late 2026."),
      ("Where is Coachella held?", "Coachella takes place at the Empire Polo Club in Indio, California, in the Coachella Valley desert."),
      ("How do I get Coachella tickets?", "Tickets go on sale on coachella.com, often selling out within hours. Passes include camping and shuttle options."),
    ]
  ),

  # ── Sales ──────────────────────────────────────────────────────────────
  dict(
    slug="black-friday", name="Black Friday", type="auto", category="Sales",
    seo_title="Black Friday 2026 Countdown — Days Until Black Friday",
    meta_desc="How many days until Black Friday 2026? Live countdown to the biggest shopping day of the year, the fourth Friday of November.",
    hero_desc="Countdown to Black Friday — fourth Friday of November.",
    content="Black Friday is the Friday after Thanksgiving in the United States and has become the unofficial start of the Christmas shopping season. Retailers offer steep discounts, and the day has expanded globally with online deals that now extend over an entire week.",
    faqs=[
      ("When is Black Friday 2026?", "Black Friday 2026 falls on Friday, November 27, 2026."),
      ("When does Black Friday start?", "Many retailers now start Black Friday deals a week early online. The main in-store event is always the Friday after US Thanksgiving."),
      ("When is Cyber Monday 2026?", "Cyber Monday 2026 is on Monday, November 30, 2026 — three days after Black Friday."),
      ("Is Black Friday only in the US?", "No. Black Friday has spread globally and is now a major shopping event in the UK, Canada, Australia, Brazil, and most of Europe."),
      ("What are the best Black Friday deals?", "Electronics, appliances, clothing, toys and travel tend to offer the deepest discounts on Black Friday, both in-store and online."),
    ]
  ),
  dict(
    slug="cyber-monday", name="Cyber Monday", type="auto", category="Sales",
    seo_title="Cyber Monday 2026 Countdown — Days Until Cyber Monday",
    meta_desc="Live countdown to Cyber Monday 2026. The biggest online shopping day of the year falls on the Monday after Black Friday.",
    hero_desc="Countdown to Cyber Monday — the biggest online shopping day.",
    content="Cyber Monday is an online shopping holiday created by retailers in 2005 to encourage people to shop online. It falls on the Monday after US Thanksgiving (three days after Black Friday) and has grown into the biggest online shopping day of the year globally.",
    faqs=[
      ("When is Cyber Monday 2026?", "Cyber Monday 2026 is on Monday, November 30, 2026."),
      ("Is Cyber Monday better than Black Friday?", "Both offer major deals. Cyber Monday focuses on online shopping and tech, while Black Friday traditionally includes both in-store and online offers. Many retailers now offer deals across the full Cyber Week."),
      ("What are the best Cyber Monday deals?", "Electronics, software, streaming services, laptops, and gaming gear typically see the deepest Cyber Monday discounts."),
      ("Is Cyber Monday only in the US?", "Originally a US event, Cyber Monday is now observed globally in the UK, Canada, Australia, and Latin America."),
    ]
  ),
  dict(
    slug="hot-sale", name="Hot Sale", type="variable", category="Sales",
    seo_title="Hot Sale Argentina 2027 Countdown — Cuántos días faltan para el Hot Sale",
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

  # ── Nature ─────────────────────────────────────────────────────────────
  dict(
    slug="full-moon", name="Next Full Moon", type="auto", category="Nature",
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

  # ── Music – ES ────────────────────────────────────────────────────────
  dict(
    slug="lollapalooza-ar", name="Lollapalooza Argentina", type="variable", category="Music",
    seo_title="Lollapalooza Argentina 2027 Countdown — Cuántos días faltan",
    meta_desc="Cuenta regresiva en vivo para el Lollapalooza Argentina 2027 en el Hipódromo de San Isidro, Buenos Aires.",
    hero_desc="Countdown to Lollapalooza Argentina 2027.",
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
    seo_title="Lollapalooza Chile 2027 Countdown — Cuántos días faltan",
    meta_desc="Cuenta regresiva en vivo para el Lollapalooza Chile 2027 en el Parque Bicentenario Cerrillos, Santiago.",
    hero_desc="Countdown to Lollapalooza Chile 2027.",
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
    seo_title="Cosquín Rock 2027 Countdown — Cuántos días faltan",
    meta_desc="Cuenta regresiva en vivo para el Cosquín Rock 2027 en Santa María de Punilla, Córdoba.",
    hero_desc="Countdown to Cosquín Rock 2027.",
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
    seo_title="Rock in Rio Lisboa 2026 Countdown — Days Until Rock in Rio",
    meta_desc="Live countdown to Rock in Rio Lisboa 2026 at Parque da Bela Vista, Lisbon. Starts September 18, 2026.",
    hero_desc="Countdown to Rock in Rio Lisboa 2026.",
    content="Rock in Rio Lisboa is one of the world's largest music festivals, held at Parque da Bela Vista in Lisbon, Portugal. The 2026 edition starts on September 18 and features international headliners across multiple stages.",
    faqs=[
      ("When is Rock in Rio Lisboa 2026?", "Rock in Rio Lisboa 2026 starts on September 18, 2026 at Parque da Bela Vista, Lisbon."),
      ("How do I get Rock in Rio Lisboa tickets?", "Tickets (called Passports) are available at the official Rock in Rio Lisboa website. They often sell out within hours of going on sale."),
      ("How many days does Rock in Rio Lisboa last?", "Rock in Rio Lisboa typically runs over two consecutive weekends — 4 days of concerts spread across 8 days."),
      ("What stages does Rock in Rio Lisboa have?", "The main stage is the Palco Mundo (World Stage). Other stages include the Palco NOS and several smaller themed stages throughout the Cidade do Rock."),
    ]
  ),

  # ── Fashion ───────────────────────────────────────────────────────────
  dict(
    slug="nyfw", name="New York Fashion Week", type="variable", category="Fashion",
    seo_title="New York Fashion Week 2026 Countdown — Days Until NYFW",
    meta_desc="Live countdown to New York Fashion Week September 2026 (Spring/Summer 2027 collections).",
    hero_desc="Countdown to New York Fashion Week — September 2026.",
    content="New York Fashion Week (NYFW) is held twice a year in New York City — in February (for Fall/Winter collections) and September (for Spring/Summer collections). It is the first of the four major fashion weeks, followed by London, Milan and Paris.",
    faqs=[
      ("When is New York Fashion Week 2026?", "NYFW September 2026 starts on September 8, 2026 (Spring/Summer 2027 collections)."),
      ("Can I attend NYFW?", "NYFW shows are primarily industry-only events (buyers, press, stylists). Some designers hold open presentations or pop-up events — check nyfw.com for public programming."),
      ("How long does New York Fashion Week last?", "NYFW typically runs for about 7–9 days. It is held twice a year: February (Fall/Winter) and September (Spring/Summer)."),
      ("What is the order of the Big Four fashion weeks?", "The Big Four run in order: New York → London → Milan → Paris. The September season typically starts in early September and ends in late October."),
    ]
  ),
  dict(
    slug="paris-fw", name="Paris Fashion Week", type="variable", category="Fashion",
    seo_title="Paris Fashion Week 2026 Countdown — Days Until PFW",
    meta_desc="Live countdown to Paris Fashion Week September 2026 — the final and most glamorous of the Big Four fashion weeks.",
    hero_desc="Countdown to Paris Fashion Week — September 2026.",
    content="Paris Fashion Week closes the Big Four fashion weeks season. The September edition (Spring/Summer 2027 collections) features shows from Chanel, Dior, Louis Vuitton, Saint Laurent and more iconic French and international houses.",
    faqs=[
      ("When is Paris Fashion Week 2026?", "Paris Fashion Week September 2026 starts on September 28, 2026 (Spring/Summer 2027 collections)."),
      ("What is the order of the Big Four Fashion Weeks?", "The Big Four run in order: New York (Sep 8) → London → Milan (Sep 16) → Paris (Sep 28)."),
      ("What brands show at Paris Fashion Week?", "Paris Fashion Week features shows from Chanel, Dior, Louis Vuitton, Balenciaga, Givenchy, Saint Laurent, Valentino and many other iconic houses."),
      ("Is Paris Fashion Week open to the public?", "Most runway shows are strictly invitation-only. However, some brands hold exhibitions, presentations and pop-up events open to a wider audience."),
    ]
  ),
  dict(
    slug="milan-fw", name="Milan Fashion Week", type="variable", category="Fashion",
    seo_title="Milan Fashion Week 2026 Countdown — Days Until MFW",
    meta_desc="Live countdown to Milan Fashion Week September 2026, featuring Prada, Gucci, Versace, Armani and more.",
    hero_desc="Countdown to Milan Fashion Week — September 2026.",
    content="Milan Fashion Week is the third of the Big Four fashion weeks, held in September for Spring/Summer collections and February for Fall/Winter. The September 2026 edition features runway shows from Prada, Gucci, Versace, Bottega Veneta and many other iconic Italian houses.",
    faqs=[
      ("When is Milan Fashion Week 2026?", "Milan Fashion Week September 2026 starts on September 16, 2026 (Spring/Summer 2027 collections)."),
      ("What brands show at Milan Fashion Week?", "Milan Fashion Week features shows from Prada, Gucci, Versace, Armani, Dolce & Gabbana, Bottega Veneta, Fendi and many other Italian and international houses."),
      ("How long does Milan Fashion Week last?", "Milan Fashion Week typically runs for about 7–8 days, with multiple shows each day across the city."),
      ("Is Milan Fashion Week open to the public?", "Most runway shows are invitation-only for buyers, press and VIPs. Some brands also hold open exhibitions or public events during the week."),
    ]
  ),
  dict(
    slug="bafweek", name="Buenos Aires Fashion Week", type="variable", category="Fashion",
    seo_title="Buenos Aires Fashion Week 2026 Countdown — Cuántos días faltan",
    meta_desc="Cuenta regresiva en vivo para el Buenos Aires Fashion Week 2026, la semana de la moda más importante de Argentina.",
    hero_desc="Countdown to Buenos Aires Fashion Week 2026.",
    content="Buenos Aires Fashion Week (BAFWeek) is Argentina's premier fashion week, held twice a year showcasing the best of Argentine and Latin American fashion design. The Spring/Summer edition takes place in October at various venues across Buenos Aires.",
    faqs=[
      ("¿Cuándo es el BAFWeek 2026?", "El Buenos Aires Fashion Week edición primavera-verano 2026 está estimado para octubre de 2026."),
      ("¿Dónde se realiza el BAFWeek?", "El BAFWeek se realiza en distintas sedes de Buenos Aires, incluyendo el Centro Metropolitano de Diseño y otros espacios culturales de la ciudad."),
      ("¿Se puede asistir al BAFWeek sin invitación?", "Algunos desfiles y presentaciones del BAFWeek son abiertos al público. Consultá la web oficial y las redes del evento para acceder a entradas o acreditaciones."),
      ("¿Quiénes participan en el BAFWeek?", "Participan los principales diseñadores y marcas de moda argentina, además de marcas regionales latinoamericanas invitadas."),
    ]
  ),

  # ── Politics ──────────────────────────────────────────────────────────
  dict(
    slug="elecciones-ar", name="Argentine Elections 2027", type="auto", category="Politics",
    seo_title="Argentine Elections 2027 Countdown — Días para las Elecciones",
    meta_desc="Cuenta regresiva para las Elecciones Generales Argentina 2027, estimadas para el 26 de octubre de 2027.",
    hero_desc="Countdown to the Argentine General Elections 2027.",
    content="Argentina celebrará elecciones generales en octubre de 2027, cuando se renovará la composición del Congreso Nacional y se elegirá al próximo presidente y vicepresidente de la Nación para el período 2027–2031.",
    faqs=[
      ("¿Cuándo son las elecciones en Argentina 2027?", "Las elecciones generales Argentina 2027 están estimadas para el 26 de octubre de 2027."),
      ("¿Qué se vota en las elecciones 2027?", "Se elige presidente, vicepresidente, y se renuevan parcialmente los cargos legislativos nacionales (diputados y senadores)."),
      ("¿Habrá PASO en 2027?", "Las Primarias Abiertas Simultáneas y Obligatorias (PASO) suelen celebrarse aproximadamente dos meses antes de las elecciones generales, en agosto de 2027."),
      ("¿Quiénes pueden votar en Argentina?", "Pueden votar los ciudadanos argentinos nativos o naturalizados mayores de 16 años. El voto es obligatorio para los mayores de 18 y optativo para los de 16 y 17 años."),
    ]
  ),
]

# ─── HTML template ─────────────────────────────────────────────────────────

def faq_json_ld(slug, name, faqs):
    items = []
    for q, a in faqs:
        items.append(f'''    {{
      "@type": "Question",
      "name": "{q.replace('"', '&quot;')}",
      "acceptedAnswer": {{ "@type": "Answer", "text": "{a.replace('"', '&quot;')}" }}
    }}''')
    return "[\n" + ",\n".join(items) + "\n  ]"

def faq_html(faqs):
    if not faqs:
        return ""
    items = "".join(
        f'<div class="cd-faq-item"><h3 class="cd-faq-q">{q}</h3><p class="cd-faq-a">{a}</p></div>'
        for q, a in faqs
    )
    return f'''<div class="cd-article">
  <p class="cd-article-body">{{}}</p>
  <div class="cd-faq"><h2 class="cd-faq-title">Frequently Asked Questions</h2>{items}</div>
</div>'''

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
}

def generate_page(ev):
    slug       = ev["slug"]
    name       = ev["name"]
    ev_type    = ev["type"]
    category   = ev["category"]
    seo_title  = ev["seo_title"]
    meta_desc  = ev["meta_desc"]
    hero_desc  = ev["hero_desc"]
    content    = ev.get("content", "")
    faqs       = ev.get("faqs", [])
    cat_color, cat_glow, cat_soft = CAT_COLORS.get(category, ('#818CF8','rgba(129,140,248,.2)','rgba(129,140,248,.08)'))

    faq_items_html = "".join(
        f'<div class="cd-faq-item"><h3 class="cd-faq-q">{q}</h3><p class="cd-faq-a">{a}</p></div>'
        for q, a in faqs
    )
    faq_section = f'''<div class="cd-article">
  <p class="cd-article-body">{content}</p>
  <div class="cd-faq"><h2 class="cd-faq-title">Frequently Asked Questions</h2>{faq_items_html}</div>
</div>''' if (content or faqs) else ""

    faq_json = faq_json_ld(slug, name, faqs) if faqs else "[]"
    country_variants = ev.get("country_variants", [])

    # ── country picker HTML + render script ───────────────────────
    if country_variants:
        cv_js = json.dumps([{"code": v["code"], "label": v["label"], "dates": v["dates"]} for v in country_variants])
        country_picker_html = f'''<div class="cd-country-picker">
  <p class="cd-cpicker-label">Date varies by country — select yours:</p>
  <div class="cd-cpicker-grid" id="cd-cpicker-grid"></div>
</div>'''
        render_script = f'''(function() {{
  var VARIANTS = {cv_js};
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
  var grid = document.getElementById('cd-cpicker-grid');
  VARIANTS.forEach(function(v, idx) {{
    var btn = document.createElement('button');
    btn.className = 'cd-cpicker-btn' + (idx === 0 ? ' active' : '');
    btn.textContent = v.label;
    btn.onclick = function() {{
      document.querySelectorAll('.cd-cpicker-btn').forEach(function(b) {{ b.classList.remove('active'); }});
      btn.classList.add('active');
      CountdownEngine.render('root', Object.assign({{}}, _cfg, {{ date: nextDate(v.dates) }}));
    }};
    grid.appendChild(btn);
  }});
  CountdownEngine.render('root', Object.assign({{}}, _cfg, {{ date: nextDate(VARIANTS[0].dates) }}));
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
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{seo_title} | countdowns.site</title>
<meta name="description" content="{meta_desc}">
<meta name="robots" content="index, follow">
<link rel="canonical" href="{BASE_URL}/countdown/{slug}/">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<meta property="og:type" content="website">
<meta property="og:url" content="{BASE_URL}/countdown/{slug}/">
<meta property="og:title" content="{seo_title}">
<meta property="og:description" content="{meta_desc}">
<link rel="alternate" hreflang="en" href="{BASE_URL}/countdown/{slug}/">
<link rel="alternate" hreflang="x-default" href="{BASE_URL}/countdown/{slug}/">
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/countdown.css">
<style>:root{{--cat-color:{cat_color};--cat-glow:{cat_glow};--cat-soft:{cat_soft};}}</style>
<script>if(localStorage.getItem('cd_theme')==='light')document.documentElement.setAttribute('data-theme','light');</script>
<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@graph": [
    {{
      "@type": "WebPage",
      "@id": "{BASE_URL}/countdown/{slug}/#webpage",
      "url": "{BASE_URL}/countdown/{slug}/",
      "name": "{seo_title}",
      "description": "{meta_desc}",
      "inLanguage": "en"
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
    <button class="theme-btn" id="theme-toggle">Light</button>
    <div class="lang-seg" role="group" aria-label="Language">
      <button class="lang-btn active">EN</button>
      <button class="lang-btn" onclick="location.href='/es/'">ES</button>
      <button class="lang-btn" onclick="location.href='/pt/'">PT</button>
      <button class="lang-btn" onclick="location.href='/fr/'">FR</button>
    </div>
  </div>
</header>
<div id="root"><div style="min-height:100vh;background:#080812"></div></div>
{country_picker_html}
{faq_section}
<footer class="site-footer">
  countdowns<span class="logo-tld">.site</span>
</footer>
<script src="/countdown-engine.js"></script>
<script>
{render_script}
// ── Theme toggle ──────────────────────────────────────────────
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
</script>
</body>
</html>'''

# ─── Generate files ────────────────────────────────────────────────────────

generated = 0
for ev in EVENTS:
    slug = ev["slug"]
    out_dir = os.path.join("countdown", slug)
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "index.html")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(generate_page(ev))
    generated += 1
    print(f"  ✓  /countdown/{slug}/")

print(f"\nGenerated {generated} pages.")
