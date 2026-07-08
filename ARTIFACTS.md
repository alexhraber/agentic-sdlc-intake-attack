# Artifact Handling Policy

This is a defensive incident-response repository, not a malware-sample distribution repository.

## Do Not Publish

- raw malware
- executable payloads
- password-protected malware archives
- live secrets
- raw environment dumps
- private tokens
- full command histories
- host triage captures that expose local paths or credentials

## Publishable Evidence

Use derived, non-executable, publication-safe material:

- hashes
- filenames
- file sizes
- static metadata
- redacted strings
- screenshots with sensitive content removed
- inert fixtures
- analyst notes
- evidence-bound behavioral summaries

## Private Retention

If an artifact must be retained privately:

- keep it encrypted;
- keep it access-controlled;
- store it outside this repository;
- label it as hostile;
- avoid filenames that can be accidentally executed;
- prevent indexing by agents, editors, search tools, and previewers;
- document who can access it and why.

## Agent Handling Rule

Do not let agents auto-open, auto-extract, auto-preview, auto-import, auto-build, or auto-execute suspicious artifacts. Agents may record provenance, compute hashes, list archive entries, inspect magic bytes, and extract strings when the operation is static and does not execute the artifact.

## Fixture Rule

Fixtures in this repository must be fake, inert, and clearly labeled. Do not replace fixtures with captured payloads.
