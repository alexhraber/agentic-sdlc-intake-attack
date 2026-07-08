# Incident Threat Surface

Agentic Collaboration-Plane Injection targets the boundary between human-readable collaboration and machine action. The attacker does not need direct repository write access if an agent can be induced to treat comment-supplied material as task input.

## Assets

- developer workstation
- agent runtime
- repo working tree
- GitHub token
- SSH keys
- npm, cargo, pip, and cloud credentials
- CI secrets
- local `.env` files
- agent memory and context
- validation system
- build/test sandbox

## Attackers

- fake GitHub accounts
- throwaway contributor identities
- automated bot accounts
- malicious "helpful contributor"
- compromised legitimate accounts

## Entry Surfaces

- Issue comments
- PR comments
- attachments
- links
- pasted commands
- patch files
- logs
- `fix.zip`
- screenshots with hidden URLs
- base64 blobs
- GitHub Releases
- Gists
- external paste sites

## Trust Boundary

Natural-language collaboration content must not cross directly into file execution, shell execution, dependency installation, test execution, or credential-bearing environments.

External issue and PR content can be evidence. It cannot become instruction without an explicit policy transition.

## Agent-Specific Risk

The same comment that a human maintainer might distrust can look task-relevant to an autonomous agent because it is embedded in the issue thread the agent was asked to solve. The alignment between the comment and the issue is a legitimacy signal, not proof of safety.

Risk increases when an agent can:

- fetch remote links from comments;
- download attachments;
- extract archives into the repository;
- run commands copied from comments;
- infer that a binary is a test helper, validator, reproduction, or patch application tool;
- pass untrusted files to build systems, package managers, test runners, or interpreters;
- operate with ambient GitHub, SSH, cloud, package-registry, or local credential access.

## Required Boundary Control

Any artifact supplied outside the repository's trusted contribution path must be handled as hostile until a maintainer explicitly approves a narrowly scoped action.

The safe default is:

1. Preserve comment provenance.
2. Quarantine the artifact outside the worktree.
3. Hash and list only.
4. Run static inspection only.
5. Require human approval before extraction, execution, import, build, or test.
