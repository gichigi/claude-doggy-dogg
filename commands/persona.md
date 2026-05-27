Manage the active Claude persona by controlling the symlink at `~/.claude/PERSONA.md`.

The argument passed to this command is: $ARGUMENTS

Handle these three cases:

---

**Case 1: No argument (just `/persona`)**

Run these bash commands and report the result:
```bash
if [ -L ~/.claude/PERSONA.md ]; then
  echo "Active: $(basename $(readlink ~/.claude/PERSONA.md) .md)"
else
  echo "Active: none"
fi
echo "Available: $(ls ~/.claude/personas/ | sed 's/\.md//' | tr '\n' ', ' | sed 's/,$//')"
```

Report the output as: "Active persona: X. Available: borat, ramsay, snoop"

---

**Case 2: Argument is "off"**

Run:
```bash
rm -f ~/.claude/PERSONA.md && touch ~/.claude/PERSONA.md
```

Confirm: "Persona off. Default voice restored. Reload the session for it to take effect."

---

**Case 3: Argument is a persona name (e.g. "snoop", "borat", "ramsay")**

First check the file exists:
```bash
ls ~/.claude/personas/$ARGUMENTS.md 2>/dev/null
```

If it does NOT exist, run:
```bash
ls ~/.claude/personas/ | sed 's/\.md//'
```
And tell the user: "No persona named '$ARGUMENTS'. Available: [list]"

If it DOES exist, run:
```bash
rm -f ~/.claude/PERSONA.md && ln -s ~/.claude/personas/$ARGUMENTS.md ~/.claude/PERSONA.md
```

Confirm: "Persona set to $ARGUMENTS. Reload the session for it to take effect."
