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

# ── Event names per language ──────────────────────────────────────────────────
NAMES = {
    "en": {
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
        "rock-in-rio": "Rock in Rio",
        "nyfw": "New York Fashion Week", "paris-fw": "Paris Fashion Week",
    },
    "es": {
        "gta6": "GTA VI", "iphone": "iPhone 2026", "f1": "la próxima carrera de F1",
        "world-cup": "la Copa del Mundo 2026", "ucl-final": "la Final de Champions League",
        "nba-finals": "las Finales de la NBA", "le-mans": "las 24 Horas de Le Mans",
        "wimbledon": "Wimbledon", "tour-de-france": "el Tour de Francia",
        "olympics-2028": "los Juegos Olímpicos 2028", "super-bowl": "el Super Bowl",
        "copa-libertadores": "la Final de Copa Libertadores",
        "christmas": "Navidad", "new-year": "Año Nuevo",
        "halloween": "Halloween", "valentines": "San Valentín",
        "easter": "Semana Santa", "mothers-day": "el Día de la Madre",
        "fathers-day": "el Día del Padre", "thanksgiving": "Thanksgiving",
        "black-friday": "el Black Friday", "cyber-monday": "el Cyber Monday",
        "full-moon": "la próxima luna llena", "eclipse": "el próximo eclipse",
        "oscars": "los Premios Óscar", "grammys": "los Grammys",
        "met-gala": "la Met Gala", "cannes": "el Festival de Cannes",
        "coachella": "Coachella", "eurovision": "Eurovisión",
        "lollapalooza-ar": "Lollapalooza Argentina",
        "rock-in-rio": "Rock in Rio",
        "dia-de-los-muertos": "el Día de los Muertos",
        "cinco-de-mayo": "el Cinco de Mayo",
        "hot-sale": "el Hot Sale",
    },
    "pt": {
        "gta6": "GTA VI", "iphone": "iPhone 2026", "f1": "a próxima corrida de F1",
        "world-cup": "a Copa do Mundo 2026", "ucl-final": "a Final da Champions League",
        "nba-finals": "as Finais da NBA", "le-mans": "as 24 Horas de Le Mans",
        "wimbledon": "Wimbledon", "tour-de-france": "o Tour de France",
        "olympics-2028": "os Jogos Olímpicos 2028", "super-bowl": "o Super Bowl",
        "christmas": "o Natal", "new-year": "o Ano Novo",
        "halloween": "o Halloween", "valentines": "o Dia dos Namorados",
        "easter": "a Páscoa", "mothers-day": "o Dia das Mães",
        "fathers-day": "o Dia dos Pais",
        "black-friday": "a Black Friday", "cyber-monday": "a Cyber Monday",
        "full-moon": "a próxima lua cheia", "eclipse": "o próximo eclipse",
        "oscars": "o Oscar", "grammys": "o Grammy",
        "met-gala": "o Met Gala", "cannes": "o Festival de Cannes",
        "coachella": "o Coachella", "rock-in-rio": "o Rock in Rio",
    },
    "fr": {
        "gta6": "GTA VI", "iphone": "iPhone 2026", "f1": "la prochaine course F1",
        "world-cup": "la Coupe du Monde 2026", "ucl-final": "la Finale de la Champions League",
        "christmas": "Noël", "new-year": "le Nouvel An",
        "halloween": "Halloween", "valentines": "la Saint-Valentin",
        "easter": "Pâques",
        "black-friday": "le Black Friday", "cyber-monday": "le Cyber Monday",
        "full-moon": "la prochaine pleine lune", "eclipse": "la prochaine éclipse",
        "oscars": "les Oscars", "grammys": "les Grammys",
        "cannes": "le Festival de Cannes", "eurovision": "l'Eurovision",
        "paris-fw": "la Fashion Week de Paris",
        "bastille-day": "le 14 Juillet",
        "tour-de-france": "le Tour de France",
    },
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
    "tour-de-france":   "#TourDeFrance #Cycling",
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
    "gta6":             "#GTA6 #GTAVI #RockstarGames",
    "iphone":           "#iPhone #Apple",
    "full-moon":        "#FullMoon",
    "eclipse":          "#Eclipse",
    "lollapalooza-ar":  "#Lollapalooza",
    "rock-in-rio":      "#RockInRio",
    "nyfw":             "#NYFW #FashionWeek",
    "paris-fw":         "#ParisFashionWeek #PFW",
}

# ── Engagement questions per event ────────────────────────────────────────────
# Used in "question" templates. None = skip question template for that event.
QUESTIONS = {
    "en": {
        "world-cup":        "Who's winning the 2026 World Cup? 🏆",
        "ucl-final":        "Who's lifting the trophy? 🏆",
        "f1":               "Who takes the win? 🏎️",
        "nba-finals":       "Who's your pick? 🏀",
        "super-bowl":       "Who's winning the Super Bowl? 🏈",
        "wimbledon":        "Who wins Wimbledon this year? 🎾",
        "oscars":           "Best Picture predictions? 🎬",
        "grammys":          "Who wins Album of the Year? 🎵",
        "christmas":        "Ready for Christmas? 🎄",
        "halloween":        "Costume ideas? 🎃",
        "coachella":        "Who are you most excited to see? 🎸",
        "gta6":             "Are you hyped? 🎮",
        "olympics-2028":    "Which sport are you watching first? 🏅",
        "black-friday":     "What are you buying? 🛍️",
        "met-gala":         "Whose look are you waiting for? 👗",
    },
    "es": {
        "world-cup":        "¿Quién gana el Mundial 2026? 🏆",
        "ucl-final":        "¿Quién levanta la Champions? 🏆",
        "f1":               "¿Quién gana la carrera? 🏎️",
        "nba-finals":       "¿Cuál es tu pick? 🏀",
        "super-bowl":       "¿Quién gana el Super Bowl? 🏈",
        "wimbledon":        "¿Quién gana Wimbledon este año? 🎾",
        "oscars":           "¿Cuál es tu predicción para Mejor Película? 🎬",
        "christmas":        "¿Ya estás listo para Navidad? 🎄",
        "halloween":        "¿Ya tenés disfraz? 🎃",
        "coachella":        "¿A quién más querés ver? 🎸",
        "gta6":             "¿Estás hipeado? 🎮",
        "black-friday":     "¿Qué vas a comprar? 🛍️",
    },
    "pt": {
        "world-cup":        "Quem vence a Copa do Mundo 2026? 🏆",
        "ucl-final":        "Quem vai erguer a taça? 🏆",
        "f1":               "Quem vence a corrida? 🏎️",
        "christmas":        "Já está preparado para o Natal? 🎄",
        "black-friday":     "O que você vai comprar? 🛍️",
        "oscars":           "Suas previsões para Melhor Filme? 🎬",
    },
    "fr": {
        "world-cup":        "Qui remporte la Coupe du Monde 2026? 🏆",
        "ucl-final":        "Qui soulève le trophée? 🏆",
        "christmas":        "Vous êtes prêts pour Noël? 🎄",
        "cannes":           "Quel film vous attend le plus? 🎬",
    },
}

# ── URL patterns ──────────────────────────────────────────────────────────────
URL_BASE = {
    "en": "https://countdowns.site/countdown/{slug}/",
    "es": "https://countdowns.site/es/countdown/{slug}/",
    "pt": "https://countdowns.site/pt/countdown/{slug}/",
    "fr": "https://countdowns.site/fr/countdown/{slug}/",
}

# ── Tweet templates ───────────────────────────────────────────────────────────
# Types:
#   "countdown" → classic countdown with URL (generates OG image preview)
#   "text"      → no URL, plain text (no image, more organic feel)
#   "question"  → engagement question, no URL
#
TEMPLATES = {
    "en": {
        "countdown": [
            "⏱️ {days} days until {name}. → {url} {hashtags}",
            "🗓️ {name} is in {days} days. → {url} {hashtags}",
            "📅 {days} days to go until {name}. Track it live → {url} {hashtags}",
            "⌛ Only {days} days until {name}! → {url} {hashtags}",
            "🔢 {days} days left. {name} is almost here. → {url} {hashtags}",
        ],
        "text": [
            "⏱️ {days} days until {name}. {hashtags}",
            "📅 {name} is just {days} days away. {hashtags}",
            "🗓️ Mark your calendar — {name} in {days} days. {hashtags}",
            "⌛ {days} days. That's how long until {name}. {hashtags}",
            "🔔 Reminder: {name} is in {days} days. {hashtags}",
        ],
        "question": [
            "{question}\n\n{days} days to go. {hashtags}",
            "{days} days until {name}.\n\n{question} {hashtags}",
            "{question}\n\n{name} is in {days} days. {hashtags}",
        ],
    },
    "es": {
        "countdown": [
            "⏱️ Faltan {days} días para {name}. → {url} {hashtags}",
            "🗓️ {name} es en {days} días. → {url} {hashtags}",
            "📅 {days} días para {name}. Seguí la cuenta regresiva → {url} {hashtags}",
            "🔢 Quedan {days} días para {name}. → {url} {hashtags}",
        ],
        "text": [
            "⏱️ Faltan {days} días para {name}. {hashtags}",
            "📅 {name} en {days} días. {hashtags}",
            "🗓️ Marcá el calendario — {name} en {days} días. {hashtags}",
            "🔔 Recordatorio: {name} es en {days} días. {hashtags}",
        ],
        "question": [
            "{question}\n\nFaltan {days} días. {hashtags}",
            "{days} días para {name}.\n\n{question} {hashtags}",
        ],
    },
    "pt": {
        "countdown": [
            "⏱️ Faltam {days} dias para {name}. → {url} {hashtags}",
            "🗓️ {name} em {days} dias. → {url} {hashtags}",
            "📅 {days} dias restantes para {name}. → {url} {hashtags}",
            "🔢 Faltam apenas {days} dias para {name}! → {url} {hashtags}",
        ],
        "text": [
            "⏱️ Faltam {days} dias para {name}. {hashtags}",
            "📅 {name} está chegando — {days} dias. {hashtags}",
            "🔔 Lembrete: {name} em {days} dias. {hashtags}",
        ],
        "question": [
            "{question}\n\nFaltam {days} dias. {hashtags}",
            "{days} dias para {name}.\n\n{question} {hashtags}",
        ],
    },
    "fr": {
        "countdown": [
            "⏱️ {days} jours avant {name}. → {url} {hashtags}",
            "🗓️ {name} dans {days} jours. → {url} {hashtags}",
            "📅 Plus que {days} jours avant {name}. → {url} {hashtags}",
        ],
        "text": [
            "⏱️ {days} jours avant {name}. {hashtags}",
            "📅 {name} approche — {days} jours. {hashtags}",
            "🔔 Rappel : {name} dans {days} jours. {hashtags}",
        ],
        "question": [
            "{question}\n\nEncore {days} jours. {hashtags}",
            "{days} jours avant {name}.\n\n{question} {hashtags}",
        ],
    },
}

# Tweet type weights: 40% countdown (with URL/image), 35% text (no image), 25% question
TWEET_TYPE_WEIGHTS = [("countdown", 40), ("text", 35), ("question", 25)]

# ── Language weights (60% EN, 25% ES, 10% PT, 5% FR) ─────────────────────────
LANG_WEIGHTS = [("en", 60), ("es", 25), ("pt", 10), ("fr", 5)]

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

def pick_event(lang):
    events = load_events()
    names = NAMES.get(lang, NAMES["en"])
    candidates = []
    for slug, event_data in events.items():
        if slug not in names:
            continue
        days = get_days_remaining(event_data.get("date"))
        if days is None or days == 0:
            continue
        candidates.append((slug, days))
    if not candidates:
        return None
    return random.choice(candidates)

# ── Post tweet ────────────────────────────────────────────────────────────────
def post_tweet():
    # Pick language
    langs, lang_w = zip(*LANG_WEIGHTS)
    lang = random.choices(langs, weights=lang_w, k=1)[0]

    result = pick_event(lang)
    if not result:
        print("No valid events found.")
        return

    slug, days = result
    name = NAMES[lang][slug]
    url = URL_BASE[lang].format(slug=slug)
    hashtags = HASHTAGS.get(slug, "")
    question = QUESTIONS.get(lang, {}).get(slug)

    # Pick tweet type — fall back to "text" if no question defined
    types, type_w = zip(*TWEET_TYPE_WEIGHTS)
    tweet_type = random.choices(types, weights=type_w, k=1)[0]
    if tweet_type == "question" and not question:
        tweet_type = "text"

    template = random.choice(TEMPLATES[lang][tweet_type])

    tweet = template.format(
        days=days,
        name=name,
        url=url,
        hashtags=hashtags,
        question=question or "",
    ).strip()

    # Safety: Twitter limit is 280 chars
    if len(tweet) > 280:
        tweet = tweet[:277] + "..."

    try:
        client.create_tweet(text=tweet)
        print(f"[{lang}][{tweet_type}] Tweet posted: {tweet}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    post_tweet()
