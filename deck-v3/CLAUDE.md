# Deck v3

Follow `../AGENTS.md` and `../CLAUDE.md`. Design and speaker-note principles live in the root `CLAUDE.md`; this file adds deck-specific rules. An explicit request to review the whole deck authorizes changes to every slide.

## Commands
Run from the project root. `<scratchpad>` is the session scratchpad directory.

| Command | Description |
|---------|-------------|
| `marp deck-v3/deck.md --allow-local-files --images png -o <scratchpad>/slide.png` | Render every slide to PNG for checking (the flag lets Marp load the diagrams in `deck-v3/img/`) |
| `marp deck-v3/deck.md --notes -o <scratchpad>/notes.txt` | Export speaker notes |
| `python3 deck-v3/check_deck.py` | Check notes, scoped font sizes and image paths; lists visible TODOs. Tests: `cd deck-v3 && python3 -m unittest test_check_deck` |

## Story and content
- Arc: hook → times changing → earlier attempt → **the turn** (assistants wait to be asked; this works a shift) → what it is (teammate model, the three kinds of work, compile, who can start it, the file) → is it safe (honest limits, write token, blast radius) → proof (GitHub's number, the library, the one-page spec) → pilot ask → appendix.
- **Demonstrate before you defend.** v3's structural difference from v2: the mechanism slides come before the safety slides, so the room has seen a real workflow file before being told why it is safe. The file slide raises the alarm (`read-all`, `bash: true`) and the safety act answers it. Do not reorder these back without reading that reasoning.
- Design for a mixed technical and non-technical audience. Each slide has one main point, written as a short, full-sentence claim. The title slide may use the product name.
- Split a slide when it asks the audience to understand two ideas. Keep related slides together, each with a distinct purpose.
- Use `../overview.md` for the brief narrative. Keep its titles and the matching draft diagrams aligned when the story changes.
- Keep facts, illustrative examples, proposals and measured results visibly distinct. Never imply a placeholder is a real workflow, demo or customer result.
- Verify gh-aw claims against official GitHub sources. Date the check and cite sources on the slide; keep qualifications beside the claim they limit.
- Keep TODOs for unknown repo names, workflow files, owners, budgets, baselines and decisions. Move presenter-only preparation into notes, but keep material gaps visible.
- End the main talk with the decision and next step. Put references after it as an appendix.
- Show `staged: true` on the ways-to-run slide and the pilot slide only.

## Visual language
The deck reads as a working document, not a product launch: a light canvas, dark text, thin borders and generous space. Restraint is the house style — if a slide needs more emphasis, give it more space, not more colour.

### Palette
- **The palette is defined once, as custom properties on `section` in the front-matter `style:` block, and nowhere else.** Everything downstream — slide rules, `<style scoped>` blocks, the `img/*.svg` prelude — refers to those names. Never write a literal colour value outside that one definition; if a slide needs a shade that has no name, add a named token rather than inlining it. Changing the deck's colours must stay a one-place edit.
- Four roles, and each colour has exactly one: ink for text, a single accent, one caution colour, one success colour, plus greys for panels, borders and secondary text. Do not introduce a fifth role.
- **Spend the accent sparingly.** It belongs on the title rule, the one big hook number, list markers, flow arrows in diagrams, and the single element a slide is arguing about. It does **not** belong on every bold word, every inline code span, every table header or every heading — tint everything and nothing is emphasised. Bold text carries its own emphasis; leave it ink.
- The caution colour marks unresolved details and gaps only. The success colour marks permitted outcomes only, and sparingly. Never use either decoratively: a clock glyph tinted as a caution on an otherwise neutral diagram reads as a warning that is not there.
- Use `<style scoped>` for one-slide tweaks; never change the global theme to fix one slide.

### Diagrams
- **No state may be signalled by colour alone.** Every diagram encodes meaning with a glyph and/or a stroke style as well: `#g-key` vs `#g-nokey` for the write credential, `#g-warn` plus a dashed stroke for a weak boundary, `#g-lock` for an enforced one. This survives bad projectors and colour-blind viewers, so it holds whatever the palette is.
- All `img/*.svg` share one byte-identical `<style>` + `<defs>` prelude carrying the same token names as the deck. Copy it from any existing diagram rather than writing a new one, and retint by editing the token line in every file at once so they cannot drift apart.
- Give every diagram a descriptive `aria-label` or `<title>`/`<desc>`. Label conceptual diagrams as illustrative.

### Layout
- Slide 1 carries the GitHub mark and wordmark, the deck title as a large heading with a short accent rule beneath it on the left, and the Octocat inside the six-step loop (Plan, Code, Test, Review, Open PR, Monitor) on the right. Keep "Open PR", never "Deploy": gh-aw does not deploy.
- Use one grid, title position, footer, spacing scale and page numbering.
- Headlines 40 px or larger, body at least 20 px, code at least 18 px. Never shrink essential content to keep a slide count.
- Process diagram for sequence, paired panels for comparison, code card with adjacent annotations for a file, chart for measured outcomes. Tables only when rows and columns help comparison. Marp's default theme styles `tr` and `pre` on its own, so the explicit overrides in `style:` must stay.
- Use `.muted` for sources, `.todo` for gaps, `.stat` for one big hook number.
- Remove decorative quotes, audience labels and repeated prose. Every visual must explain something.
- Show denominators and source dates for statistics. No invented screenshots, logos or demo outcomes.

## Speaker notes
- Every slide, including the title and status/sources slide, has Marp speaker notes in a plain HTML comment `<!-- … -->` after the slide body. Directive comments like `<!-- _class: lead -->` are not notes; keep them in separate comments.
- Notes follow the root order (plain-English line, technical detail, numbers and sources, audience questions) and end with a transition. Do not merely repeat the slide.
- Put technical depth, commands, source qualifications, preparation TODOs and fallback demo steps in notes. Keep essential qualifications on the slide too.

## Verification
- After any edit, render and look at every changed slide. Nothing may run off the bottom edge or overlap; table and code text must be readable. Check dense code and data slides at full size. Compiling is not a visual check.
- Confirm every slide has a note.
- `deck.md` is the only source. `deck.html` is **generated from it** — never hand-edit `deck.html`, and regenerate it after changing `deck.md`:
  `marp deck-v3/deck.md --allow-local-files -o deck-v3/deck.html </dev/null`
  It keeps `img/*.svg` as relative links, so `deck.html` must stay in `deck-v3/` beside `img/`. (The `</dev/null` is required: marp hangs waiting on stdin otherwise.)

## Pending work
- `todo.md` in this folder is the consolidated list of patches and proposed slides not yet applied. Check it before starting any editing session.
- `RESOURCES.md` is the research companion to `todo.md`: where `todo.md` records **what is wrong**, `RESOURCES.md` records **what better material exists to put there**, every item with a primary source and a check date. Read it before editing the mechanism act, the safety act, or the proof slides. Its own index table maps each section to a slide **title**, because slide numbers drift (all three decks moved on 18 Oct 2026).
- It is scoped to **this deck's mechanism-first arc**, so it carries the artifact and documentation detail the other two decks do not need: the 344 agentic workflows and 344 committed lock files in `github/gh-aw`, the 50 documented frontmatter settings behind the thirteen shown, and the one documented **hard** block in the whole safety model (a failed or skipped redaction blocks publication even when detection uses `continue-on-error`). `../deck-v1/RESOURCES.md` (cost, business case) and `../deck-v2/RESOURCES.md` (survey and audience evidence) hold deliberately different material. Do not copy between them; cite the source, not the other file.
- Each deck uses **different real pull requests** as examples. v3's three are `github/gh-aw` #69936, #69394 and #68929 — one per kind of work on the "three kinds of work" slide (8 as of 18 Oct 2026), chosen so this deck never shows the PR deck-v2 screenshots.
- Two findings are flagged **unverified on purpose** and must not reach a slide until their semantics are confirmed: `environment:` as a human approval gate before the write job, and `protected-files:` as path enforcement for a docs-only pilot. They are the highest-value items in the file and also the easiest to overclaim.
- `todo.md` §7 is the index of which `RESOURCES.md` findings beat which existing item. Start there rather than re-reading both files.
