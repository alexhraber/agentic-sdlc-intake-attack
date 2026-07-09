# Intent

## Product Outcome
- Create a defensive incident-writeup repository for the agentic SDLC intake attack, documenting how fake GitHub accounts used issue comments and malicious ZIP artifacts to smuggle executable payloads into autonomous coding-agent workflows, with safe static-analysis notes, IOCs, detection guidance, and governance policy that prevents untrusted collaboration content from becoming agent action.

## What This Project Is
agentic-sdlc-intake-attack is a not classified yet project built using Python.
Create a defensive incident-writeup repository for the agentic SDLC intake attack, documenting how fake GitHub accounts used issue comments and malicious ZIP artifacts to smuggle executable payloads into autonomous coding-agent workflows, with safe static-analysis notes, IOCs, detection guidance, and governance policy that prevents untrusted collaboration content from becoming agent action.

Key operating facts:
- **Primary languages**: Python
- **Detected surfaces**: not detected yet

## Product View
```mermaid
flowchart LR
  U[Primary User] --> P[agentic-sdlc-intake-attack]
  P --> O[User-visible Outcome]
  P --> G[Proof Gates]
  G --> E[Evidence Artifacts]
```

## Inferred Baseline
- Repository: agentic-sdlc-intake-attack
- Product type: not classified yet
- Primary languages: Python
- Detected surfaces: not detected yet

## Scope
| Area | In Scope | Proof Surface |
|---|---|---|
| Core workflow | Define a concrete user-visible workflow | Acceptance criteria + tests |
| Data contracts | Document canonical inputs/outputs | [INTERFACES.md](./INTERFACES.md) and schema checks |
| Delivery quality | Block promotion on broken proof surfaces | [VALIDATION.md](./VALIDATION.md) blocking gates |

## Non-Goals (Falsifiable)
| Non-goal | How to falsify |
|---|---|
| Feature creep beyond the primary outcome | Any PR adds capability not tied to outcome criteria |
| Shipping without evidence | Missing validation artifacts for promoted changes |
| Ambiguous ownership boundaries | Missing owner/system-of-record in interfaces |

## Constraints
- Technical: runtime, dependency, and topology boundaries are explicit.
- Operational: deployment, rollback, and incident ownership are defined.
- Security/compliance: sensitive data handling and authz are mandatory.

## Acceptance Criteria (must be objectively testable)
- [ ] Done when the repository safely documents the agentic SDLC intake attack end-to-end, including evidence-bound static analysis, IOCs, threat model, detection guidance, artifact-handling rules, and governance policy proving that untrusted collaboration content cannot become autonomous agent execution.
- [ ] Non-functional targets are met (latency, reliability, cost, etc.).
- [ ] Validation gates pass and artifacts are attached.
- [ ] `pytest -q` passes for unit/integration scenarios
- [ ] `ruff check .` passes for lint quality
- [ ] `mypy .` passes for typed modules in production paths

## Epistemic Custody Fields

### Active Assumptions
- The attacker used fake or newly generated GitHub accounts to search for agentic SDLC repositories.
- The attacker specifically framed the ZIP as a repository fix to trick autonomous intake routines that read issue threads.

### Confidence & Risk Level
- **Confidence**: High. The hashes, certificate strings, Go runtime metadata, and API patching behavior have been statically verified.
- **Risk**: High. The vulnerability lies in the lack of an execution boundary in autonomous coding systems.

### Measured vs Inferred Facts
| Fact | Source (Provenance) | Type (Measured/Inferred) |
|---|---|---|
| ZIP contains a GUI PE Windows binary | Static archive list and magic bytes | Measured |
| Executable loads VirtualProtect and patches GetUserNameA | Imports table and string signatures | Measured |
| The target was autonomous agent runtimes | Aligned comments on agent-created issues | Inferred |

### Unresolved Contradictions
- None. Static metadata maps cleanly to the documented threat surface.

### Deferred Questions
- The exact C2 network configuration is unknown since no execution occurred.

### Stop Conditions
- Stop immediately if any build script, notebook, or test command attempts to run the target binary or load external packages.

### Proof Required Before Completion
- Passed `decapod validate` run and completed verification baseline.

## Tradeoffs Register
| Decision | Benefit | Cost | Review Trigger |
|---|---|---|---|
| Simplicity vs extensibility | Faster iteration | Potential rework | Feature set expands |
| Strict gates vs dev speed | Higher confidence | More upfront discipline | Lead time regressions |

## First Implementation Slice
- [ ] Define the smallest user-visible workflow to ship first.
- [ ] Define required data/contracts for that workflow.
- [ ] Define what is intentionally postponed until v2.

## Open Questions (with decision deadlines)
| Question | Owner | Deadline | Decision |
|---|---|---|---|
| Which interfaces are versioned at launch? | TBD | YYYY-MM-DD | |
| Which non-functional target is hardest to hit? | TBD | YYYY-MM-DD | |
