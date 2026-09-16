# Setup — do this before the workshop

Takes about 20 minutes, mostly downloading. **Host: replace every placeholder with a tested command.**

## 1. Check your machine

| You need | How to check |
|---|---|
| {{DEVICE_AND_OS}} | `{{HARDWARE_CHECK}}` |
| {{SOFTWARE_AND_VERSION}} | `{{VERSION_CHECK}}` |
| {{ACCOUNT_OR_NETWORK}} | `{{ACCOUNT_CHECK}}` |
| {{DISK_AND_RAM}} | {{RESOURCE_NOTE}} |

## 2. Install

```bash
git clone {{REPO_URL}}
cd {{REPO_FOLDER}}
{{SETUP_COMMAND}}
```

## 3. Download the model / assets (this is the slow part)

```bash
{{ASSET_DOWNLOAD_COMMAND}}
```

Size: {{ASSET_SIZE}}. License/terms: {{LICENSE_NOTE}}.
{{NOTE_ANY_CLOUD_UPLOAD_OR_JOB_COST}}

## 4. Prove it works

```bash
{{READINESS_COMMAND}}
```

You should see:

```text
{{READINESS_EXPECTED_OUTPUT}}
```

**See that? You're ready.** → [Lab 1](labs/1-run.md)

**Don't see that?** Message {{HOST_CONTACT}} with the full error before the workshop. There's a backup machine/pairing plan.
