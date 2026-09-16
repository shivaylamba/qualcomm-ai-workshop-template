# Host notes

Everything you need to run this. Attendees only see [START-HERE.md](START-HERE.md).

## Run of show (90 min)

| Time | What | You're doing |
|---|---|---|
| 0:00 | Welcome | Show the finished app working. Ask: "where would you use this?" Take 2 answers. Send the START-HERE link. |
| 0:05 | Lab 1 demo | Run it once. Point at input → {{QUALCOMM_TECHNOLOGY}} call → output. 5 min, no tangents. |
| 0:10 | **Lab 1, they build** | Stop talking. Walk the room. |
| 0:20 | Lab 2 demo | Open the TODO, read the contract aloud, show what passing looks like. **Do not code the answer.** |
| 0:25 | **Lab 2, they build** | 30 min. Announce the halfway swap at 0:40. At 0:50 say "10 minutes left, get something running." |
| 0:55 | **Lab 3, they build** | Circulate. Ask "what did you pick?" Nudge people whose idea is too big. |
| 1:20 | Show and tell | 3 volunteers × 60 sec. Line them up during Lab 3 so nobody freezes. |
| 1:30 | Close | One next step each. Share the solution repo link now, not before. |

**60-minute version:** drop Lab 3, close at Lab 2 demos.

## Four questions that do all the work

- Opening: *"Where would you use this?"* — you want a real problem, not product vocabulary.
- Lab 1: *"Which part of this runs on your device?"* — checks they know what the technology actually does.
- Lab 2: *"What will this do before you run it?"* — forces a prediction, catches confusion early.
- Close: *"Show one result and one thing that's still broken."* — evidence, not claims.

## When someone is stuck

Wait 5 minutes before helping — struggle is the lesson. Then: point at the contract → name the API they need → only then show `solution/`, and ask them to explain it back.

Never paste the answer into the room chat. It ends Lab 2 for everyone.

## When things go wrong

| Problem | Do this |
|---|---|
| Setup broken for one person | Pair them with a neighbour immediately. Don't debug it live. |
| Setup broken for many | Switch everyone to the prepared fallback: {{FALLBACK_PLAN}} |
| Running 10+ min behind | Cut Lab 3 to 10 minutes. Never cut Lab 2 or the demos. |
| Nobody volunteers to demo | Ask a specific person you saw something interesting from during Lab 3. |
| Someone finished early | Send them to "Go further", or make them a floating helper. |

## Prep the week before

- [ ] Every blank filled with a real, tested command — run `python scripts/check_template.py --release`
- [ ] `starter/` and `solution/` actually exist and both run on the target device
- [ ] You did the setup yourself on a clean machine and timed it
- [ ] Assets pre-downloaded and mirrored somewhere the room's wifi can survive
- [ ] Fallback ready: spare machine, recorded run, or a pairing plan
- [ ] Setup instructions sent to attendees 3 days ahead, with your contact
- [ ] One person who's never seen it followed START-HERE.md end to end
- [ ] No secrets, private data, or unlicensed weights in the repo

Note honestly what you tested and on what device. A passing link check is not a tested workshop.
