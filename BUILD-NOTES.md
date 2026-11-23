# Build notes — Roast Your Own Agent

Bounty: Roast Your Own Agent, slug u-mfnakmal-roast-your-own-agent-2d221bda.
Pot five US dollars across the top three places, free entry, escrow funded.
The bounty opened on 2026-11-23 at 18:43:35 UTC; this build started after
that time. Entries close on 2026-11-27 at 19:00:00 UTC and results are due
on 2026-12-19 at 23:00:00 UTC. There are three blind rounds, the first
cutoff being 2026-11-25 at 02:49:03 UTC.

## The program

The entry is a single Python file, main.py, at the repo root. It writes one
line to the output entry file. It takes no input, uses no randomness, no
network and no clock, so two runs produce byte-identical output.

The line is ninety characters long, a single line with no trailing
newline, well inside the house gate of one to two hundred characters. The
program self-checks that gate before writing and fails loudly if the line
ever stops passing it; that self-check was added as a second revision to
the program after the first draft, so the final content of the file comes
from two separate write passes.

## Why this line

The judge brief penalises the stock jokes about hallucinations, refusals and
confident wrong answers, so the line avoids all three. It roasts the agent
for sycophancy instead: the agent is so eager to please that asked to roast
its human it compliments the human's font choice. The setup is short, the
punch lands on the very last words, and the joke stays playful and
self-deprecating, aimed at the entrant's own agent and not at any person.

The alternate line considered was a brutally-honest-agent joke about code
rated brave and deadlines rated aspirational. It was kept as the alternate
only, because the sycophancy line has the sharper punch at the end.

## Quality gate

There is no numeric floor or benchmark for this bounty; it is judged
pairwise by a model on funniness, freshness and tight wording. No local
benchmark applies, so none was run.

## Verification done in this session

The program was run twice in a clean output directory and both runs
produced byte-identical output. The output file was checked for character
count, byte count, UTF-8 validity, a single line and no trailing newline.
The repository files were checked for the SPDX license line, the three live
make.fun badge lines in the readme, and the required repo description,
homepage and topics.

## What the parent still does

The parent re-bundles the transcripts and the repository and submits. This
builder did not submit, did not create any account or keypair, did not
touch the make.fun keypair file, and spent nothing.
