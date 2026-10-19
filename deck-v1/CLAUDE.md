# Deck v1

Follow `../AGENTS.md` and `../CLAUDE.md`. Design and speaker-note principles live in the root `CLAUDE.md`; this file adds deck-specific rules. An explicit request to review the whole deck authorizes changes to every slide.

## Commands
Run from the project root. `<scratchpad>` is the session scratchpad directory.

| Command | Description |
|---------|-------------|
| `marp --html deck-v1/deck.md --allow-local-files -o deck-v1/deck.html </dev/null` | Render `deck.html` from `deck.md` |
| `marp --html deck-v1/deck.md --allow-local-files --pdf -o deck-v1/deck.pdf </dev/null` | Render `deck.pdf` |
| `marp --html deck-v1/deck.md --allow-local-files --images png -o <scratchpad>/slide.png </dev/null` | Render every slide to PNG for checking |
| `marp deck-v1/deck.md --notes -o <scratchpad>/notes.txt </dev/null` | Export speaker notes |

**Every render needs `--html`.** Without it Marp escapes the inline `<svg>`, and slide 1 comes out as raw SVG source on a black canvas instead of the title layout. The other 19 slides look fine without it, so a flagless render silently damages exactly one slide — verified 17 Oct 2026 by rendering both ways. `--allow-local-files` is needed for `img/*.svg`, and `</dev/null` stops marp hanging on stdin.

## Story and content
- Arc: documentation problem → earlier attempt → agentic workflow → visible example → controls → safe first use → pilot decision.
- Design for a mixed technical and non-technical audience. Each slide has one main point, written as a short, full-sentence claim. The title slide may use the product name.
- Split a slide when it asks the audience to understand two ideas. Keep related slides together, each with a distinct purpose.
- Use `../overview.md` for the brief narrative. Keep its titles and the matching draft diagrams aligned when the story changes.
- Keep facts, illustrative examples, proposals and measured results visibly distinct. Never imply a placeholder is a real workflow, demo or customer result.
- Verify gh-aw claims against official GitHub sources. Date the check and cite sources on the slide; keep qualifications beside the claim they limit.
- Keep TODOs for unknown repo names, workflow files, owners, budgets, baselines and decisions. Move presenter-only preparation into notes, but keep material gaps visible.
- End the main talk with the decision and next step. Put references after it as an appendix.
- Show `staged: true` on the staged-mode slide and the pilot slide only.

## Visual language
- Bookend theme (deliberate, user-chosen 17 Oct 2026): the title slide and the decision slide share one dark surface and one accent, set in each slide's `<style scoped>`; every other slide is white. Thin borders, generous space.
- Glow and neon only on the title slide's central Octocat. No glow on rules, bars, boxes or wires.
- Make slide 1 follow the layout of `../slide-styling/title-slide.html`: GitHub mark and wordmark, then the deck's title as a large heading with a short rule beneath it on the left; the Octocat inside the six-step loop (Plan, Code, Test, Review, Open PR, Monitor) on the right. Reuse its SVG rather than redesigning. Keep "Open PR", never "Deploy": gh-aw does not deploy.
- Keep all theme CSS in the front-matter `style:` block. **The palette is defined there and only there** — read the `section` token block for the current values rather than restating them in this file. Code blocks follow the light panel tokens, matching how GitHub's own docs set code (user-chosen 17 Oct 2026, replacing earlier dark panels, which read as a leftover once the slides went white). Use `<style scoped>` for one-slide tweaks; never change the global theme to fix one slide.
- `img/*.svg` restate the same tokens in their own `:root`, so the diagrams and the front matter must be changed together.
- Contrast is the constraint, not a particular swatch. Every foreground token clears 4.5:1 on every surface it sits on and borders clear 3:1, because a projector is dimmer than a monitor and hairline borders dissolve on one. Re-measure before changing any token; do not swap in a web-default border grey, which is typically far below 3:1 on white. Checked 18 Oct 2026.
- Use one grid, title position, footer, spacing scale and page numbering. Colour carries meaning, not decoration: the accent marks the one idea of a slide, neutral carries all structure, and the reserved caution token appears at most once on a slide and only where GitHub's own docs warn or conflict — never on housekeeping.
- At 1280 × 720: 44–54 px headlines, 26–32 px body, at least 20 px code. Compact citations may be smaller. Never shrink essential content to keep a slide count.
- Process diagram for sequence, paired panels for comparison, code card with adjacent annotations for a file, chart for measured outcomes. Tables only when rows and columns help comparison.
- Use `.muted` for sources, `.todo` for a line of outstanding work, `.gap` for an inline gap marker in a table or field, `.stat` for one big hook number.
- Remove decorative quotes, audience labels and repeated prose. Every visual must explain something.
- Label conceptual diagrams as illustrative. Show denominators and source dates for statistics. No invented screenshots, logos or demo outcomes.
- Give diagrams descriptive SVG labels; do not convey meaning by colour alone.

## Speaker notes
- Every slide, including the title and source appendix, has Marp speaker notes in a plain HTML comment `<!-- … -->` after the slide body. Directive comments like `<!-- _class: lead -->` are not notes; keep them in separate comments.
- Notes follow the root order (plain-English line, technical detail, numbers and sources, audience questions) and end with a transition. Do not merely repeat the slide.
- Put technical depth, commands, source qualifications, preparation TODOs and fallback demo steps in notes. Keep essential qualifications on the slide too.
- Keep `speaker-notes.md` in sync as the rehearsal copy.

## Verification
- After any edit, render and look at every changed slide. Nothing may run off the bottom edge or overlap; table and code text must be readable. Check dense code and data slides at full size. Compiling is not a visual check.
- Confirm every slide has a note.
- `deck.html` is generated from `deck.md`: never edit it directly. Re-render it, and update `deck.pdf`, after `deck.md` changes.

## Pending work
- `todo.md` in this folder is the consolidated list of patches and proposed slides not yet applied. Check it before starting any editing session.
- `RESOURCES.md` is the research companion to `todo.md`: where `todo.md` records **what is wrong**, `RESOURCES.md` records **what better material exists to put there**, every item with a primary source and a check date. Read it before editing the cost slide, the evidence slide, or any slide carrying a `TODO` number.
- It is scoped to **this deck's business case** — money, risk, baseline, decision. `../deck-v2/RESOURCES.md` (audience and survey evidence) and `../deck-v3/RESOURCES.md` (mechanism and frontmatter detail) hold deliberately different material, and each deck uses a different real pull request as its example so no two decks show the same screenshot. Do not copy between them; if a fact is needed in two decks, cite the source, not the other file.
- Its §9 "Do not use" list exists to stop retired claims coming back: notably "~$10 per run" (omits detection's separate 400 AIC budget, so the real ceiling is ~$14) and the daily-AI-credit-cap "conflict", which the docs resolved on 18 Oct 2026.
- `todo.md` §7 is the index of which `RESOURCES.md` findings beat which existing item. Start there rather than re-reading both files.
