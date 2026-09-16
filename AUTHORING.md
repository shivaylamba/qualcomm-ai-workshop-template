# Make a workshop from this template

## 1. Choose the promise, not a product tour

Write one sentence: “In {{DURATION}}, participants will build {{USEFUL_THING}} with {{QUALCOMM_TECHNOLOGY}}.” Pick a problem someone understands without event-specific background. State three observable outcomes: explain, build, evaluate.

Use the [topic mappings](resources/EXAMPLE-TOPICS.md) as ideas, not preverified implementations. Select 60 minutes/3 labs or 90–120 minutes/4 labs. Preserve time for learner work and reflection.

## 2. Use the GitHub template

Create a repository with **Use this template**, or clone and point its remote at your own repository. Keep the root title as “Qualcomm AI Topic” while presenting this generic pattern; replace it with the actual topic for a delivered course.

Fill `workshop.json`. Update README, attendee start, setup, lab pages, and instructor notes. Search all files for `{{` to find unresolved fields. Never make attendees hunt through an authoring guide for their first command.

## 3. Author one progressive build

- Lab 1: first real output plus the minimum architecture needed to explain it.
- Lab 2: a small implementation task with an intentionally incomplete starter and a useful resulting capability.
- Lab 3: a prediction, failure case, controlled change, and evidence-based decision.
- Optional Lab 4: a learner-selected extension using the same scaffold.

Each lab must name its input, editable file, exact command, expected observation, checkpoint, two hints, and next page. Include a reference answer separately. Give at least one test that prevents hardcoded fixture answers.

## 4. Complete the resource folders

Put learner code in `starter/`, completed code in `solution/`, safe sample data in `data/`, and real tests in `tests/`. The README files in those folders are instructions to you, not implementations. Add a dependency lock, model provenance, and source links where relevant. Do not package credentials, unlicensed weights, private datasets, or unreviewed binaries.

## 5. Verify and rehearse

Run the structure checker, then the release placeholder check. Separately execute your actual setup and labs on the intended device. Record command, version, device, observation, failures, and untested boundaries in `VERIFICATION.md`. A link checker cannot establish runtime correctness.

Ask a teammate unfamiliar with the project to follow only `START-HERE.md`. Time their run; fix navigation before adding more explanation. Pilot the exercise, not just the reference demo.

## 6. Publish

Complete [the release checklist](instructor/RELEASE-CHECKLIST.md). Confirm the chosen agenda sums to its advertised duration. Set the attendee entry link in the event invitation. Keep instructor answers out of the first-page attendee flow.
