#!/usr/bin/env python3
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BANNED_JS = ROOT / "banned-words.js"
BACKUP = ROOT / "banned-words.js.bak"

text = BANNED_JS.read_text(encoding="utf-8")
match = re.search(r"window\.BANNED_WORDS\s*=\s*\[([\s\S]*?)\];", text)
if not match:
    raise SystemExit("Could not find window.BANNED_WORDS array in banned-words.js")

items = re.findall(r'"((?:\\.|[^"\\])*)"|\'((?:\\.|[^\'\\])*)\'', match.group(1))
words = [a or b for (a, b) in items]
words = [word.strip() for word in words if word.strip()]

output = ["window.BANNED_WORDS = ["]
for index, word in enumerate(words):
    escaped = word.replace("\\", "\\\\").replace('"', '\\"')
    comma = "," if index < len(words) - 1 else ""
    output.append(f'  "{escaped}"{comma}')
output.append("];")
output_text = "\n".join(output) + "\n"

BACKUP.write_text(text, encoding="utf-8")
BANNED_JS.write_text(output_text, encoding="utf-8")
print(f"Wrote {BANNED_JS} with {len(words)} entries; backup at {BACKUP}")
