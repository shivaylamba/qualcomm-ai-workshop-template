# What to say — 10 minutes

Four tabs open: **README** · **labs/2-build.md** · **EXAMPLES.md** · **HOST.md**

Talk for 6 minutes. Leave 4 for them. The one line you repeat three times:
**"The structure never changes. Only the topic changes."**

---

## 1. The problem (30 sec — say it before you share your screen)

> "Most workshops are an hour of slides and fifteen minutes of copy-paste. People leave without having built anything.
> So before we picked any topic, we fixed the ratio."

## 2. The ratio → **README**, the time block (1 min)

> "90 minutes. 70 of them are attendees typing.
> Five-minute demo from the host, then we get out of the way. Lab 2 alone is 35 minutes of their hands on the keyboard.
> Setup happens before the event — it never eats the clock."

## 3. The shape → **labs/2-build.md** (1.5 min)

> "Every lab, in every workshop, has the same six blocks:
> what you'll build → watch → your turn → **done when** → go further → stuck."

Point at **Done when**:

> "Every lab ends with one checkable thing. Nobody sits there quietly wondering whether they finished."

## 4. The proof it's reusable → **EXAMPLES.md**, the table (1.5 min)

> "These five rows are the entire difference between a GenieX workshop and an AI Hub workshop.
> Same 90 minutes. Same six blocks. Same host notes.
> You don't design a workshop — you pick a topic and fill in five things."

## 5. GenieX, made real → scroll down (1.5 min)

> "Lab 1 — they run it, and the host unplugs the network. It still answers. That teaches on-device inference better than any slide.
> Lab 2 — one function is missing: the agent can't read your files yet. Make it able to. Thirty minutes, and the host does not write the answer.
> Lab 3 — they point it at their own notes, and they decide what the agent may do without asking them.
> That last one is what they're still thinking about next week."

Say this honestly:

> "The file names in that example are illustrative — whoever owns the GenieX workshop writes and tests the real ones."

## 6. You're not on your own → **HOST.md** (30 sec)

> "Minute-by-minute run of show, four questions that carry the room, and a table for when setup breaks — because it will."

---

## Then hand it over (4 min)

Ask these, not "thoughts?" — name a person if it goes quiet:

- "Is 35 minutes too long or too short for Lab 2?"
- "For your topic, what's the one function you'd take out for Lab 2?"
- "Where does setup break for your technology?"
- "Anything here you'd refuse to use as-is?"

## Close — get two things from each person

**Your topic. Your Lab 2 function.** Write them down on the call.

---

### If they ask

**"Is 90 minutes enough to teach GenieX?"**
> "We're not teaching GenieX. We're getting one working thing onto their laptop and showing them where to look next. Coverage is what docs are for."

**"What if setup breaks on the day?"**
> "Setup is prework with a readiness command, and HOST.md has the fallback table. One person broken — pair them. Many broken — switch to the prepared fallback. We never debug installs live."

**"How do we stop someone shipping a half-filled template?"**
> "There's a checker. It refuses to pass until every blank is a real, tested command." *(Run `python scripts/check_template.py --release` only if they want to see it.)*
