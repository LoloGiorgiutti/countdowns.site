# CLAUDE.md — countdowns.site Project Reference

> **READ THIS FIRST.** This file documents confirmed architecture decisions, 
> known-good implementations, and critical rules. Do NOT change confirmed 
> behaviors without explicit user instruction.

---

## Stack & Deployment

- **Frontend**: Pure static HTML/CSS/JS — no framework, no build step
- **Hosting**: Cloudflare Pages — auto-deploys on `git push` to `main` branch on `github.com/LoloGiorgiutti/countdowns.site`
- **Live URL**: https://countdowns.site
- **Deploy time**: ~1 minute after push

---

## Key Files

| File | Purpose |
|------|---------|
| `index.html` | Main homepage — hub grid, country selector, language switcher |
| `countdown-engine.js` | All countdown calculations — AUTO/variable/fixed types |
| `countdown.css` | All styles |
| `countdowns-data.json` | Variable event dates (edited via admin panel) |
| `events-meta.json` | Per-event countries + categories (edited via admin panel) |
| `admin/index.html` | Password-protected admin panel (password: `countdowns2026`) |
| `_generate_hubs.py` | Generates static language hub pages (es/, pt/, fr/) |
| `es/`, `pt/`, `fr/` | Pre-generated translated hub pages |
| `countdown/` | Individual countdown pages (English) |
| `es/countdown/`, `pt/countdown/`, `fr/countdown/` | Translated individual pages |

---

## Architecture — CONFIRMED RULES (do not break)

### Country vs Language (CRITICAL)
- **Country** (`localStorage.cd_country`) = filters WHICH events show
- **Language** (`localStorage.cd_lang`) = controls display language
- These are INDEPENDENT. Changing country sets default language but user can override.
- `filteredEvents()` always filters by country, never by language.
- When `cd_country = 'global'` → show ALL events regardless of country.

### Boot Priority (language)
1. `cd_lang` (explicit user choice) → use it
2. `cd_country`-derived → `countryToLang(savedCountry)`
3. Fallback → `'en'`

### Country Change
- Always clears `cd_lang` (resets to country default language)
- Always calls `setLang(countryToLang(code))`
- Geolocation: **silent auto-apply on first visit** (no modal). Small toast notification only.
- Modal available via flag button in header for manual change.

### Date Policy (CRITICAL — do NOT add estimated dates)
- **Only show confirmed official dates** or astronomically certain dates (eclipses, full moons).
- Unconfirmed/estimated dates → `date: null` → shows "Date TBA"
- This is enforced in `countdowns-data.json` with `_policy` field.
- Examples of what NOT to do: adding "estimated" Copa Libertadores date, estimated Lollapalooza date, etc.

### Admin Panel
- GitHub token stored in `localStorage.admin_gh_token`
- Saves by committing directly to GitHub via API → triggers Cloudflare auto-deploy
- Date field: separate `date` + `time` inputs (time defaults to 00:00 if empty)
- Session password: `sessionStorage.admin_ok = '1'`

---

## Country List (38 countries)

Maintained in TWO places — keep in sync:
1. `COUNTRY_LIST` in `countdown-engine.js` (user-facing selector, exposed as `CountdownEngine.COUNTRY_LIST`)
2. `ALL_COUNTRIES` in `admin/index.html` (admin country checkboxes)

Groups: English high-CPC (US,GB,CA,AU,IE,NZ,SG,AE) / Spanish LatAm (AR,MX,CL,CO,PE,UY,VE,EC,BO,PY,CR,PA,DO,PR) / Spanish Europe (ES) / Portuguese (BR,PT) / French (FR,BE,CH) / German (DE,AT) / Nordic (SE,NO,DK,FI) / Other European (NL,IT,GR)

---

## Countdown Engine — AUTO Date Formulas

### CONFIRMED CORRECT dates (verified, do not change without research):

**Día del Niño:**
- `AR` = 3rd Sunday of August → `nthWeekday(y, 7, 3, 0)` ✅ (user confirmed)
- `UY` = 2nd Sunday of August → `nthWeekday(y, 7, 2, 0)` ✅
- `CL` = 4th Sunday of October → `nthWeekday(y, 9, 4, 0)` ✅
- `MX` = April 30 (fixed) ✅
- `BR` = October 12 (fixed, Dia das Crianças) ✅
- default = November 20 (UN International Children's Day) ✅

**Día de la Madre:**
- `AR`, `UY` = 3rd Sunday October ✅
- `MX` + most LatAm = May 10 (fixed) ✅
- `GB`, `IE` = Mothering Sunday = Easter − 21 days ✅
- `FR` = Last Sunday of May ✅
- `PT` = 1st Sunday of May ✅
- default = 2nd Sunday of May (US/CA/AU/etc.) ✅

**Día del Padre:**
- `ES` = March 19 (San José, fixed) ✅
- `BR` = 2nd Sunday of August ✅
- default = 3rd Sunday of June ✅

**Other key formulas:**
- `thanksgiving` = 4th Thursday November (US) ✅
- `memorial-day` = Last Monday of May ✅
- `labor-day` = 1st Monday of September (US-style) ✅
- `black-friday` = 4th Friday November ✅
- `cyber-monday` = Black Friday + 3 days ✅
- `easter` = Computus algorithm ✅
- `full-moon` = pre-calculated table ✅
- `new-year` = TZ-aware Jan 1 ✅
- `christmas` = TZ-aware Dec 25 ✅

### Country National Days (COUNTRY_NATIONAL_DATES):
All stored as `{m: month_0indexed, d: day}`. Verified entries:
- AR: Jul 9 (Independence Day) ✅
- 25-de-mayo: May 25 (AR only, Revolution Day) ✅
- CL: Sep 18 (fiestas-patrias) ✅
- BR: Sep 7 ✅
- US: Jul 4 ✅
- FR: Jul 14 ✅
- NO: May 17 ✅
- CH: Aug 1 ✅
- DE: Oct 3 ✅
- AE: Dec 2 ✅

---

## CSS — Known Bugs Fixed (do NOT revert)

### Hero label text visibility
- `.hub-hero-label span` was sizing ALL spans to 6×6px, hiding the text span
- **Fix**: Changed to `.hub-hero-label span:first-child` in `countdown.css`
- **Do NOT** change back to `.hub-hero-label span`

### Footer visibility in dark mode
- `.site-footer { color: rgba(255,255,255,.5) }`
- `[data-theme="light"] .site-footer { color: rgba(0,0,0,.35) }`
- Located in inline `<style>` in `index.html`

---

## Known Limitations / TODOs

- Individual countdown pages (`/countdown/xxx/`) are static HTML — date changes via admin take ~1 min to deploy
- Thanksgiving is US-only (Canada = 2nd Monday October — not yet implemented)
- Labor Day shows US date (Sep) — many countries celebrate May 1 instead (not yet split)
- Hub pages for Nordic/German-speaking countries fall back to English (`/` not `/de/` etc.)
- `cd_lang` explicit choice persists until next country change

---

## How to Add a New Event

1. Add to `EVENTS` array in `index.html` with `{slug, name, type, countries, regions, cat, url}`
2. If `type: 'variable'`: add entry in `countdowns-data.json`
3. If `type: 'auto'`: add getter function in `countdown-engine.js` AUTO dict
4. Add to `events-meta.json` (countries + cat)
5. Generate countdown page: add to `_generate_hubs.py` EVENTS list and run `python3 _generate_hubs.py`
6. Push to GitHub

## Language Support
- EN: default (`/`)
- ES: `/es/` (hub) + `/es/countdown/*/`
- PT: `/pt/` (hub) + `/pt/countdown/*/`
- FR: `/fr/` (hub) + `/fr/countdown/*/`
- Other languages fall back to English pages
