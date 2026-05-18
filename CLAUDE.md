# CLAUDE.md — countdowns.site Project Reference

> **READ THIS FIRST before touching any file.**  
> This document records confirmed architecture decisions, verified date formulas,
> and the mandatory protocol for adding new countdowns.  
> Do NOT change confirmed behaviors without explicit user instruction.

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

- [ ] Date is correct for the primary country
- [ ] Timezone is the LOCAL timezone of the event (not UTC)
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
| AR | 3rd Sunday August | `nthWeekday(y, 7, 3, 0)` ✅ user-confirmed |
| UY | 2nd Sunday August | `nthWeekday(y, 7, 2, 0)` ✅ |
| CL | 4th Sunday October | `nthWeekday(y, 9, 4, 0)` ✅ |
| MX | April 30 (fixed) | `midnightInTZ(tz, y, 3, 30)` ✅ |
| BR | October 12 (fixed) | `midnightInTZ(tz, y, 9, 12)` ✅ |
| default | November 20 (UN Day) | `midnightInTZ(tz, y, 10, 20)` ✅ |

### Día de la Madre (Mother's Day)
| Country | Date | Formula |
|---------|------|---------|
| AR, UY | 3rd Sunday October | `nthWeekday(y, 9, 3, 0)` ✅ |
| MX + most LatAm | May 10 (fixed) | `midnightInTZ(tz, y, 4, 10)` ✅ |
| GB, IE | Mothering Sunday = Easter − 21 days | `easterDate(y) − 21` ✅ |
| FR | Last Sunday May | `lastWeekday(y, 4, 0)` ✅ |
| PT | 1st Sunday May | `nthWeekday(y, 4, 1, 0)` ✅ |
| default (US/CA/AU/etc.) | 2nd Sunday May | `nthWeekday(y, 4, 2, 0)` ✅ |

### Día del Padre (Father's Day)
| Country | Date | Formula |
|---------|------|---------|
| ES | March 19 (San José, fixed) | `midnightInTZ(tz, y, 2, 19)` ✅ |
| BR | 2nd Sunday August | `nthWeekday(y, 7, 2, 0)` ✅ |
| default | 3rd Sunday June | `nthWeekday(y, 5, 3, 0)` ✅ |

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

## Known Limitations / Future TODOs

- International Workers' Day (May 1) not yet a separate event for LatAm/Europe
- Hub pages for DE, AT, SE, NO, DK, FI, NL, IT, GR fall back to English (no `/de/` etc.)
- `sitemap.xml` must be manually regenerated when adding events
- `cd_lang` explicit choice persists until next country change
