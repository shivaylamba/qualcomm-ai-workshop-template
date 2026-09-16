# The script — read this out loud

Four tabs open before you start: **README** · **labs/2-build.md** · **EXAMPLES.md** · **HOST.md**
Six minutes of talking. Four minutes of them. `[Square brackets are stage directions — don't read those.]`

---

`[Don't share your screen yet. Just talk.]`

Before I show you anything, I want to say what problem this is solving.

Most technical workshops go the same way. The host talks for an hour. Then there's fifteen minutes at the end where everyone copy-pastes commands from a slide, half of them hit an error, and time runs out. People walk out having watched someone else build something.

So before we picked a single topic — before GenieX, before AI Hub, before anything — we fixed the ratio. That's what I want to show you. It takes about six minutes, and then I want your feedback, because you're the ones who'll be running these.

`[Share screen. README, scroll to the time block.]`

Here's the shape of every workshop we run.

Ninety minutes. Seventy of those minutes are attendees typing.

Five minutes of welcome. Then three labs. In each lab the host demos for about five minutes, and then shuts up and lets people build. Lab 2 alone — that's thirty-five minutes of their hands on the keyboard. And at the end, ten minutes where three people show what they made.

One thing that matters more than it looks: setup is not in this ninety minutes. Installing, downloading models, logging in — that all happens before the event, with a readiness command people run at home. Setup is what kills workshops. The slowest laptop in the room sets the pace for everyone. So we take it out of the clock entirely.

`[Switch to labs/2-build.md.]`

This is a lab. Every lab, in every workshop we ever run, looks exactly like this.

Six blocks. What you'll build. Watch first — that's the host demo. Your turn — that's them. Done when. Go further, if they finish early. And stuck, which gives them three hints in order, so they try things before asking a human.

`[Point at "Done when".]`

This one is my favourite and it's the smallest thing on the page.

Every lab ends with one checkable statement. "Done when the check passes and you can explain your own code to the person next to you." Nobody in that room ever has to sit there quietly wondering if they've finished or if they've fallen behind. They just look at the line. That single sentence removes most of the anxiety in a hands-on session.

`[Switch to EXAMPLES.md. Stay on the table at the top.]`

Now — the actual point of today.

We are not going to design a new workshop every time. This structure is fixed. What changes is the topic.

These five rows are the entire difference between a GenieX workshop and an AI Hub workshop. What they build. What Lab 1 runs. What they implement in Lab 2. How they personalise it in Lab 3. And the judgement call they have to make.

Same ninety minutes. Same six blocks. Same host notes. You pick a topic and fill in five things.

`[Scroll down to the GenieX section.]`

Let me make that real with GenieX, because it's easier to see than to describe.

What they build: a copilot that reads their notes and drafts tomorrow's plan, running on their own machine.

Lab 1, fifteen minutes. They send one prompt and get an answer. Then the host unplugs the network — and it still answers. That one moment teaches on-device inference better than any slide I could write. Then they go change the prompt and run it themselves.

Lab 2, thirty-five minutes. This is the heart of it. We ship them the app with one function deleted. The comment says: the agent can't see your files yet, make it able to. That's it. They implement it, they run the check, and then they ask the copilot something that forces it to use the thing they just built. And — this matters — the host does not write that function on screen. If you demo the answer, everybody waits for you instead of trying.

Lab 3, twenty-five minutes. They point it at their own notes. Their own output format. Maybe one more tool. And somewhere in there they have to decide what this agent is allowed to do without asking them first. That's the question they'll still be thinking about next week. That's the part they tell other people about.

Then three volunteers demo for sixty seconds: here's what it does, here's the line I changed, here's what still doesn't work. And we explicitly say a broken thing you understand beats a working thing you copied.

One honest note — the file and function names in that GenieX example are illustrative. Whoever owns that workshop writes and tests the real ones against the current SDK. I didn't want to pretend otherwise.

`[Switch to HOST.md. Ten seconds. Just scroll it.]`

And nobody's on their own when they run one of these. There's a host page — minute-by-minute run of show, the four questions that carry a room, and a table for what to do when setup breaks. Because it will break, for somebody, every single time.

`[Stop sharing or leave it on HOST.md.]`

That's it. That's the whole thing — six pages, and you fill in the blanks.

Now I'd rather hear from you than keep talking.

---

## The feedback round — 4 minutes

`[Ask these one at a time. If it's quiet, name a person: "<name>, you've run these before — what do you think?"]`

1. **"Is thirty-five minutes too long or too short for Lab 2?"** — That's the riskiest number in the whole thing, and I'd rather get it wrong now than in a room.
2. **"For your topic — what's the one function you'd take out for Lab 2?"** — This is the best question. It makes people try the template on their own material, live.
3. **"Where does setup break for your technology?"** — Surfaces the real delivery risk.
4. **"Is there anything here you'd refuse to use as-is?"** — Gives people permission to disagree. They won't otherwise.

## Closing ask — don't skip this

> "Two things from each of you before we drop off: your topic, and the one function attendees will write in Lab 2. Not a title — the function. If you've got a date you could pilot it, even better."

`[Write them down on the call. A list of topic names is not an outcome.]`

---

## If they ask

**"Is ninety minutes really enough to teach GenieX?"**
> "We're not teaching GenieX. We're getting one working thing onto their laptop and showing them where to look next. Coverage is what documentation is for — a workshop is for building."

**"What if setup breaks on the day?"**
> "It's prework, with a readiness command people run at home, and I chase anyone who hasn't confirmed. On the day: one person broken, pair them with a neighbour. Several broken, we switch to the prepared fallback. We never debug installs live — that's how you lose the room."

**"How do we stop someone shipping a half-finished template?"**
> "There's a checker. It refuses to pass while any blank is still a placeholder." `[Only run it if they ask to see it.]`

**"What if attendees are at really different skill levels?"**
> "Pairs, and the 'go further' block. Fast people get extra work or become floating helpers. Slow people still hit 'done when', because the bar is one function, not the whole app."
