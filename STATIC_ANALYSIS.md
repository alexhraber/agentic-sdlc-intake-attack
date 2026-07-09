# Static Analysis Methodology

This workflow is static-only. Do not execute attacker-provided files. Do not run binaries. Do not install unknown packages. Do not fetch live payloads.

## Safe Workflow

1. Copy the artifact into quarantine.
2. Compute hashes before inspection.
3. Inspect archive listing without extraction when possible.
4. Check for path traversal.
5. Check compression ratio.
6. Extract only into a disposable quarantine directory if necessary and approved.
7. Identify magic bytes and file type.
8. Run strings safely.
9. Inspect PE headers statically.
10. Look for imports, suspicious APIs, certificates, packed or obfuscated indicators.
11. Never execute.
12. Never upload to third-party sandboxes unless authorized.
13. Document evidence boundaries.

## Example Safe Commands

Hashing:

```bash
sha256sum quarantine/core_fix_v2.zip
md5sum quarantine/core_fix_v2.exe
```

Archive listing without extraction:

```bash
unzip -l quarantine/core_fix_v2.zip
zipinfo quarantine/core_fix_v2.zip
7z l quarantine/core_fix_v2.zip
```

File type and magic inspection:

```bash
file quarantine/core_fix_v2.zip
file quarantine/core_fix_v2.exe
```

String extraction:

```bash
strings -a quarantine/core_fix_v2.exe
strings -a -n 8 quarantine/core_fix_v2.exe
```

PE metadata:

```bash
objdump -x quarantine/core_fix_v2.exe
rabin2 -I quarantine/core_fix_v2.exe
rabin2 -i quarantine/core_fix_v2.exe
osslsigncode verify quarantine/core_fix_v2.exe
```

## Archive Safety Checks

Before extracting any archive, inspect entries for:

- absolute paths;
- `..` traversal;
- Windows drive paths;
- UNC paths;
- symlinks;
- nested archives;
- executable extensions;
- hidden files;
- startup/task/config paths.

Prefer listing and metadata inspection over extraction. If extraction is required, use a disposable quarantine directory outside the repository worktree and do not execute or import the extracted files.

## Evidence Boundary Language

Use precise labels:

- **Confirmed by static evidence:** observed in archive listing, hashes, strings, headers, imports, or certificate metadata.
- **Likely:** supported by context and static evidence but not directly proven.
- **Possible:** plausible risk path requiring additional evidence.
- **Unproven:** not established by available evidence.

## Core Fix v2.exe Analysis Findings

- File type: PE32+ Windows GUI executable (x86‑64), 2.8 MiB.
- PE Header: architecture i386:x86‑64, entry point `0x0000000140073280`, image base `0x0000000140000000`.
- Sections observed: `.text`, `.rdata`, `.data`, `.pdata`, `.xdata`, `.idata`, `.reloc`, `.symtab`.
- Imports from `kernel32.dll` include: WriteFile, WriteConsoleW, WerSetFlags, WerGetFlags, WaitForMultipleObjects, WaitForSingleObject, VirtualQuery, VirtualFree, VirtualAlloc, TlsAlloc, SwitchToThread, SuspendThread, SetWaitableTimer, SetProcessPriorityBoost, SetEvent, SetErrorMode, SetConsoleCtrlHandler, RtlVirtualUnwind, RtlLookupFunctionEntry.
- Strings show Go build ID and decoy text, no obvious malicious payload.
- YARA: no rules configured.
- ClamAV: no detections.

