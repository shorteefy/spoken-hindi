#!/usr/bin/env python3
"""hindi_check.py - a check tool for Spoken Hindi.

Finds violations of the Spoken Hindi writing rules in text or Markdown.
Uses only the Python standard library. Word tables are read from
references/substitutions.md and references/word-list.md, so new words
go into those files, not into this script.

Usage:
    python hindi_check.py [--mode procedural|descriptive|mixed] [--strict] FILE...
    (FILE can be .md, .txt, or .html. HTML tags, <pre>, and <code> are skipped.)
    cat draft.md | python hindi_check.py --mode descriptive

The tool ignores code blocks, inline code, URLs, and YAML frontmatter.
Exit code 0 = no errors. Exit code 1 = one or more errors.
Warnings never change the exit code.
"""

import argparse
import html
import io
import re
import sys
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

SKILL_DIR = Path(__file__).resolve().parent.parent
SUBS_FILE = SKILL_DIR / "references" / "substitutions.md"
WORDS_FILE = SKILL_DIR / "references" / "word-list.md"

LIMITS = {"procedural": 20, "descriptive": 25, "mixed": 25}
MAX_PARA_SENTENCES = 6

DEVA = r"ऀ-ॿ"
# Letters only: the danda (U+0964, U+0965) and digits are not part of a word.
DEVA_WORD = re.compile("[ऀ-ॣ॰-ॿ]+")
DEVA_DIGIT = re.compile(r"[०-९]")

# Rule 2.2: Roman Hindi. Only words that are almost never English.
ROMAN_HINDI = {
    "hai", "hain", "nahi", "nahin", "nahee", "karo", "karna", "karte",
    "karta", "karti", "kya", "kaise", "kyun", "kyon", "kyunki", "matlab",
    "lekin", "aur", "mein", "kuch", "abhi", "phir", "isliye", "yeh",
    "woh", "tha", "thi", "raha", "rahi", "rahe", "gaya", "hoga", "chahiye",
    "sakta", "sakte", "wala", "wali", "wale", "bhi", "agar", "toh",
    "kijiye", "dijiye", "lijiye", "dekho", "batao", "chalo", "accha",
    "acha", "theek", "thik", "haan", "bahut", "zyada", "jaldi",
}

# Rule 4.3: passive with जाना after a perfective participle.
PASSIVE_JANA = re.compile(
    rf"[{DEVA}]+(?:या|यी|ये|ई|ए|ा|ी|े)\s+"
    r"(?:जाता|जाती|जाते|जाएगा|जाएगी|जाएँगे|जाएंगे|जाना|जा\s+सक|जा\s+रहा|जा\s+रही|जा\s+रहे)"
)
# Active uses of "<verb> जाना" that are not passive.
PASSIVE_FALSE = {"चला", "चली", "चले", "आ", "हो", "बन", "रह", "सो", "मिल", "भाग", "ले", "दे"}

TU_FORMS = re.compile(r"(?<![ऀ-ॿ])(?:तुम|तुम्हें|तुमको|तुम्हारा|तुम्हारी|तुम्हारे|तुमने)(?![ऀ-ॿ])")
AAP_FORMS = re.compile(r"(?<![ऀ-ॿ])(?:आप|आपको|आपका|आपकी|आपके|आपने)(?![ऀ-ॿ])")

# A sentence ends at । ? ! · or at ". " (English sentences).
SENT_SPLIT = re.compile(r"(?<=[।?!·])\s+|(?<=[.])\s+(?=[A-Zऀ-ॿ])")

# Verb and noun endings stripped in --strict mode to find a word-list root.
SUFFIXES = sorted([
    "ना", "नी", "ने", "ता", "ती", "ते", "ा", "ी", "े", "ो", "ें", "ों", "ूँ",
    "एगा", "एगी", "एँगे", "एंगे", "ेगा", "ेगी", "ेंगे", "ऊँगा", "इए", "िए",
    "इये", "िये", "ाइए", "कर", "ाओ", "ओ", "ए", "ई", "या", "यी", "ये",
    "ियाँ", "ियां", "ाएँ", "ाएं", "एँ", "एं",
], key=len, reverse=True)


# ---------------------------------------------------------------- tables

def read_table(text, header_start):
    """Return the rows of the first Markdown table after a header line."""
    rows = []
    start = text.find(header_start)
    if start < 0:
        return rows
    in_table = False
    for line in text[start:].splitlines()[1:]:
        if line.startswith("|"):
            in_table = True
            cells = [c.strip() for c in line.strip("|").split("|")]
            if set(cells[0]) <= set("-: "):
                continue
            rows.append(cells)
        elif in_table:
            break
    return rows[1:]  # drop the header row


def load_substitutions():
    text = SUBS_FILE.read_text(encoding="utf-8")
    formal = {}
    for cells in read_table(text, "## हिस्सा 1"):
        level = cells[2] if len(cells) > 2 else "error"
        formal[cells[0]] = (cells[1], level)
    translit = {}
    for cells in read_table(text, "## हिस्सा 2"):
        level = cells[2] if len(cells) > 2 else "error"
        translit[cells[0]] = (cells[1], level)
    return formal, translit


def load_word_roots():
    roots = set()
    for line in WORDS_FILE.read_text(encoding="utf-8").splitlines():
        if not re.match(rf"^[{DEVA}]", line):
            continue
        head = line.split("—")[0]
        for w in DEVA_WORD.findall(head):
            roots.add(w)
            if w.endswith("ना") and len(w) > 2:
                roots.add(w[:-2])
    return roots


# ---------------------------------------------------------------- helpers

# HTML input: paragraph breaks become PARA, so line numbers stay the same.
PARA = "\x1e"
BLOCK_TAG = re.compile(r"</?(?:p|li|ul|ol|h[1-6]|div|section|article|header|footer|nav|"
                       r"tr|td|th|table|blockquote|br|hr|dt|dd|figcaption|button|label)\b[^>]*>",
                       re.IGNORECASE)


def blank_out(m):
    """Replace a match with spaces but keep its newlines, so line numbers stay the same."""
    return re.sub(r"[^\n]", " ", m.group())


def strip_html(text):
    """Remove markup, code, styles, and scripts from an HTML file."""
    text = re.sub(r"(?is)<!--.*?-->", blank_out, text)
    text = re.sub(r"(?is)<(style|script|pre|code|svg|head)\b.*?</\1>", blank_out, text)
    text = BLOCK_TAG.sub(f" {PARA} ", text)
    text = re.sub(r"<[^>]*>", " ", text)
    return html.unescape(text)


def strip_markdown(text):
    """Remove the parts of the text that the rules do not control."""
    text = re.sub(r"^---\n.*?\n---\n", "", text, flags=re.DOTALL)
    text = re.sub(r"```.*?```", lambda m: "\n" * m.group().count("\n"), text, flags=re.DOTALL)
    text = re.sub(r"`[^`\n]*`", " CODE ", text)
    text = re.sub(r"https?://\S+", " URL ", text)
    text = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", text)
    return text


def clean_line(line):
    line = line.replace(PARA, " ")
    line = re.sub(r"^\s*(?:#+|[-*>]|\d+[.)])\s*", "", line)
    line = line.replace("**", "").replace("__", "")
    return line


def word_boundary(word):
    return re.compile(rf"(?<![{DEVA}]){re.escape(word)}(?![{DEVA}])")


def paragraphs(text):
    """Yield (first_line_no, paragraph_text) pairs. Tables are skipped."""
    buf, start = [], None
    for no, line in enumerate(text.splitlines(), 1):
        if not line.strip() or line.lstrip().startswith("|"):
            if buf:
                yield start, " ".join(buf)
            buf, start = [], None
            continue
        if re.match(r"^\s*(?:#+|[-*]|\d+[.)])\s", line) and buf:
            yield start, " ".join(buf)
            buf, start = [], None
        pieces = line.split(PARA)
        for i, piece in enumerate(pieces):
            if i > 0 and buf:
                yield start, " ".join(buf)
                buf, start = [], None
            if not piece.strip():
                continue
            if start is None:
                start = no
            buf.append(clean_line(piece))
    if buf:
        yield start, " ".join(buf)


# ---------------------------------------------------------------- checks

def check(text, mode, strict, formal, translit, roots, is_html=False):
    issues = []  # (line, level, rule, message)
    body = strip_markdown(strip_html(text) if is_html else text)
    lines = body.splitlines()

    formal_res = [(w, word_boundary(w), sub, lvl) for w, (sub, lvl) in formal.items()]
    translit_res = [(w, word_boundary(w), eng, lvl) for w, (eng, lvl) in translit.items()]

    for no, raw in enumerate(lines, 1):
        if raw.lstrip().startswith("|"):
            continue
        line = clean_line(raw)

        has_hindi = bool(DEVA_WORD.search(line))

        for w, rx, eng, lvl in translit_res:
            if rx.search(line):
                issues.append((no, lvl, "2.3", f'"{w}" Devanagari में है। English में लिखिए: {eng}'))

        for w, rx, sub, lvl in formal_res:
            if rx.search(line):
                issues.append((no, lvl, "1.3", f'"{w}" formal है। बोलचाल वाला लिखिए: {sub}'))

        roman = [w for w in re.findall(r"[A-Za-z]+", line) if w.lower() in ROMAN_HINDI]
        if len(roman) >= 2:
            issues.append((no, "error", "2.2", f"Roman Hindi: {', '.join(roman[:5])}। Devanagari में लिखिए।"))

        if DEVA_DIGIT.search(line):
            issues.append((no, "error", "2.4", "देवनागरी अंक हैं। 0–9 वाले अंक लिखिए।"))

        if ";" in line and has_hindi:
            issues.append((no, "error", "5.5", "Semicolon है। दो sentence बनाइए।"))

        if re.search(rf"[{DEVA}]\.(?:\s|$)", line):
            issues.append((no, "error", "9.1", 'Hindi sentence "." से ख़त्म हुआ। "।" लगाइए।'))

        for m in PASSIVE_JANA.finditer(line):
            first = m.group().split()[0]
            if first not in PASSIVE_FALSE:
                issues.append((no, "warning", "4.3", f'शायद passive: "{m.group()}"। करने वाले को subject बनाइए।'))

        if "द्वारा" in line and not any(i[0] == no and "द्वारा" in i[3] for i in issues):
            issues.append((no, "error", "4.2", '"द्वारा" passive बनाता है। Active sentence लिखिए।'))

        if strict:
            for w in DEVA_WORD.findall(line):
                if not known(w, roots):
                    issues.append((no, "warning", "1.1", f'"{w}" word-list में नहीं है।'))

    # Rule 5.1 and 7.6: sentence length and paragraph size.
    limit = LIMITS[mode]
    # Only sentences with Hindi count. English UI text and sample data are not checked.
    for start, para in paragraphs(body):
        sentences = [s for s in SENT_SPLIT.split(para) if DEVA_WORD.search(s)]
        for s in sentences:
            n = len([t for t in s.split() if re.search(rf"[\w{DEVA}]", t)])
            if n > limit:
                issues.append((start, "error", "5.1", f"Sentence में {n} शब्द हैं (limit {limit}): \"{s[:60]}…\""))
        if len(sentences) > MAX_PARA_SENTENCES:
            issues.append((start, "error", "7.6", f"Paragraph में {len(sentences)} sentence हैं (limit {MAX_PARA_SENTENCES})।"))

    # Rule 6.2: आप and तुम mixed in one text.
    if TU_FORMS.search(body) and AAP_FORMS.search(body):
        issues.append((0, "error", "6.2", "आप और तुम दोनों हैं। एक ही form रखिए।"))

    return sorted(issues, key=lambda i: (i[0], i[2]))


def known(word, roots):
    if word in roots:
        return True
    for suf in SUFFIXES:
        if word.endswith(suf) and len(word) > len(suf):
            stem = word[: -len(suf)]
            if stem in roots or stem + "ा" in roots or stem + "ना" in roots:
                return True
    return False


# ---------------------------------------------------------------- main

def main():
    ap = argparse.ArgumentParser(description="Check text against the Spoken Hindi rules.")
    ap.add_argument("files", nargs="*", help="files to check (default: standard input)")
    ap.add_argument("--mode", choices=LIMITS, default="mixed",
                    help="procedural = 20 words, descriptive/mixed = 25 words per sentence")
    ap.add_argument("--strict", action="store_true",
                    help="also warn about Devanagari words that are not in the word list")
    args = ap.parse_args()

    formal, translit = load_substitutions()
    roots = load_word_roots() if args.strict else set()

    if args.files:
        sources = [(f, Path(f).read_text(encoding="utf-8")) for f in args.files]
        sources = [(f, t, Path(f).suffix.lower() in (".html", ".htm")) for f, t in sources]
    else:
        stdin = io.TextIOWrapper(sys.stdin.buffer, encoding="utf-8")
        data = stdin.read()
        sources = [("<stdin>", data, data.lstrip().lower().startswith(("<!doctype", "<html")))]

    errors = warnings = 0
    for name, text, is_html in sources:
        for no, level, rule, msg in check(text, args.mode, args.strict, formal, translit, roots, is_html):
            where = f"{name}:{no}" if no else name
            print(f"{where}: {level} [नियम {rule}] {msg}")
            errors += level == "error"
            warnings += level == "warning"

    print(f"\n{errors} error, {warnings} warning")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
