# Safe Publication Checklist

Before publishing incident material, verify:

- [ ] No malware binaries committed.
- [ ] No live secrets.
- [ ] No raw environment dumps.
- [ ] No private GitHub tokens.
- [ ] No doxxing of fake profiles beyond necessary public handles if included.
- [ ] No instructions that improve attacker operations.
- [ ] No executable reproduction exploit.
- [ ] No attribution beyond evidence.
- [ ] All claims labeled confirmed, likely, possible, or unproven.
- [ ] All fixtures are inert and clearly labeled.
- [ ] Hashes are provided with context.
- [ ] Network indicators are omitted unless actually known.
- [ ] Screenshots are redacted.
- [ ] Scripts refuse to execute files.
- [ ] Artifact-retention notes point outside the public repo.

This repository should remain useful for defenders without becoming an artifact distribution channel or operational guide for attackers.
