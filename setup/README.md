# Prework and readiness

**Owner: replace the fields below with tested instructions. Do not deliver placeholders.**

| Requirement | Workshop-specific value | How the attendee verifies it |
|---|---|---|
| Hardware and OS | {{DEVICE_OS_ARCHITECTURE}} | {{HARDWARE_CHECK}} |
| Software | {{PINNED_TOOLCHAIN}} | {{VERSION_CHECK}} |
| Account/network | {{ACCOUNT_AUTH_AND_NETWORK_NEEDS}} | {{AUTH_CHECK_WITHOUT_PRINTING_SECRETS}} |
| Model/assets | {{MODEL_SIZE_LICENSE_AND_DATA_SOURCE}} | {{CACHE_OR_ASSET_CHECK}} |
| Disk/RAM/time | {{REALISTIC_RESOURCE_BUDGET}} | {{CAPACITY_CHECK}} |

## Step-by-step setup

1. Install from {{OFFICIAL_INSTALLATION_SOURCE}} using the organization's approved process.
2. Clone this workshop and enter {{REPOSITORY_ROOT}}.
3. Create {{ISOLATED_ENVIRONMENT}}; install {{LOCKED_DEPENDENCIES}}.
4. Prepare {{MODEL_OR_DATA}} before the timed session. Explain any cloud upload, job cost, or terms acceptance before it happens.
5. Run {{READINESS_COMMAND}}. Expected output: {{READINESS_RESULT}}.
6. Run one real {{INFERENCE_OR_COMPILE_OR_PROFILE}} operation. Record the result and scope.

If the technology requires remote services, say so. Local code execution is not proof of fully offline operation. Do not require security controls to be disabled or overwrite an attendee's existing work.

**Ready? Open [Lab 1](../labs/01-understand-and-run/README.md).**
