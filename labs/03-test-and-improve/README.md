# Test and improve

Time: 15 / 20 / 25 minutes in the 60 / 90 / 120-minute formats.

> Template: the workshop author must replace the {{PLACEHOLDERS}} before attendees use this lab.

## Goal

Find a failure and improve one measurable property.

## Before you begin

Complete [setup](../../setup/README.md) and the preceding lab, if any. Keep your [worksheet](../../WORKSHEET.md) open.

## Learn

{{SHORT_EXPLANATION_OF_THE_CONCEPT_WITH_ONE_AUTHORITATIVE_SOURCE}}

## Predict

Choose a likely failure: missing input, misleading output, unsupported hardware, latency, or an unsafe action.

## Do

1. Run {{BASELINE_TEST_COMMAND}} and save the observed result.
2. Add one edge case to {{TEST_CASE_FILE}}; predict its result.
3. Run {{EDGE_CASE_COMMAND}}. Distinguish a platform error from an application failure.
4. Improve {{EDITABLE_COMPONENT}} without changing several variables at once.
5. Repeat the same comparison and record both results.
6. Explain what the test does not prove.

## Checkpoint

Submit before/after evidence for the same input plus one remaining limitation. A safe refusal can be the correct result.

## Hints

Check inputs and logs first. Then isolate one component. Use {{KNOWN_RECOVERY_COMMAND}} only after identifying the failure.

## Reflect

Did you improve quality, safety, latency, or usability? What was the tradeoff?

## Next

Continue to [the next step](../../labs/04-personalize/README.md). Lab 4 is optional; if skipping it, complete your [final demo](../../WORKSHEET.md).

