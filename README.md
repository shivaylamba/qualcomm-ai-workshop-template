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

## Use it for your topic

Copy this repo. Don't redesign anything — fill in the blanks.

1. **Pick your topic** and write one sentence: what attendees build in 90 minutes.
2. **Add the code.** Finished app in `solution/`, same app with one function removed in `starter/`. That missing function is Lab 2.
3. **Replace every `{{PLACEHOLDER}}`** in the 6 pages with real, tested commands.
4. **Check it:** `python scripts/check_template.py --release` — it fails until every blank is filled.

The 90-minute shape, the six blocks in every lab, and the "Done when" line stay exactly as they are. That's what makes every workshop feel the same.

See [EXAMPLES.md](EXAMPLES.md) for the same template filled in for GenieX and AI Hub.

The checker validates pages and links only — it does not run any SDK. Test your own commands on the real device before you deliver.
