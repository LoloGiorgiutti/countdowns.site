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

# ── URL patterns ──────────────────────────────────────────────────────────────
URL_BASE = {
    "en": "https://countdowns.site/countdown/{slug}/",
    "es": "https://countdowns.site/es/countdown/{slug}/",
    "pt": "https://countdowns.site/pt/countdown/{slug}/",
    "fr": "https://countdowns.site/fr/countdown/{slug}/",
}

# ── Tweet templates ───────────────────────────────────────────────────────────
TEMPLATES = {
    "en": [
        "⏱️ {days} days until {name}. → {url}",
        "🗓️ {name} is in {days} days. Start your countdown → {url}",
        "📅 {days} days to go until {name}. → {url}",
        "🔢 {days} days left until {name}. → {url}",
        "⌛ Only {days} days until {name}! → {url}",
    ],
    "es": [
        "⏱️ Faltan {days} días para {name}. → {url}",
        "🗓️ {name} es en {days} días. → {url}",
        "📅 {days} días para {name}. Seguí la cuenta regresiva → {url}",
        "🔢 Quedan {days} días para {name}. → {url}",
    ],
    "pt": [
        "⏱️ Faltam {days} dias para {name}. → {url}",
        "🗓️ {name} em {days} dias. → {url}",
        "📅 {days} dias restantes para {name}. → {url}",
        "🔢 Faltam apenas {days} dias para {name}! → {url}",
    ],
    "fr": [
        "⏱️ {days} jours avant {name}. → {url}",
        "🗓️ {name} dans {days} jours. → {url}",
        "📅 Plus que {days} jours avant {name}. → {url}",
    ],
}

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
    # Weight toward closer events (more timely)
    return random.choice(candidates)

# ── Post tweet ────────────────────────────────────────────────────────────────
def post_tweet():
    # Pick language
    langs, weights = zip(*LANG_WEIGHTS)
    lang = random.choices(langs, weights=weights, k=1)[0]

    result = pick_event(lang)
    if not result:
        print("No valid events found.")
        return

    slug, days = result
    name = NAMES[lang][slug]
    url = URL_BASE[lang].format(slug=slug)
    template = random.choice(TEMPLATES[lang])
    tweet = template.format(days=days, name=name, url=url)

    try:
        client.create_tweet(text=tweet)
        print(f"[{lang}] Tweet posted: {tweet}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    post_tweet()
