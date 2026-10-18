# Rigor pass: on-slide claim status convention

Patches for `deck-v2/deck.md` **on-slide text only** (slide bodies and muted source lines). Speaker notes and diagrams are other agents' work and are only listed, never patched, at the end.

**Built against** `deck.md` md5 `1ad516b16eb7e1d0135f88bd18ee3e1f`, 17 slides, 2026-10-17. `deck.md` was edited four times while this ran; all 18 OLD strings were re-checked against the latest version and each appears **exactly once**. Before applying, re-check:

```sh
cd /Users/donalmoloney/PycharmProjects/NewPresGithubAgenticWorkflows
grep -c 'PASTE THE OLD STRING' deck-v2/deck.md   # must print 1
```

**Verified**: all 18 patches applied to a scratch copy and rendered with
`marp deck-v2/deck.md --allow-local-files --images png -o <scratch>/f.png </dev/null`.
All 17 slides render with no overflow and no overlap. Three patches add a line (P14, P17, P18); each was rendered and checked. Renders: `/private/tmp/claude-501/-Users-donalmoloney-PycharmProjects-NewPresGithubAgenticWorkflows/524a599c-eb1f-42b9-9c41-8c4edd6dd9a0/scratchpad/rigor/final/`.

Two OLD strings contain a **curly apostrophe** (U+2019): P2 (`deck’s`) and P16 (`file’s`). Copy them exactly.

---

## 1. The convention

**The status word comes first in every muted line that names a source, followed by a colon.** Five words, no more — the audience only has to catch the first one.

| Word | Means | Used on |
|---|---|---|
| **Measured:** | a counted result with a stated method and date — a named study, or your own API check | 2, 3, 11 |
| **Reported by GitHub:** | GitHub's own figure, quote or guidance about its own product | 6, 10, 12, 13 |
| **Self-reported:** | a claim from your own repo, no independent check | 11 |
| **Documented:** | product behaviour or file content read straight from gh-aw's reference docs or a public repo file | 5, 6, 7, 8, 9, 12, 13, 14, 15 |
| **This deck's interpretation:** | your reading, not anyone's claim | 3, 5 |

Three supporting rules:

1. **Labels modify, they don't lead.** *trimmed*, *paraphrased*, *illustrative*, *small sample*, *private* sit **after** the status word, inside the same line. This is the vocabulary the root `CLAUDE.md` already prescribes, so the deck and its own rules use one set of words.
2. **A muted span that names no source is a caveat, not an attribution, and takes no status word.** It stays beside the claim it limits (slide 7's `continue-on-error` line, slide 6's "best-effort estimate"). The slide's attribution line then carries the status word.
3. **"This deck's interpretation", not "this deck's reading"** — the brief suggested the latter, but `CLAUDE.md` and slide 3 already say "interpretation", and slide 3's diagram label says it too. One phrase, three places.
4. **A percentage the source computed is part of the quotation.** Never re-derive or re-round it; put it inside the scope of the status word (see P10, and F7 for why this rule exists).

The legend goes on slide 17 (P18) so the discipline is legible to anyone who reads the deck without you.

---

## 2. Claim table

Every factual claim visible on a slide. "sources.md" column gives the ledger's status; the ledger's own slide numbers are stale (see F1), so rows are matched by content.

| # | Claim on the slide | Attribution today | sources.md | Should carry | Patch |
|---|---|---|---|---|---|
| 1 | Title, subtitle, loop diagram — no factual claim | — | — | none | — |
| 2 | 56.5% of 12,374 developers say outdated information blocks context | "Stack Overflow Developer Survey 2026" (no status) | verified; 6,989/12,374, question wording recorded | Measured | P1 |
| 3 | 43.2M PRs merged per month, +23% YoY | "Measured: GitHub Octoverse 2025" | verified | Measured | — |
| 3 | Nearly 1 billion commits pushed in 2025, +25.1% | same | verified ("pushed") | Measured | — |
| 3 | Autonomy ladder L1 Operator → L5 Observer | "Ladder: Feng et al., arXiv 2506.12469, illustrative" | verified for names/order; **L1–L5 numbering not checked** | citation + *illustrative* | F11 |
| 3 | gh-aw sits at L4 | "the L4 placement is this deck's interpretation" (trailing) | n/a, interpretation | This deck's interpretation (leading) | P2 |
| 4 | Earlier attempt — all TODO | TODO markers | — | none, leave the gaps | — |
| 5 | `on:`, `permissions`/`tools`/`network`, `safe-outputs`, Markdown body are the parts of a workflow file | **none** | verified, frontmatter reference | Documented | P3 |
| 5 | Teammate mapping | "this deck's model, not GitHub terminology" | n/a, interpretation | This deck's interpretation | P3 |
| 6 | Only a draft PR; `draft: true` is a policy the agent cannot override | catch-all "gh-aw docs (safe outputs…)" at the foot | verified, quoted in docs | Documented | P6 |
| 6 | Never merged automatically | "GitHub Blog guidance, not a hard limit" | verified; an experimental merge output exists | Reported by GitHub | P4 |
| 6 | Agent is read-only and fenced in | "next two slides show how" | verified | covered by 7 and 8 | — |
| 6 | 1,000 AI Credits (~$10) per run by default, model is yours to choose | **none** — the best-effort caveat is only in the notes | verified; AIC is "computed on a best-effort basis" | Documented + caveat | P5 |
| 6 | Does not replace build, test or release pipelines | "GitHub Blog" | verified | Reported by GitHub | P6 |
| 7 | Activation → Agent (read-only) → Detection (no write) → Safe outputs (scoped token) | "gh-aw architecture documentation" | verified | Documented | P7 |
| 7 | Detection scans every proposed output before anything is written | foot line only | verified, threat-detection page | Documented | P7 |
| 7 | A failed check defaults to a caution notice (`continue-on-error` true) | caveat, in place | verified | caveat — keep as is | — |
| 7 | Four of its six jobs shown | in the foot line | verified | Documented | P7 |
| 8 | Container, opt-in tools, Squid egress allowlist, API proxy, MCP gateway | "gh-aw architecture and network reference" | verified, except the API-proxy wording | Documented | P8, F4 |
| 8 | MCP gateway "not a strong security boundary" | "the documentation's own wording" | verified | Documented | P8 |
| 9 | The 13 frontmatter lines | "Frontmatter trimmed from `workflows/update-docs.md`…" | verified; trimmed items listed in the ledger | Documented + *trimmed* | P9 |
| 9 | Shift / access badge / outbox / tools annotations | **none** (inherit the foot line) | all verified | Documented | P9 |
| 10 | GitHub reports 57 of 59 PRs merged | title + "reported by GitHub, small sample" | verified | Reported by GitHub | P10 |
| 10 | A 96% merge rate for the Daily Documentation Updater | same | **96% is GitHub's own wording**, confirmed 17 Oct 2026 (F7) | Reported by GitHub, 96% inside its scope | P10 |
| 10 | Merged ≠ correct; small sample | caveats, in place | — | keep, add "repos not named" | P10 |
| 11 | 98 briefs, 98 docs pages, 6 shared modules | "File counts verified via the GitHub API, 17 Oct 2026" | **no ledger row** | Measured | P11, F6 |
| 11 | 0 have ever run; 4 of 98 compiled locally | "the repository's own `agents.md` — a self-report" | **no ledger row** | Self-reported | P11, F6 |
| 11 | No release tagged, sandbox repo does not exist | **unattributed** — the muted line covers only the compile result and the "not yet run" column | **no ledger row** | needs a method | F6 |
| 12 | `staged: true` runs it for real and writes nothing | **none** | verified, but the docs say "Staging is not a sandbox" | Documented + caveat | P13, F5 |
| 12 | GitHub reports 96% for its own docs workflow | "GitHub reports…: a number to test, not to assume" | verified | Reported by GitHub | P12 |
| 12 | Hypothesis, measure, decision rule | proposals, visibly framed as such | — | none | — |
| 13 | `.md` + generated `.lock.yml` go in the PR | **none** | verified ("commit **both** files") | Documented | P14 |
| 13 | Activation, Agent, Detection, Safe outputs — four of the six | **none** | verified | Documented | P14 |
| 13 | `gh aw logs <workflow>`, `gh aw audit <run-id>` | **none** | verified, CLI page | Documented | P14 |
| 13 | "Treat the workflow Markdown as code…" | "GitHub Blog" (no date) | verified, Blog 13 Feb 2026 | Reported by GitHub | P15 |
| 14 | Markdown card (frontmatter + one-line body) | "Body paraphrased; the real file's instructions are longer" | verified | Documented + *paraphrased* | P16 |
| 14 | `gh aw compile` → `.lock.yml` → Actions runs it | **none** | verified, CLI page | Documented | P16 |
| 14 | "Commit and review both files" (diagram caption) | **none** | "commit both" verified; **"review" is the deck's advice** | diagram owner | F10 |
| 15 | Four trigger routes: repo event, schedule, manual, comment | **none** | verified, triggers page | Documented | P17 |
| 15 | `gh aw trial` uses a temporary private repo (experimental) | "(experimental)" inline | verified | Documented | P17 |
| 15 | `staged: true` previews every output and writes nothing | **none** | verified, but "Staging is not a sandbox" | Documented + caveat | P17, F5 |
| 16 | Three URLs + changelog URL | the URLs themselves | verified, all resolve | none | F8 |
| 17 | Fact-check date, status, deliberate omissions | self-describing | verified | add the legend | P18 |

**Where the gaps are**: 12 on-slide claims carry no attribution at all today (slides 5, 6 cost, 9 annotations, 11 release/sandbox, 12 staged, 13 ×3, 14 compile, 15 ×3). Eight more cite a source with no status word. Slides 3 and 11 are the only two that already say what kind of evidence they are.

---

## 3. Patches

Each is `OLD` → `NEW`, one exact occurrence.

### P1 — slide 2, the survey figure

OLD
```
<span class="muted">Stack Overflow Developer Survey 2026</span>
```
NEW
```
<span class="muted">Measured: Stack Overflow Developer Survey 2026.</span>
```

### P2 — slide 3, lead with the interpretation (OPTIONAL, lowest priority)

The only change is moving "this deck's interpretation" to the front of its own clause so all three status words lead. Same length; renders as two muted lines either way. Skip it if you would rather not touch the slide that already works. **The OLD string contains a curly apostrophe in `deck’s`.**

OLD
```
Measured: GitHub Octoverse 2025. Ladder: Feng et al., arXiv 2506.12469, illustrative; the L4 placement is this deck’s interpretation.
```
NEW
```
Measured: GitHub Octoverse 2025. Ladder: Feng et al., arXiv 2506.12469, illustrative. This deck's interpretation: the L4 placement.
```

### P3 — slide 5, source the settings and label the mapping

The four settings in the diagram are a documented fact and currently carry no source. Renders on one line, inside the slide.

OLD
```
<span class="muted">The teammate mapping is this deck's model, not GitHub terminology.</span>
```
NEW
```
<span class="muted">Documented: the gh-aw frontmatter reference. This deck's interpretation: the teammate mapping, not GitHub terminology.</span>
```

### P4 — slide 6, "never merged automatically"

OLD
```
<span class="muted">Never merged automatically: GitHub Blog guidance, not a hard limit.</span>
```
NEW
```
<span class="muted">Reported by GitHub: "never merged automatically" is Blog guidance, not a hard limit.</span>
```

### P5 — slide 6, the cost caveat moves onto the slide

`~$10` is the only dollar figure in the deck and the docs call AIC best-effort. The caveat was in the notes only; `CLAUDE.md` says every number carries its caveat on the slide. Stays within two lines; the orange TODO is untouched.

OLD
```
by default, and you choose the model. <span class="todo">TODO: our own measured cost per run.</span>
```
NEW
```
by default, and you choose the model. <span class="muted">AI Credits are a best-effort estimate.</span> <span class="todo">TODO: our own measured cost per run.</span>
```

### P6 — slide 6, the foot line becomes two statuses

OLD
```
<span class="muted">gh-aw docs (safe outputs, cost management); GitHub Blog.</span>
```
NEW
```
<span class="muted">Documented: gh-aw safe-outputs and cost-management reference. Reported by GitHub: Blog, 13 Feb 2026.</span>
```

### P7 — slide 7, name the page the detection caveat comes from

OLD
```
<span class="muted">gh-aw architecture documentation; four of its six jobs shown.</span>
```
NEW
```
<span class="muted">Documented: gh-aw architecture and threat-detection reference; four of its six jobs shown.</span>
```

### P8 — slide 8

OLD
```
<span class="muted">gh-aw architecture and network reference. The MCP gateway caveat is the documentation's own wording.</span>
```
NEW
```
<span class="muted">Documented: gh-aw architecture and network reference; the MCP gateway caveat is the docs' own wording.</span>
```

### P9 — slide 9

OLD
```
<span class="muted">Frontmatter trimmed from `workflows/update-docs.md` in githubnext/agentics.</span>
```
NEW
```
<span class="muted">Documented: `workflows/update-docs.md` in githubnext/agentics, frontmatter trimmed.</span>
```

### P10 — slide 10, pulls the 96% inside the attribution and adds "repos not named"

`including the 96%` is deliberate: the blog computes the percentage itself (F7), so it is quoted, not derived. It also avoids stuttering against the body sentence. Renders as two muted lines, same as today.

OLD
```
<span class="muted">gh-aw blog, 13 Jan 2026; reported by GitHub, small sample. Merged is not the same as correct.</span>
```
NEW
```
<span class="muted">Reported by GitHub, including the 96%: gh-aw blog, 13 Jan 2026; small sample, repos not named. Merged is not the same as correct.</span>
```

I considered also changing the body to "…as GitHub reports it" (your suggested "96% as reported"), and rejected it: with the title already saying "GitHub reports that 57 of 59…" and the muted line saying "Reported by GitHub", the slide would attribute the same figure three times in three lines, and "as GitHub reports it. Reported by GitHub:" reads badly. One attribution, scoped to include the percentage, does the same work. Say so if you disagree and I will cut it the other way.

### P11 — slide 11, split the measured from the self-reported

Slightly **shorter** than the current line; still two muted lines.

OLD
```
<span class="muted">`DonalMoloney/Agentic-Workflows-Lib`, private. File counts verified via the GitHub API, 17 Oct 2026. The compile result and the "not yet run" column are the repository's own `agents.md` — a self-report, not a CI result.</span>
```
NEW
```
<span class="muted">Measured: file counts via the GitHub API, 17 Oct 2026, `DonalMoloney/Agentic-Workflows-Lib` (private). Self-reported: the compile result and the "not yet run" column come from that repo's own `agents.md`, not a CI result.</span>
```

### P12 — slide 12, the measure

OLD
```
<span class="muted">GitHub reports 96% for its own docs workflow: a number to test, not to assume.</span>
```
NEW
```
<span class="muted">Reported by GitHub: 96% for its own docs workflow, a number to test, not to assume.</span>
```

### P13 — slide 12, staged mode gets a source and the docs' own limit

See **F5**: "writes nothing" is stronger than the docs. This is the minimum honest fix; the alternative wording is in F5.

OLD
```
then draft pull requests only, every one reviewed.
```
NEW
```
then draft pull requests only, every one reviewed. <span class="muted">Documented: gh-aw staged mode; the docs warn it is not a sandbox.</span>
```

### P14 — slide 13, the three steps get a source (ADDS A LINE — rendered, fits)

OLD
```
3. **Dig in:** `gh aw logs <workflow>` across runs, `gh aw audit <run-id>` for one run.
```
NEW
```
3. **Dig in:** `gh aw logs <workflow>` across runs, `gh aw audit <run-id>` for one run.

<span class="muted">Documented: gh-aw architecture and CLI reference.</span>
```

### P15 — slide 13, date the quote

OLD
```
> <span class="muted">GitHub Blog</span>
```
NEW
```
> <span class="muted">Reported by GitHub: Blog, 13 Feb 2026</span>
```

### P16 — slide 14

**The OLD string contains a curly apostrophe in `file’s`.**

OLD
```
<span class="muted">Body paraphrased; the real file’s instructions are longer.</span>
```
NEW
```
<span class="muted">Documented: gh-aw CLI reference; the body is paraphrased, the real instructions are longer.</span>
```

### P17 — slide 15, the only slide with no source line at all (ADDS A LINE — rendered, fits)

OLD
```
- `staged: true` under `safe-outputs:` previews every output and writes nothing.
```
NEW
```
- `staged: true` under `safe-outputs:` previews every output and writes nothing.

<span class="muted">Documented: gh-aw triggers, trial and staged-mode reference.</span>
```

### P18 — slide 17, the legend (ADDS A BULLET — rendered, two lines, fits)

This is the slide that turns a habit into a visible method. It is the backup slide, so it costs nothing in the room and does all its work for anyone reading the deck later.

OLD
```
- Fact-checked 17 Oct 2026 against the gh-aw documentation
```
NEW
```
- How to read a source line: **Measured** (counted, method named) · **Reported by GitHub** · **Self-reported** (my repo) · **Documented** (gh-aw docs) · **This deck's interpretation**.
- Fact-checked 17 Oct 2026 against the gh-aw documentation
```

---

## 4. Needs your decision — not fixed here

**F1. `sources.md` slide numbers are stale.** The ledger says "15 slides, the status and sources slide is 15". The deck has 17 and a different order: ledger 6 → deck 9, ledger 7 → deck 14, ledger 8 → deck 15, ledger 9 → decks 7 and 8, ledger 10 → deck 6, ledger 11 → deck 13, ledger 12 → deck 10, ledger 13 → deck 12, ledger 14 → deck 16, ledger 15 → deck 17. Anyone checking a claim against the ledger today lands on the wrong slide. It is the deck's authority, so it should be renumbered — or, better, keyed by claim text rather than slide number, since the order has changed twice today alone.

**F2. "could not verify" — the 72.6% trustworthiness figure.** Correctly **not** on any slide; it sits in slide 2's note as a TODO. No on-slide action. Decision: it stays off until a URL exists. (Note is another agent's file.)

**F3. "conflicting" — the daily AI Credit cap.** Correctly off the slides and recorded on slide 17 exactly as `CLAUDE.md` requires. No action.

**F4. "changed" — the API proxy.** The ledger's mismatch 1 is **already fixed in the visible diagram** (slide 8's box now reads "Keeps the engine token out of the container"). Two leftovers: the image's `aria-label` in `deck.md` still says *"an API proxy holding the engine token"*, and the ledger row still reads "changed". Suggested alt text: *"an API proxy that keeps the engine's auth token out of the agent's container"*. Diagram owner's line to change; the ledger row is yours.

**F5. Staging is overclaimed on two slides.** Slide 12: "runs it for real and writes nothing". Slide 15: "previews every output and writes nothing". The docs say plainly *"Staging is not a sandbox"* — custom jobs, scripts, external MCP servers and custom credentials are **not** skipped. For a plain docs workflow the claim holds, but a security-minded listener who knows the page will catch it. P13 adds the docs' own caveat to slide 12. For slide 15, your choice:
- keep the bullet and let P17's source line carry it, or
- reword to `previews every safe output instead of writing it` (precise, same length).

**F6. Slide 11's six numbers have no ledger row at all.** The slide is the one place you speak about your own work, so it is the one the room will push on hardest, and it is the only slide with no entry in `sources.md`. Two things:
- Add rows for: 98 briefs, 98 docs pages, 6 shared modules (method: GitHub API, 17 Oct 2026), 4 of 98 compiled, 0 runs (method: the repo's `agents.md`).
- **"No release tagged, and the sandbox repo does not exist" is currently attributed to nothing** — the muted line covers only the compile result and the "not yet run" column. Was that checked through the API or read from `agents.md`? It needs one or the other before it can carry a status word.

**F7. RESOLVED — "96%" is GitHub's own figure.** Checked against the 13 Jan 2026 post on 17 Oct 2026. Its exact wording: *"57 merged PRs out of 59 proposed (96% merge rate)"*, alongside *"88 merged PRs out of 103 proposed (85% merge rate)"* and *"10 merged PRs out of 10 proposed (100% merge rate)"*. So the percentage is quoted, not derived — including the fact that 57/59 is 96.61% and GitHub prints 96%, where convention would give 97%. Two consequences:
- P10 scopes the attribution to cover it (`Reported by GitHub, including the 96%`). **Do not "correct" 96% to 97% on any slide** — that would replace a quotation with our own arithmetic and inherit an error we did not make.
- The same applies to the 85% and 100% figures if either reaches a slide or a note.

Two follow-ups that are not slide patches:
- **Ledger amendment** (`sources.md`, slide-12 row, whoever owns that file). Replace the caveat with: *"Blog wording: '57 merged PRs out of 59 proposed (96% merge rate)'. The percentage is GitHub's own, including its rounding of 96.61% to 96%. The page does not say which repositories the PRs were opened in; the workflow names link to definition files in githubnext/agentics and github/gh-aw, which are the workflow sources, not the PR repositories."* That last sentence independently confirms the ledger's own mismatch 4, so the row can move from "see mismatch 4" to settled.
- **Speaker note, slide 10** (notes owner): one line for the person in the room who divides 57 by 59 — "96% is GitHub's own wording; the exact figure is 96.6%."

**F8. Slide 16 hard-codes "slide 9's `update-docs.md`".** Correct right now. The order has already moved twice today; if it moves again this silently points at the wrong slide. Consider "the `update-docs.md` shown earlier".

**F9. If you reject P5**, the alternative is to drop `~$10` and say only "1,000 AI Credits by default". A dollar figure invites exactness the docs explicitly do not offer.

**F11. The ladder's L1–L5 numbering is unverified.** The ledger confirms the five names and their order from the abstract but records "L1 to L5 numbering not checked in the full text" — and the diagram labels every rung L1…L5 and the muted line says "L4". Either check the paper or soften the diagram labels to names only. Low risk, but it is the one number on slide 3 that is not Octoverse.

---

## 5. Spotted, not mine to change

- **Diagram, slide 8**: the `aria-label` lags the fixed diagram box (F4).
- **Diagram, slide 14**: the caption "Commit and review both files" — the quick start says commit both; *"and review"* is the deck's own advice, per the ledger. A small interpretation inside a caption.
- **Diagram, slide 3**: labels L1–L5 (F11).
- **Notes, slide 5**: the typical-jobs claim moved off the slide into the note and kept its "the grouping is mine" caveat there. Correct — flagging only so it is not lost on the next pass.
- **Notes, slide 10**: add the 96% / 96.6% line from F7.
