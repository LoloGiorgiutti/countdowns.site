# CLAUDE.md — countdowns.site Project Reference

> **READ THIS FIRST before touching any file.**  
> This document records confirmed architecture decisions, verified date formulas,
> and the mandatory protocol for adding new countdowns.  
> Do NOT change confirmed behaviors without explicit user instruction.

---

## ⚠️ EVENT DATA ACCURACY — MANDATORY RULE

**Every time an event date or time is added or edited**, Claude must verify the information carefully before writing it. Wrong times directly affect users trusting the countdown.

### Rules:
| Rule | Detail |
|------|--------|
| ❌ NEVER assume a time is correct without verifying | A 1-hour error in a UTC offset causes wrong countdowns for millions of users |
| ✅ ALWAYS verify UTC offset for each race/event location | e.g. CEST = UTC+2, BST = UTC+1, EDT = UTC-4, JST = UTC+9 |
| ✅ ALWAYS cross-check with official sources or known race history | Standard F1/MotoGP race starts = 15:00 local time |
| ✅ When in doubt, ASK the user — don't guess | Especially for new events or events with non-standard times |

### Known timezone rules for recurring events:
- **F1 European races (CEST, UTC+2)**: race at 15:00 local → `T13:00:00Z`
- **F1 British GP (BST, UTC+1)**: race at 15:00 local → `T14:00:00Z`
- **F1 night races** (Singapore, Las Vegas, Abu Dhabi): confirm separately — non-standard times
- **Argentina time = UTC-3** year-round (no daylight saving) — use to sanity-check: 13:00 UTC = 10:00 AR, 14:00 UTC = 11:00 AR

### Past corrections (track record):
- May 2026: All European F1 races had `T14:00:00Z` (wrong) → corrected to `T13:00:00Z`. British GP had `T15:00:00Z` → corrected to `T14:00:00Z`. User had to catch this error.

---

## 🚨 SEO CRISIS HISTORY — READ BEFORE TOUCHING ANYTHING SEO-RELATED

**Context (May 2026):** The site suffered a major SEO drop due to a sequence of structural mistakes. This section documents what happened and what must NEVER be repeated. Claude's limited memory across sessions caused real damage. Every future session must read this first.

### What happened:

1. **1,460 thin date pages were created** (`/countdown/january-01`, `/countdown/may-27`, etc.) all at once. These pages were near-identical in structure and appeared suddenly on a relatively new domain.
2. **Google interpreted this as content spam / bot behavior** and dropped the entire domain's impressions from ~4,000/day to ~100/day — affecting ALL pages including the good event countdowns.
3. **The correct fix** was to mark all 1,460 date pages with `noindex, follow` and remove them from the sitemap. This was applied and is the current state.
4. **In a subsequent session, Claude (without memory of the above) incorrectly reversed this fix**, briefly re-indexing all 1,460 date pages. This was immediately reverted, but the damage from that momentary change is unknown.

### Current SEO state (May 2026):
- ~100–200 impressions/day (down from ~4,000) — recovery in progress, estimated weeks
- Date pages: **noindex, follow** — DO NOT CHANGE THIS
- Sitemap: **846 URLs** (event countdowns only, no date pages) — DO NOT ADD DATE PAGES
- The domain is in a recovery phase — stability is more important than any new optimization

### HARD RULES — never override without explicit user confirmation:

| Rule | Reason |
|------|--------|
| ❌ NEVER re-index the date pages (`/countdown/january-01` etc.) | They caused the SEO crisis. They stay noindex until the domain fully recovers AND the user explicitly decides otherwise. |
| ❌ NEVER add date pages back to sitemap.xml | Same reason. Sitemap stays at ~846 event URLs. |
| ❌ NEVER make bulk structural changes (adding/removing hundreds of URLs at once) | This is what triggered the Google penalty. Any bulk change needs the user's explicit sign-off. |
| ❌ NEVER submit or recommend submitting the sitemap to Search Console | User already did this. Doing it again repeatedly has no benefit and may signal instability. |
| ❌ NEVER recommend "re-indexing" or "adding more pages to sitemap" as a fix for low impressions | The low impressions are a recovery phase — time is the fix, not more pages. |
| ✅ DO wait for organic recovery | Google re-evaluates penalized domains over weeks. Stability + no new errors is the best action. |
| ✅ DO focus on content quality of the ~846 indexed event pages | Better titles, descriptions, structured data on existing pages. |
| ✅ DO ask the user before any change that affects robots meta tags or sitemap | These are high-risk SEO levers. |

### What actually helps recovery (confirmed):
- **Time + stability** — no new crawl signals of instability
- **Improving meta titles/descriptions** on the 846 indexed event pages
- **Building backlinks** to event pages (if user does outreach)
- **GA4 + Search Console** are now set up — monitor but don't panic

### What does NOT help (and may hurt):
- Re-submitting the sitemap repeatedly
- Toggling noindex on/off
- Adding hundreds of new pages at once
- Any "quick SEO fix" that touches robots meta or sitemap in bulk

---

## Owner & Goals

- **Developer**: Lorenzo Giorgiutti (solo developer, no team)
- **Primary goal for 2026**: Reach **$1,000/month** in revenue — ideally by Q4 2026, at latest by end of year
- **Monetization model**: Google AdSense display ads (currently pending approval as of May 2026)
- **Current traffic**: ~100–200 impressions/day in Search Console (SEO recovery phase as of May 2026 — was ~4,000/day before the date-pages incident)
- **SEO approach**: Stability first. Do not make bulk changes. Improve existing indexed pages. Wait for recovery.
- **Expansion priority**: Quality over quantity — improve the ~846 indexed event pages before adding new ones

### Path to $1,000/month — realistic breakdown:
To earn $1,000/month with AdSense at ~$3–5 RPM (typical for this content type):
- Need ~200,000–330,000 pageviews/month (~6,500–11,000/day)
- Current state: well below that — recovery is step 1
- Step 1 (now): Recover from SEO penalty → get back to 4,000 impressions/day → ~100 clicks/day
- Step 2: Grow indexed event pages with high search intent (e.g. "countdown to Christmas 2026", "how many days until Black Friday")
- Step 3: AdSense approval → monetize existing traffic
- Step 4: Scale with new high-traffic events, backlinks, social
- **Do not rush any step** — instability hurts more than it helps at this stage

## Sister Site

- **calculate.website** (formerly calculadora.live) — same owner, same concept: a globally-targeted multi-language calculator/tool site. Being developed in parallel. Treat as a separate project; do not conflate with countdowns.site.

---

## Stack & Deployment

- **Frontend**: Pure static HTML/CSS/JS — no framework, no build step
- **Hosting**: Cloudflare Pages → auto-deploys on `git push` to `main`
- **Repo**: `github.com/LoloGiorgiutti/countdowns.site`
- **Live URL**: https://countdowns.site
- **Deploy time**: ~1 minute after push

---

## Key Files

| File | Purpose |
|------|---------|
| `index.html` | Homepage — hub grid, country selector, language switcher |
| `countdown-engine.js` | All countdown logic — AUTO/variable/fixed types, TZ handling |
| `countdown.css` | All styles |
| `countdowns-data.json` | Variable event dates (editable via admin panel) |
| `events-meta.json` | Per-event countries + categories (editable via admin panel) |
| `admin/index.html` | Password-protected admin panel (pw: `countdowns2026`) |
| `_generate_hubs.py` | Generates static language pages (es/, pt/, fr/) |
| `es/`, `pt/`, `fr/` | Pre-generated translated hub + countdown pages |
| `countdown/` | Individual countdown pages (English) |
| `sitemap.xml` | SEO sitemap (regenerate with `python3 generate_sitemap.py` after adding events) |

---

## ══════════════════════════════════════
## PROTOCOL: HOW TO ADD A NEW COUNTDOWN
## ══════════════════════════════════════

Follow ALL steps in order. Missing any step causes broken pages or wrong dates.

### STEP 1 — Define the event

Answer these questions before touching code:

| Question | Why it matters |
|----------|---------------|
| What is the slug? (lowercase, hyphenated) | Used as URL and key everywhere |
| What type? `auto` / `variable` / `fixed` | Determines which files to edit |
| What is the exact confirmed date + time? | **ONLY confirmed official dates. Never estimate.** |
| What timezone is the event in? | Critical for countdown accuracy |
| Which countries care? (or `['global']`) | Controls visibility in hub |
| What category? | Sports / Holidays / Music / Entertainment / Sales / Nature / Politics / Fashion / Technology / National Days / Jewish Holidays / Months / Seasons / School / Time |
| Does it recur annually? → `auto`. One-time? → `variable`. | |

**Type guide:**
- `auto` = recurring event with a formula (e.g. "3rd Sunday of May every year")
- `variable` = specific known date stored in `countdowns-data.json` (concerts, tournaments)
- `fixed` = hardcoded date, only for things like Olympics 2028 opening

---

### STEP 2 — Add to EVENTS array in `index.html`

Add a line to the correct category section:

```javascript
{ slug:'slug-here', name:'Display Name', type:'auto|variable|fixed',
  countries:['AR','UY'], regions:['es'], cat:'Music',
  url:'/countdown/slug-here/' },
```

**`countries` rules:**
- `['global']` = show for ALL countries
- Specific list = only show for those countries
- Use `LATAM` variable for all Latin American countries

**`regions` rules (for translated page links):**
- `['global']` = has pages in all languages
- `['es']` = only ES translated page exists
- Add more as pages are generated

---

### ══════════════════════════════════════
### CRITICAL: TIMEZONE TYPE — Determine BEFORE setting any date
### ══════════════════════════════════════

Every new countdown must be classified into one of two types:

#### TYPE A — "Global moment" event
The event happens at one specific moment in time worldwide.
Everyone's countdown hits zero at the same instant.

**Examples:** Champions League Final, FIFA World Cup matches, NBA Finals,
Oscars ceremony, Grammys, F1 race start, Super Bowl, Copa Libertadores Final,
Le Mans 24h start, concerts/festivals with a confirmed stage time.

**Rule:** Store the exact local kickoff time WITH its timezone offset.
The engine converts it to the user's local display, but all users reach zero at the same moment.

```json
"ucl-final": { "date": "2026-05-30T16:00:00Z" }
"world-cup":  { "date": "2026-06-11T19:00:00Z" }
"oscars":     { "date": "2027-03-14T19:00:00-04:00" }
```

**⚠️ ALWAYS verify the official kickoff time before storing.**
Confirmed sources: UEFA.com, FIFA.com, NBA.com, official broadcaster press releases.
Do NOT assume 21:00 CEST because "that's the tradition" — UEFA changed UCL Final to 18:00 CEST for 2026.

#### TYPE B — "Midnight local" event
The event is a holiday or recurring date that starts at midnight in each country's timezone.
A user in Tokyo and a user in Buenos Aires both reach zero at midnight their own time.

**Examples:** Christmas, New Year's, Halloween, Valentine's Day, Mother's Day,
Independence Day, national holidays, birthdays.

**Rule:** These are almost always `type: 'auto'` in countdown-engine.js using
`midnightInTZ(tz, year, month, day)` or `nthWeekday(...)` formulas.
Do NOT store a single UTC timestamp for these — use the auto formula.

```javascript
// ✅ Correct for midnight-local events
'christmas': function() {
  return { date: nextOccurrence(function(y) { return midnightInTZ(tz, y, 11, 25); }) };
}
// ❌ WRONG — would show countdown ending at wrong time in most countries
"christmas": { "date": "2026-12-25T00:00:00Z" }
```

#### Decision flowchart:

```
New event → Does it happen at the same physical moment for everyone?
  YES → TYPE A (global moment) → store ISO 8601 with confirmed TZ offset
  NO  → Does it start at midnight in each local timezone?
    YES → TYPE B (midnight local) → use auto formula with midnightInTZ()
    NO  → special case, ask user
```

#### Common mistakes to avoid:
- ❌ Storing `T20:00:00-08:00` (LA time) for Grammys when it actually airs at `T20:00:00-05:00` (ET)
- ❌ Using `T00:00:00Z` (UTC midnight) for Christmas → it would expire at different wall-clock times per country
- ❌ Using "traditional" time (e.g. 21:00 CEST for UCL) without verifying the actual confirmed time
- ✅ Always check: `the-official-site.com` or search `"[event] kickoff time UTC 2026"`

---

### STEP 3a — If `type: 'variable'`, add to `countdowns-data.json`

```json
"slug-here": {
  "date": "2026-09-15T21:00:00-03:00",
  "note": "Short description — venue, city, official source."
}
```

**Date format**: `YYYY-MM-DDTHH:MM:SS±HH:MM` (ISO 8601 with explicit timezone offset)

**If date not yet confirmed**: use `"date": null` and explain in `note` when it will be announced.  
**NEVER use an estimated date as if it were confirmed.**

---

### CRITICAL: VARIANTS dates in static pages must include timezone offset
Individual countdown pages (generated by `_generate_hubs.py`) contain a hardcoded `VARIANTS` array.
Date strings in VARIANTS MUST include timezone offset to avoid UTC parsing bug:
- ✅ `"2026-08-16T00:00:00-03:00"` (Argentina/Uruguay — UTC-3)
- ❌ `"2026-08-16"` → parsed as UTC midnight → displays as Aug 15 in UTC-3 timezones!

Always use `YYYY-MM-DDTHH:MM:SS±HH:MM` format in VARIANTS dates, never bare `YYYY-MM-DD`.

---

### STEP 3b — If `type: 'auto'`, add getter to `countdown-engine.js`

Add inside the `AUTO = { ... }` dict:

```javascript
'slug-here': function () {
  var tz = getCountryTZ();
  var country = getCurrentCountry();
  // Country-specific logic if needed:
  if (country === 'AR') {
    return { date: nextOccurrence(function (y) { return tzDay(tz, nthWeekday(y, 7, 3, 0)); }) };
  }
  // Default:
  return { date: nextOccurrence(function (y) { return midnightInTZ(tz, y, MONTH_0INDEXED, DAY); }) };
},
```

**Helper reference (months are 0-indexed: Jan=0, Dec=11):**
- `nthWeekday(year, month, n, weekday)` → nth weekday of month (0=Sun, 1=Mon … 6=Sat)
- `lastWeekday(year, month, weekday)` → last weekday of month
- `midnightInTZ(tz, year, month, day)` → midnight in country's timezone
- `tzDay(tz, date)` → converts a JS Date to TZ-aware midnight
- `nextOccurrence(fn)` → returns next future occurrence of annual event
- `getCountryTZ()` → returns IANA timezone string for current country
- `getCurrentCountry()` → returns `localStorage.cd_country` or `'global'`

---

### STEP 4 — Generate the countdown page

Add the event to `_generate_hubs.py` EVENTS list, then run:

```bash
python3 _generate_hubs.py
```

This generates:
- `countdown/slug-here/index.html` (EN)
- `es/countdown/slug-here/index.html` (ES)
- `pt/countdown/slug-here/index.html` (PT)
- `fr/countdown/slug-here/index.html` (FR)

---

### STEP 5 — Update `events-meta.json`

```json
"slug-here": {
  "countries": ["AR", "UY"],
  "cat": "Music"
}
```

---

### STEP 6 — Verify before pushing

- [ ] **Timezone type confirmed**: TYPE A (global moment) or TYPE B (midnight local)?
- [ ] **If TYPE A**: official kickoff time verified from primary source (UEFA.com, FIFA.com, NBA.com, etc.)
- [ ] **If TYPE B**: uses `midnightInTZ()` formula, NOT a fixed UTC timestamp
- [ ] Date and time are correct for the event's actual location
- [ ] Countdown page renders correctly in browser
- [ ] Event appears in hub when that country is selected
- [ ] Event does NOT appear for unrelated countries
- [ ] If date TBA → shows "Date to be confirmed" cleanly, not a wrong number

---

### STEP 7 — Push

```bash
git add -A
git commit -m "Add [event name] countdown"
git push
```

Cloudflare deploys in ~1 minute.

---

### WORKED EXAMPLE: Coldplay Buenos Aires 2026

```
Slug:      coldplay-bsas-2026
Type:      variable (specific concert date)
Date:      2026-11-05T21:00:00-03:00  (Buenos Aires = UTC-3)
Countries: ['AR', 'UY', 'CL', 'BO', 'PY']
Category:  Music
Note:      "Coldplay — Music of the Spheres World Tour · Estadio Monumental, Buenos Aires"
```

Steps: add to `index.html` EVENTS → Music section · add to `countdowns-data.json` · add to `_generate_hubs.py` and run · add to `events-meta.json` · push.

---

## Architecture — CONFIRMED RULES (do not break)

### Country vs Language (CRITICAL)
- **Country** (`localStorage.cd_country`) = filters WHICH events appear in hub
- **Language** (`localStorage.cd_lang`) = controls display language ONLY
- These are INDEPENDENT — user can see AR events in English, US events in Spanish
- `filteredEvents()` filters by country, never by language
- `cd_country = 'global'` → show ALL events

### Boot Priority (language)
1. `cd_lang` explicit override → use it
2. `cd_country`-derived → `countryToLang(savedCountry)`
3. Fallback → `'en'`

### Country Change Behavior
- Clears `cd_lang` (resets to country's default language)
- Calls `applyCountry(code)` → `setLang(countryToLang(code))` → `loadHub()`
- **First visit**: silent geolocation via ipapi.co → auto-apply WITHOUT modal
- Small toast: "Showing countdowns for 🇦🇷 Argentina" (3 seconds)
- Modal available via 🌍 flag button in header for manual override

### Date Policy (CRITICAL — NEVER BREAK)
- **Only confirmed official dates or astronomically certain dates**
- Unconfirmed → `"date": null` → shows "Date TBA" cleanly
- `_policy` field in `countdowns-data.json` documents this rule
- Examples of violations: estimated Copa Libertadores, estimated Lollapalooza

### Admin Panel
- GitHub token in `localStorage.admin_gh_token`
- Commits directly to GitHub API → triggers Cloudflare auto-deploy
- Date field: separate `date` + `time` inputs (time defaults 00:00 if empty)
- Session: `sessionStorage.admin_ok = '1'`

---

## Verified Date Formulas (DO NOT change without research + user confirmation)

### Día del Niño (Children's Day)
| Country | Date | Formula |
|---------|------|---------|
| MX | April 30 (fixed) | `midnightInTZ(tz, y, 3, 30)` ✅ |
| AE | March 15 (fixed) | `midnightInTZ(tz, y, 2, 15)` ✅ |
| BO | April 12 (fixed) | `midnightInTZ(tz, y, 3, 12)` ✅ user-confirmed |
| ES | April 15 (fixed) | `midnightInTZ(tz, y, 3, 15)` ✅ |
| CO | Last Saturday April | `tzDay(tz, lastWeekday(y, 3, 6))` ✅ |
| EC, NI, PT, BE | June 1 (fixed) | `midnightInTZ(tz, y, 5, 1)` ✅ |
| US | 2nd Sunday June | `tzDay(tz, nthWeekday(y, 5, 2, 0))` ✅ |
| VE, PA, CU | 3rd Sunday July | `tzDay(tz, nthWeekday(y, 6, 3, 0))` ✅ |
| AR, UY, PE | 3rd Sunday August | `tzDay(tz, nthWeekday(y, 7, 3, 0))` ✅ user-confirmed |
| PY | August 16 (fixed) | `midnightInTZ(tz, y, 7, 16)` ✅ |
| PR | 2nd Sunday August | `tzDay(tz, nthWeekday(y, 7, 2, 0))` ✅ |
| CR | September 9 (fixed) | `midnightInTZ(tz, y, 8, 9)` ✅ |
| HN | September 10 (fixed) | `midnightInTZ(tz, y, 8, 10)` ✅ |
| DO | September 29 (fixed) | `midnightInTZ(tz, y, 8, 29)` ✅ |
| DE, AT | September 20 (fixed) | `midnightInTZ(tz, y, 8, 20)` ✅ |
| GT, SV | October 1 (fixed) | `midnightInTZ(tz, y, 9, 1)` ✅ |
| SG | 1st Friday October | `tzDay(tz, nthWeekday(y, 9, 1, 5))` ✅ |
| AU | 4th Wednesday October | `tzDay(tz, nthWeekday(y, 9, 4, 3))` ✅ |
| CL | 4th Sunday October | `tzDay(tz, nthWeekday(y, 9, 4, 0))` ✅ |
| BR | October 12 (fixed) | `midnightInTZ(tz, y, 9, 12)` ✅ |
| NZ | 1st Sunday March | `tzDay(tz, nthWeekday(y, 2, 1, 0))` ✅ |
| default | November 20 (UN Day) | `midnightInTZ(tz, y, 10, 20)` ✅ |

### Día de la Madre (Mother's Day)
| Country | Date | Formula |
|---------|------|---------|
| AR | 3rd Sunday October | `nthWeekday(y, 9, 3, 0)` ✅ |
| MX, GT, SV | May 10 (fixed) | `midnightInTZ(tz, y, 4, 10)` ✅ |
| GB, IE | Mothering Sunday = Easter − 21 days | `easterDate(y) − 21` ✅ |
| FR, SE, DO | Last Sunday May | `lastWeekday(y, 4, 0)` ✅ |
| PT, ES | 1st Sunday May | `nthWeekday(y, 4, 1, 0)` ✅ |
| BO | May 27 (fixed) | `midnightInTZ(tz, y, 4, 27)` ✅ |
| PY | May 15 (fixed) | `midnightInTZ(tz, y, 4, 15)` ✅ |
| NI | May 30 (fixed) | `midnightInTZ(tz, y, 4, 30)` ✅ |
| CR | August 15 (fixed) | `midnightInTZ(tz, y, 7, 15)` ✅ |
| PA | December 8 (fixed) | `midnightInTZ(tz, y, 11, 8)` ✅ |
| NO | 2nd Sunday February | `nthWeekday(y, 1, 2, 0)` ✅ |
| default (US/CA/AU/UY/CL/CO/PE/EC/VE/BR/etc.) | 2nd Sunday May | `nthWeekday(y, 4, 2, 0)` ✅ |

### Día del Padre (Father's Day)
| Country | Date | Formula |
|---------|------|---------|
| ES, BO, HN | March 19 (San José, fixed) | `midnightInTZ(tz, y, 2, 19)` ✅ |
| BR, PT | 2nd Sunday August | `nthWeekday(y, 7, 2, 0)` ✅ |
| AU, NZ | 1st Sunday September | `nthWeekday(y, 8, 1, 0)` ✅ |
| DE, AT | Ascension Thursday = Easter + 39 days | `easterDate(y) + 39` ✅ |
| UY | 2nd Sunday July | `nthWeekday(y, 6, 2, 0)` ✅ |
| GT, SV | June 17 (fixed) | `midnightInTZ(tz, y, 5, 17)` ✅ |
| NI | June 23 (fixed) | `midnightInTZ(tz, y, 5, 23)` ✅ |
| DO | Last Sunday July | `lastWeekday(y, 6, 0)` ✅ |
| FI | 2nd Sunday November | `nthWeekday(y, 10, 2, 0)` ✅ |
| default (US/CA/MX/AR/CL/CO etc.) | 3rd Sunday June | `nthWeekday(y, 5, 3, 0)` ✅ |

### Thanksgiving
| Country | Date | Formula |
|---------|------|---------|
| CA | 2nd Monday October | `nthWeekday(y, 9, 2, 1)` ✅ |
| US (default) | 4th Thursday November | `nthWeekday(y, 10, 4, 4)` ✅ |

### Other confirmed formulas
- `easter` = Computus algorithm ✅
- `full-moon` = pre-calculated astronomical table ✅
- `memorial-day` = Last Monday May (US) ✅
- `labor-day` = 1st Monday September (US/CA) ✅
- `black-friday` = 4th Friday November ✅
- `cyber-monday` = Black Friday + 3 days ✅
- `new-year` = TZ-aware Jan 1 ✅
- `christmas` = TZ-aware Dec 25 ✅
- `bastille-day` = July 14 (FR/BE/CH) ✅
- `fiestas-patrias` = Sep 18 (CL) ✅
- `25-de-mayo` = May 25 (AR) ✅
- `independence-day` = July 4 (US) ✅
- `super-bowl` = 2nd Sunday February ✅
- `met-gala` = 1st Monday May ✅

---

## CSS — Confirmed Fixes (DO NOT revert)

### Hero label dot vs text
- `.hub-hero-label span:first-child` = the blinking purple dot (6×6px)
- If changed back to `.hub-hero-label span`, the text span becomes invisible (6×6px bug)
- **Always use `:first-child` selector** in `countdown.css`

### Footer visibility
- Dark mode: `.site-footer { color: rgba(255,255,255,.5) }`
- Light mode: `[data-theme="light"] .site-footer { color: rgba(0,0,0,.35) }`

---

## Country List (38 countries) — Keep in Sync

Two files must always have the same list:
1. `COUNTRY_LIST` in `index.html`
2. `ALL_COUNTRIES` in `admin/index.html`

Groups: English (US, GB, CA, AU, IE, NZ, SG, AE) / Spanish LatAm (AR, MX, CL, CO, PE, UY, VE, EC, BO, PY, CR, PA, DO, PR) / Spanish Europe (ES) / Portuguese (BR, PT) / French (FR, BE, CH) / German (DE, AT) / Nordic (SE, NO, DK, FI) / Other EU (NL, IT, GR)

---

## Content — Daily Date Pages

- **1,460 daily pages** exist at `/countdown/month-day/` and language variants (`/es/`, `/pt/`, `/fr/`)
- Each page has: zodiac sign, season, day-of-year, week number, Famous Birthdays section, This Day in History section, FAQ section
- **Famous Birthdays data**: `_daily_data.py` — 3 people per date, globally famous criterion
- **Historical events data**: also in `_daily_data.py`
- **Translation of `known_for` descriptions**: phrase-substitution via `_KF_TRANS` dict in `_generate.py` (ES/PT/FR)
- Daily pages are tagged `noindex` (too many, low individual authority) — excluded from sitemap
- To regenerate all daily pages: `python3 _generate.py`
- To regenerate sitemap: `python3 _generate_sitemap.py`

---

## Audience & Geography

- Content is geo-targeted: each event shows only for its relevant countries
- Language follows country by default but is independently overridable
- Target markets by volume: English-speaking (US, GB, CA, AU) + Spanish LatAm (AR, MX, CO, CL) + Brazilian Portuguese (BR) + French (FR)
- Hub pages exist for EN, ES, PT, FR — other languages (DE, IT, etc.) fall back to EN

---

## Evergreen Philosophy (CORE DESIGN PRINCIPLE)

The site must remain permanently useful at every URL, forever. No page should ever become a dead end.

### How each event type handles the past:

| Type | Behavior after date passes |
|------|---------------------------|
| `auto` (recurring) | Resets automatically to next year's occurrence. Already evergreen. |
| `variable` (one-time) | Flips to **elapsed timer mode**: "How many days since [Event]" |
| `fixed` (hardcoded) | Same as variable — elapsed timer after date passes |

### Elapsed Timer Mode (variable/fixed events after date)

When a `variable` or `fixed` event's date has passed:
- The countdown page flips from "How long until X" → **"How many days since X"**
- Shows a live chronometer counting **up** (days/hours/minutes/seconds elapsed)
- Headline pattern: **"How many days since [Event Name]?"** (EN) / equivalent in ES/PT/FR
- The URL remains permanently accessible and always shows accurate elapsed time
- SEO value: "how many days since [event]" is a real search query with lasting traffic

### Past Events in the Hub

- Past `variable` events are **removed from the main hub grid**
- They appear in a **collapsible "Past Events" section at the bottom** of the hub
- Section is collapsed by default — user can expand it
- This applies to ALL variable events without exception

### Why this matters for SEO & revenue

- Permanent URLs = permanent backlink value, no 404s
- "How many days since X" queries have long-tail search volume that persists for years
- Keeps domain authority accumulating rather than losing pages over time
- More indexed pages = more AdSense impressions surface area

### Implementation status
- `auto` events: ✅ already implemented
- Elapsed timer for past variable events: ✅ implemented (countdown-engine.js)
- Collapsible past events hub section: ✅ implemented (index.html + _generate_hubs.py)

---

## 🔒 Homepage Design — LOCKED STRUCTURE (do not overwrite)

The English homepage (`index.html`) has a specific multi-layer design that must be preserved exactly. It is **NOT generated** by any script — it is hand-crafted. Never replace it with a simplified or auto-generated version.

### Current design layers (all must coexist):
1. **Featured section** — top 3 soonest events as large `hub-fc` cards with gradient + glow
2. **Search bar** — real-time filtering via `.hub-search-input`
3. **Compact grid** — remaining events as `hub-cc` cards with category color
4. **Favorites system** — star button on every card (`hub-fav-btn`), localStorage key `cd_favorites`, badge counter in header, link to `/favorites/`
5. **Past Events collapsible** — `<details class="hub-past-details">` at the bottom of both chrono and category views
6. **Sort toggle** — "Soonest first" / "By category"

### Key classes that must exist in index.html:
- `.hub-fc`, `.hub-fc-name`, `.hub-fc-days-num` — featured cards
- `.hub-cc`, `.hub-compact-grid` — compact cards grid
- `.hub-search-input`, `.hub-search-wrap` — search bar
- `.hub-fav-btn`, `.hub-fav-header-link`, `.hub-fav-badge` — favorites
- `.hub-past-details` — collapsible past events

### Current line count: ~1070 lines
If you ever see `index.html` at < 800 lines, something was lost — stop and investigate before committing.

### What NOT to do:
- ❌ Never run `_generate_hubs.py` output into `index.html` (that script generates es/pt/fr only)
- ❌ Never replace `index.html` with a simplified version "to add one feature"
- ❌ Never copy the structure from `es/index.html` into `index.html` (different templates)
- ✅ Always `wc -l index.html` before committing — should be > 1000 lines

### ⚠️ MANDATORY: Sync ES/PT/FR after any index.html change

`es/index.html`, `pt/index.html`, and `fr/index.html` are **generated from `index.html`** as their template.  
If `index.html` is modified (new feature, new section, UI change), you **MUST** regenerate all language hubs immediately:

```bash
python3 _generate_hubs.py
```

Then verify all four files are in sync:
```bash
wc -l index.html es/index.html pt/index.html fr/index.html
# es/pt/fr should be within ~30 lines of index.html
```

**This is non-negotiable.** In May 2026, the ES/PT/FR hubs were left at ~730 lines (old design) while EN was at 1073 lines (new design) — users on those languages saw a completely different, degraded homepage. This must never happen again.

---

## Known Limitations / Future TODOs

- International Workers' Day (May 1) not yet a separate event for LatAm/Europe
- Hub pages for DE, AT, SE, NO, DK, FI, NL, IT, GR fall back to English (no `/de/` etc.)
- `sitemap.xml` must be manually regenerated when adding events
- `cd_lang` explicit choice persists until next country change
- AdSense `ads.txt` present at root and serving correctly — awaiting Google approval (as of May 2026)
- calculate.website is a separate sister project — do not mix files or deployments
