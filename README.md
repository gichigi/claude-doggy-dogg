# Personas

Voice profiles for Claude Code. Switching personas changes how Claude talks without changing what it does.

## How it works

Three symlinks form the chain that lets Claude pick up a persona at session start:

```
~/.claude/CLAUDE.md
  └── @~/.claude/PERSONA.md          (loaded by reference)
        └── symlink → ~/.claude/personas/<name>.md
              └── symlink → /Users/tahi/Local Documents/Coding/personas/<name>.md
```

- `CLAUDE.md` loads `PERSONA.md` via the `@` import directive.
- `PERSONA.md` is a symlink to the active persona file. Swapping personas = re-pointing this symlink.
- `~/.claude/personas/` is itself a symlink to this repo, so the originals live here under version control.

Symlinks resolve transitively, so the chain works the same as if the files lived in `~/.claude/` directly.

## Switching personas

Run `/persona <name>` in Claude Code. The skill at `~/.claude/skills/persona/SKILL.md` repoints `PERSONA.md` to the chosen file. Reload the session for the new voice to take effect.

- `/persona` — show the active persona and list available ones
- `/persona <name>` — switch to that persona
- `/persona off` — clear the persona (empty `PERSONA.md`, default voice)

## Voices

- **borat** — Borat Sagdiyev. Broken formal English, naively sincere, references Kazakhstan.
- **ramsay** — Gordon Ramsay. Direct, exacting, kitchen metaphors, frustration at bad code paired with proper praise.
- **snoop** — Snoop Dogg. Laid back, dropped g's, "cuz"/"homie", treats bugs as minor inconveniences.

## Persona file format

Each persona is a small markdown file with this shape:

```md
# Persona: <Name>

<One-line character description>

## Voice rules
- <Behavioural/tonal rules — how they talk, not just what they say>

## Example phrases
- <Phrasebook of representative lines>

## Opening
<Principle for how to open, not a fixed phrase>

## Sign-off
<Principle for how to close, not a fixed phrase>
```

## Design decisions

### Cadence over catchphrase

Early versions had fixed opener and sign-off lines (e.g. Ramsay's "Now get it done. Yes, chef."). This caused two problems:

1. **Monotony.** Every response started and ended identically.
2. **Misfit.** Fixed sign-offs often didn't match the content of the response. "Yes, chef" also positioned Ramsay backwards — he's the chef, not the junior.

Snoop survived this template because his vocabulary is *sprinkleable* — small filler words ("cuz", "gonna", "ya feel me") that bleed naturally into every sentence. Ramsay and Borat's vocab is *performative* — set pieces that only fire on cue, so when nothing triggers them the bookends are all you hear and the persona reads as costume.

**Current rule:** Openings and sign-offs are described as principles, not fixed phrases. The model varies them in-character each time. The cadence in the prose between is what carries the voice.

### Originals live in the repo, not under `~/.claude/`

The symlink chain means there's exactly one source of truth for each persona file. No copy-paste between locations, no version drift. Editing in this repo immediately affects the live persona.

### No em dashes

Per global instructions in `~/.claude/CLAUDE.md`. Voice rules in each persona should reinforce this where the character would naturally trend toward them.
