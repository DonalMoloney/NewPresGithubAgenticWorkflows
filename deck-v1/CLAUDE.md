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
- Bookend theme (deliberate, user-chosen 17 Oct 2026): the title slide and the decision slide are deep cinematic black (`#050507`, dark vignette) with purple accents (`#a98bf0` / `#d3c4fb`), set in each slide's `<style scoped>`. Every other slide is white. Thin borders, generous space, no red theme.
- Glow and neon only on the title slide's central Octocat. No glow on rules, bars, boxes or wires.
- Make slide 1 follow the layout of `../slide-styling/title-slide.html`: GitHub mark and wordmark, then the deck's title as a large heading with a short rule beneath it on the left; the Octocat inside the six-step loop (Plan, Code, Test, Review, Open PR, Monitor) on the right. Reuse its SVG rather than redesigning. Keep "Open PR", never "Deploy": gh-aw does not deploy.
- Keep all theme CSS in the front-matter `style:` block (inner slides use GitHub's Primer light palette: canvas `#ffffff`, panel `#f6f8fa`, border `#6e7781`, text `#1f2328`, muted `#59636e`, accent `#0969da` / `#0550ae`, caution `#bc4c00`, success `#1a7f37`; tinted fills accent `#ddf4ff`, caution `#fff1e5`, success `#dafbe1`). Code blocks are light (`var(--panel)` `#f6f8fa`, text `var(--ink)` `#1f2328`, 1px `var(--line)` border), matching how GitHub's own docs set code — user-chosen 17 Oct 2026, replacing the earlier dark `#080808` panels, which read as a leftover once the slides went white. Use `<style scoped>` for one-slide tweaks; never change the global theme to fix one slide.
- `img/*.svg` hardcode the same light palette in their own `:root`; change them together with the front matter.
- The border token deliberately departs from Primer. Primer's own `borderColor-default` `#d0d7de` is 1.45:1 on white, far below WCAG's 3:1 for non-text, and a projector is dimmer than a monitor, so box strokes and card borders dissolve. `#6e7781` is still a Primer grey and measures 4.55:1 on white, 4.27:1 on panel and 4.00–4.11:1 on the tinted fills. The bookend slides use `#6b6280` (3.57:1 on `#050507`) for the same reason. Do not "correct" either back to the Primer web value. Checked 17 Oct 2026.
- Use one grid, title position, footer, spacing scale and page numbering. Orange is for unresolved details or cautions; green sparingly for permitted outcomes.
- At 1280 × 720: 44–54 px headlines, 26–32 px body, at least 20 px code. Compact citations may be smaller. Never shrink essential content to keep a slide count.
- Process diagram for sequence, paired panels for comparison, code card with adjacent annotations for a file, chart for measured outcomes. Tables only when rows and columns help comparison.
- Use `.muted` for sources, `.todo` for gaps, `.stat` for one big hook number.
- Remove decorative quotes, audience labels and repeated prose. Every visual must explain something.
- Label conceptual diagrams as illustrative. Show denominators and source dates for statistics. No invented screenshots, logos or demo outcomes.
- Give diagrams descriptive SVG labels; do not convey meaning by colour alone.

## Speaker notes
- Every slide, including the title and source appendix, has Marp speaker notes in a plain HTML comment `<!-- … -->` after the slide body. Directive comments like `<!-- _class: lead -->` are not notes; keep them in separate comments.
- Notes follow the root order (plain-English line, technical detail, numbers and sources, audience questions) and end with a transition. Do not merely repeat the slide.
- Put technical depth, commands, source qualifications, preparation TODOs and fallback demo steps in notes. Keep essential qualifications on the slide too.
- Keep `speaker-notes.md` in sync as the rehearsal copy.

## Verification
- After any edit, render and look at every changed slide. Nothing may run off the bottom edge or overlap; table and code text must be readable. Check dense code and data slides at full size and at phone width. Compiling is not a visual check.
- Confirm every slide has a note.
- `deck.html` is generated from `deck.md`: never edit it directly. Re-render it, and update `deck.pdf`, after `deck.md` changes.
