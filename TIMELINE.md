# Timeline

Exact timestamps are unknown or intentionally omitted for public safety. This timeline records the generalized sequence and preserves evidence boundaries.

## Generalized Sequence

1. Agent created issues in a legitimate repository workflow.
2. Fake or newly generated GitHub accounts appeared.
3. Comments were posted with language aligned to the issue context.
4. ZIP artifacts were attached or linked as purported fixes.
5. The artifact was manually quarantined and statically inspected.
6. A binary payload was discovered inside the archive.
7. The execution path risk was identified: an autonomous agent could ingest the issue, treat the comment as task context, extract the archive, and execute or tool-ingest the payload.
8. The agentic intake policy gap was identified.
9. Recommended controls were drafted: quarantine, static-only handling, human approval, and source-diff-only contribution paths.

## Evidence Boundaries

Confirmed:

- A suspicious ZIP artifact was framed as a fix.
- The archive contained a Windows executable.
- Static metadata and hashes were recorded.

Likely:

- The attack intended to launder malicious artifacts through ordinary GitHub collaboration surfaces.
- Agentic automation was part of the target model because agent-created issues become future agent context.

Unknown:

- Exact creation time of the fake GitHub accounts.
- Exact comment timestamps for every related issue.
- Whether any agent or maintainer executed the binary.
- Whether the payload contacted network infrastructure.

Unproven:

- Actor identity.
- Campaign scale.
- Successful compromise.
- Network C2 for this specific artifact.
