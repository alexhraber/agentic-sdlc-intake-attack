# Interfaces

## Contract Principles
- Keep command-line utilities focused, with zero interactive prompts.
- All scripts return standard exit codes: `0` for success, `1` for finding warnings/vulnerabilities, and `2` for syntax or parameter errors.
- External files are passed as absolute or relative filesystem arguments, with path resolution validation.

## API / CLI Contracts
| Interface / Script | Input Argument | Output Behavior | Errors | Idempotency |
|---|---|---|---|---|---|
| `check_archive_paths.py` | `<zipfile>` | Prints internal ZIP file names and compression details to stdout. Finds paths with traversal, nested archives, or executable extensions. | Exit `1`: Warning findings.<br>Exit `2`: Missing file or argument. | Idempotent |
| `list_archive.sh` | `<archive>` | Prints MIME type and ZIP entry headers without extraction. | Exit `1`: Missing command or error.<br>Exit `2`: Invalid argument count. | Idempotent |
| `hash_artifact.sh` | `<file> [file ...]` | Prints SHA-256 and MD5 hashes, alongside file magic identification. | Exit `1`: File not found.<br>Exit `2`: Missing arguments. | Idempotent |
| `static_strings.sh` | `<file> [min-length]` | Safely dumps ASCII/Unicode printable strings above min-length. | Exit `1`: command not found.<br>Exit `2`: Invalid arguments. | Idempotent |

## Fixture Schemas

### PE Features Schema (`fixtures/static-pe-features.public.json`)
```json
{
  "artifact": "string (filename)",
  "sha256": "string (sha256 hex)",
  "features": [
    {
      "feature": "string (type of feature)",
      "value": "string or array (observed value)",
      "flagged": "boolean (true if anomalous/hostile)",
      "reason": "string (security analyst context)"
    }
  ]
}
```

### Claims Classification Schema (`fixtures/claims-classification.public.json`)
```json
{
  "safety_rule": "string (guideline formula)",
  "claims": [
    {
      "claim": "string (asserted security claim)",
      "classification": "CONFIRMED | LIKELY | POSSIBLE | UNPROVEN",
      "basis": "string (evidence reference)"
    }
  ]
}
```

## Outbound Dependencies
No external network dependencies are allowed. The pipeline operates entirely offline. 
The static HTML renders rely only on standard Google Fonts link imports for typography, rendering locally with fallback system fonts if internet access is blocked in the environment.

## Consumed Surfaces
- Input: `/home/arx/Downloads/core_fix_v2.zip` (Attacker-provided artifact quarantined outside worktree).
- Outputs:
  - `docs/notebooks/index.html` (Landing Dashboard)
  - `docs/notebooks/*.html` (Sanitized static walkthroughs)\n