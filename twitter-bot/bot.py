import tweepy
import random
import os
import json
from datetime import datetime, timezone
from dotenv import load_dotenv

load_dotenv()

# ── Twitter client ────────────────────────────────────────────────────────────
client = tweepy.Client(
    consumer_key=os.getenv("API_KEY"),
    consumer_secret=os.getenv("API_SECRET"),
    access_token=os.getenv("ACCESS_TOKEN"),
    access_token_secret=os.getenv("ACCESS_TOKEN_SECRET")
)

# ── Event names ───────────────────────────────────────────────────────────────
NAMES = {
    "gta6": "GTA VI", "iphone": "iPhone 2026", "f1": "the next F1 race",
    "world-cup": "the 2026 FIFA World Cup", "ucl-final": "the Champions League Final",
    "nba-finals": "the NBA Finals", "le-mans": "24 Hours of Le Mans",
    "wimbledon": "Wimbledon", "tour-de-france": "Tour de France",
    "olympics-2028": "the 2028 Olympics", "super-bowl": "the Super Bowl",
    "copa-libertadores": "the Copa Libertadores Final",
    "christmas": "Christmas", "new-year": "New Year's",
    "halloween": "Halloween", "valentines": "Valentine's Day",
    "easter": "Easter", "mothers-day": "Mother's Day",
    "fathers-day": "Father's Day", "thanksgiving": "Thanksgiving",
    "black-friday": "Black Friday", "cyber-monday": "Cyber Monday",
    "full-moon": "the next full moon", "eclipse": "the next eclipse",
    "oscars": "the Oscars", "grammys": "the Grammys",
    "met-gala": "the Met Gala", "cannes": "Cannes Film Festival",
    "coachella": "Coachella", "eurovision": "Eurovision",
    "lollapalooza-ar": "Lollapalooza Argentina",
    "lollapalooza-cl": "Lollapalooza Chile",
    "rock-in-rio": "Rock in Rio",
    "nyfw": "New York Fashion Week", "paris-fw": "Paris Fashion Week",
    "elecciones-ar": "Argentina's elections",
    "bastille-day": "Bastille Day",
    "dia-de-los-muertos": "Día de los Muertos",
}

# ── Hashtags per event ────────────────────────────────────────────────────────
HASHTAGS = {
    "world-cup":        "#WorldCup2026 #FIFA",
    "ucl-final":        "#UCLFinal #ChampionsLeague",
    "f1":               "#F1 #Formula1",
    "nba-finals":       "#NBAFinals #NBA",
    "super-bowl":       "#SuperBowl #NFL",
    "wimbledon":        "#Wimbledon #Tennis",
    "le-mans":          "#LeMans24 #LeMans",
    "tour-de-france":   "#TourDeFrance",
    "olympics-2028":    "#Olympics2028 #Olympics",
    "copa-libertadores":"#Libertadores #Conmebol",
    "oscars":           "#Oscars #AcademyAwards",
    "grammys":          "#GRAMMYs",
    "met-gala":         "#MetGala",
    "cannes":           "#Cannes #CannesFilmFestival",
    "coachella":        "#Coachella",
    "eurovision":       "#Eurovision",
    "christmas":        "#Christmas #Xmas",
    "new-year":         "#NewYear #NYE",
    "halloween":        "#Halloween",
    "black-friday":     "#BlackFriday",
    "cyber-monday":     "#CyberMonday",
    "thanksgiving":     "#Thanksgiving",
    "valentines":       "#ValentinesDay",
    "mothers-day":      "#MothersDay",
    "fathers-day":      "#FathersDay",
    "easter":           "#Easter",
    "gta6":             "#GTA6 #GTAVI #RockstarGames",
    "iphone":           "#iPhone #Apple",
    "full-moon":        "#FullMoon",
    "eclipse":          "#Eclipse",
    "lollapalooza-ar":  "#Lollapalooza",
    "lollapalooza-cl":  "#Lollapalooza",
    "rock-in-rio":      "#RockInRio",
    "nyfw":             "#NYFW #FashionWeek",
    "paris-fw":         "#ParisFashionWeek #PFW",
}

# ── Engagement questions per event ────────────────────────────────────────────
QUESTIONS = {
    "world-cup":        ("Who's winning the 2026 World Cup? 🏆\n\n{days} days to go.", "#WorldCup2026 #FIFA"),
    "ucl-final":        ("Who lifts the trophy at the Champions League Final? 🏆\n\n{days} days left.", "#UCLFinal #ChampionsLeague"),
    "f1":               ("Who's taking the win at the next F1 race? 🏎️\n\n{days} days to go.", "#F1 #Formula1"),
    "nba-finals":       ("NBA Finals in {days} days — who's your pick? 🏀", "#NBAFinals #NBA"),
    "super-bowl":       ("Super Bowl in {days} days. Who wins? 🏈\n\nDrop your prediction 👇", "#SuperBowl #NFL"),
    "wimbledon":        ("Wimbledon is {days} days away 🎾\n\nWho wins the men's and women's titles this year?", "#Wimbledon #Tennis"),
    "oscars":           ("The Oscars are in {days} days 🎬\n\nWhat's your Best Picture prediction?", "#Oscars #AcademyAwards"),
    "grammys":          ("The GRAMMYs are in {days} days 🎵\n\nWho wins Album of the Year?", "#GRAMMYs"),
    "christmas":        ("Christmas is {days} days away 🎄\n\nAre you ready?", "#Christmas"),
    "halloween":        ("Halloween in {days} days 🎃\n\nAlready have a costume idea?", "#Halloween"),
    "coachella":        ("Coachella is {days} days away 🎸\n\nWho are you most excited to see?", "#Coachella"),
    "gta6":             ("GTA VI drops in {days} days 🎮\n\nAre you ready? What are you expecting?", "#GTA6 #GTAVI"),
    "olympics-2028":    ("The 2028 Olympics are in {days} days 🏅\n\nWhich sport are you most excited for?", "#Olympics2028"),
    "black-friday":     ("Black Friday is {days} days away 🛍️\n\nWhat's on your list this year?", "#BlackFriday"),
    "met-gala":         ("The Met Gala is in {days} days 👗\n\nWhose look are you most excited to see?", "#MetGala"),
    "thanksgiving":     ("Thanksgiving is {days} days away 🦃\n\nWhat's your favorite dish?", "#Thanksgiving"),
    "valentines":       ("Valentine's Day is {days} days away 💝\n\nDo you already have plans?", "#ValentinesDay"),
    "tour-de-france":   ("Tour de France starts in {days} days 🚴\n\nWho wins this year?", "#TourDeFrance"),
    "wimbledon":        ("Wimbledon is {days} days away 🎾\n\nWho wins the title this year?", "#Wimbledon #Tennis"),
    "le-mans":          ("24 Hours of Le Mans in {days} days 🏁\n\nWho's your pick to win?", "#LeMans24"),
}

# ── URL pattern ───────────────────────────────────────────────────────────────
URL_BASE = "https://countdowns.site/countdown/{slug}/"

# ── Tweet templates by days-range ─────────────────────────────────────────────
# "close"  → days <= 30
# "medium" → 31–90 days
# "far"    → > 90 days
#
# All "countdown" templates include {url} → Twitter will show OG image preview.
# "question" templates have no URL → plain text, no image.

TEMPLATES = {
    "close": [
        # Urgency / excitement
        "🚨 {days} days until {name}. It's almost time. → {url} {hashtags}",
        "⏳ Only {days} days left until {name}. → {url} {hashtags}",
        "🔥 {name} is {days} days away. Things are heating up. → {url} {hashtags}",
        "📢 {days} days to {name}. Don't miss it. → {url} {hashtags}",
        "⚡ {name} in {days} days. Get ready. → {url} {hashtags}",
        "🎯 {days} days. {name} is RIGHT around the corner. → {url} {hashtags}",
        "👀 {days} days until {name}. Are you ready? → {url} {hashtags}",
        "📅 We're {days} days out from {name}. The countdown is on. → {url} {hashtags}",
        "🏁 {days} days to go. {name} is almost here. → {url} {hashtags}",
        "⏰ T-minus {days} days until {name}. → {url} {hashtags}",
    ],
    "medium": [
        # Building anticipation
        "📅 {name} is {days} days away. Start getting excited. → {url} {hashtags}",
        "🗓️ Mark your calendar — {name} in {days} days. → {url} {hashtags}",
        "⏱️ {days} days until {name}. The wait is real. → {url} {hashtags}",
        "📌 {name} is coming. {days} days to go. → {url} {hashtags}",
        "🔔 Reminder: {name} is in {days} days. → {url} {hashtags}",
        "🧭 {days} days on the clock until {name}. → {url} {hashtags}",
        "📊 {days} days until {name}. Track the countdown live → {url} {hashtags}",
        "🎯 {days} days until {name}. Already counting. → {url} {hashtags}",
        "⌛ {days} days. That's how long until {name}. → {url} {hashtags}",
        "🗓️ {name} in {days} days. Time flies. → {url} {hashtags}",
        "📍 {days} days to {name}. Don't lose track. → {url} {hashtags}",
        "🔢 {days} days and counting until {name}. → {url} {hashtags}",
    ],
    "far": [
        # Patience / long wait
        "📅 {days} days until {name}. The wait begins. → {url} {hashtags}",
        "🗓️ {name} is still {days} days away. Plan ahead. → {url} {hashtags}",
        "⏳ {days} days until {name}. Patience is a virtue. → {url} {hashtags}",
        "📌 Save the date — {name} is {days} days from now. → {url} {hashtags}",
        "🔭 {days} days until {name}. Far but worth the wait. → {url} {hashtags}",
        "📊 {days} days on the clock until {name}. Start counting. → {url} {hashtags}",
        "🗓️ {name} — {days} days to go. Mark it. → {url} {hashtags}",
        "⏱️ {days} days. That's how far away {name} still is. → {url} {hashtags}",
        "🔔 Just a heads up — {name} is in {days} days. → {url} {hashtags}",
        "📅 {days} days until {name}. The countdown starts now. → {url} {hashtags}",
        "🧭 {days} days to {name}. Follow the live countdown → {url} {hashtags}",
        "🗓️ {name} is {days} days away. Still a while, but here we go. → {url} {hashtags}",
    ],
}

# ── Language weights — English only ──────────────────────────────────────────
LANG_WEIGHTS = [("en", 100)]

# ── Tweet type weights ────────────────────────────────────────────────────────
# 70% countdown (with URL+image), 30% question (no URL, no image)
TWEET_TYPE_WEIGHTS = [("countdown", 70), ("question", 30)]

# ── Load real countdown data ──────────────────────────────────────────────────
def load_events():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    data_path = os.path.join(script_dir, "..", "countdowns-data.json")
    with open(data_path) as f:
        data = json.load(f)
    return data["events"]

def get_days_remaining(date_str):
    if not date_str:
        return None
    try:
        dt = datetime.fromisoformat(date_str)
        if dt.tzinfo is None:
            dt = dt.replace(tzinfo=timezone.utc)
        now = datetime.now(timezone.utc)
        delta = (dt - now).days
        return delta if delta >= 0 else None
    except Exception:
        return None

def pick_event():
    events = load_events()
    candidates = []
    for slug, event_data in events.items():
        if slug not in NAMES:
            continue
        days = get_days_remaining(event_data.get("date"))
        if days is None or days == 0:
            continue
        candidates.append((slug, days))
    if not candidates:
        return None
    return random.choice(candidates)

def days_range(days):
    if days <= 30:
        return "close"
    elif days <= 90:
        return "medium"
    else:
        return "far"

# ── Post tweet ────────────────────────────────────────────────────────────────
def post_tweet():
    result = pick_event()
    if not result:
        print("No valid events found.")
        return

    slug, days = result
    name = NAMES[slug]
    url = URL_BASE.format(slug=slug)
    hashtags = HASHTAGS.get(slug, "")

    # Pick tweet type
    types, type_w = zip(*TWEET_TYPE_WEIGHTS)
    tweet_type = random.choices(types, weights=type_w, k=1)[0]

    # Fall back to countdown if no question defined for this event
    if tweet_type == "question" and slug not in QUESTIONS:
        tweet_type = "countdown"

    if tweet_type == "question":
        question_template, q_hashtags = QUESTIONS[slug]
        tweet = question_template.format(days=days, name=name) + "\n\n" + q_hashtags
    else:
        template = random.choice(TEMPLATES[days_range(days)])
        tweet = template.format(days=days, name=name, url=url, hashtags=hashtags).strip()

    # Safety: Twitter limit is 280 chars
    if len(tweet) > 280:
        tweet = tweet[:277] + "..."

    try:
        client.create_tweet(text=tweet)
        print(f"[{tweet_type}][{days_range(days)}] Tweet posted: {tweet}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    post_tweet()
