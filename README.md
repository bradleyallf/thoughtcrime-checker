# Thoughtcrime Checker

A small static, client-side web app for checking text against a curated banned-word list.

## Files

- `index.html` is the main checker.
- `replacer.html` replaces flagged words and phrases with approved text.
- `banned-words.js` is the canonical banned-word list.
- `banned-words.html` renders the canonical list in the browser.

## Maintenance

To trim whitespace and remove duplicate entries (ignoring case), run:

```sh
python3 scripts/normalize_banned_words.py
```

This preserves the first occurrence and list order, and saves a `.bak` backup.

Serve the repo locally when testing browser behavior:

```sh
python3 -m http.server 8000
```

Then open `http://localhost:8000/index.html`.

If the banned-word list page needs to be regenerated, run:

```sh
python3 scripts/generate_banned_html.py
```

## Deployment

Deployment is handled by GitHub Actions in `.github/workflows/pages.yml`, which publishes the static repo to GitHub Pages.
