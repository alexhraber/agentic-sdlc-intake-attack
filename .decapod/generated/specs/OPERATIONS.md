# Operations

## Operational Readiness Checklist
- [x] Containment guidelines and safe publication policies linked in the root repository.
- [x] Static build verification scripts integrated into the pipeline.
- [x] Rendered notebook output directory configured for static server hosting (e.g. GitHub Pages).
- [x] Decapod validation hooks active on pre-commit and pre-promotion gates.

## Deployment Model
The repository is deployed as a static web site to GitHub Pages:
- Renders are compiled within the container workspace.
- Changes are pushed to `origin:main`.
- Deployment pipelines rebuild and serve `docs/notebooks/index.html` as the entry dashboard.

## Service Level Objectives
| SLI | SLO Target | Measurement Window | Owner |
|---|---|---|---|
| Dashboard Availability | 99.9% (served via CDN/Pages) | 30d | Platform Security Team |
| P95 Page Load | < 300ms (highly optimized CSS/HTML) | 7d | Platform Security Team |
| Build Pipeline Success | > 99% (zero-flake static compiler) | 30d | DevSecOps |

## Monitoring
Since the output is static HTML/CSS, monitoring relies on the hosting platform's performance and availability signals:
- **Build Alerts**: Notifications are sent via email or Slack if the GitHub Action build container encounters an compilation or validation failure.
- **Access Logs**: Standard web server logs tracking client fetches of HTML pages and CSS assets.

## Incident Response (Post-Incident Guide)
1. **Detection**: Identify anomalous issue comments containing ZIP attachments or external download links.
2. **Quarantine**: Copy the ZIP file path to a remote, network-isolated workspace.
3. **Verify Integrity**: Compute SHA-256 signatures of the ZIP archive and PE executable.
4. **Draft Post-Mortem**: Document findings in the `TIMELINE.md` and update `IOCS.md` with the new signatures.
5. **Publish**: Re-run the compile pipeline to update the rendered hub and push to main.

## Secrets Management
This project contains no runtime API secrets or database credentials:
- **Signing Keys**: Developer commits are signed locally using GPG/SSH keys stored on secure hardware tokens.
- **Access Tokens**: GitHub push tokens are handled securely via `gh` CLI helper integration.\n