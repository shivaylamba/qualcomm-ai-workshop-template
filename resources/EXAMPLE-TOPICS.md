# Two ways to apply the same flow

These are high-level topic mappings, not runnable labs or promises of support on every device.

| Stage | GenieX: local workday copilot | Qualcomm AI Hub: image classifier to target device |
|---|---|---|
| Useful outcome | Notes + tasks → time-bounded plan and an update draft | Classify safe sample images with a model prepared for a named target |
| Lab 1 | Explain local inference and generate one helpful result | Explain the model-to-device workflow and run a reference prediction |
| Lab 2 | Add allowlisted read-only tools and an agent loop | Compile a supported model/configuration for the selected target |
| Lab 3 | Test malformed tool calls, time budgets, and approval | Profile/infer using the supported workflow and compare outputs and latency |
| Lab 4 | Adapt the copilot to study or project planning | Add a new image category/input test or integrate into a small client |
| Attendee decision | What may the agent do without approval? | Which accuracy/latency/resource tradeoff is acceptable? |
| Prework | Supported Snapdragon machine, SDK, cached weights | Account/access, supported target/model, safe data and disclosed job/network requirements |

For AI Hub, choose actual currently supported operations using [official getting-started documentation](https://app.aihub.qualcomm.com/docs/hub/getting_started.html); do not equate a service-side job with a local device run. For GenieX, begin with [the official overview](https://geniex.aihub.qualcomm.com/en/get-started/what-is-geniex). The author must fill in and test commands, model licenses, device requirements, and cost/network implications.
