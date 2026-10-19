# Deck v4

Follow `../AGENTS.md` and `../CLAUDE.md`. Design and speaker-note principles live in the root `CLAUDE.md`; this file adds deck-specific rules. An explicit request to review the whole deck authorizes changes to every slide.

v4 is a copy of `deck-v3/` taken 18 Oct 2026 and redesigned: new visual identity, new layout, new story spine. Do not re-sync styling from v1, v2 or v3.

## Commands
Run from the project root. `<scratchpad>` is the session scratchpad directory.

| Command | Description |
|---------|-------------|
| `marp deck-v4/deck.md --allow-local-files --images png -o <scratchpad>/s.png </dev/null` | Render every slide to PNG for checking |
| `marp deck-v4/deck.md --allow-local-files -o deck-v4/deck.html </dev/null` | Regenerate `deck.html` (never hand-edit it) |
| `python3 deck-v4/check_deck.py` | Check notes, scoped font sizes, image paths; lists visible TODOs. Tests: `cd deck-v4 && python3 -m unittest test_check_deck` |

`</dev/null` is required: marp hangs on stdin otherwise.

## Story spine
TED-style, built to give the payoff early: tease, reveal, explain, answer the objection, ask. One through-line: AI stops waiting to be asked, so the chores nobody schedules get done.

1. **Hook:** a statement with no source on it (*A page in our docs is wrong right now.*).
2. **The problem:** one big number (56.5% outdated information), then the volume that widens it.
3. **The earlier attempt:** the personal beat; its third beat must land on "it only ran when a person remembered to run it".
4. **The turn:** an assistant waits to be asked; this one works a shift.
5. **The result:** when GitHub ran a docs workflow, people merged 57 of the 59 pull requests it opened, with the weaker rates from the same post beside it.
6. **How it works:** a teammate you brief, the real 13-line file, one command that compiles it.
7. **Is it safe:** it will get things wrong; no write key; layers, not one wall.
8. **What I've built, then the ask:** 98 written and 0 run, then one stale page for a month.
9. **Appendix** (header `Appendix`): three kinds of work, triggers, autonomy ladder, one-page spec, debugging, links, status and sources.

The result comes before the mechanism on purpose (v3 put it after safety). Keep the file slide before the safety slides, so the room has seen a real workflow before being told why it is safe. Show `staged: true` on the ask slide only.

Marp's `<!-- header: ... -->` persists to later slides until changed, so a header set on one slide labels the whole act. Reordering slides can leave a label on the wrong act: re-check labels after any move.

## Visual language
A dark stage: near-black canvas, off-white heavy sans type, one hot accent. Big type, one idea per slide, generous space.

### Palette
- **The palette is defined once, as custom properties on `section` in the front-matter `style:` block, and nowhere else.** Slide rules, `<style scoped>` blocks and the `img/*.svg` prelude refer to those names. Never write a literal colour outside that definition; if a slide needs a shade with no name, add a named token.
- The SVG diagrams carry their own copy of the palette in a `:root{}` line and in the arrow-marker `fill` values, because they are standalone files. When the palette changes, retint every `img/*.svg` in one pass so they cannot drift from `deck.md`.
- Roles: ink for text, one accent (`--accent`), one caution colour (`--warn`), one success colour (`--good`), greys for panels and borders. No fifth role.
- **Spend the accent sparingly:** section label, the one big number, list markers, flow arrows, the single element a slide argues about. Not every bold word.
- Caution marks genuine weak boundaries and warnings (dashed stroke plus glyph). Success marks permitted writes only. **Gaps (`.todo`) use neutral grey with a dashed border, never the caution colour.**
- Use `<style scoped>` for one-slide tweaks; never change the global theme to fix one slide.

### Layout
- Headlines 44 px or larger (slides that carry a diagram use 44 to 46 px so the picture fits), body at least 20 px, code at least 18 px. Never shrink essential content to keep a slide count.
- Classes: `say` (one huge statement, left-aligned, vertically centred), `num` (centred block for a big number), `.stat` (the number), `.muted` (sources), `.todo` (gap), `.k` (small caps label), `.card`/`.cards` (panels), `.source` (pinned footer line).
- Slide 1 carries the GitHub mark and wordmark, the deck title large with a short accent rule beneath, and the Octocat inside the six-step loop on the right. Keep "Open PR", never "Deploy".
- Diagram slides: set `section { padding-top: 80px }`, keep the title to two lines, and size the image with `w:` (1136 fits the full width). Always render and check the bottom edge.
- No state may be signalled by colour alone: every diagram pairs colour with a glyph (`#g-key` / `#g-nokey`, `#g-warn` plus dashed stroke, `#g-lock`) or a stroke style.
- Give every diagram a descriptive `aria-label` or `<title>`/`<desc>`. Label conceptual diagrams as illustrative.
- Show denominators and source dates for statistics. No invented screenshots, logos or demo outcomes.

## Speaker notes
- Every slide has Marp speaker notes in a plain HTML comment after the slide body. Directive comments (`<!-- header: ... -->`, `<!-- _class: ... -->`) are separate comments.
- Notes follow the root order: the plain-English line to say, technical detail, numbers and sources, likely questions, then a transition. Careful-wording warnings live here.
- Speak them rather than read them: the first line of each note is what you say out loud.

## Verification
- After any edit, render and look at every changed slide. Nothing may run off the bottom edge or overlap. Compiling is not a visual check.
- Run `python3 deck-v4/check_deck.py`; confirm 0 errors.
- `deck.md` is the only source; regenerate `deck.html` after every change.

## Pending work
- `todo.md` lists what still needs content or verification.
- `RESOURCES.md` records better material with primary sources and check dates. Its v4 section is first; the rest was written for v3 and uses v3 slide numbers, so match by title.
- Two findings stay **unverified on purpose** and must not reach a slide: `environment:` as a human approval gate before the write job, and `protected-files:` as path enforcement.
- Real pull requests for the proof slide: `github/gh-aw` #69936, #69394 and #68929 (as of 18 Oct 2026); v3 and v4 use these so no deck shows another deck's PR.
