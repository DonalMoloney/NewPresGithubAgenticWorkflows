@AGENTS.md

## Claude Code specifics
- After editing `draft-overview.html`, open it with Playwright and screenshot light and dark mode plus a phone-width viewport before saying it is done.
- The HTML is draft material for slides. When the user asks to build the final deck, use the `slides` skill and reuse the draft diagrams and wording rather than redesigning them.
- Keep edits surgical: change only the slide the user named.
- When creating the deck (in `deck-v1/`: `deck.md` content, `deck.html` slides), build from `slide-styling/title-slide.html`: it is the title slide and the reference for layout, blue neon palette (not red) and styling of every other slide. Reuse its structure and tokens rather than the `-v2` variants.
- Folder layout is in `AGENTS.md`. Keep `overview.md` at the root; draft HTML lives in `slide-styling/`.

## Deck design principles (all decks)
- **One idea per slide.** The title is the claim; the body is the evidence for it. If a slide overflows, split it into two claim-titled slides. Never shrink body text below 20px or code below 18px to make it fit.
- **Plain English first, technical second.** The room is mixed. Reuse the teammate model throughout: job description = markdown body, shift = `on:`, access badge = `permissions`/`tools`, outbox = `safe-outputs`.
- **Show mechanism over quotes.** A real setting (`draft: true`, `max-ai-credits`, the separate write job) beats a blog quote. Use quotes as support, not proof.
- **Real artifacts over invented examples.** Show `workflows/update-docs.md` from githubnext/agentics. Label it "trimmed" or "paraphrased" when cut.
- **Every number and quote carries a muted on-slide source,** plus its caveat: "illustrative", "reported by GitHub", "this deck's interpretation".
- **Never overclaim safety.** Do not say detection "always blocks" (`continue-on-error` defaults to `true`). Present "never merged automatically" as GitHub Blog guidance, not a hard limit.
- **When official sources conflict, leave the fact off the slide** and record the conflict on the deck's status and sources slide (e.g. the daily AI Credit cap default).
- **Say each fact once.** Do not repeat a point across slides.
- **Keep gaps visible** as orange TODO markers until the user supplies real content.

## Speaker notes (all decks)
- Give every slide a note. Write it in this order: the plain-English line to say, the technical detail, exact numbers and quotes with sources, then likely audience questions with answers.
- Put careful-wording warnings in the notes (what not to claim).
- Write TODO in a note rather than inventing the story or the ask.
