#!/usr/bin/env python3
"""
Download event-specific OG images from Wikimedia Commons.
All images are Creative Commons licensed (free to use with attribution).
Run from repo root: python3 _download_og_images.py

To add a custom image manually:
  → Save it as og-images/{slug}.jpg (1200×630px recommended)
  → Re-run python3 _generate.py to regenerate all pages
"""
import os
import ssl
import urllib.request
import urllib.error

# macOS Python SSL fix
ssl_ctx = ssl._create_unverified_context()

OUT_DIR = "og-images"
os.makedirs(OUT_DIR, exist_ok=True)

# Each entry: (slug, direct_image_url, credit)
# All sourced from Wikimedia Commons — CC licensed
# Use Special:FilePath — the correct Wikimedia Commons endpoint
WM = "https://commons.wikimedia.org/wiki/Special:FilePath/"

IMAGES = [
    ("world-cup",
     WM + "2022_FIFA_World_Cup_opening_ceremony_(cropped).jpg?width=1200",
     "FIFA World Cup 2022 opening ceremony, Wikimedia Commons CC BY-SA 4.0"),

    ("f1",
     WM + "Lewis_Hamilton_2016_Malaysia_2.jpg?width=1200",
     "F1 race, Wikimedia Commons CC BY-SA 3.0"),

    ("ucl-final",
     WM + "UEFA_Champions_League_Final_2019_(47898971651).jpg?width=1200",
     "UCL Final 2019, Wikimedia Commons CC BY 2.0"),

    ("nba-finals",
     WM + "2016_NBA_Finals_Media_Day_(27891386932).jpg?width=1200",
     "NBA Finals, Wikimedia Commons CC BY-SA 2.0"),

    ("super-bowl",
     WM + "Super_Bowl_LVI_(52008518682).jpg?width=1200",
     "Super Bowl LVI, Wikimedia Commons CC BY-SA 2.0"),

    ("wimbledon",
     WM + "2013_Wimbledon_Championships_-_Centre_Court.jpg?width=1200",
     "Wimbledon Centre Court, Wikimedia Commons CC BY-SA 3.0"),

    ("christmas",
     WM + "Christmas_tree_at_Rockefeller_Center_(51717799000)_(cropped).jpg?width=1200",
     "Rockefeller Center Christmas Tree, Wikimedia Commons CC BY 2.0"),

    ("halloween",
     WM + "Jack-o'-lantern_2003-10-31.jpg?width=1200",
     "Halloween Jack-o-lantern, Wikimedia Commons CC BY-SA 2.0"),

    ("oscars",
     WM + "AMPAS_annual_meeting_2018_11.jpg?width=1200",
     "Oscars ceremony, Wikimedia Commons CC BY-SA 4.0"),

    ("grammys",
     WM + "66th_Grammy_Awards.jpg?width=1200",
     "Grammy Awards, Wikimedia Commons CC BY-SA 4.0"),

    ("coachella",
     WM + "Coachella_2012.jpg?width=1200",
     "Coachella 2012, Wikimedia Commons CC BY 2.0"),

    ("new-year",
     WM + "Fireworks_at_New_Years_2012,_Tallinn.jpg?width=1200",
     "New Year fireworks, Wikimedia Commons CC BY-SA 3.0"),

    ("thanksgiving",
     WM + "Thanksgiving-Brownell.jpg?width=1200",
     "Thanksgiving, Wikimedia Commons Public Domain"),

    ("black-friday",
     WM + "Crowd_outside_Best_Buy_on_Black_Friday_(2010).jpg?width=1200",
     "Black Friday crowd, Wikimedia Commons CC BY-SA 2.0"),

    ("met-gala",
     WM + "Metropolitan_Museum_of_Art_-_by_Don_Ramey_Logan.jpg?width=1200",
     "Metropolitan Museum of Art, Wikimedia Commons CC BY-SA 4.0"),

    ("tour-de-france",
     WM + "Tour_de_France_2022_-_étape_6_-_6.jpg?width=1200",
     "Tour de France 2022, Wikimedia Commons CC BY-SA 4.0"),

    ("le-mans",
     WM + "24h_du_Mans_2019_(Porsche_GT_Team)_(48104476677).jpg?width=1200",
     "24 Hours of Le Mans 2019, Wikimedia Commons CC BY-SA 2.0"),

    ("olympics-2028",
     WM + "Olympic_flag.jpg?width=1200",
     "Olympic flag, Wikimedia Commons CC BY-SA 3.0"),

    ("copa-libertadores",
     WM + "Copa_Libertadores_2019_Final_-_Flamengo_vs_River_Plate_(cropped).jpg?width=1200",
     "Copa Libertadores Final 2019, Wikimedia Commons CC BY-SA 2.0"),

    ("valentines",
     WM + "Valentinekartka.jpg?width=1200",
     "Valentine's Day card, Wikimedia Commons CC BY-SA 3.0"),

    ("easter",
     WM + "Easter_eggs_-_straw_decoration.jpg?width=1200",
     "Easter eggs, Wikimedia Commons CC BY-SA 3.0"),

    ("cannes",
     WM + "Cannes_Palais_des_festivals.jpg?width=1200",
     "Cannes Palais des festivals, Wikimedia Commons CC BY-SA 3.0"),

    ("eurovision",
     WM + "Eurovision_Song_Contest_2023_-_Grand_Final_(52950111060).jpg?width=1200",
     "Eurovision 2023, Wikimedia Commons CC BY-SA 2.0"),

    ("full-moon",
     WM + "FullMoon2010.jpg?width=1200",
     "Full moon, Wikimedia Commons CC BY-SA 3.0"),

    ("gta6",
     WM + "Rockstar_Games_Logo.svg?width=1200",
     "Rockstar Games logo, Wikimedia Commons"),
]

def download(slug, url, credit):
    import subprocess, urllib.parse
    # URL-encode the filename portion only
    parts = url.split("?")
    base = parts[0]
    query = parts[1] if len(parts) > 1 else ""
    encoded = urllib.parse.quote(base, safe=":/?=&#%")
    full_url = encoded + ("?" + query if query else "")

    # Follow redirects to get actual file extension
    tmp_path = os.path.join(OUT_DIR, f"_tmp_{slug}")
    result = subprocess.run(
        ["curl", "-s", "-L", "-k", "--max-time", "20",
         "-A", "countdowns.site/og-image-downloader",
         "-o", tmp_path, "-w", "%{content_type}", full_url],
        capture_output=True, text=True
    )
    content_type = result.stdout.strip()
    ext = ".jpg" if "jpeg" in content_type or "jpg" in content_type else ".png"
    out_path = os.path.join(OUT_DIR, f"{slug}{ext}")

    if os.path.exists(out_path):
        os.remove(tmp_path)
        print(f"  ✓ {slug} (already exists)")
        return
    if os.path.exists(tmp_path) and os.path.getsize(tmp_path) > 5000:
        os.rename(tmp_path, out_path)
        print(f"  ✓ {slug} → {out_path}")
        print(f"    Credit: {credit}")
    else:
        if os.path.exists(tmp_path):
            os.remove(tmp_path)
        print(f"  ✗ {slug} — FAILED (file too small or missing)")

if __name__ == "__main__":
    print(f"Downloading OG images to /{OUT_DIR}/...\n")
    for slug, url, credit in IMAGES:
        download(slug, url, credit)
    print(f"\nDone! Run python3 _generate.py to regenerate pages with new images.")
    print("\nTo add a custom image for any event:")
    print("  → Save it as og-images/{slug}.jpg (1200×630px recommended)")
    print("  → Run python3 _generate.py")
