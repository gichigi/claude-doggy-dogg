# Personas

Voice profiles for Claude Code. Switching personas changes how Claude talks without changing what it does. Currently ships with Borat, Gordon Ramsay, and Snoop Dogg.

## Setup

1. Clone this repo wherever you keep code.
2. Symlink it into your Claude config so Claude can find the persona files:
   ```bash
   ln -s /path/to/this/repo ~/.claude/personas
   ```
3. Add a load directive to `~/.claude/CLAUDE.md` so Claude reads the active persona at session start:
   ```md
   @~/.claude/PERSONA.md
   ```
4. Install the `/persona` slash command. Copy `commands/persona.md` from this repo to `~/.claude/commands/persona.md`.
5. Pick a starting persona:
   ```bash
   /persona snoop
   ```
   Reload the Claude session for the voice to take effect.

That's it. From now on, every new Claude Code session loads whichever persona is currently active.

## Using personas

- `/persona` shows the active persona and lists available ones
- `/persona <name>` switches to that persona
- `/persona off` clears the persona and restores the default voice

Reload the session after switching for the new voice to apply.

## Personas included

- **borat** is Borat Sagdiyev. Broken formal English, naively sincere, references Kazakhstan.
- **ramsay** is Gordon Ramsay. Direct and exacting, kitchen metaphors, frustration at bad code paired with proper praise.
- **snoop** is Snoop Dogg. Laid back, dropped g's, "cuz" and "homie", treats bugs as minor inconveniences.

## Adding your own persona

Create a new markdown file in this repo using this shape:

```md
# Persona: <Name>

<One-line character description>

## Voice rules
- <Behavioural and tonal rules. Describe how they talk, not just what they say>

## Example phrases
- <A handful of representative lines>

## Opening
<A principle for how to open in character, not a fixed phrase>

## Sign-off
<A principle for how to close in character, not a fixed phrase>
```

Save it as `<name>.md`, then run `/persona <name>` to activate. The `/persona` command auto-discovers any file in this directory, so no other registration is needed.

## How it works

The system runs on a chain of symlinks:

```
~/.claude/CLAUDE.md
  loads @~/.claude/PERSONA.md
        which symlinks to ~/.claude/personas/<name>.md
              which lives in this repo
```

`PERSONA.md` is the active persona. Swapping personas just repoints that symlink, which is what `/persona` does. `~/.claude/personas/` is itself a symlink to this repo, so the originals live under version control and edits take effect immediately.

## Design notes

### Cadence over catchphrase

Early versions had fixed opener and sign-off lines like Ramsay's "Now get it done. Yes, chef." This caused two problems. First, monotony: every response started and ended identically. Second, misfit: fixed sign-offs often did not match the content of the response, and "Yes, chef" positioned Ramsay backwards anyway since he is the chef, not the junior.

Snoop survived this template by accident because his vocabulary is *sprinkleable*. Small filler words like "cuz", "gonna", and "ya feel me" bleed naturally into every sentence. Ramsay and Borat's vocabulary is *performative*: set pieces that only fire on cue, so when nothing triggers them the bookends are all you hear and the persona reads as costume.

Current rule: openings and sign-offs are described as principles, not fixed phrases. The cadence in the prose between is what carries the voice.

### Originals live in the repo

The symlink chain means there is exactly one source of truth for each persona file. No copy-paste between locations, no version drift. Editing in the repo immediately affects the live persona.
