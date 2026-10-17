# GitHub Agentic Workflows — Presentation Spine

**Story in one line:** We ship faster than our docs can keep up. AI agents can now do the work, not just suggest it. GitHub Agentic Workflows let them keep repos up to date automatically. Here's how, and here's what I'm asking for.

## Style — GitHub dark theme (Primer colours)
| Use | Colour | Hex |
|---|---|---|
| Background | Canvas dark | `#0d1117` |
| Panels / cards | Canvas subtle | `#161b22` |
| Borders | Border | `#30363d` |
| Main text | Foreground | `#e6edf3` |
| Secondary text | Muted | `#7d8590` |
| Accent / links / headings | Blue | `#2f81f7` |
| Agent / AI highlights | Purple | `#a371f7` |
| Success / "it works" | Green | `#3fb950` |
| Code font | Monospace | `SFMono-Regular, Consolas, monospace` |

## Title slide
- **Title:** GitHub Agentic Workflows
- **Subtitle:** From AI that suggests to AI that does
- **Shows:** dark `#0d1117` background, title in `#e6edf3`, subtitle in `#7d8590`, a thin blue-to-purple (`#2f81f7` → `#a371f7`) accent line, a small terminal-style snippet in monospace, e.g. `gh aw run update-docs`
- **Footer:** my name · date

## Part 1 — The problem

### Slide 1 — We ship faster, so our docs go stale faster
- **Shows:** graph with two lines pulling apart: delivery speed going up, docs freshness going down
- **Also shows:** agent autonomy levels beside the graph, L1 Operator to L5 Observer (Feng et al., arXiv 2506.12469), with L4 Approver highlighted as where gh-aw sits: the agent proposes a pull request, a human approves
- **Note:** the L4 placement is my interpretation, not GitHub's claim; the paper's abstract names the levels but does not define them

### Slide 2 — AI has moved from suggesting work to doing it
- **Shows:** table comparing traditional AI (assists) with agentic AI (executes)

### Slide 3 — I tried to fix this before, but it left a gap
- **Shows:** my earlier project, what it solved, and the gap [TODO: name the gap]
- **Note:** an earlier, crude AI-tool attempt; details to add once I find it

## Part 2 — The solution

### Slide 4 — GitHub Agentic Workflows: describe a task in plain English, and an AI agent does it in your repo
- **Shows:** what they are, in one sentence and one picture

### Slide 5 — Demo: watch it work
- **Shows:** a live run, ideally one that updates docs
- **Note:** a couple of demos, live or as screenshots

### Slide 6 — How it works: write a markdown file, and GitHub runs it as a workflow with safety limits
- **Shows:** diagram: repo event → agent runs → result (PR, issue, comment)

### Slide 7 — Why it matters: routine work like docs, triage and reports gets done without anyone doing it
- **Shows:** the value, with one number if possible

## Part 3 — Getting started

### Slide 8 — You can start today with workflows I've already built
- **Shows:** my repo collection, and which one to try first

### Slide 9 — What can go wrong, and how it's controlled
- **Shows:** safety limits, cost, and where it isn't a good fit

### Slide 10 — My ask: adopt GitHub Agentic Workflows
- **Shows:** the decision I need from you
