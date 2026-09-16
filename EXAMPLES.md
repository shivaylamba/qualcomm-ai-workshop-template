# The same structure, two topics

The five blanks below are the *only* things that change between workshops. Everything else — the 90-minute shape, the six blocks in every lab, the host notes — stays exactly as it is.

| The blank | GenieX | Qualcomm AI Hub |
|---|---|---|
| **They build** | A local copilot that turns messy notes into a time-boxed plan | An image classifier running on a real target device |
| **Lab 1 — Run it** | Send one prompt, see it answer with no network | Run a reference prediction on a supported model |
| **Lab 2 — Build it** | Add one tool the agent can call | Compile a model for the chosen target |
| **Lab 3 — Make it yours** | Point it at your own notes | Add your own image category, compare latency |
| **Their decision** | What may the agent do without asking me? | Which accuracy/latency tradeoff is acceptable? |

---

## Worked example: GenieX, 90 minutes

**They build:** a copilot that reads their notes and drafts tomorrow's plan — running on their own machine.

### Lab 1 — Run it (15 min)

*Watch first (5 min):* host sends one prompt, shows the answer, then pulls the network cable — it still works. That's the whole point of the technology, made physical.

*Your turn (10 min):* run it, change the prompt, run it again.

*Done when:* two different prompts gave two different answers, and you can point at the line that called GenieX.

*Go further:* find the evidence in the code that this ran locally. Don't take our word for it.

### Lab 2 — Build it (35 min) ← the heart

*Watch first (5 min):* host opens `starter/tools.py`, reads the TODO aloud:

> `read_notes(path) -> str` — the agent can't see your files yet. Make it able to.

Host shows what passing looks like, then **stops** and does not write the answer.

*Your turn (30 min):* implement the tool, register it with the agent loop, run the check, then ask the copilot something that forces it to use your tool.

*Done when:* the check passes **and** you can explain your own code to the person next to you.

*Stuck?* (1) print what the agent actually passed in — is it the shape you assumed? (2) look at the tool-registration example. (3) compare with `solution/`, then close it and type your own.

### Lab 3 — Make it yours (25 min)

*Pick one:* your own notes folder · a different output format (calendar blocks? a standup message?) · one more tool of your choosing.

*The real lesson:* you now decide what this thing is allowed to do without asking you. Write that rule down before you build it.

*Done when:* someone else ran your version and got a result — or you can explain exactly why it didn't.

### Their 60-second demo

> Here's what it does → here's the line I changed → here's what still doesn't work.

---

## Before you deliver a GenieX version of this

Start from [the official GenieX docs](https://geniex.aihub.qualcomm.com/en/get-started/what-is-geniex) and confirm the current API, supported hardware, and model licensing yourself. The file names and function above are illustrative — the workshop author writes and tests the real ones. For AI Hub, see [getting started](https://app.aihub.qualcomm.com/docs/hub/getting_started.html), and be clear with attendees about which steps are a cloud job and which run on the device.
