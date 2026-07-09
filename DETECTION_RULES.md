# Detection Rules

These are practical triage signals for maintainers, security engineers, and agentic SDLC platform builders.

## High-Signal Patterns

- New account + first interaction + attachment.
- ZIP attached to issue comment.
- Archive contains binary instead of patch/source.
- Comment claims to fix issue but provides no diff.
- Executable disguised as core fix, patch, hotfix, test helper, validator, reproduction, or logs.
- Agent-created issue receives unusually aligned response from unknown account.
- Comment asks maintainer or agent to run file locally.
- Archive contains `.exe`, `.dll`, `.scr`, `.ps1`, `.bat`, `.cmd`, `.js`, `.vbs`, `.jar`, `.sh`, ELF, Mach-O, or PE payload.
- Archive contains nested archives.
- Archive paths attempt traversal.
- Archive contains symlinks.
- Archive contains hidden files or startup/task files.
- Payload signed with suspicious, mismatched, expired, or self-signed certificate.
- Binary contains obfuscated symbols or suspicious API imports.
- Suggested command requires `curl | bash`, `npm install`, `pip install`, `cargo run`, `chmod +x`, or direct execution.

## Agentic Workflow Signals

- The issue was created by an autonomous agent or automation account.
- The comment mirrors the exact agent-generated issue language.
- The comment supplies an artifact rather than a PR.
- The comment implies urgency or asks the agent to "test this fix".
- The suggested workflow would cause an agent to fetch, unzip, import, build, or execute outside the trusted repository path.

## Safe GitHub Search Queries

These queries are intended for defensive triage. Tune organization and repository filters before use.

```text
org:YOUR_ORG is:issue is:open "fix.zip"
org:YOUR_ORG is:issue is:open "core_fix"
org:YOUR_ORG is:issue is:open "attached" "zip"
org:YOUR_ORG is:issue is:open "run this" "zip"
org:YOUR_ORG is:issue is:open "validator" ".exe"
org:YOUR_ORG is:issue is:open "hotfix" ".zip"
org:YOUR_ORG is:pr "download" "zip"
org:YOUR_ORG "chmod +x" "issue comment"
```

## Safe Triage Queries

Use the GitHub CLI to enumerate potentially relevant issue comments without downloading attachments:

```bash
gh issue list --repo OWNER/REPO --state all --search "zip in:comments"
gh issue list --repo OWNER/REPO --state all --search "\"fix.zip\" in:comments"
gh issue list --repo OWNER/REPO --state all --search "\"core_fix\" in:comments"
gh pr list --repo OWNER/REPO --state all --search "\"download\" \"zip\" in:comments"
```

Review comment text and provenance first. Do not fetch or open artifacts during broad search.

## Archive Triage Signals

Flag an archive when:

- it contains absolute paths;
- it contains `..` path components;
- it contains paths beginning with `/`, `\`, drive letters, or UNC paths;
- it contains symlinks;
- it contains hidden directories such as `.github`, `.vscode`, `.config`, or startup/task locations;
- it contains file extensions that can execute;
- compressed size is tiny but uncompressed size is unexpectedly large;
- archive names or internal names differ from the claimed fix.

## Binary Triage Signals

Flag a binary when static inspection shows:

- `VirtualProtect`, `VirtualAlloc`, `WriteProcessMemory`, `CreateRemoteThread`, `LoadLibrary`, `GetProcAddress`, `GetUserNameA/W`, `Crypt*`, `WinHttp*`, or `Internet*` imports;
- Additional observed imports in core_fix_v2.exe: `WriteFile`, `WriteConsoleW`, `VirtualQuery`, `VirtualFree`, `SuspendThread`, `SetWaitableTimer`, `SetProcessPriorityBoost`, `SetEvent`, `SetErrorMode`, `SetConsoleCtrlHandler`, `RtlVirtualUnwind`, `RtlLookupFunctionEntry`.
- packed or high-entropy sections;
- mismatched or suspicious signing metadata;
- randomized module paths or symbols;
- embedded decoy text unrelated to the issue;
- hard-coded identifiers, tokens, hostnames, or URLs.

## Response Rule

When these signals appear, reject the artifact path and request a normal source diff through a trusted contribution route. If execution occurred, treat the host as potentially compromised.
