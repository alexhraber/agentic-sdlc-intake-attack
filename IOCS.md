# Indicators of Compromise

These indicators are provided for defensive detection and incident-response correlation. They are evidence-bound to the inspected artifact described here. Network indicators are not known from this artifact unless separately discovered. No C2 URLs are asserted.

## File Indicators

| Type | Indicator | Context | Confidence |
|---|---|---|---|
| Archive filename | `core_fix_v2.zip` | ZIP attachment framed as a repository fix or useful artifact | Confirmed |
| Payload filename | `core_fix_v2.exe` | Windows executable inside the archive | Confirmed |
| Archive SHA-256 | `647248d2c272c9c2cf11d1be039910728beca88c1359b4a42c932d4e29cf6380` | Hash of inspected archive | Confirmed |
| EXE SHA-256 | `d85d164e46fabb085609f2586e8fec364539a6ec81f74659f0cb28ac76e7880b` | Hash of contained executable | Confirmed |
| EXE MD5 | `4db8e85743a1ae8b1d26a3bccbffb6d1` | Legacy hash for correlation only | Confirmed |

## Static Characteristics

| Type | Indicator | Context | Confidence |
|---|---|---|---|
| File type | Windows x64 PE executable | Not a source diff, patch, or normal repo fix | Confirmed |
| Runtime string | Go 1.25.4 | Go runtime indicator visible statically | Confirmed |
| Subsystem | Windows GUI | Unusual for a source-code fix artifact | Confirmed |
| Module path | `YHWntfKsr` | Random-looking visible module path | Confirmed |
| Decoy strings | Russian calendar/AVL-tree demo text | Visible text unrelated to claimed repository fix | Confirmed |
| Certificate subject | `CN=computrabajo.com` | Suspicious/self-signed-looking certificate with random-looking organization/location fields | Confirmed static observation |
| API behavior | `advapi32.dll!GetUserNameA` and `kernel32.dll!VirtualProtect` | Dynamic loading and memory-protection behavior observed statically | Confirmed static observation |
| Hooking behavior | patching `GetUserNameA` with a jump stub | Behavior inferred from static inspection, not execution | Confirmed static observation |
| Replacement string | `5a3f1c7f6f2f7421` | Hard-coded string found during static inspection | Confirmed |

## Contextual Indicators

- New or newly generated GitHub account comments on an agent-created issue.
- Comment is closely aligned with issue language but supplies an archive instead of a source diff.
- Artifact name uses fix-oriented terms such as `core_fix`, `patch`, `hotfix`, `validator`, `test_helper`, or `reproduction`.
- Archive contains executable content unrelated to the repository language or contribution path.

## Non-Indicators

- No network indicators are published here.
- No C2 URL is known from the static evidence described in this repository.
- No actor attribution is asserted.
