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

## Analytics and privacy

All three webpages use Cloudflare Web Analytics to measure visits, page views,
and page performance. Text entered into the checker or replacer is processed
locally in the browser and is not sent to Cloudflare or our servers. No custom
analytics events capture editor input. The site does not collect entered text,
flagged words, replacement output, keystrokes, or session recordings.

The public site token is embedded in the beacon snippet before `</body>` in
`index.html`, `replacer.html`, and `banned-words.html`. The word-list generator
in `scripts/generate_banned_html.py` includes the same snippet and privacy notice
so regeneration preserves them. Update all four files if the token changes.

View reports in the Cloudflare dashboard under **Web Analytics**, selecting
`thoughtcrime-checker.com` and the desired date range. Visits and page views
measure traffic, not an exact count of distinct people. Collection begins after
the snippet is deployed; it cannot reconstruct previously unrecorded traffic.
Nameservers and GitHub Pages hosting do not need to change.
