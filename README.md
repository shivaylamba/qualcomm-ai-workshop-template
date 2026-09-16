# Qualcomm AI Workshop Template

A 90-minute hands-on workshop where attendees **build one small working thing** with a Qualcomm AI technology (GenieX, Qualcomm AI Hub, or similar). Most of the time is theirs to type code, not watch slides.

Fork it, fill in the blanks marked `{{LIKE_THIS}}`, run it.

## The whole template is 6 pages

| Page | Who reads it | What it is |
|---|---|---|
| [START-HERE.md](START-HERE.md) | Attendee | The only link you send them |
| [setup.md](setup.md) | Attendee, before the event | Install + one readiness command |
| [labs/1-run.md](labs/1-run.md) | Attendee | Get one real result running |
| [labs/2-build.md](labs/2-build.md) | Attendee | Build the feature themselves |
| [labs/3-make-it-yours.md](labs/3-make-it-yours.md) | Attendee | Change it for their own use case |
| [HOST.md](HOST.md) | You | Run of show, what to say, what to do when things break |

Plus [workshop.json](workshop.json) (your topic in one place), [EXAMPLES.md](EXAMPLES.md) (two filled-in topic ideas), and `starter/` + `solution/` for code.

## How the 90 minutes are spent

```text
 5 min  Welcome — show the finished thing
15 min  Lab 1  Run it            (5 host demo + 10 attendees)
35 min  Lab 2  Build it          (5 host demo + 30 attendees)  ← the heart
25 min  Lab 3  Make it yours     (25 attendees, host circulates)
10 min  Show and tell — 3 volunteers, 60 seconds each
```

**~70 of the 90 minutes are attendees typing.** Setup happens before the event, not inside the clock.
Short on time? Drop Lab 3 and you have a 60-minute workshop.

## Every lab looks the same

**You'll build** → **Watch first** (host demos live) → **Your turn** (they build) → **Done when** (one checkable result) → **Go further** → **Stuck?** (three hints).

Attendees never have to guess what to do next or whether they finished.

## Make it yours

Read **[BUILD-YOUR-OWN.md](BUILD-YOUR-OWN.md)** — the whole process, in the order you actually do it. The short version:

1. Answer five questions on paper: what they build, the first result, the one thing they implement, how they personalize it, the judgement call they make.
2. Write the finished app in `solution/`. Cut one function out of it into `starter/` — that hole is Lab 2.
3. Fill in the pages and replace every `{{PLACEHOLDER}}`, then run `python scripts/check_template.py --release`.
4. Do a timed dry run on a clean machine, then hand the START-HERE link to one person who has never seen it and say nothing.

Don't change the six blocks in a lab, the 90-minute shape, or the "Done when" line — that's the part every workshop shares. Everything else is yours.

The checker validates pages and links only — it does not run any SDK. Test your own commands on the real device before you deliver.
