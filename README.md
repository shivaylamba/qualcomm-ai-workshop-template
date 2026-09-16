# Qualcomm AI Topic

**A reusable, technology-neutral workshop template for a 60–120 minute hands-on session.** Replace the topic with GenieX, Qualcomm AI Hub, or another Qualcomm AI technology and give attendees one useful thing to build.

This is an authoring scaffold, not an implemented SDK tutorial. `{{PLACEHOLDERS}}` must be replaced before delivery. No Qualcomm hardware, account, or model is required to browse this template. It is community-authored, not an official certification course.

## Start in the right place

| You are… | Open first | You will find… |
|---|---|---|
| An attendee | [START-HERE.md](START-HERE.md) | Prerequisites, first lab, next steps, checkpoints |
| A workshop lead | [Instructor notes](instructor/README.md) | Run of show, prompts, hints, recovery, assessment |
| A teammate creating a workshop | [AUTHORING.md](AUTHORING.md) | Clone/customize/pilot/publish checklist |
| Presenting this pattern today | [10-minute repository tour](PRESENTATION.md) | A timed click-through, not another slide deck |

## The experience

```text
Before the event: prepare and verify
          ↓
Lab 1: understand the technology + get one result
          ↓
Lab 2: build a useful capability
          ↓
Lab 3: make a decision, test a failure, improve it
          ↓
Lab 4 (optional): personalize and show what you built
          ↓
Leave with working code, evidence, and a clear next step
```

One project grows across the labs. Every lab uses **goal → brief concept → predict → do → check → reflect → next**. Attendees change something meaningful, not merely replay commands.

| Phase | 60 min / 3 labs | 90 min / 4 labs | 120 min / 4 labs |
|---|---:|---:|---:|
| Welcome and outcome | 5 | 5 | 10 |
| [Lab 1: first result](labs/01-understand-and-run/README.md) | 10 | 15 | 20 |
| [Lab 2: build](labs/02-build/README.md) | 20 | 25 | 35 |
| Break | 0 | 0 | 5 |
| [Lab 3: test and improve](labs/03-test-and-improve/README.md) | 15 | 20 | 25 |
| [Lab 4: personalize](labs/04-personalize/README.md) | Omit | 15 | 15 |
| Show and reflect | 10 | 10 | 10 |
| **Total** | **60** | **90** | **120** |

Installation and large downloads are prework, not hidden in these totals. See [two example topic mappings](resources/EXAMPLE-TOPICS.md) and [the teaching references](resources/TEACHING-PATTERN.md).

## Reuse it

Click **Use this template** on GitHub, or clone it. Fill in [workshop.json](workshop.json), author the labs, and add real code/data under [starter](starter/README.md) and [solution](solution/README.md). Keep the attendee path and instructor path separate.

```text
python scripts/check_template.py
python scripts/check_template.py --release
```

The first command checks scaffold structure, links, and timing. The release command additionally refuses unresolved placeholders. It is expected to fail on an uncustomized template; it does not execute or certify your technology implementation.
