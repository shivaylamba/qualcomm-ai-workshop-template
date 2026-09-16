# Build your own workshop

You're not designing a curriculum. You're answering five questions and cutting one hole in a working app. Budget a day, not a week.

Do it in this order — most people write the pages first and end up rewriting them.

## 1. Answer the five blanks (30 minutes, on paper)

Don't open the repo yet.

1. **They build:** one sentence, something a person outside your team would recognise as useful. Not "explore the SDK."
2. **Lab 1 — Run it:** what's the first real result, and what's the moment that shows the technology doing its job? (GenieX unplugs the network. What's yours?)
3. **Lab 2 — Build it:** the one thing they implement themselves. See below — this is the whole workshop.
4. **Lab 3 — Make it yours:** the three options you'll offer when they point it at their own use case.
5. **Their decision:** the judgement call they make that has no single right answer. This is what they'll still be thinking about next week.

If you can't fill these in on paper, the workshop isn't ready — no amount of editing the repo will fix it.

## 2. Build the finished app first

Write `solution/` before anything else. Keep it small enough that *you* could build it in 30 minutes from scratch. If it takes you two hours, it's too big for the room — cut a feature.

Then get it running on the actual target device, not just your laptop.

## 3. Cut one hole in it — that's Lab 2

Copy `solution/` to `starter/`, delete one function, and leave a TODO with a one-line contract:

```python
def read_notes(path) -> str:
    """TODO(lab 2): the agent can't see your files yet. Make it able to."""
```

**A good Lab 2 hole:**
- takes you ~5 minutes to fill; takes them ~30 (that ratio is about right)
- has one obviously correct shape but several valid implementations
- fails loudly and legibly when it's wrong
- doesn't need anything they haven't seen in Lab 1

**A bad one:** config fiddling, a one-line API call, anything where the hard part is guessing a parameter name, or anything that needs three files changed at once.

This single decision determines whether your workshop works. Spend real time on it.

## 4. Write the check command

One command that tells them they're done — `pytest tests/test_lab2.py`, a script, whatever. It must pass only for a real implementation, not for a hardcoded return value. Attendees will find the shortcut; that's fine, just don't leave it lying open.

## 5. Now fill in the pages, in this order

| Order | File | Watch for |
|---|---|---|
| 1 | [workshop.json](workshop.json) | Your five answers in one place |
| 2 | [setup.md](setup.md) | Run every command on a **clean** machine. Your laptop lies to you. |
| 3 | [labs/2-build.md](labs/2-build.md) | Write this before labs 1 and 3 — they exist to serve it |
| 4 | [labs/1-run.md](labs/1-run.md) | Cut anything that isn't needed for Lab 2 |
| 5 | [labs/3-make-it-yours.md](labs/3-make-it-yours.md) | Three concrete options, not "be creative" |
| 6 | [START-HERE.md](START-HERE.md) | Their only link. Read it as someone who knows nothing. |
| 7 | [HOST.md](HOST.md) | Your fallback plan, your contact, your timings |

Don't touch the six blocks in a lab, the 90-minute shape, or the "Done when" line. Those are the template. Everything else is yours.

## 6. Check it

```bash
python scripts/check_template.py            # pages, links, lab structure
python scripts/check_template.py --release  # fails while any blank is unfilled
```

This checks the paperwork, not your code. It cannot tell you whether your commands work.

## 7. Dry run, then pilot

**Dry run (you, clean machine, stopwatch):** do the setup from scratch and time it. Then do all three labs as an attendee, typing everything. If Lab 2 takes you more than 10 minutes, it's too big for their 30.

**Pilot (one person who's never seen it):** hand them only the START-HERE link and say nothing. Watch where they hesitate. Every hesitation is a page you need to fix — don't explain it to them, write it down.

Fix navigation before you add more explanation. Almost every confusing workshop is a navigation problem wearing an explanation costume.

## 8. Three days before

- Send the setup link and your contact. Ask people to reply "ready" once the readiness command passes.
- Mirror large assets somewhere the venue wifi can survive.
- Prepare the fallback: a spare machine, a pairing plan, or a recorded run.
- Chase anyone who hasn't replied. Unprepared attendees are the number one way this goes wrong.

## The mistakes to avoid

- **Teaching coverage instead of one build.** Docs cover. Workshops build.
- **A Lab 2 that's too big.** Nobody finishes, everyone feels bad, you end up pasting the answer.
- **Setup inside the clock.** It eats the build time and it's always the slowest person who sets the pace.
- **Demoing the solution before Lab 2.** They'll wait for you to show the answer instead of trying.
- **No fallback.** Something always breaks. Decide now what you'll do.
