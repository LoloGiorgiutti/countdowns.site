"""
Rich premium content for top-20 countdown pages.
Injected into English pages only when slug matches.
Structure per entry:
  overview  – list of HTML paragraph strings
  key_info  – list of (label, value) tuples
  timeline  – list of (year_label, description) tuples
  facts     – list of fact strings
  faqs      – list of (question, answer) tuples  (replaces default faqs)
  related   – list of slugs
"""

RICH_CONTENT = {

  # ─── CHRISTMAS ────────────────────────────────────────────────────────────────
  "christmas": {
    "overview": [
      "Christmas is the most widely celebrated holiday on Earth, observed by more than two billion people across over 160 countries. Held every year on December 25, it commemorates the birth of Jesus Christ for Christians and has grown into a global cultural and commercial season embraced by people of all backgrounds. The weeks leading up to the day — known as the Christmas season or Advent — are marked by decorating homes and trees, exchanging gifts, listening to carols, and gathering with family.",
      "The modern Christmas we recognise today is a blend of ancient winter festivals, Christian tradition, and 19th-century reinvention. Many of its most iconic elements — the decorated fir tree, Santa Claus, stockings by the fireplace — were popularised in Britain and the United States during the Victorian era. Charles Dickens' <em>A Christmas Carol</em> (1843) cemented ideals of generosity and family togetherness that still define the holiday. Today Christmas is the single largest retail event on the global calendar, with consumers in the US alone spending over $900 billion during the holiday season.",
      "Whether you celebrate with religious services, a family roast dinner, a Secret Santa office party, or a quiet evening watching films, the countdown to Christmas builds a shared sense of anticipation that cuts across cultures. The live counter above shows the exact days, hours, minutes and seconds remaining until December 25."
    ],
    "key_info": [
      ("Date", "December 25 every year"),
      ("Public holiday in", "160+ countries"),
      ("US holiday spending", "$900 billion+ annually"),
      ("Most gifted category", "Electronics & clothing"),
      ("Christmas trees sold (US)", "~25–30 million per year"),
      ("Most-streamed Christmas song", "Mariah Carey — All I Want for Christmas Is You"),
    ],
    "timeline": [
      ("4th century AD", "December 25 officially chosen by the Roman Church to celebrate the birth of Christ"),
      ("1843", "Charles Dickens publishes <em>A Christmas Carol</em>, shaping modern Christmas values"),
      ("1870", "Christmas declared a federal public holiday in the United States"),
      ("1930s", "Coca-Cola advertising campaigns cement the red-suited, jolly image of Santa Claus"),
      ("1994", "Amazon launches — online Christmas shopping begins its rise to dominance"),
    ],
    "facts": [
      "The word 'Christmas' comes from the Old English <em>Crīstesmæsse</em>, meaning 'Christ's Mass'.",
      "Finland exports around 2 million Christmas trees to other European countries each year.",
      "In Australia and New Zealand, Christmas falls in summer — beach barbecues are a common tradition.",
      "The world's first Christmas card was sent in England in 1843, the same year Dickens wrote <em>A Christmas Carol</em>.",
      "Rudolph the Red-Nosed Reindeer was invented in 1939 as a promotional booklet for a US department store chain.",
      "Japan has a unique Christmas tradition: eating KFC fried chicken on December 25, started by a 1974 marketing campaign.",
      "The tallest artificial Christmas tree on record stood 51 metres (167 ft) tall, erected in Brazil in 2016.",
    ],
    "faqs": [
      ("How many days until Christmas?", "The live counter at the top of this page shows the exact days, hours, minutes and seconds until December 25."),
      ("What day is Christmas 2026?", "Christmas Day 2026 falls on a Friday, December 25."),
      ("What day is Christmas 2027?", "Christmas Day 2027 falls on a Saturday, December 25."),
      ("How many weeks until Christmas?", "Divide the days shown in the counter by 7 to get the number of weeks. For example, 70 days = exactly 10 weeks."),
      ("When is Christmas Eve?", "Christmas Eve is always December 24 — the evening before Christmas Day. Many families hold their main celebrations on Christmas Eve night."),
      ("Is Christmas a public holiday everywhere?", "Christmas is a public holiday in over 160 countries. In some countries such as Saudi Arabia and China it is not an official holiday, though it may still be commercially celebrated."),
      ("Why is Christmas on December 25?", "December 25 was chosen by the early Christian Church in the 4th century. It coincides with existing winter solstice festivals, making it easier to adopt as a Christian celebration."),
      ("What is Advent?", "Advent is the four-week period before Christmas, beginning on the Sunday nearest to November 30. It is a time of spiritual preparation in the Christian tradition and is now widely associated with Advent calendars and Christmas decorations."),
      ("What are the 12 Days of Christmas?", "The 12 Days of Christmas run from December 25 to January 5 (the eve of Epiphany). They are distinct from the lead-up to Christmas and are celebrated in many Christian traditions as the Christmas season proper."),
      ("What is the most popular Christmas gift?", "Electronics consistently top Christmas gift lists in the US, UK and Australia. Gift cards, toys, clothing and books are also perennial favourites. Mobile phones and gaming consoles are among the single most-requested items."),
      ("How much do people spend on Christmas?", "In the United States, holiday retail spending typically exceeds $900 billion per season. UK consumers average around £600 per household, and Australians spend approximately AUD $500 per person on gifts."),
      ("When should I start Christmas shopping?", "Retailers recommend starting by late October or early November to take advantage of sales events like Black Friday and Cyber Monday and to avoid late shipping delays."),
    ],
    "related": ["new-year", "black-friday", "cyber-monday", "thanksgiving", "halloween"],
  },

  # ─── NEW YEAR ─────────────────────────────────────────────────────────────────
  "new-year": {
    "overview": [
      "New Year's Day on January 1 is the most universally observed public holiday on earth, celebrated by virtually every country regardless of religion, culture or hemisphere. The transition from December 31 (New Year's Eve) into January 1 is marked by fireworks displays, street parties, televised countdowns and the clinking of glasses across every time zone — a rolling wave of celebration that takes roughly 26 hours to travel the globe.",
      "The tradition of marking a new year dates back at least 4,000 years to ancient Babylon, where a spring festival called Akitu celebrated the new agricultural cycle. The Romans later adopted January 1 as the start of the civil year, naming the month after Janus — the two-faced god who looks both backward into the past and forward into the future. Today's secular New Year celebration retains that symbolic idea: reflection on the year gone and optimism about the year ahead.",
      "The world's most-watched New Year's Eve events include the Sydney Harbour Bridge fireworks (seen by over a billion TV viewers), the Edinburgh Hogmanay street party, London's Thames fireworks, and New York City's Times Square ball drop — a tradition that dates to 1907. New Year's resolutions, another ancient custom, remain popular: surveys show around 40% of adults in English-speaking countries make at least one resolution each year, most commonly around fitness, diet or finances."
    ],
    "key_info": [
      ("Date", "January 1 every year"),
      ("New Year's Eve", "December 31"),
      ("First country to celebrate", "Kiribati (UTC+14)"),
      ("Last country to celebrate", "Baker Island, USA (UTC−12)"),
      ("Times Square ball drop since", "1907"),
      ("Global TV viewers (Sydney fireworks)", "1+ billion"),
    ],
    "timeline": [
      ("2000 BC", "Ancient Babylonians celebrate Akitu — the world's earliest recorded New Year festival — in spring"),
      ("46 BC", "Julius Caesar establishes January 1 as the start of the Roman calendar year"),
      ("1582", "Pope Gregory XIII introduces the Gregorian calendar, standardising January 1 globally"),
      ("1907", "The first Times Square ball drop takes place in New York City on December 31"),
      ("1994", "Sydney's New Year's Eve fireworks become one of the first events broadcast live worldwide via satellite"),
    ],
    "facts": [
      "January is named after Janus, the Roman god of beginnings, gates and transitions.",
      "Scotland's New Year celebration is called Hogmanay and is considered one of the world's great street parties.",
      "In Spain and some Latin American countries, it is traditional to eat exactly 12 grapes at midnight — one for each stroke of the clock.",
      "The Times Square ball is 3.7 metres (12 feet) in diameter, covered in 2,688 crystal triangles and weighs 5,386 kg (11,875 lbs).",
      "Around 1 million people attend the Times Square celebration in person every year, with another 58 million watching on US television.",
      "New Year's Day is the world's most widely observed public holiday, recognised as an official holiday in 167 countries.",
    ],
    "faqs": [
      ("How many days until New Year?", "The live counter above shows the exact time remaining until January 1. It updates every second."),
      ("What day is New Year's Day 2027?", "New Year's Day 2027 falls on a Friday, January 1."),
      ("What day is New Year's Day 2028?", "New Year's Day 2028 falls on a Saturday, January 1."),
      ("Where does New Year start first?", "New Year's Day arrives first in the Line Islands of Kiribati at UTC+14 — 26 hours before the last places on Earth celebrate."),
      ("What are the best New Year fireworks in the world?", "The most famous displays are Sydney (Australia), Dubai (UAE), London's Thames Embankment, Edinburgh's Hogmanay (Scotland), and New York City's Times Square ball drop."),
      ("What is Hogmanay?", "Hogmanay is Scotland's traditional New Year celebration, running from December 31 to January 1 (or longer). Edinburgh hosts one of the world's largest street parties, with torchlight processions and the singing of <em>Auld Lang Syne</em>."),
      ("Why do we sing Auld Lang Syne at New Year?", "<em>Auld Lang Syne</em> is a poem by Scottish poet Robert Burns (1788), set to a traditional folk melody. It became a New Year's Eve anthem after being broadcast by Guy Lombardo's orchestra in the US in 1929."),
      ("What time zone celebrates New Year last?", "Baker Island and Howland Island (both US territories) at UTC−12 are the last inhabited places to cross into the New Year."),
      ("What are popular New Year's resolutions?", "The most common resolutions include exercising more, losing weight, saving money, quitting smoking or drinking, learning a new skill and spending more time with family."),
      ("Is New Year's Day always January 1?", "In the Gregorian calendar, yes. However, other calendars have different New Year dates: Chinese New Year falls in January or February, the Islamic New Year moves each year, and the Jewish New Year (Rosh Hashanah) falls in September or October."),
    ],
    "related": ["christmas", "thanksgiving", "halloween", "easter"],
  },

  # ─── HALLOWEEN ────────────────────────────────────────────────────────────────
  "halloween": {
    "overview": [
      "Halloween falls on October 31 each year and is one of the most commercially significant holidays in the English-speaking world. In the United States alone, consumers spend over $12 billion annually on costumes, decorations, candy and related merchandise — making it the second-largest commercial holiday after Christmas. The holiday is also enormously popular in Canada, the United Kingdom, Ireland and Australia, and has been growing in continental Europe and beyond.",
      "The origins of Halloween lie in the ancient Celtic festival of Samhain (pronounced 'SAH-win'), observed across Ireland, Scotland and Wales around 2,000 years ago. Celts believed that on the night of October 31, the boundary between the living and the dead became permeable, allowing spirits to roam the earth. When the Roman Empire conquered Celtic lands, Samhain merged with two Roman festivals — Feralia and Pomona — and later with the Christian feast of All Hallows' Eve (the night before All Saints' Day on November 1). Irish and Scottish immigrants brought Halloween traditions to North America in the 19th century.",
      "The holiday's modern form — trick-or-treating, jack-o'-lanterns, haunted houses and costume parties — developed primarily in the United States during the 20th century. Today it is a broadly secular celebration of imagination, fear and community, enjoyed by children and adults alike. The live countdown above shows exactly how long until October 31."
    ],
    "key_info": [
      ("Date", "October 31 every year"),
      ("US consumer spending", "$12 billion+ annually"),
      ("Candy sold in US (Halloween week)", "600 million pounds"),
      ("Most popular adult costume (US)", "Witch"),
      ("Most popular candy (US)", "Reese's Peanut Butter Cups"),
      ("Origin festival", "Celtic Samhain, ~2,000 years ago"),
    ],
    "timeline": [
      ("500 BC", "Celtic peoples observe Samhain — a harvest festival marking the end of summer and the start of the 'dark half' of the year"),
      ("9th century", "The Christian Church establishes All Saints' Day on November 1; October 31 becomes All Hallows' Eve"),
      ("1840s", "Irish immigrants fleeing the Great Famine bring Halloween traditions to North America"),
      ("1920s–1930s", "Trick-or-treating becomes widespread across the United States and Canada"),
      ("1978", "John Carpenter's film <em>Halloween</em> transforms the holiday into a cultural touchstone for horror cinema"),
    ],
    "facts": [
      "The word 'Halloween' is a contraction of 'All Hallows' Evening' — the night before All Saints' Day.",
      "Jack-o'-lanterns were originally carved from turnips in Ireland before pumpkins became the standard in North America.",
      "Americans buy roughly 600 million pounds of candy in the week leading up to Halloween — more candy sold in any other week of the year.",
      "The fear of Halloween is called Samhainophobia.",
      "Trick-or-treating as we know it today became standardised in the US during the 1950s, when suburban neighbourhoods made it a community ritual.",
      "Orange and black are Halloween's colours because orange represents harvest and autumn leaves, while black symbolises darkness and death.",
      "The highest-grossing horror franchise of all time is <em>Halloween</em> (1978), which spawned 13 films and earned over $700 million worldwide.",
    ],
    "faqs": [
      ("How many days until Halloween?", "The live countdown above shows the exact days, hours, minutes and seconds until October 31."),
      ("What day is Halloween 2026?", "Halloween 2026 falls on a Saturday, October 31."),
      ("What day is Halloween 2027?", "Halloween 2027 falls on a Sunday, October 31."),
      ("What is the origin of trick-or-treating?", "Trick-or-treating evolved from the medieval practice of 'souling', where poor people would go door to door on All Souls' Day offering prayers for the dead in exchange for food. Irish immigrants brought similar traditions to the US, where it developed into the candy-centred custom we know today."),
      ("Why do we carve pumpkins?", "The jack-o'-lantern tradition comes from an Irish legend about a man named Stingy Jack who tricked the Devil. Irish immigrants originally carved turnips; when they arrived in America, they found pumpkins much easier to carve."),
      ("Is Halloween celebrated outside the US?", "Yes. Halloween is widely celebrated in Canada, Ireland, the UK, Australia and New Zealand. It is growing in popularity in Germany, France, Spain and parts of Latin America, though traditions vary."),
      ("What are the most popular Halloween costumes?", "For adults: witches, vampires, ghosts, zombies and pop culture characters. For children: superheroes, princesses, animals and characters from current films and TV shows."),
      ("What is the most popular Halloween candy in the US?", "Reese's Peanut Butter Cups consistently top US Halloween candy rankings, followed by Snickers, Kit Kat, Candy Corn and M&Ms."),
      ("When should I buy Halloween decorations?", "Retailers typically put Halloween stock on shelves in September. For the best selection and prices, shop in late September or early October."),
      ("What is Día de los Muertos and is it the same as Halloween?", "Día de los Muertos (Day of the Dead) is a Mexican and Central American tradition observed November 1–2 to honour deceased family members. While it overlaps with Halloween on the calendar, it is a distinct cultural celebration with different origins, meaning and rituals."),
    ],
    "related": ["thanksgiving", "christmas", "dia-de-los-muertos", "new-year"],
  },

  # ─── BLACK FRIDAY ─────────────────────────────────────────────────────────────
  "black-friday": {
    "overview": [
      "Black Friday is the biggest shopping day of the year in the United States and one of the largest retail events globally. It falls on the Friday after US Thanksgiving — the fourth Thursday of November — and marks the traditional start of the Christmas shopping season. In 2023, US consumers spent $9.8 billion online on Black Friday alone, a figure that has grown almost every year since online shopping became mainstream.",
      "The term 'Black Friday' originated in Philadelphia in the 1960s, where police used it to describe the chaotic foot traffic and congestion that occurred the day after Thanksgiving as shoppers flooded stores. The phrase spread nationally by the 1980s. One popular but disputed folk etymology claims the name refers to retailers moving from 'in the red' (operating at a loss) to 'in the black' (profit) — though historians note the police usage predates this explanation.",
      "Today Black Friday has expanded well beyond the United States. Retailers in the UK, Canada, Australia, Germany, Brazil and dozens of other countries now run major Black Friday promotions. Deals extend across the entire week, with many retailers launching 'Black Friday Week' campaigns beginning on Monday. Online shopping has shifted consumer behaviour dramatically — while physical store visits peaked around 2012, digital spending on Black Friday has grown by double digits in most years since."
    ],
    "key_info": [
      ("Date", "Friday after US Thanksgiving (4th Thursday of November)"),
      ("Black Friday 2026", "November 27, 2026"),
      ("US online spend (2023)", "$9.8 billion"),
      ("Most discounted categories", "Electronics, appliances, fashion, toys"),
      ("Average US household spend", "$300–$400 on Black Friday weekend"),
      ("Countries with major BF events", "USA, UK, Canada, Australia, Brazil, Germany"),
    ],
    "timeline": [
      ("1961", "Philadelphia police begin using the term 'Black Friday' to describe post-Thanksgiving shopping chaos"),
      ("1980s", "The term 'Black Friday' spreads nationally as retailers embrace it as a positive shopping event"),
      ("2005", "The term 'Cyber Monday' is coined to describe the online equivalent of Black Friday"),
      ("2012", "Online Black Friday sales surpass $1 billion for the first time in the US"),
      ("2020", "COVID-19 accelerates the shift to online; many US stores close on Thanksgiving Day itself, ending the in-store 'doorbusters' era"),
    ],
    "facts": [
      "The Monday after Thanksgiving was once called 'Black Monday' in the retail industry before Cyber Monday replaced that term.",
      "Adobe Analytics reported that US shoppers spent $1,000 per second online during peak Black Friday 2023.",
      "The UK adopted Black Friday as a major shopping event around 2013, driven by US retailers like Amazon operating there.",
      "Electronics and televisions are the most-discounted Black Friday category in the US every year.",
      "More than 196 million Americans shopped during the five-day Thanksgiving-to-Cyber-Monday weekend in 2023.",
      "RFID and inventory technology has largely ended the dangerous 'door-buster' stampedes that made early 2000s Black Fridays infamous.",
    ],
    "faqs": [
      ("When is Black Friday 2026?", "Black Friday 2026 falls on November 27, 2026 — the day after US Thanksgiving."),
      ("When is Black Friday 2027?", "Black Friday 2027 falls on November 26, 2027."),
      ("What time do Black Friday sales start?", "Online deals often begin on Thanksgiving Day (Thursday) or even the week before. Physical stores typically open at midnight or 5–6 AM on Friday, though many chains now open at midnight."),
      ("What are the best Black Friday deals?", "The biggest discounts are typically on TVs and electronics, smartphones, laptops, kitchen appliances, toys and clothing. Deals of 40–70% off are common in these categories."),
      ("Is Black Friday better than Cyber Monday?", "Black Friday traditionally has the best deals on electronics and physical goods. Cyber Monday focuses on online-only deals, particularly in fashion, software and digital subscriptions. Today many retailers offer the same deals across both days."),
      ("Do UK and Australian retailers do Black Friday?", "Yes. Black Friday is now a major event in the UK, Australia, Canada, Germany, Brazil and many other countries. Most major retailers run deals for the entire Black Friday week."),
      ("Should I wait for Black Friday or buy now?", "For electronics, Black Friday consistently delivers the lowest prices of the year. However, some products (like newly released items) may not be discounted. Amazon, Walmart and Best Buy tend to offer year-long price-match guarantees you can take advantage of."),
      ("What is the Black Friday weekend?", "The Black Friday weekend refers to the stretch from Friday to Cyber Monday — often called the 'Cyber Five'. It is the single biggest shopping period of the US retail calendar."),
      ("Are Black Friday prices really the lowest?", "Generally yes for electronics and appliances — studies show Black Friday prices on TVs and laptops are on average 20–25% lower than at other times of year. Some other product categories see comparable discounts at other sale events."),
      ("Is Black Friday a public holiday?", "No. Black Friday is not an official US public holiday, though many employers give workers the day off as part of the Thanksgiving long weekend."),
    ],
    "related": ["cyber-monday", "thanksgiving", "christmas", "new-year"],
  },

  # ─── THANKSGIVING ─────────────────────────────────────────────────────────────
  "thanksgiving": {
    "overview": [
      "Thanksgiving is a national holiday in the United States celebrated on the fourth Thursday of November, and in Canada on the second Monday of October. It originated as a harvest festival and has grown into the most-travelled holiday in America — with more than 55 million people flying or driving to be with family and friends over the long weekend. The holiday centres on a large shared meal, traditionally featuring roast turkey, stuffing, cranberry sauce, mashed potatoes and pumpkin pie.",
      "The historical roots of US Thanksgiving are usually traced to a 1621 feast shared between English Pilgrims at Plymouth Colony in Massachusetts and the Wampanoag people who had helped them survive their first harsh winter in the New World. The event was not then called Thanksgiving; the holiday as we know it today developed over centuries. President Abraham Lincoln proclaimed Thanksgiving a national holiday in 1863, at the height of the Civil War, as a call for national unity. Canada's Thanksgiving has separate roots and was officially established in 1879.",
      "Beyond the family meal, Thanksgiving in the US is now synonymous with American football (the NFL has scheduled games on Thanksgiving since 1920), the Macy's Thanksgiving Day Parade in New York City, and — on the following day — Black Friday, the start of the Christmas shopping season. Over 46 million turkeys are eaten in the United States on Thanksgiving Day alone."
    ],
    "key_info": [
      ("US Thanksgiving 2026", "November 26, 2026"),
      ("Canadian Thanksgiving 2026", "October 12, 2026"),
      ("Turkeys eaten in US on Thanksgiving", "46 million+"),
      ("Americans who travel for Thanksgiving", "55 million+"),
      ("Macy's Parade first held", "1924"),
      ("Origin event", "Plymouth Colony harvest feast, 1621"),
    ],
    "timeline": [
      ("1621", "Pilgrims at Plymouth Colony share a three-day autumn harvest feast with Wampanoag people — later idealised as the 'First Thanksgiving'"),
      ("1789", "President George Washington proclaims the first national Thanksgiving Day"),
      ("1863", "President Abraham Lincoln establishes Thanksgiving as an annual national holiday on the last Thursday of November"),
      ("1924", "Macy's Department Store holds the first Thanksgiving Day Parade in New York City"),
      ("1941", "Congress officially fixes Thanksgiving to the fourth (not last) Thursday of November"),
    ],
    "facts": [
      "More than 46 million turkeys are eaten in the United States on Thanksgiving Day — more than on Christmas or Easter.",
      "The Macy's Thanksgiving Day Parade draws about 3.5 million spectators on the streets of Manhattan and 28 million TV viewers.",
      "Benjamin Franklin reportedly advocated for the turkey to be the national bird of the United States instead of the bald eagle.",
      "The US President has formally 'pardoned' a turkey each year since 1989, sparing it from becoming dinner.",
      "The busiest day for US airports is not Thanksgiving itself but the Wednesday before, known as 'Thanksgiving Eve'.",
      "Canadian Thanksgiving predates US Thanksgiving — Martin Frobisher gave thanks for surviving his arctic voyages in 1578, over 40 years before the Plymouth feast.",
    ],
    "faqs": [
      ("When is Thanksgiving 2026?", "US Thanksgiving 2026 is on November 26. Canadian Thanksgiving 2026 is on October 12."),
      ("When is Thanksgiving 2027?", "US Thanksgiving 2027 is on November 25. Canadian Thanksgiving 2027 is on October 11."),
      ("Why is Thanksgiving on a Thursday?", "President Lincoln's 1863 proclamation set it on the last Thursday of November. FDR moved it to the fourth Thursday in 1939 to extend the Christmas shopping season, which caused controversy ('Franksgiving') before Congress made the fourth Thursday permanent in 1941."),
      ("What do people eat on Thanksgiving?", "The traditional Thanksgiving meal features roast turkey, stuffing (or dressing), mashed potatoes, sweet potatoes, cranberry sauce, green bean casserole, corn bread, dinner rolls and pumpkin pie. Regional variations abound."),
      ("Do other countries celebrate Thanksgiving?", "The US and Canada both celebrate Thanksgiving, on different dates. Liberia holds a Thanksgiving in November, and some Caribbean nations have related harvest traditions. It is not observed in the UK, Australia or most other countries."),
      ("What NFL games are on Thanksgiving?", "The NFL traditionally schedules three games on Thanksgiving: two in the afternoon (Detroit Lions and Dallas Cowboys always host one each) and a third primetime game in the evening."),
      ("What is the Macy's Thanksgiving Day Parade?", "The Macy's Thanksgiving Day Parade is an annual event in New York City held every Thanksgiving morning since 1924. It features giant character balloons, floats, marching bands and celebrity performances, watched by millions on television."),
      ("Is Thanksgiving a good time to travel?", "Thanksgiving weekend is the busiest travel period in the United States. Book flights and hotels well in advance if travelling. Many attractions, museums and stores are closed on Thanksgiving Day itself."),
      ("When do Black Friday sales start?", "Many US retailers now launch Black Friday deals on Thanksgiving Day (Thursday) evening or even earlier in the week. The biggest online sales start at midnight on Friday."),
      ("What is Friendsgiving?", "Friendsgiving is an informal celebration of Thanksgiving with friends rather than family, typically held the weekend before or after Thanksgiving Day. It has grown in popularity since the 2010s."),
    ],
    "related": ["black-friday", "christmas", "new-year", "halloween", "cyber-monday"],
  },

  # ─── SUPER BOWL ───────────────────────────────────────────────────────────────
  "super-bowl": {
    "overview": [
      "The Super Bowl is the annual championship game of the National Football League (NFL) and the single most-watched television broadcast in the United States every year. Held on the second Sunday of February — a day known as 'Super Bowl Sunday' — it routinely draws over 100 million viewers in the US alone and an estimated 200 million globally. More than 70,000 fans attend the game in person, while millions more watch at parties, bars and restaurants making it one of the great shared cultural events in American life.",
      "First played in January 1967 between the NFL and AFL champions, the Super Bowl quickly grew from a regular sporting event into a national spectacle. The halftime show — now among the most-watched live performances in the world — has featured artists from Prince to Beyoncé, Shakira, Eminem, Rihanna and Usher. The game's commercials are themselves an attraction: 30 seconds of Super Bowl advertising time costs around $7 million, and the ads are reviewed and ranked by millions of viewers who watch them as entertainment.",
      "Super Bowl Sunday has effectively become an unofficial American holiday. US adults consume an estimated 1.3 billion chicken wings on Super Bowl Sunday, and it is the second-biggest day for food consumption in the US after Thanksgiving. The host city — which changes each year — benefits from a significant economic boost, with the NFL estimating each Super Bowl injects $400–$500 million into the local economy."
    ],
    "key_info": [
      ("Date", "Second Sunday of February"),
      ("Super Bowl LXI (2027)", "February 7, 2027"),
      ("Average US viewership", "100–125 million"),
      ("30-second ad cost", "~$7 million (2024)"),
      ("Chicken wings consumed (US)", "1.3 billion on Super Bowl Sunday"),
      ("First Super Bowl", "January 15, 1967 (Green Bay Packers won)"),
    ],
    "timeline": [
      ("January 1967", "Super Bowl I: Green Bay Packers defeat Kansas City Chiefs 35–10 at the LA Memorial Coliseum"),
      ("1993", "Michael Jackson's halftime show transforms the Super Bowl halftime slot into a prime-time spectacle"),
      ("2015", "Super Bowl XLIX draws 114.4 million viewers — the most-watched US television broadcast in history at the time"),
      ("2022", "Super Bowl LVI is held at SoFi Stadium, Los Angeles — the first Super Bowl with a $6M+ 30-second ad rate"),
      ("2024", "Super Bowl LVIII in Las Vegas: Taylor Swift's relationship with Chiefs TE Travis Kelce drives record international viewership"),
    ],
    "facts": [
      "The trophy awarded to the winning team is the Vince Lombardi Trophy, named after the legendary Green Bay Packers coach.",
      "The New England Patriots and Pittsburgh Steelers are tied for the most Super Bowl wins, with 6 each.",
      "Super Bowl Sunday is the second-largest food consumption day in the US, behind only Thanksgiving.",
      "The halftime show is produced independently from the game — the performing artists are not paid, but production costs can reach $13 million.",
      "The term 'Super Bowl' was coined by Kansas City Chiefs owner Lamar Hunt, inspired by his daughter's Super Ball toy.",
      "Nevada sportsbooks take in more bets on the Super Bowl than any other single sporting event — over $185 million in 2024.",
    ],
    "faqs": [
      ("When is the Super Bowl 2027?", "Super Bowl LXI is scheduled for Sunday, February 7, 2027."),
      ("Where is the Super Bowl 2027?", "Super Bowl LXI will be held at Levi's Stadium in Santa Clara, California (home of the San Francisco 49ers)."),
      ("How long does the Super Bowl last?", "The Super Bowl typically lasts about 3.5 to 4 hours, including pre-game ceremonies, the national anthem, the game itself and the halftime show."),
      ("Who has won the most Super Bowls?", "The New England Patriots and Pittsburgh Steelers share the record with 6 Super Bowl championships each."),
      ("Who performs at the Super Bowl halftime show?", "The NFL selects a headline artist for the halftime show each year. Recent performers include Usher (2024), Rihanna (2023), Dr. Dre / Snoop Dogg / Eminem (2022) and The Weeknd (2021)."),
      ("How much do Super Bowl tickets cost?", "Face value tickets start at around $950, but secondary market prices for desirable seats routinely exceed $8,000–$10,000 in the weeks leading up to the game."),
      ("How much do Super Bowl ads cost?", "A 30-second advertising spot during the Super Bowl costs approximately $6.5–$7 million in 2024, making it the most expensive advertising time on US television."),
      ("How many people watch the Super Bowl?", "In the US, average viewership is 100–115 million. The 2015 Super Bowl holds the US broadcast record at 114.4 million viewers. Global viewership including international broadcasts is estimated at 150–200 million."),
      ("What is Super Bowl Sunday?", "Super Bowl Sunday is the informal name for the day of the Super Bowl — the second Sunday of February. It is not an official US holiday but functions as one for many Americans, with office pools, viewing parties and widespread time off."),
      ("Can I stream the Super Bowl?", "Yes. The Super Bowl is broadcast simultaneously by a major US network (rotating between CBS, Fox, NBC and ABC) and streamed on that network's free streaming service, making it accessible without a cable subscription."),
    ],
    "related": ["thanksgiving", "nfl-season", "oscars", "christmas"],
  },

  # ─── GTA 6 ────────────────────────────────────────────────────────────────────
  "gta6": {
    "overview": [
      "Grand Theft Auto VI (GTA 6) is the most anticipated video game release in history, developed by Rockstar Games. It is the successor to Grand Theft Auto V, which was released in 2013 and went on to become the second best-selling video game of all time, with over 200 million copies sold and a thriving online component (GTA Online) that remained commercially dominant for more than a decade. The extraordinary longevity of GTA V is a key reason anticipation for its sequel has reached unprecedented levels.",
      "Rockstar Games officially revealed GTA 6 with a trailer in December 2023, which became the fastest video game trailer to reach 100 million views on YouTube — taking less than 24 hours. The trailer confirmed that the game returns to Vice City, the Miami-inspired setting last visited in Grand Theft Auto: Vice City (2002), and features Lucia as the series' first playable female protagonist alongside a male character, Jason. The setting spans a fictional version of Miami and surrounding Florida-inspired environments.",
      "GTA 6 is being developed for PlayStation 5 and Xbox Series X/S. A PC release date has not been confirmed, following the pattern of previous Rockstar titles. The game's production represents one of the largest creative and financial investments in entertainment history, with industry analysts estimating the budget may exceed $2 billion when marketing is included. Every confirmed detail — from the map size to the mission structure — has been the subject of intense analysis and discussion by the gaming community."
    ],
    "key_info": [
      ("Developer", "Rockstar Games"),
      ("Publisher", "Take-Two Interactive"),
      ("Platforms", "PlayStation 5, Xbox Series X/S"),
      ("Reveal trailer", "December 4, 2023"),
      ("Setting", "Vice City (fictional Miami, Florida)"),
      ("Protagonist", "Lucia (first playable female lead in GTA series)"),
    ],
    "timeline": [
      ("2013", "Grand Theft Auto V launches for PS3/Xbox 360 — goes on to sell 200 million+ copies"),
      ("July 2022", "Rockstar Games officially confirms GTA 6 is in development"),
      ("December 2023", "First GTA 6 trailer released — 100 million YouTube views in under 24 hours"),
      ("2024", "Multiple leaks and analyst reports suggest the game's production budget is among the largest in entertainment history"),
      ("TBC", "GTA 6 release — exact date to be confirmed by Rockstar Games"),
    ],
    "facts": [
      "The first GTA 6 trailer surpassed 100 million YouTube views in under 24 hours — faster than any video game trailer ever.",
      "GTA V is the second best-selling video game of all time, behind only Minecraft, with over 200 million copies sold.",
      "GTA Online generated over $1 billion per year for multiple years running, funding much of GTA 6's development.",
      "Lucia is the first playable female protagonist in a mainline Grand Theft Auto game in the series' 26-year history.",
      "Vice City in GTA 6 is based on Miami and appears to feature a significantly larger and more detailed map than any previous GTA game.",
      "Industry analysts estimate GTA 6's total development and marketing budget could reach $1–2 billion, making it one of the most expensive creative projects ever made.",
    ],
    "faqs": [
      ("When does GTA 6 come out?", "Rockstar Games has not yet confirmed an official release date. The live counter above tracks the latest confirmed or expected window. Check Rockstar's official channels for the most up-to-date information."),
      ("What platforms will GTA 6 be on?", "GTA 6 has been confirmed for PlayStation 5 and Xbox Series X/S. No PC release date has been announced, though a PC version is widely expected to follow as with previous Rockstar titles."),
      ("What is GTA 6 set?", "GTA 6 is set in Vice City, a fictional version of Miami, Florida. The game appears to cover a large region inspired by South Florida including urban areas, beaches, suburbs and the Everglades."),
      ("Who is the main character in GTA 6?", "The primary playable protagonist is Lucia, the first female lead in a mainline GTA game. She appears alongside a male character named Jason in a dual-protagonist structure."),
      ("Will GTA 6 have GTA Online?", "Rockstar Games has not announced specific details about GTA 6's online component. Given the massive success of GTA Online, an online mode is universally expected to be included."),
      ("How much will GTA 6 cost?", "No pricing has been officially announced. Industry analysts expect it to follow standard new-release pricing of $69.99–$79.99 USD for PS5 and Xbox Series X/S versions."),
      ("Will GTA 6 come to PC?", "No PC release has been confirmed. Previous Rockstar major releases (GTA V, Red Dead Redemption 2) arrived on PC 1–2 years after the console launch."),
      ("How big will the GTA 6 map be?", "Rockstar has not released official map size information. Based on the trailer footage and developer comments, analysts believe it will be significantly larger than GTA V's Los Santos map."),
      ("Can I pre-order GTA 6?", "Pre-orders have not yet been officially opened by Rockstar Games or major retailers. Pre-orders typically open a few months before a confirmed release date."),
      ("What engine does GTA 6 use?", "GTA 6 uses an updated version of Rockstar's proprietary RAGE (Rockstar Advanced Game Engine), substantially upgraded from GTA V's version."),
    ],
    "related": ["christmas", "black-friday", "cyber-monday", "oscars"],
  },

  # ─── CYBER MONDAY ─────────────────────────────────────────────────────────────
  "cyber-monday": {
    "overview": [
      "Cyber Monday is the biggest online shopping day of the year in the United States, the UK, Canada, Australia and many other countries. It falls on the Monday immediately after Thanksgiving weekend — three days after Black Friday. In 2023, US consumers spent $12.4 billion online on Cyber Monday, making it the largest US e-commerce day ever recorded and surpassing even Black Friday's online total. The day was invented in the United States in 2005 and has since become a global retail phenomenon.",
      "The term 'Cyber Monday' was coined by Ellen Davis and Scott Culp of the National Retail Federation (NRF) in a November 2005 press release titled <em>'Cyber Monday Quickly Becoming One of the Biggest Online Shopping Days of the Year.'</em> The concept was rooted in a real observed behaviour: after the Thanksgiving weekend, online sales spiked the following Monday as workers returned to offices with fast internet connections — home broadband was not yet universal in 2005. The name stuck and became a marketing phenomenon.",
      "Today Cyber Monday is dominated by deals on electronics, software, subscriptions, fashion and home goods. Amazon, Walmart, Best Buy and Apple offer some of the deepest discounts of the year. Unlike Black Friday, Cyber Monday is almost entirely an online event — there are no physical store queues, no door-buster stampedes, and deals often extend through the entire Cyber Week from Monday to Friday. The day is particularly strong for deal seekers in the US, UK, Canada and Australia, where broadband penetration and e-commerce infrastructure are most mature."
    ],
    "key_info": [
      ("Date", "Monday after US Thanksgiving (3 days after Black Friday)"),
      ("Cyber Monday 2026", "November 30, 2026"),
      ("US online spend (2023)", "$12.4 billion — record high"),
      ("Origin", "United States, coined by NRF in 2005"),
      ("Top deal categories", "Electronics, software, fashion, subscriptions"),
      ("Peak shopping time", "9–11 PM Eastern Time (US)"),
    ],
    "timeline": [
      ("2005", "The National Retail Federation coins the term 'Cyber Monday' in a press release; the concept goes viral"),
      ("2010", "Cyber Monday surpasses Black Friday in online sales for the first time in the US"),
      ("2012", "Cyber Monday becomes the first US e-commerce day to break $2 billion in online spending"),
      ("2019", "US Cyber Monday spending tops $9 billion, driven by mobile shopping surpassing desktop for the first time"),
      ("2023", "US consumers spend $12.4 billion on Cyber Monday — the largest US e-commerce day in history"),
    ],
    "facts": [
      "Cyber Monday was a US invention — created by the National Retail Federation in 2005 — and is now celebrated in over 20 countries.",
      "Adobe Analytics reports that peak US shopping on Cyber Monday occurs between 9–11 PM Eastern Time.",
      "In 2023, mobile devices accounted for over 55% of all Cyber Monday online purchases — up from less than 10% in 2012.",
      "Amazon's Cyber Monday is typically the company's biggest sales day, exceeding even Prime Day in some years.",
      "UK retailers adopted Cyber Monday around 2010 and it is now one of the biggest e-commerce days in Britain.",
      "The average discount on electronics during Cyber Monday is approximately 30%, with some items discounted 50–70%.",
    ],
    "faqs": [
      ("When is Cyber Monday 2026?", "Cyber Monday 2026 falls on November 30, 2026 — the Monday after US Thanksgiving."),
      ("When is Cyber Monday 2027?", "Cyber Monday 2027 falls on November 29, 2027."),
      ("Is Cyber Monday only in the US?", "No. Cyber Monday originated in the US in 2005 but is now a major shopping event in the UK, Canada, Australia, Germany, Brazil and many other countries. It is not limited to Latin America."),
      ("Is Cyber Monday better than Black Friday for deals?", "For online purchases, Cyber Monday typically offers the deepest discounts on electronics, software, fashion and subscriptions. Black Friday tends to have better in-store deals and earlier access to limited stock. Today many retailers run identical deals across both days."),
      ("What are the best Cyber Monday deals?", "Historically the best Cyber Monday deals are on laptops, tablets, televisions, headphones, video games, streaming subscriptions, software and fashion. Amazon, Walmart, Best Buy and Apple consistently offer notable discounts."),
      ("How long do Cyber Monday deals last?", "Most major retailers extend Cyber Monday deals through the full 'Cyber Week' — from Monday to Friday. Some deals sell out within hours; others last the full week."),
      ("Do UK and Australian retailers do Cyber Monday?", "Yes. Most major retailers in the UK (Amazon UK, Currys, Argos, John Lewis) and Australia (JB Hi-Fi, Harvey Norman, Amazon AU) now offer Cyber Monday deals."),
      ("When do Cyber Monday deals start?", "Many retailers start their Cyber Monday sales on Sunday night or even on Black Friday itself. The largest single-day deals typically go live at midnight ET on Monday."),
      ("Can I get Cyber Monday deals on a phone?", "Yes. Over 55% of Cyber Monday purchases are now made on mobile devices. All major retailers have mobile apps and mobile-optimised websites for easy shopping."),
      ("What is Cyber Week?", "Cyber Week refers to the extended period of online deals from Black Friday through Cyber Monday and often the entire first week of December. It was created by retailers to spread demand and reduce server overload on a single day."),
    ],
    "related": ["black-friday", "thanksgiving", "christmas", "new-year"],
  },

  # ─── INDEPENDENCE DAY ─────────────────────────────────────────────────────────
  "independence-day": {
    "overview": [
      "Independence Day — commonly called the Fourth of July — is the United States' national holiday, celebrating the adoption of the Declaration of Independence on July 4, 1776. On that date, the Second Continental Congress formally declared that the thirteen American colonies were no longer subject to British rule, founding a new sovereign nation. The holiday is observed with fireworks, parades, barbecues, concerts, family gatherings and patriotic ceremonies across every state in the country.",
      "The Declaration of Independence was primarily drafted by Thomas Jefferson and proclaimed that all men are created equal, with unalienable rights to life, liberty and the pursuit of happiness. The document was adopted by the Continental Congress on July 4, though the Revolutionary War itself would continue until 1783. Congress declared Independence Day a federal holiday in 1870, and since 1941 it has been a paid federal holiday for government workers. It is now one of the most universally observed holidays in the United States.",
      "The Fourth of July is synonymous with fireworks — an estimated 14,000 fireworks displays take place across the US on July 4. The largest is Macy's Fourth of July Fireworks Spectacular in New York City, which uses approximately 48,000 shells and is watched by around 3 million spectators on the ground and 7 million on television. Americans spend over $2 billion on fireworks each year, accounting for more than 90% of global consumer fireworks consumption."
    ],
    "key_info": [
      ("Date", "July 4 every year"),
      ("Independence Day 2026", "Saturday, July 4, 2026"),
      ("Year of US independence", "1776"),
      ("Fireworks displays on July 4", "~14,000 across the US"),
      ("US spending on fireworks", "$2 billion+ per year"),
      ("Largest fireworks show", "Macy's NYC — ~48,000 shells"),
    ],
    "timeline": [
      ("July 4, 1776", "Continental Congress adopts the Declaration of Independence, founding the United States of America"),
      ("1777", "Philadelphia holds the first organised July 4 celebration with fireworks and a 13-gun salute"),
      ("1870", "US Congress declares Independence Day a federal holiday"),
      ("1941", "Independence Day becomes a paid federal holiday for government employees"),
      ("2026", "The United States celebrates its 250th anniversary of independence — the 'Semiquincentennial'"),
    ],
    "facts": [
      "The Fourth of July 2026 marks the 250th anniversary of American independence — a milestone known as the Semiquincentennial.",
      "John Adams and Thomas Jefferson — both Founding Fathers and former Presidents — both died on July 4, 1826, exactly 50 years after the Declaration was signed.",
      "The Liberty Bell in Philadelphia is ceremonially tapped 13 times every July 4 — once for each original colony.",
      "Americans consume approximately 155 million hot dogs on the Fourth of July, more than on any other day of the year.",
      "The first fireworks used on Independence Day were by the Continental Army on July 4, 1777 — exactly one year after independence.",
      "Nathan's Famous Hot Dog Eating Contest on Coney Island, Brooklyn, has been held every July 4 since 1972 and is a major American tradition.",
    ],
    "faqs": [
      ("When is Independence Day 2026?", "Independence Day 2026 falls on Saturday, July 4, 2026. Because it falls on a Saturday, the observed federal holiday may shift to Friday, July 3."),
      ("What is the Fourth of July celebrating?", "The Fourth of July celebrates the adoption of the Declaration of Independence on July 4, 1776, when the thirteen American colonies declared independence from British rule and founded the United States of America."),
      ("When did the US declare independence from Britain?", "The Continental Congress voted to declare independence on July 2, 1776, and formally adopted the Declaration of Independence on July 4, 1776. John Adams famously predicted July 2 would be celebrated, not July 4."),
      ("Who wrote the Declaration of Independence?", "The Declaration of Independence was primarily written by Thomas Jefferson, with revisions from Benjamin Franklin, John Adams and the full Continental Congress. It was adopted on July 4, 1776."),
      ("Why do Americans celebrate with fireworks?", "Fireworks have been part of July 4 celebrations since 1777, when the first anniversary of independence was marked by Philadelphia with fireworks and a 13-gun salute. John Adams wrote in 1776 that the occasion ought to be celebrated with 'illuminations' — an early term for fireworks."),
      ("Is the Fourth of July a federal holiday?", "Yes. Independence Day was made a federal holiday in 1870 and has been a paid federal holiday since 1941. Banks, government offices and many businesses close on July 4."),
      ("What is special about Independence Day 2026?", "July 4, 2026 marks the 250th anniversary of American independence — the Semiquincentennial. Major national celebrations are planned across the country, making it one of the most significant Independence Days in US history."),
      ("Where are the best Fourth of July fireworks?", "The most famous displays are Macy's Fireworks in New York City, the National Mall in Washington DC, the Boston Pops Fireworks Spectacular, Navy Pier in Chicago and the Hollywood Bowl in Los Angeles."),
      ("Do other countries celebrate on July 4?", "July 4 is a US holiday. The Philippines and Rwanda also celebrate independence days in July, on different dates. Many US embassies worldwide hold Fourth of July receptions."),
      ("What food is traditional on the Fourth of July?", "Classic Fourth of July food includes burgers and hot dogs on the grill, potato salad, corn on the cob, coleslaw, watermelon, apple pie and ice cream. Americans consume about 155 million hot dogs on July 4."),
    ],
    "related": ["memorial-day", "labor-day", "thanksgiving", "new-year"],
  },

  # ─── BACK TO SCHOOL ───────────────────────────────────────────────────────────
  "back-to-school": {
    "overview": [
      "Back-to-school season is one of the largest consumer spending periods of the year in the United States, Canada, the United Kingdom and Australia. In the US alone, families spend over $41 billion preparing for the return to school each year — second only to the Christmas holiday season. The timing varies by country: in the US and Canada, school typically resumes in late August or early September after a summer break; in Australia it begins in late January or early February after the Christmas/summer holiday; and in the UK children return in September after the summer holidays.",
      "For retailers, back-to-school is a crucial seasonal moment for categories including clothing, footwear, backpacks, stationery, laptops, tablets and school supplies. Major retailers like Walmart, Target, Amazon, Staples and Best Buy run prominent back-to-school promotions for 4–6 weeks before the start of term. Many US states also run 'sales tax holiday' weekends during the back-to-school period, temporarily exempting clothing, school supplies and computers from state sales tax — creating a significant incentive to buy during a narrow window.",
      "Beyond the commercial aspect, the back-to-school transition represents a genuine milestone for millions of families: the excitement of a new grade, new teachers, new friendships and new challenges. University students heading to college for the first time represent a particularly large spending cohort, purchasing furniture, bedding, electronics, kitchen items and toiletries for dorm rooms and apartments."
    ],
    "key_info": [
      ("US back-to-school spending", "$41 billion+ annually"),
      ("US school return (approx.)", "Mid-August to early September"),
      ("UK school return", "Early September"),
      ("Australia school return", "Late January / early February"),
      ("Top spend categories", "Clothing, electronics, supplies, footwear"),
      ("US college/university spending", "$94 billion annually"),
    ],
    "timeline": [
      ("19th century", "The US standardises a September school start aligned with harvest seasons and urban migration patterns"),
      ("1960s–1970s", "Major US retailers begin targeted back-to-school marketing campaigns"),
      ("1990s", "The rise of personal computers makes electronics a major back-to-school spending category for the first time"),
      ("2010s", "Tablets and smartphones become standard back-to-school purchases; cloud-based school platforms emerge"),
      ("2020", "COVID-19 triggers a massive shift to remote learning, fundamentally changing what families buy for the school year"),
    ],
    "facts": [
      "US back-to-school spending is the second-largest retail season of the year after Christmas, exceeding $41 billion annually.",
      "The average US family spends approximately $890 on back-to-school supplies for K-12 students.",
      "College back-to-school spending in the US exceeds $94 billion annually — larger than K-12 by a significant margin.",
      "Over 17 US states run sales-tax-free holiday weekends during August to encourage back-to-school purchasing.",
      "Backpacks are among the most contested back-to-school items: the average US child goes through 2–3 backpacks during their school years.",
      "Laptops overtook desktop computers as the preferred student computing device by 2012 and now account for the majority of school technology spending.",
    ],
    "faqs": [
      ("When does back to school start in the US?", "US school start dates vary by state and district, but most public schools resume between mid-August and the Tuesday after Labor Day (first Monday of September)."),
      ("When does back to school start in the UK?", "In England, Wales and Northern Ireland, schools typically return in the first week of September. Scotland's school year restarts in mid-August."),
      ("When does back to school start in Australia?", "Australian schools return in late January (most states) to early February (some states) after the summer holiday break."),
      ("What are the best back-to-school deals?", "The best deals on laptops, tablets, school supplies and clothing appear in late July through August in the US. Amazon, Walmart, Target, Staples and Best Buy all run dedicated back-to-school sales. College students should also check for educational discounts from Apple, Microsoft and Adobe."),
      ("What do I need for back to school?", "Essential items vary by age and grade, but typically include: backpack, stationery (pens, pencils, rulers, scissors), notebooks and folders, a calculator, PE kit and appropriate clothing. Many schools provide a specific supply list. High school and college students often also need a laptop or tablet."),
      ("Are there back-to-school tax-free weekends?", "Yes. Many US states run sales-tax holidays for school supplies, clothing and computers in July–August. Dates vary by state — check your state's revenue department website for this year's dates."),
      ("What is the best laptop for school?", "For K-12 students, a Chromebook (budget-friendly, durable) or iPad is often recommended. For high school and university, a Windows laptop or MacBook Air provides more versatility. Look for at least 8GB RAM, 256GB storage and 10-hour battery life."),
      ("How much should I budget for back to school?", "US families average $890 per K-12 child. College students average significantly more ($1,200–$2,500) when including electronics and dorm supplies. University students in the UK should budget £600–£1,200 for a laptop, textbooks and supplies."),
    ],
    "related": ["labor-day", "memorial-day", "thanksgiving", "christmas"],
  },

  # ─── EASTER ───────────────────────────────────────────────────────────────────
  "easter": {
    "overview": [
      "Easter is the most important festival in the Christian calendar, celebrating the resurrection of Jesus Christ from the dead — an event described in the New Testament as occurring three days after his crucifixion. Unlike Christmas, Easter is a moveable feast: it falls on the first Sunday after the first full moon following the spring equinox (March 21), meaning the date can fall anywhere between March 22 and April 25. Easter Sunday is preceded by Holy Week and the fasting period of Lent (40 days), and followed by Eastertide (50 days).",
      "Easter is a public holiday across the UK, Australia, Canada, the United States, and most of Europe and Latin America. In the UK, Australia and Canada, Good Friday (two days before Easter Sunday) and Easter Monday (the day after) are also public holidays, creating a four-day long weekend that is a major travel period. Australia sees its biggest domestic travel surge of the year over the Easter long weekend, and UK roads are among the busiest of the year on Easter Thursday and Friday.",
      "Alongside its religious significance, Easter has a rich tradition of secular customs including egg decorating, egg hunts, hot cross buns and the Easter Bunny — traditions with roots in pre-Christian Germanic spring festivals. Chocolate Easter eggs have become the holiday's dominant commercial expression in the UK, Australia and Ireland: UK consumers spend over £400 million on Easter chocolate every year, while US spending on Easter exceeds $24 billion annually."
    ],
    "key_info": [
      ("Easter 2027", "March 28, 2027"),
      ("Easter 2028", "April 16, 2028"),
      ("Public holiday in", "US, UK, Canada, Australia, most of Europe"),
      ("UK Easter chocolate spend", "£400 million+ per year"),
      ("US total Easter spend", "$24 billion+ annually"),
      ("Good Friday / Easter Monday", "Public holidays in UK, Australia, Canada"),
    ],
    "timeline": [
      ("1st century AD", "The Resurrection of Jesus Christ — the foundational event that Easter commemorates — is recorded in the New Testament Gospels"),
      ("325 AD", "The First Council of Nicaea standardises the date of Easter: first Sunday after the full moon following March 21"),
      ("600s", "Pope Gregory sends missionaries to England; pagan spring festival (Ēostre) merges with Christian Easter celebrations"),
      ("19th century", "German immigrant communities bring the Easter Bunny and egg-hunting traditions to North America"),
      ("1873", "Cadbury introduces the first modern chocolate Easter egg in the UK, revolutionising Easter gifting"),
    ],
    "facts": [
      "The word 'Easter' may derive from 'Ēostre' — an Anglo-Saxon spring goddess mentioned by the Venerable Bede in the 8th century.",
      "Cadbury Creme Eggs are produced at a rate of 1.5 million per day in the months leading up to Easter.",
      "The Easter Island in the Pacific Ocean was named by Dutch explorer Jacob Roggeveen, who arrived there on Easter Sunday, April 5, 1722.",
      "In Ukraine, intricately decorated Easter eggs called <em>pysanky</em> are considered a major national folk art tradition.",
      "Easter is a public holiday in 47 of the 50 US states (when Good Friday is included); Easter Sunday itself is not a federal holiday.",
      "The world's largest Easter egg hunt took place in Winter Park, Florida in 2007 — 9,753 children searched for 501,000 eggs.",
    ],
    "faqs": [
      ("When is Easter 2027?", "Easter Sunday 2027 falls on March 28, 2027."),
      ("When is Easter 2028?", "Easter Sunday 2028 falls on April 16, 2028."),
      ("How is the date of Easter calculated?", "Easter falls on the first Sunday after the first full moon that occurs on or after the spring equinox (March 21). This calculation, known as the 'computus', means Easter can fall anywhere between March 22 and April 25."),
      ("Is Easter a public holiday?", "Easter is a public holiday in the US, UK, Canada, Australia and most European countries. In the UK, Australia and Canada, Good Friday and Easter Monday are also public holidays, creating a four-day weekend."),
      ("What is Good Friday?", "Good Friday is the Friday before Easter Sunday, commemorating the crucifixion of Jesus Christ. It is a public holiday in the UK, Australia, Canada and many other countries, though not a federal holiday in the US."),
      ("What is Easter Monday?", "Easter Monday is the day after Easter Sunday and is a public holiday in the UK, Australia, Canada and most of Europe. In the US it is not an official holiday."),
      ("Why do we have Easter eggs?", "Eggs are an ancient symbol of new life and spring. The Christian tradition associates eggs with the resurrection. Decorated eggs date back to early Christian practice; chocolate eggs became popular after Cadbury introduced them in the UK in 1873."),
      ("What is the Easter Bunny?", "The Easter Bunny is a folkloric figure that delivers chocolate eggs and gifts to children, similar to Santa Claus at Christmas. It derives from German-American immigrant traditions involving a hare delivering eggs on Easter morning."),
      ("What are hot cross buns?", "Hot cross buns are spiced sweet buns marked with a white cross on top, traditionally eaten on Good Friday in the UK, Australia and parts of the Commonwealth. They are now sold from February onwards in supermarkets."),
      ("What do people eat on Easter?", "Traditional Easter foods vary by country: roast lamb is traditional in many Christian cultures; in the UK, Australia and US, chocolate eggs and hot cross buns are staples. Easter Sunday lunch typically features a large family roast."),
    ],
    "related": ["christmas", "thanksgiving", "halloween", "new-year"],
  },

  # ─── VALENTINE'S DAY ──────────────────────────────────────────────────────────
  "valentines": {
    "overview": [
      "Valentine's Day is celebrated on February 14 each year as a day dedicated to love, romance and affection. It is one of the most commercially significant dates on the global calendar: Americans spend around $26 billion on Valentine's Day gifts, flowers and experiences annually, while UK consumers spend over £1 billion. The holiday is also widely observed in Canada, Australia, France, Germany and many other countries, though its commercial intensity varies significantly by region.",
      "The holiday is named after Saint Valentine — or possibly more than one Christian martyr of that name — from the early centuries AD. The romantic associations of Valentine's Day developed in the Middle Ages, notably through the writings of Geoffrey Chaucer and other poets who described February 14 as the time when birds chose their mates. The first recorded Valentine's message was sent by Charles, Duke of Orléans, to his wife in 1415 while imprisoned in the Tower of London. The mass-production of Valentine's cards began in the 1840s in the UK and US.",
      "Today Valentine's Day is the second-largest greeting card sending occasion in the US (after Christmas), with approximately 145 million cards exchanged annually. The most popular gifts are chocolates, flowers (particularly red roses), jewellery, perfume and romantic experiences like restaurant meals. It is the single busiest day of the year for restaurants in most English-speaking countries."
    ],
    "key_info": [
      ("Date", "February 14 every year"),
      ("US spending", "$26 billion annually"),
      ("UK spending", "£1 billion+"),
      ("Cards sent in US", "145 million"),
      ("Most popular gift", "Chocolates, roses, jewellery"),
      ("Busiest day for", "Restaurants, florists, chocolatiers"),
    ],
    "timeline": [
      ("270 AD", "Saint Valentine, a Roman priest, is martyred — his feast day established as February 14"),
      ("1382", "Geoffrey Chaucer's <em>Parlement of Foules</em> is the first recorded association of Valentine's Day with romantic love"),
      ("1415", "Charles, Duke of Orléans, writes what is considered the world's oldest Valentine to his wife while imprisoned in the Tower of London"),
      ("1840s", "Esther Howland begins mass-producing Valentine's cards in the United States; similar commercial cards emerge in Britain"),
      ("2000s", "Online and app-based gifting makes Valentine's Day a significant e-commerce moment; Uber, Airbnb and restaurant booking platforms see annual February 14 spikes"),
    ],
    "facts": [
      "About 1 billion Valentine's Day cards are sent worldwide each year, making it the second-largest card-sending holiday after Christmas.",
      "Teachers receive more Valentine's Day cards than any other group — a tradition driven by US school card-exchange customs.",
      "Red roses are the most popular Valentine's Day flower: the US imports approximately 250 million roses in the weeks before February 14.",
      "Richard Cadbury produced the first Valentine's Day candy box in the 1860s — decorated heart-shaped chocolate boxes became a lasting symbol.",
      "Valentine's Day is the busiest day of the year for US florists, card shops and high-end restaurants.",
      "About 9 million people buy their pets a Valentine's Day gift in the US, spending around $700 million annually on pet-related Valentine's items.",
    ],
    "faqs": [
      ("When is Valentine's Day 2027?", "Valentine's Day 2027 falls on Sunday, February 14."),
      ("When is Valentine's Day 2028?", "Valentine's Day 2028 falls on Monday, February 14."),
      ("Is Valentine's Day a public holiday?", "Valentine's Day is not a public holiday in any country. Shops, schools and offices remain open."),
      ("Who was Saint Valentine?", "Saint Valentine was likely a Christian priest in Rome martyred around 270 AD. His historical connection to romantic love is unclear — the romantic associations developed through medieval literary tradition, particularly Chaucer's poetry."),
      ("What are the most popular Valentine's Day gifts?", "The most popular gifts are: chocolates and sweets, red roses or mixed flowers, jewellery (especially gold and diamonds), perfume, personalised cards and romantic experiences (restaurant dinners, spa breaks, weekend getaways)."),
      ("How much should I spend on a Valentine's Day gift?", "US adults spend an average of $192 on Valentine's Day. UK adults spend around £49 per person. There is no standard amount — the gesture and personalisation matter more than the price."),
      ("When should I book a Valentine's Day restaurant?", "Popular restaurants in major cities can fully book out for February 14 within 24–48 hours of opening reservations — sometimes as early as January. Book as early as possible if you want a specific venue."),
      ("What are good Valentine's Day date ideas?", "Popular ideas include: dinner at a favourite restaurant, a weekend hotel getaway, cooking a meal at home, a live music show or theatre performance, a spa day or couples massage, a scenic hike or picnic, or a cooking class together."),
      ("Do same-sex couples celebrate Valentine's Day?", "Yes. Valentine's Day is broadly inclusive and celebrated by couples of all genders and orientations. It is also increasingly observed as a day to celebrate friendships ('Galentine's Day') and self-love."),
      ("What is Galentine's Day?", "Galentine's Day is an unofficial holiday on February 13, popularised by the TV show <em>Parks and Recreation</em> (2010), celebrating female friendships. Many people now celebrate it as a broader 'friends' day before Valentine's Day."),
    ],
    "related": ["easter", "mothers-day", "christmas", "new-year"],
  },

  # ─── MOTHER'S DAY ─────────────────────────────────────────────────────────────
  "mothers-day": {
    "overview": [
      "Mother's Day is a celebration honouring mothers and motherhood, observed on different dates in different countries. In the United States, Canada, Australia and many other countries, it falls on the second Sunday of May. In the UK and Ireland, it is observed on the fourth Sunday of Lent (Mothering Sunday), which can fall in March or April. The US holiday was formally established by Congress in 1914 following a campaign by activist Anna Jarvis, who ironically later turned against its commercialisation.",
      "Mother's Day is the third-largest retail occasion in the United States, with consumers spending over $35 billion annually. The most popular gifts are flowers (it is the single biggest day for flower purchases in the US), greeting cards, restaurant meals, jewellery, spa services and personalised gifts. Approximately 84 million Americans celebrate Mother's Day, making it one of the most universally observed occasions in the country.",
      "UK Mother's Day — Mothering Sunday — has older roots tied to the Christian calendar: historically it was a day when servants and apprentices were allowed to return home to their 'mother church' and visit their families. Today it is celebrated with flowers, cards and family meals in the same spirit as the US holiday, though its date is earlier in the year, tied to the Lenten calendar rather than the Gregorian calendar."
    ],
    "key_info": [
      ("US/Canada/Australia date", "Second Sunday of May"),
      ("UK / Ireland date", "Fourth Sunday of Lent (March or April)"),
      ("US Mother's Day 2027", "May 9, 2027"),
      ("US spending", "$35 billion+ annually"),
      ("Biggest spending category", "Flowers — largest flower-buying day in US"),
      ("Founded in US", "1914 by Congress, after Anna Jarvis's campaign"),
    ],
    "timeline": [
      ("1860s–1870s", "Julia Ward Howe and Ann Reeves Jarvis advocate for a day honouring mothers, initially as a peace movement"),
      ("1908", "Anna Jarvis holds the first unofficial Mother's Day service in West Virginia after her mother's death"),
      ("1914", "President Woodrow Wilson signs a law establishing the second Sunday of May as Mother's Day in the US"),
      ("1920s", "Anna Jarvis campaigns against the commercialisation of Mother's Day; she spent much of her later life fighting greeting card companies and florists"),
      ("Present", "Mother's Day is observed in over 50 countries, each with its own date and traditions"),
    ],
    "facts": [
      "Mother's Day is the busiest day of the year for US restaurants — many families take mums out for a meal.",
      "The US Postal Service processes more mail on the days around Mother's Day than almost any other time of year, driven by card-sending.",
      "Anna Jarvis, who founded US Mother's Day, never had children herself and died penniless — having spent her inheritance fighting the commercialisation of the holiday she created.",
      "In the UK, Mothering Sunday dates back to the 16th century as a Christian observance of the 'mother church'.",
      "Carnations are the traditional Mother's Day flower in the US; pink and red carnations represent living mothers while white carnations symbolise deceased mothers.",
      "About 113 million Mother's Day cards are sent in the US each year — more than any holiday except Christmas and Valentine's Day.",
    ],
    "faqs": [
      ("When is Mother's Day 2027?", "In the US, Canada and Australia, Mother's Day 2027 falls on Sunday, May 9, 2027."),
      ("When is Mother's Day in the UK?", "UK Mothering Sunday 2027 falls on March 14, 2027 (fourth Sunday of Lent). It is not the same date as US Mother's Day."),
      ("Is Mother's Day a public holiday?", "Mother's Day is not a public holiday in the US, UK, Canada or Australia. Businesses, schools and government offices remain open."),
      ("What are the most popular Mother's Day gifts?", "The most popular gifts are flowers (especially carnations and roses), greeting cards, brunch or dinner at a restaurant, jewellery, spa treatments, personalised items (photo books, engraved jewellery) and gift cards."),
      ("What is the difference between Mother's Day and Mothering Sunday?", "In the US, Canada and Australia, 'Mother's Day' is the secular celebration on the second Sunday of May. In the UK, 'Mothering Sunday' is the traditional Christian observance on the fourth Sunday of Lent — the two are often conflated but are historically distinct."),
      ("How do I plan a Mother's Day restaurant booking?", "Mother's Day is the busiest restaurant day of the year in the US and UK. Book as early as possible — at least 2–3 weeks in advance for popular venues, or earlier in major cities."),
      ("What flowers should I give for Mother's Day?", "Carnations are the traditional US Mother's Day flower. Roses, tulips, peonies and lilies are also popular. In the UK, daffodils are a common Mothering Sunday choice. A personalised bouquet in your mother's favourite colours is always appreciated."),
      ("Why did Anna Jarvis oppose the commercialisation of Mother's Day?", "Anna Jarvis created Mother's Day as a personal and heartfelt tribute to her own mother. She wanted it expressed through handwritten letters, not purchased goods. She was infuriated by greeting card companies, florists and candy makers profiting from her holiday, and spent decades (and her entire fortune) unsuccessfully trying to have it decommercialised."),
    ],
    "related": ["valentines", "fathers-day", "easter", "christmas"],
  },

  # ─── FATHER'S DAY ─────────────────────────────────────────────────────────────
  "fathers-day": {
    "overview": [
      "Father's Day is a celebration honouring fathers and fatherhood, observed on the third Sunday of June in the United States, United Kingdom, Canada, Australia and many other countries. It was first celebrated in the United States in 1910, inspired by Mother's Day, and became a permanent US national holiday in 1972 when President Richard Nixon signed it into law. Today it is one of the most widely observed family celebrations globally, with US consumers spending over $22 billion annually.",
      "The most popular Father's Day gifts are greeting cards, clothing, electronics, tools, sporting goods, restaurant meals and experiences. Father's Day is the peak day for mobile phone gifting in the US and the biggest day for men's grooming purchases. In the US, approximately 75 million fathers are celebrated on Father's Day, with most adult children giving cards, calling or visiting in person.",
      "Like Mother's Day, Father's Day is celebrated on different dates in different countries: Portugal and Spain observe it on March 19 (the feast of Saint Joseph), while Russia celebrates Defender of the Fatherland Day on February 23. The third-Sunday-of-June version, however, is the most globally widespread and includes major markets such as the US, UK, Canada, Australia, Ireland, India and most of Latin America."
    ],
    "key_info": [
      ("Date (US/UK/AU)", "Third Sunday of June"),
      ("Father's Day 2026", "June 21, 2026"),
      ("Father's Day 2027", "June 20, 2027"),
      ("US spending", "$22 billion+ annually"),
      ("First celebrated in US", "1910"),
      ("National US holiday since", "1972 (Nixon)"),
    ],
    "timeline": [
      ("1909", "Sonora Smart Dodd of Washington State proposes a Father's Day holiday, inspired by her own father raising six children alone after her mother's death"),
      ("1910", "Spokane, Washington holds the first Father's Day celebration on June 19"),
      ("1924", "President Calvin Coolidge supports Father's Day nationally, though it remains unofficial"),
      ("1966", "President Lyndon B. Johnson proclaims the third Sunday of June as Father's Day by presidential proclamation"),
      ("1972", "President Nixon signs Father's Day into law as a permanent US national holiday"),
    ],
    "facts": [
      "Father's Day in the US generates over $22 billion in spending — about $6 billion less than Mother's Day, a gap often jokingly noted in surveys.",
      "The most popular Father's Day gift in the US for the past decade has been greeting cards, followed by clothing and electronics.",
      "Sonora Smart Dodd, who founded US Father's Day, was raised by a single father — a Civil War veteran who raised six children on a farm in Washington State.",
      "Father's Day is the second-busiest day for collect and long-distance phone calls in the US, after Mother's Day.",
      "In Germany, Father's Day (Vatertag) is a uniquely raucous celebration: men traditionally hike with wagons full of beer and food on Ascension Day (40 days after Easter).",
      "About 93% of adult children in the US give their fathers a card on Father's Day — making it the fourth-largest card-sending holiday.",
    ],
    "faqs": [
      ("When is Father's Day 2026?", "Father's Day 2026 in the US, UK, Canada and Australia falls on Sunday, June 21, 2026."),
      ("When is Father's Day 2027?", "Father's Day 2027 falls on Sunday, June 20, 2027."),
      ("Is Father's Day a public holiday?", "Father's Day is not a public holiday in the US, UK, Canada or Australia. Schools and businesses remain open."),
      ("What are the best Father's Day gifts?", "Popular gifts include: sports or hobby equipment, clothing and shoes, electronics (headphones, tablets, smartwatches), tools, grilling accessories, restaurant experiences, whisky/beer/wine, personalised gifts, subscription boxes and streaming subscriptions."),
      ("How is Father's Day different from Mother's Day?", "In the US, Father's Day spending averages about $196 per celebrant vs $274 for Mother's Day, though the number of people celebrating is similar. Father's Day tends to skew more toward experiential gifts (golf trips, sports tickets) while Mother's Day skews more toward flowers and fine dining."),
      ("Why is Father's Day in June?", "June was chosen partly to accommodate Washington State's proposal in 1910, and partly because it fell mid-year, balancing Mother's Day in May. The third Sunday of June became standard in the US after various attempts to pin it to other dates."),
      ("What countries celebrate Father's Day on the same date?", "The third Sunday of June is observed in the US, UK, Canada, Australia, Ireland, India, South Africa, Singapore and most of Latin America. Spain and Portugal celebrate Father's Day on March 19 (Saint Joseph's Day). Germany celebrates on Ascension Day."),
      ("How can I celebrate Father's Day?", "Common ways to celebrate: a family meal (brunch, barbecue or restaurant dinner), a day out doing dad's favourite activity, a sports event, a round of golf, a home-cooked breakfast, a handmade card from children, or a personalised gift. Quality time and acknowledgement matter more than spend."),
    ],
    "related": ["mothers-day", "valentines", "thanksgiving", "christmas"],
  },

  # ─── F1 ───────────────────────────────────────────────────────────────────────
  "f1": {
    "overview": [
      "Formula 1 (F1) is the pinnacle of single-seater motorsport and the world's most-watched annual motor racing series. The F1 World Championship has been held every year since 1950, with races taking place across five continents from March to November. Each season consists of 20–24 Grands Prix, held at iconic circuits including Monaco, Silverstone, Monza, Spa-Francorchamps, Suzuka and Las Vegas. The live counter above tracks the time until the next F1 race on the calendar.",
      "The sport has experienced a remarkable surge in global popularity since the mid-2010s, driven substantially by the Netflix docuseries <em>Drive to Survive</em> (launched 2019), which opened F1 to a massive new audience in the United States and beyond. F1 now has over 750 million fans worldwide and generates $3.2 billion in annual revenues. The American Grand Prix in Austin, Texas regularly draws 400,000+ spectators over the race weekend — the largest crowd in Formula 1 history — reflecting the sport's dramatic US growth.",
      "Each F1 car represents approximately $15 million of engineering and is built around a 1.6-litre turbocharged hybrid power unit capable of revving to 15,000 RPM and producing around 1,000 horsepower. The cars can accelerate from 0 to 100 km/h (62 mph) in under 2 seconds and sustain lateral G-forces of 6g in high-speed corners. The Constructors' Championship (team title) and Drivers' Championship (individual title) are the sport's two premier honours."
    ],
    "key_info": [
      ("Season", "March to November/December"),
      ("Races per season", "24 Grands Prix (2024)"),
      ("Most Drivers' titles", "Lewis Hamilton & Michael Schumacher (7 each)"),
      ("Most Constructors' titles", "Ferrari (16)"),
      ("F1 global fan base", "750 million+"),
      ("Top team budgets", "$400–$500 million per year"),
    ],
    "timeline": [
      ("1950", "The first Formula 1 World Championship is held; Nino Farina wins the inaugural Drivers' title driving for Alfa Romeo"),
      ("1994", "Ayrton Senna, three-time world champion, dies in a crash at Imola — a turning point that transformed F1 safety standards"),
      ("2010", "Sebastian Vettel, aged 23, becomes the youngest F1 World Champion in history"),
      ("2019", "Netflix launches <em>Drive to Survive</em> — F1's global fanbase and US audience grow dramatically"),
      ("2021", "Max Verstappen wins his first World Championship in a historic final-lap overtake at Abu Dhabi; Verstappen goes on to win three consecutive titles (2021–2023)"),
    ],
    "facts": [
      "An F1 car's steering wheel alone contains 25+ buttons and functions — and costs approximately $50,000.",
      "F1 tyres are heated to operating temperatures of 100–110°C before and during use — at the wrong temperature they perform poorly.",
      "The Monaco Grand Prix track is so narrow that overtaking is nearly impossible — making qualifying (Saturday) effectively the most important session of the weekend there.",
      "Ayrton Senna (1988–1991) and Michael Schumacher (2000–2004) are considered by many to be the greatest F1 drivers in history, along with Lewis Hamilton.",
      "An F1 pit stop takes an average of 2.5 seconds, with 20 team members operating simultaneously on four tyres.",
      "Ferrari has competed in every single F1 World Championship season since 1950 — the only constructor to do so.",
    ],
    "faqs": [
      ("When is the next F1 race?", "The live countdown above shows the exact time until the next Formula 1 Grand Prix. The full race calendar is available on the official Formula 1 website."),
      ("How many F1 races are there in a season?", "The 2024 F1 season features 24 Grands Prix — the most in the sport's history. The number has grown steadily from 17 races in 2010."),
      ("Who has won the most F1 world championships?", "Lewis Hamilton (UK) and Michael Schumacher (Germany) share the record with 7 Drivers' World Championship titles each. Max Verstappen won three consecutive titles (2021, 2022, 2023)."),
      ("What team has won the most F1 Constructors' championships?", "Ferrari holds the record with 16 Constructors' Championships. Mercedes won an unprecedented 8 consecutive titles from 2014 to 2021. Red Bull Racing has been dominant since 2022."),
      ("How fast do F1 cars go?", "F1 cars reach top speeds of around 350–370 km/h (220–230 mph) on the fastest straights. The fastest official speed recorded in an F1 race was 372.6 km/h by Valtteri Bottas at the 2016 Italian Grand Prix."),
      ("What is a sprint race in F1?", "Sprint races are shorter Saturday races (about 100 km / 60 miles) introduced in 2021. They award championship points and set part of the Sunday grid. Only a few rounds per season feature sprint races."),
      ("How do F1 points work?", "Points are awarded to the top 10 finishers: 25, 18, 15, 12, 10, 8, 6, 4, 2, 1. An additional point is awarded for the fastest lap to a driver finishing in the top 10."),
      ("What is the difference between F1, F2 and F3?", "F1 is the top tier of single-seater racing. F2 (Formula 2) and F3 (Formula 3) are the primary feeder series where drivers develop before reaching F1. Most F1 drivers came through the F2 or F3 system."),
      ("Is F1 popular in the United States?", "F1's US popularity has grown dramatically since <em>Drive to Survive</em> launched in 2019. The US Grand Prix at Circuit of the Americas in Austin regularly breaks F1 attendance records with 400,000+ fans. The Las Vegas Grand Prix (added 2023) and Miami Grand Prix (added 2022) further reflect F1's US ambitions."),
    ],
    "related": ["oscars", "super-bowl", "wimbledon", "olympics-2028"],
  },

  # ─── LA 2028 OLYMPICS ─────────────────────────────────────────────────────────
  "olympics-2028": {
    "overview": [
      "The 2028 Summer Olympics — officially the Games of the XXXIV Olympiad — will be held in Los Angeles, California from July 14 to July 30, 2028. This will be LA's third time hosting the Summer Olympics, after 1932 and 1984, making it one of the most experienced host cities in Olympic history. The Games are expected to attract over 10,500 athletes from more than 200 nations competing across 32 sports and approximately 329 events.",
      "The LA 2028 Olympics are notable for their financial model: unlike many recent host cities that required massive new infrastructure investment, Los Angeles is leveraging existing world-class venues built for the 1984 Games and expanded since. The Coliseum, SoFi Stadium, Crypto.com Arena, Pauley Pavilion and Dodger Stadium are among the venues planned for use. The goal is to deliver a net-positive Games that generates surplus revenue rather than debt — a model the IOC hopes will serve as a template for future Olympics.",
      "Several new sports are confirmed for the LA 2028 programme, including flag football (driven by the sport's massive US popularity), cricket (returning after a 128-year absence), squash, lacrosse and baseball/softball. Flag football's inclusion in particular has generated excitement in the United States, where the NFL's influence on American culture gives it enormous appeal. The Games will be broadcast to an estimated 3.5 billion viewers worldwide."
    ],
    "key_info": [
      ("Dates", "July 14–30, 2028"),
      ("Host city", "Los Angeles, California, USA"),
      ("Previous LA Olympics", "1932, 1984"),
      ("Athletes expected", "10,500+"),
      ("Nations participating", "200+"),
      ("New sports for 2028", "Flag football, cricket, squash, lacrosse"),
    ],
    "timeline": [
      ("1932", "Los Angeles hosts the Summer Olympics for the first time; the event is a success despite the Great Depression"),
      ("1984", "LA hosts again — the Soviet-bloc boycott reduces competition but the Games are hugely profitable and set a commercial template"),
      ("2017", "The IOC awards the 2028 Summer Olympics to Los Angeles, with Paris 2024 awarded simultaneously in a rare dual announcement"),
      ("2024", "Paris 2024 Summer Olympics — widely praised as among the best-organised Games in modern history, raising expectations for LA 2028"),
      ("July 14, 2028", "Opening ceremony at the LA Memorial Coliseum — the same venue used in 1932 and 1984"),
    ],
    "facts": [
      "Los Angeles will become only the third city (after London and Paris) to host the Summer Olympics three times.",
      "The 1984 Los Angeles Olympics generated a then-unprecedented profit of $225 million — changing how Olympic Games are financially structured.",
      "Flag football will make its Olympic debut at LA 2028 — the NFL has been a major advocate for the sport's inclusion.",
      "Cricket returns to the Olympics at LA 2028 for the first time since the Paris 1900 Games, where only two teams competed.",
      "LA 2028 will be the first Summer Olympics primarily funded by private investment rather than public money, aiming to avoid the debt burden seen in Athens 2004, Beijing 2008 and Rio 2016.",
      "The Paralympic Games will follow immediately after, with the LA 2028 Paralympics running from August 15 to 27, 2028.",
    ],
    "faqs": [
      ("When is the 2028 Olympics?", "The LA 2028 Summer Olympics run from July 14 to July 30, 2028. The Opening Ceremony is July 14."),
      ("Where is the 2028 Olympics?", "The 2028 Summer Olympics are held in Los Angeles, California, USA."),
      ("What new sports are in the 2028 Olympics?", "New sports confirmed for LA 2028 include flag football, cricket (T20 format), squash, lacrosse and baseball/softball. Flag football is particularly anticipated given American football's dominance in US culture."),
      ("How can I buy tickets for the 2028 Olympics?", "Tickets for LA 2028 will be sold through the official LA28 website. Registration for access to future ticket sales opens well in advance — check la28.org for the latest information."),
      ("What venues will be used for the 2028 Olympics?", "Key venues include the LA Memorial Coliseum (athletics/opening ceremony), SoFi Stadium (flag football), Crypto.com Arena (basketball), Pauley Pavilion (gymnastics), Dodger Stadium (baseball/softball) and various beach/coastal venues for water sports."),
      ("What is the mascot for the 2028 Olympics?", "LA28 has announced 'Angeles' as the Games' brand character. The full mascot reveal is expected closer to the Games."),
      ("How many athletes compete at the Olympics?", "Approximately 10,500 athletes from 200+ nations are expected to compete at LA 2028, across 32 sports and 329 events."),
      ("What is the Olympic motto?", "The Olympic motto is <em>Citius, Altius, Fortius — Communiter</em>, meaning 'Faster, Higher, Stronger — Together'. The word 'Together' was added in 2021."),
      ("When is the 2032 Olympics?", "The 2032 Summer Olympics will be held in Brisbane, Australia. Brisbane was awarded the Games in July 2021."),
    ],
    "related": ["wimbledon", "f1", "super-bowl", "independence-day"],
  },

  # ─── OSCARS ───────────────────────────────────────────────────────────────────
  "oscars": {
    "overview": [
      "The Academy Awards — universally known as the Oscars — are the most prestigious awards in the global film industry, presented annually by the Academy of Motion Picture Arts and Sciences (AMPAS) since 1929. Held in Los Angeles each spring (typically March), the ceremony is broadcast to an estimated 35–50 million viewers in the United States and hundreds of millions internationally. The golden Oscar statuette is the most recognised trophy in entertainment and winning one is considered the pinnacle of a film career.",
      "The Academy was founded in 1927 by MGM studio chief Louis B. Mayer and originally had 36 members. Today AMPAS has over 10,000 voting members across 17 branches, representing every aspect of filmmaking from actors to cinematographers, directors to visual effects artists. Each branch votes for nominees and winners in its own category, with the full membership voting for Best Picture. The eligibility window runs from January 1 to December 31 of the prior year, making December a particularly intense period for major film releases seeking awards consideration.",
      "The Oscars' cultural footprint extends well beyond film: the ceremony consistently generates billions of dollars of media coverage, can transform a film's box office performance (a Best Picture win typically adds $25–$60 million in post-ceremony theatrical revenues), and influences the careers of actors, directors and writers for decades. The ceremony is held at the Dolby Theatre in Hollywood, preceded by the famous red carpet where fashion choices are scrutinised by hundreds of journalists worldwide."
    ],
    "key_info": [
      ("First ceremony", "May 16, 1929 (12th May 1929 by current calendar)"),
      ("Host venue", "Dolby Theatre, Hollywood, Los Angeles"),
      ("Voting body", "10,000+ AMPAS members"),
      ("Most Best Picture wins", "Ben-Hur, Titanic, Lord of the Rings: Return of the King (11 each)"),
      ("Most acting wins", "Katharine Hepburn (4 Best Actress)"),
      ("US TV viewers", "35–50 million annually"),
    ],
    "timeline": [
      ("May 1929", "First Academy Awards ceremony — a 15-minute private dinner at the Hollywood Roosevelt Hotel; Wings wins Best Picture"),
      ("1953", "The ceremony is televised for the first time, watched by 43 million Americans"),
      ("1974", "David Niven is interrupted mid-speech by a streaker — one of the most infamous moments in Oscar history"),
      ("1998", "Titanic wins 11 Oscars, tying the all-time record held by Ben-Hur"),
      ("2022", "Will Smith slaps presenter Chris Rock on stage — the most-discussed moment in Oscars history for decades"),
    ],
    "facts": [
      "The Oscar statuette stands 34.3 cm (13.5 inches) tall, weighs 3.8 kg (8.5 lbs) and is made of britannium plated in gold.",
      "The longest Best Picture winner is <em>Gone with the Wind</em> (1939) at 3 hours 58 minutes.",
      "The first Best Picture winner was <em>Wings</em> (1927) — a silent film about World War I fighter pilots.",
      "Meryl Streep holds the record for most Oscar nominations with 21, winning 3 times.",
      "The entire 1st Academy Awards ceremony in 1929 lasted just 15 minutes.",
      "Only 3 films have won all 5 major categories (Best Picture, Director, Actor, Actress, Screenplay): <em>It Happened One Night</em>, <em>One Flew Over the Cuckoo's Nest</em> and <em>The Silence of the Lambs</em>.",
    ],
    "faqs": [
      ("When are the Oscars 2027?", "The 99th Academy Awards are expected in March 2027. The exact date will be confirmed by AMPAS closer to the time."),
      ("Where are the Oscars held?", "The Academy Awards ceremony has been held at the Dolby Theatre in Hollywood, Los Angeles since 2002."),
      ("How are Oscar winners decided?", "Oscar nominees are selected by members of the relevant Academy branch (e.g., actors nominate actors). Winners in most categories are then chosen by the full Academy membership of 10,000+ members. Best Picture uses a preferential ballot system."),
      ("What film has won the most Oscars?", "Three films share the record with 11 wins each: <em>Ben-Hur</em> (1959), <em>Titanic</em> (1997) and <em>The Lord of the Rings: The Return of the King</em> (2003)."),
      ("Who has the most Oscar nominations?", "Meryl Streep holds the record with 21 acting nominations (3 wins). Walt Disney received the most Oscars overall — 22 competitive and 4 honorary Oscars."),
      ("What is the Best Picture Oscar?", "Best Picture is the highest honour at the Academy Awards, awarded to the producers of the winning film. It is the last award of the evening and the most prestigious."),
      ("What is the Oscar eligibility period?", "Films must be released in US cinemas between January 1 and December 31 of the qualifying year. This is why many awards-contending films are released in November and December."),
      ("How long is the Oscars ceremony?", "The Academy Awards ceremony typically runs 3 to 3.5 hours, though some ceremonies have exceeded 4 hours. The red carpet pre-show usually begins 2 hours before the telecast."),
      ("Can I attend the Oscars?", "The Academy Awards are a ticketed private industry event — tickets are not available to the general public. Seats are allocated to AMPAS members, nominees, presenters and studio guests."),
      ("What is the Oscars red carpet?", "The red carpet outside the Dolby Theatre is where celebrities arrive before the ceremony, photographed and interviewed by hundreds of press and broadcasters. It begins 2 hours before the telecast and is a major fashion event in its own right."),
    ],
    "related": ["grammys", "met-gala", "f1", "super-bowl"],
  },

  # ─── MEMORIAL DAY ─────────────────────────────────────────────────────────────
  "memorial-day": {
    "overview": [
      "Memorial Day is a US federal holiday observed on the last Monday of May that honours the men and women who died while serving in the United States armed forces. It is one of the nation's most solemn civic observances, marked by ceremonies at cemeteries and memorials, the display of the American flag and a presidential proclamation. The most significant ceremony takes place at Arlington National Cemetery in Virginia, where the President or Vice President lays a wreath at the Tomb of the Unknown Soldier.",
      "Memorial Day has its origins in the aftermath of the Civil War, when communities in both the North and South began holding ceremonies to decorate the graves of fallen soldiers with flowers — a practice that gave rise to the holiday's original name, Decoration Day. The holiday was officially proclaimed in 1868 by General John A. Logan, commander of the Grand Army of the Republic, and originally observed on May 30. Congress moved it to the last Monday of May in 1971 to create a consistent three-day weekend.",
      "In practice, Memorial Day weekend is also the unofficial start of summer in the United States — a long weekend of barbecues, beach trips, outdoor events and retail sales. Americans travel in enormous numbers: Memorial Day weekend is one of the busiest travel periods of the year, with an estimated 38 million Americans making trips of 50 miles or more. Major US retailers use the long weekend to launch summer sales events, and auto dealers have historically offered some of the year's best new car deals on Memorial Day weekend."
    ],
    "key_info": [
      ("Date", "Last Monday of May"),
      ("Memorial Day 2026", "May 25, 2026"),
      ("Memorial Day 2027", "May 31, 2027"),
      ("Original name", "Decoration Day"),
      ("Proclaimed", "1868 by General John A. Logan"),
      ("Americans who travel", "38 million+ over Memorial Day weekend"),
    ],
    "timeline": [
      ("1865", "Communities in the North and South begin decorating soldiers' graves after the Civil War — the practice that becomes Memorial Day"),
      ("May 30, 1868", "General John A. Logan proclaims the first national Decoration Day; flowers are placed on graves at Arlington National Cemetery"),
      ("1882", "The name 'Memorial Day' begins to be used alongside 'Decoration Day'"),
      ("1966", "Congress and President Johnson declare Waterloo, New York, the official birthplace of Memorial Day"),
      ("1971", "Congress moves Memorial Day to the last Monday in May as part of the Uniform Monday Holiday Act"),
    ],
    "facts": [
      "At 3 PM local time on Memorial Day, Americans are asked to pause for a National Moment of Remembrance — a practice established by Congress in 2000.",
      "The tradition of placing red poppies on graves for Memorial Day was popularised by the 1915 poem <em>In Flanders Fields</em> by Canadian Lieutenant Colonel John McCrae.",
      "Memorial Day weekend is one of the most dangerous driving weekends in the US — traffic fatality rates spike due to the volume of travel.",
      "More than 620,000 US soldiers died in the Civil War — the bloodiest conflict in American history — which directly inspired the creation of Memorial Day.",
      "The American flag is flown at half-staff until noon on Memorial Day, then raised to full staff for the rest of the day.",
      "Approximately 24 million living US veterans are honoured on Memorial Day, along with all who have fallen in service.",
    ],
    "faqs": [
      ("When is Memorial Day 2026?", "Memorial Day 2026 falls on Monday, May 25, 2026."),
      ("When is Memorial Day 2027?", "Memorial Day 2027 falls on Monday, May 31, 2027."),
      ("What is Memorial Day?", "Memorial Day is a US federal holiday that honours military personnel who died while serving in the US armed forces. It is observed on the last Monday of May."),
      ("What is the difference between Memorial Day and Veterans Day?", "Memorial Day (last Monday of May) honours military personnel who died in service. Veterans Day (November 11) honours all US military veterans — both living and deceased — for their service."),
      ("Is Memorial Day a public holiday?", "Yes. Memorial Day is a federal public holiday in the United States. Government offices, banks, schools and many businesses are closed."),
      ("What is the National Moment of Remembrance?", "Since 2000, Congress has asked all Americans to pause for one minute of silence at 3 PM local time on Memorial Day to honour fallen service members."),
      ("What happens at Arlington National Cemetery on Memorial Day?", "The President or Vice President lays a wreath at the Tomb of the Unknown Soldier at Arlington National Cemetery in Virginia — the most significant Memorial Day ceremony in the country."),
      ("Are stores open on Memorial Day?", "Most major retailers and supermarkets are open on Memorial Day, often running major sales promotions. However, government offices, banks, post offices and schools are closed."),
      ("What is the Memorial Day weekend sale?", "Memorial Day weekend is a major US retail sales event, particularly for mattresses, appliances, furniture, outdoor goods and new cars. Many retailers offer some of the year's best discounts over the three-day weekend."),
    ],
    "related": ["independence-day", "labor-day", "thanksgiving", "veterans-day"],
  },

  # ─── WIMBLEDON ────────────────────────────────────────────────────────────────
  "wimbledon": {
    "overview": [
      "Wimbledon — officially The Championships, Wimbledon — is the oldest and most prestigious tennis tournament in the world, held annually at the All England Lawn Tennis and Croquet Club in Wimbledon, south-west London. First held in 1877, it is one of the four Grand Slam tournaments alongside the Australian Open, French Open and US Open, and is widely regarded as the most prestigious of the four. Wimbledon is the only Grand Slam still played on grass — the surface on which tennis was originally invented — giving it a unique character and playing style.",
      "Wimbledon takes place over two weeks in late June and early July, with matches contested on 18 courts including the iconic Centre Court (capacity 15,000) and No. 1 Court (capacity 12,000). The Championships attract over 500,000 spectators across the fortnight, with millions more watching on television globally. BBC coverage in the UK is watched by up to 14 million viewers for the men's final, while ESPN and Tennis Channel carry the broadcast in the United States.",
      "The tournament is famous for strict traditions: all players must wear predominantly white clothing, play is preceded by curtseying to the Royal Box (though this was made optional in 2003), and strawberries with cream are consumed in their millions — around 28,000 kg of strawberries and 10,000 litres of cream are sold at Wimbledon each year. The queue to buy day tickets — 'The Queue' — is itself a cultural institution, with fans camping overnight for the chance to attend."
    ],
    "key_info": [
      ("Wimbledon 2026 dates", "June 29 – July 12, 2026"),
      ("Surface", "Grass"),
      ("Founded", "1877"),
      ("Location", "All England Club, Wimbledon, London"),
      ("Spectators per year", "500,000+"),
      ("Strawberries sold", "28,000 kg per Championships"),
    ],
    "timeline": [
      ("1877", "The first Wimbledon Championships is held; Spencer Gore wins the men's singles — the only event contested"),
      ("1884", "Women's singles and men's doubles are added to the programme"),
      ("1968", "Wimbledon becomes the first Grand Slam to admit professional players — the dawn of the Open Era"),
      ("2009", "The retractable roof over Centre Court is completed, ending rain delays on the main show court"),
      ("2022", "Russian and Belarusian players are banned from Wimbledon following Russia's invasion of Ukraine — the only Grand Slam to impose such a ban"),
    ],
    "facts": [
      "Wimbledon is the only Grand Slam tournament played on grass — the surface tennis was originally invented for.",
      "Roger Federer holds the men's record with 8 Wimbledon singles titles. Martina Navratilova holds the women's record with 9 titles.",
      "Wimbledon players are required to wear predominantly white clothing — any colour must be 'minimal' and confined to a single trim of 1cm or less.",
      "The grass courts at Wimbledon are mowed to exactly 8mm — maintained by a grounds team of over 30 people working year-round.",
      "Wimbledon is the world's second-largest annual sporting event by global audience, behind only the Olympics.",
      "The prize money at Wimbledon 2024 was £50 million total — with £2.7 million for each singles champion.",
    ],
    "faqs": [
      ("When is Wimbledon 2026?", "Wimbledon 2026 runs from Monday, June 29 to Sunday, July 12, 2026."),
      ("When is Wimbledon 2027?", "Wimbledon 2027 is expected to run from late June to mid-July 2027. The exact dates will be confirmed by the All England Club."),
      ("Where is Wimbledon held?", "Wimbledon is held at the All England Lawn Tennis and Croquet Club (AELTC) in Wimbledon, south-west London, UK. SW19 is the postcode famously associated with the Championships."),
      ("How do I get tickets for Wimbledon?", "Wimbledon tickets are obtained via: (1) the public ballot, which opens in the autumn before the Championships; (2) The Queue — joining the line outside the grounds on the day (limited same-day ground passes and court tickets are available daily); (3) corporate hospitality packages. Debenture holders (long-term seat-holders) also have guaranteed access."),
      ("What surface is Wimbledon played on?", "Wimbledon is played on natural grass — the only Grand Slam to use this surface. The courts are maintained to 8mm height and are prepared year-round by a dedicated grounds team."),
      ("Who has won the most Wimbledon titles?", "In the Open Era (1968–present), Roger Federer holds the men's record with 8 titles. Martina Navratilova holds the women's record with 9 titles. Novak Djokovic has 7 men's titles."),
      ("What is 'The Queue' at Wimbledon?", "The Queue is the famous unofficial line of fans who camp overnight outside the All England Club to buy day tickets on the morning of play. Ground passes (allowing entry to the outer courts) are always available on the day; Centre Court and No. 1 Court tickets are more limited. The Queue is a British cultural institution and has its own dedicated Wimbledon page of tips and etiquette."),
      ("What are the Wimbledon dress code rules?", "Players must wear predominantly white clothing at all times on court. White must be the primary colour and any non-white colours (including within patterns) must be a single trim no wider than 1cm. Undershorts and compression shorts must also be white."),
      ("Why are strawberries and cream associated with Wimbledon?", "Strawberries have been sold at Wimbledon since the late 19th century, coinciding with the British strawberry season. Around 28,000 kg of strawberries and 10,000 litres of cream are consumed at Wimbledon each year. The combination has become inseparable from the event's British summer character."),
      ("Can I watch Wimbledon on TV in the US?", "In the United States, Wimbledon is broadcast on ESPN and the Tennis Channel, with additional streaming via the ESPN app and ESPN+. In the UK, Wimbledon is on BBC One and BBC Two (free-to-air) as well as the BBC iPlayer streaming service."),
    ],
    "related": ["f1", "olympics-2028", "super-bowl", "easter"],
  },

  # ─── LABOR DAY ────────────────────────────────────────────────────────────────
  "labor-day": {
    "overview": [
      "Labor Day in the United States and Canada is a federal public holiday observed on the first Monday of September, dedicated to the social and economic achievements of the working class. It marks the unofficial end of summer — with school returning in the days before or after, and outdoor events winding down — making it one of the most significant transitional moments of the US and Canadian calendar. Over 35 million Americans travel during Labor Day weekend, making it one of the three busiest travel weekends of the year.",
      "The US Labor Day holiday was born out of the late 19th-century labour movement, a turbulent period of industrial expansion, long working hours and poor conditions. Labour unions in New York City organised the first Labor Day parade on September 5, 1882, attracting 10,000 workers. The holiday spread to other states and was declared a federal holiday by Congress in 1894, during the aftermath of the Pullman Strike — a nationwide railway workers' strike that had paralysed the country and resulted in the deaths of 13 strikers.",
      "Labor Day weekend is a major commercial event: retail sales in the US during Labor Day weekend typically exceed $12 billion, with major promotions on furniture, appliances, mattresses, cars and clothing. It is also the last major outdoor event weekend before the autumn — beaches, theme parks, sports venues and national parks see peak attendance. College football's opening weekend typically coincides with Labor Day, adding a major sporting dimension to the holiday."
    ],
    "key_info": [
      ("Date (US/Canada)", "First Monday of September"),
      ("Labor Day 2026", "September 7, 2026"),
      ("Labor Day 2027", "September 6, 2027"),
      ("First US Labor Day parade", "September 5, 1882 (New York City)"),
      ("Federal holiday since", "1894"),
      ("Americans who travel", "35 million+ over the weekend"),
    ],
    "timeline": [
      ("September 5, 1882", "First Labor Day parade held in New York City by the Central Labor Union, attracting 10,000 workers"),
      ("1887", "Oregon becomes the first US state to make Labor Day an official public holiday"),
      ("1894", "Congress passes the Labor Day bill and President Grover Cleveland signs it into law — six days after federal troops ended the Pullman Strike"),
      ("1938", "The Fair Labor Standards Act establishes the 40-hour work week in the US, enshrining many of the rights Labor Day was created to champion"),
      ("Present", "Labor Day weekend is the last major summer weekend in the US — marked by retail sales, outdoor events and college football"),
    ],
    "facts": [
      "Labor Day in most other countries (including the UK, Australia, and most of Europe) is observed on May 1 — International Workers' Day.",
      "The first Labor Day parade in 1882 featured workers carrying signs reading 'Eight Hours for Work, Eight Hours for Rest, Eight Hours for Recreation'.",
      "President Grover Cleveland signed Labor Day into federal law just six days after ordering federal troops to break the Pullman Strike — a politically calculated move to ease tensions with the labour movement.",
      "Labor Day weekend is one of the busiest weekends for new car sales in the US, alongside Memorial Day and Fourth of July.",
      "The tradition of 'no white after Labor Day' in fashion dates from Gilded Age social etiquette, when white summer clothing was packed away after the holiday. The rule has largely faded in modern fashion.",
      "College football's season typically begins on Labor Day weekend, generating billions in associated economic activity across host cities.",
    ],
    "faqs": [
      ("When is Labor Day 2026?", "Labor Day 2026 in the United States and Canada falls on Monday, September 7, 2026."),
      ("When is Labor Day 2027?", "Labor Day 2027 falls on Monday, September 6, 2027."),
      ("What is Labor Day?", "Labor Day is a US and Canadian federal holiday on the first Monday of September, honouring the contributions of workers and the labour movement. It marks the unofficial end of summer and is associated with long-weekend travel, retail sales and outdoor events."),
      ("Is Labor Day the same in all countries?", "No. In the US and Canada, Labor Day is the first Monday of September. Most other countries, including the UK, Australia and those in Europe, observe International Workers' Day on May 1."),
      ("Is Labor Day a public holiday?", "Yes. Labor Day is a federal public holiday in the United States and Canada. Government offices, banks, schools and many businesses are closed."),
      ("What is open on Labor Day?", "Major supermarkets, most big-box retailers (Walmart, Target, Home Depot) and restaurants are typically open on Labor Day, often running sales. Government offices, banks, US Postal Service and schools are closed."),
      ("What are the best Labor Day sales?", "Labor Day is a major sales event for furniture, mattresses, appliances, TVs, clothing and new cars. Many retailers offer 20–40% discounts. It is traditionally one of the best times of the year to buy a new vehicle."),
      ("Why is Labor Day in September in the US?", "The first US Labor Day was held in September 1882 and the date stuck. Congress chose not to align with May 1 (International Workers' Day) partly because May 1 had become associated with socialist and communist movements, which were politically sensitive in the US."),
      ("What is the 'no white after Labor Day' rule?", "This is a fashion guideline from the Gilded Age (late 19th century) suggesting that white summer clothes should not be worn after Labor Day. The rule has faded significantly in modern fashion and is widely ignored, though it persists as a cultural reference."),
    ],
    "related": ["memorial-day", "independence-day", "thanksgiving", "back-to-school"],
  },

}
