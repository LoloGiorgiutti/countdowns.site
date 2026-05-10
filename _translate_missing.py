#!/usr/bin/env python3
"""
Generates missing content/faqs translations for all language pages.

Reads EVENTS from _generate.py and existing translations from _translations.py,
then calls Claude API to fill in missing content/faqs for each (lang, slug) pair.
Results are saved to _translations_auto.py (never overwrites _translations.py).
_generate.py automatically merges both files (manual translations take priority).

Usage:
  export ANTHROPIC_API_KEY=sk-ant-...
  python3 _translate_missing.py

Install deps if needed:
  pip install anthropic
"""
import os, sys, json

try:
    import anthropic
except ImportError:
    print("ERROR: anthropic package not found. Run: pip install anthropic")
    sys.exit(1)

from _generate import EVENTS, SLUG_LANGS
from _translations import TRANSLATIONS

try:
    from _translations_auto import TRANSLATIONS_AUTO
except ImportError:
    TRANSLATIONS_AUTO = {}

LANG_NAMES = {
    'es': 'Spanish',
    'pt': 'Brazilian Portuguese',
    'fr': 'French',
}

client = anthropic.Anthropic()  # reads ANTHROPIC_API_KEY from env


def translate_event(slug, name, content, faqs, target_lang):
    lang_name = LANG_NAMES[target_lang]
    prompt = (
        f'Translate this countdown page content from English to {lang_name}.\n'
        f'Event: "{name}"\n\n'
        f'Article (translate this):\n{content or "(none)"}\n\n'
        f'FAQs (translate questions and answers):\n'
        f'{json.dumps(faqs or [], ensure_ascii=False)}\n\n'
        f'Return ONLY valid JSON with two keys:\n'
        f'{{"content": "translated article", "faqs": [["translated q", "translated a"], ...]}}\n\n'
        f'Rules:\n'
        f'- Keep proper nouns, brand names, numbers, dates unchanged\n'
        f'- Be natural and idiomatic in {lang_name}\n'
        f'- Use empty string if content input is "(none)"\n'
        f'- Return empty array if faqs input is empty'
    )
    msg = client.messages.create(
        model='claude-haiku-4-5-20251001',
        max_tokens=2048,
        messages=[{'role': 'user', 'content': prompt}]
    )
    text = msg.content[0].text.strip()
    if text.startswith('```'):
        text = '\n'.join(text.split('\n')[1:])
        text = text.rsplit('```', 1)[0].strip()
    data = json.loads(text)
    return {
        'content': data.get('content', '') or '',
        'faqs': [tuple(f) for f in (data.get('faqs') or [])],
    }


def _get_existing(lang, slug):
    """Return merged translation entry: auto first, manual overrides."""
    auto = TRANSLATIONS_AUTO.get(lang, {}).get('events', {}).get(slug, {})
    manual = TRANSLATIONS.get(lang, {}).get('events', {}).get(slug, {})
    merged = dict(auto)
    merged.update(manual)
    return merged


def main():
    if not os.environ.get('ANTHROPIC_API_KEY'):
        print('ERROR: ANTHROPIC_API_KEY env var not set.')
        sys.exit(1)

    # Build the updated auto-translations dict
    import copy
    updated = copy.deepcopy(TRANSLATIONS_AUTO)

    count = 0
    skipped = 0

    for ev in EVENTS:
        slug = ev['slug']
        content_en = ev.get('content', '')
        faqs_en = ev.get('faqs', [])

        if not content_en and not faqs_en:
            continue  # nothing to translate

        for lang in ['es', 'pt', 'fr']:
            if lang not in SLUG_LANGS.get(slug, set()):
                continue

            t = _get_existing(lang, slug)

            needs_content = bool(content_en) and not t.get('content')
            needs_faqs = bool(faqs_en) and not t.get('faqs')

            if not needs_content and not needs_faqs:
                skipped += 1
                continue

            print(f'  {slug} → {lang}...', end=' ', flush=True)
            try:
                result = translate_event(
                    slug, ev['name'],
                    content_en if needs_content else '',
                    faqs_en if needs_faqs else [],
                    lang,
                )

                if lang not in updated:
                    updated[lang] = {'events': {}}
                if 'events' not in updated[lang]:
                    updated[lang]['events'] = {}
                if slug not in updated[lang]['events']:
                    updated[lang]['events'][slug] = {}

                if needs_content and result['content']:
                    updated[lang]['events'][slug]['content'] = result['content']
                if needs_faqs and result['faqs']:
                    updated[lang]['events'][slug]['faqs'] = result['faqs']

                count += 1
                print('✓')
            except Exception as e:
                print(f'✗  {e}')

    if count == 0:
        print(f'Nothing new to translate ({skipped} already complete). All done.')
        return

    # Write _translations_auto.py
    out_path = '_translations_auto.py'
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write('"""\nAuto-generated translations — do not edit manually.\n')
        f.write('Run _translate_missing.py to regenerate.\n"""\n\n')
        f.write('TRANSLATIONS_AUTO = {\n')
        for lang, lang_data in updated.items():
            f.write(f'  {repr(lang)}: {{\n')
            f.write(f'    \'events\': {{\n')
            for slug, fields in lang_data.get('events', {}).items():
                f.write(f'      {repr(slug)}: dict(\n')
                if fields.get('content'):
                    f.write(f'        content={repr(fields["content"])},\n')
                if fields.get('faqs'):
                    f.write(f'        faqs=[\n')
                    for q, a in fields['faqs']:
                        f.write(f'          ({repr(q)}, {repr(a)}),\n')
                    f.write(f'        ],\n')
                f.write(f'      ),\n')
            f.write(f'    }},\n')
            f.write(f'  }},\n')
        f.write('}\n')

    print(f'\n✓ Wrote {count} new translations to {out_path}')
    print('  Now run: python3 _generate.py')


if __name__ == '__main__':
    main()
