#!/usr/bin/env python3
"""Build the reviewed public forensic notebooks without executing cells."""

from __future__ import annotations

import json
from pathlib import Path

try:
    import nbformat
except ImportError as exc:
    raise SystemExit("nbformat is required. Run `uv sync` first.") from exc

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "notebooks"

SAFETY = (
    "> **Safety boundary:** This workbook performs static analysis of sanitized "
    "excerpts, fake fixtures, and derived public metadata. It does not execute "
    "attacker code, inspect the analyst's environment, or contact any network."
)


def md(text: str):
    return nbformat.v4.new_markdown_cell(text.strip())


def py(text: str):
    return nbformat.v4.new_code_cell(text.strip())


def notebook(title: str, cells: list):
    kernelspec = {"display_name": "Python 3", "language": "python", "name": "python3"}
    language_info = {"name": "python", "file_extension": ".py", "version": "3.12"}

    result = nbformat.v4.new_notebook()
    result.metadata = {
        "kernelspec": kernelspec,
        "language_info": language_info,
        "incident_publication": {
            "safe_static_analysis": True,
            "attacker_code_executed": False,
            "network_access_required": False,
            "raw_payload_published": False,
        },
    }
    result.cells = [
        md(f"# {title}\n\n{SAFETY}"),
        *cells,
    ]
    return result


def specs():
    return {
        "00-analysis-map-and-safety-boundary.ipynb": notebook(
            "Analysis Map and Safety Boundary",
            [
                md(
                    """
## Question and Method

This technical appendix reconstructs how a commenter-supplied ZIP archive crossed trust boundaries:

```text
GitHub Issue created by agent
  -> Attacker comments on the issue
  -> ZIP attachment supplied as fix
  -> Agent ingests issue context
  -> Agent extracts archive
  -> Executable payload discovered (core_fix_v2.exe)
  -> Target: Agent execution bridge / Human maintainer
```

The notebooks analyze this threat path without executing the code. Their governing rule is:

> **capability != observed execution != proven transmission**

Static features demonstrate code capability. Runtime audit logs establish execution.
Network trace telemetry is required to prove completed transmission.
"""
                ),
                md(
                    """
## Artifact and Publication Map

| Layer | Artifact | Public treatment | Reason |
|---|---|---|---|
| Issue Comment | issue details / commenter metadata | sanitized overview | ingress carrier |
| ZIP Archive | `core_fix_v2.zip` | file checksums & index | delivery wrapper |
| Executable Payload | `core_fix_v2.exe` | static PE characteristics | raw payload withheld |
| C2 / Network Path | public IOCs | logical path analysis | no live contact |
"""
                ),
                py(
                    """
layers = [
    {"step": 1, "boundary": "collaboration plane -> agent context", "question": "What is the ingress source?"},
    {"step": 2, "boundary": "context ingestion -> archive extraction", "question": "Does the agent unzip the file?"},
    {"step": 3, "boundary": "archive extraction -> file inspection", "question": "What files are discovered?"},
    {"step": 4, "boundary": "discovered files -> tool execution", "question": "Does the agent execute the PE binary?"},
]
layers
"""
                ),
            ],
        ),
        "01-artifact-metadata-and-checksums.ipynb": notebook(
            "Artifact Metadata and Checksums",
            [
                md(
                    """
## Inbound Archive Verification

To prevent execution, we perform static validation using checksums and metadata.
"""
                ),
                py(
                    """
import json
from pathlib import Path

# Load static metadata fixture
metadata = json.loads(Path("../fixtures/artifact-metadata.public.json").read_text())

print(f"Inspected Archive: {metadata['artifact']}")
print(f"Archive SHA-256:   {metadata['sha256']}")
print(f"Archive size:       {metadata['byte_size']} bytes")
"""
                ),
                py(
                    """
print("Archive Contents:")
for file in metadata["files"]:
    print(f" - File name: {file['name']}")
    print(f"   SHA-256:   {file['sha256']}")
    print(f"   MD5:       {file['md5']}")
    print(f"   Type:      {file['file_type']}")
    print(f"   Runtime:   {file['compiler_runtime']}")
"""
                ),
            ],
        ),
        "02-static-pe-feature-analysis.ipynb": notebook(
            "Static PE Feature Analysis",
            [
                md(
                    """
## Static Characteristics of Discovered Binary

Instead of executing the payload, we map features extracted from static inspection of imports, strings, headers, and certificates.
"""
                ),
                py(
                    """
import json
from pathlib import Path

# Load PE features fixture
pe_features = json.loads(Path("../fixtures/static-pe-features.public.json").read_text())

print(f"Binary Target: {pe_features['artifact']}")
print(f"SHA-256:       {pe_features['sha256']}")
"""
                ),
                py(
                    """
print("Extracted Features:")
for feat in pe_features["features"]:
    status = "⚠️ [FLAGGED]" if feat["flagged"] else "ℹ️ [INFO]"
    print(f"{status} {feat['feature'].upper()}: {feat['value']}")
    print(f"    Context: {feat['reason']}")
"""
                ),
            ],
        ),
        "03-evidence-boundary-and-claims.ipynb": notebook(
            "Evidence Boundary and Claims Classification",
            [
                md(
                    """
## Claims Verification Ledger

We classify incident claims based on the strength of available evidence.
"""
                ),
                py(
                    """
import json
from pathlib import Path

claims_data = json.loads(Path("../fixtures/claims-classification.public.json").read_text())
print(f"Governing Safety Rule: {claims_data['safety_rule']}\\n")

print("Claim Matrix:")
for c in claims_data["claims"]:
    print(f"Claim:          {c['claim']}")
    print(f"Classification: {c['classification']}")
    print(f"Basis:          {c['basis']}\\n")
"""
                ),
            ],
        ),
    }


def main():
    OUT.mkdir(exist_ok=True)
    for filename, nb in specs().items():
        nbformat.write(nb, OUT / filename)
    print(f"Wrote notebooks to {OUT}")


if __name__ == "__main__":
    main()
