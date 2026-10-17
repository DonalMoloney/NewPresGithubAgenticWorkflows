"""Check deck.md against the deck rules in CLAUDE.md.

Errors: a slide without a speaker note, scoped font sizes below 20px
(18px for pre/code), image paths that do not exist.
Warnings: visible TODO markers on a slide.

Usage: python3 check_deck.py [path/to/deck.md]
"""
import os
import re
import sys

DIRECTIVE = re.compile(
    r"^\s*_?(class|header|footer|paginate|backgroundColor|backgroundImage|color|theme|style)\s*:[^\n]*\s*$"
)
FONT = re.compile(r"([^{}]+)\{[^}]*?font-size:\s*(\d+)px", re.S)
IMAGE = re.compile(r"!\[[^\]]*\]\(([^)\s]+)\)")


def split_slides(md):
    """Split Marp markdown into slides, skipping front matter and `---` inside code fences."""
    lines = md.split("\n")
    if lines and lines[0] == "---":
        lines = lines[lines.index("---", 1) + 1:]
    slides, current, fence = [], [], False
    for line in lines:
        if line.startswith("```"):
            fence = not fence
        if line == "---" and not fence:
            slides.append("\n".join(current))
            current = []
        else:
            current.append(line)
    slides.append("\n".join(current))
    return slides


def check(path):
    """Return (errors, warnings) for the deck at path."""
    with open(path) as fh:
        slides = split_slides(fh.read())
    base = os.path.dirname(path)
    errors, warnings = [], []
    for n, slide in enumerate(slides, 1):
        comments = re.findall(r"<!--(.*?)-->", slide, re.S)
        if not any(not DIRECTIVE.match(c) for c in comments):
            errors.append(f"slide {n}: no speaker note")
        for style in re.findall(r"<style scoped>(.*?)</style>", slide, re.S):
            for selector, size in FONT.findall(style):
                size = int(size)
                code = re.search(r"\b(pre|code)\b", selector)
                if size < 18 or (size < 20 and not code):
                    errors.append(f"slide {n}: font-size {size}px on '{selector.strip()}'")
        for src in IMAGE.findall(slide):
            if not src.startswith(("http:", "https:", "data:")) and not os.path.exists(os.path.join(base, src)):
                errors.append(f"slide {n}: missing image {src}")
        todos = len(re.findall(r'class="todo"', slide))
        if todos:
            warnings.append(f"slide {n}: {todos} visible TODO marker(s)")
    return errors, warnings


if __name__ == "__main__":
    deck = sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.path.dirname(__file__), "deck.md")
    errs, warns = check(deck)
    for w in warns:
        print("warn ", w)
    for e in errs:
        print("ERROR", e)
    print(f"{len(errs)} error(s), {len(warns)} warning(s)")
    sys.exit(1 if errs else 0)
