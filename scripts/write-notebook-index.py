#!/usr/bin/env python3
"""Write the static notebook learning hub used by GitHub Pages."""

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "docs/notebooks/index.html"

NOTEBOOKS = [
    (
        "00-analysis-map-and-safety-boundary.html",
        "Analysis Map and Safety Boundary",
        "Maps the complete incident architecture, public/private evidence boundary, and claim-confidence model.",
    ),
    (
        "01-artifact-metadata-and-checksums.html",
        "Artifact Metadata and Checksums",
        "Validates and displays the ZIP archive and PE hashes and basic file properties.",
    ),
    (
        "02-static-pe-feature-analysis.html",
        "Static PE Feature Analysis",
        "Displays the static features (Go runtime version, certificates CN, dynamically loaded dlls, memory protections).",
    ),
    (
        "03-evidence-boundary-and-claims.html",
        "Evidence Boundary and Claims Classification",
        "Maps the claims using the capability != observed execution != proven transmission rule.",
    ),
]


def main() -> int:
    missing = [
        filename
        for filename, _, _ in NOTEBOOKS
        if not (ROOT / "docs/notebooks" / filename).exists()
    ]
    if missing:
        raise SystemExit(f"Missing rendered notebooks: {', '.join(missing)}")

    items = "\n".join(
        (
            f'<li><a href="{filename}">{title}</a>'
            f"<p>{description}</p></li>"
        )
        for filename, title, description in NOTEBOOKS
    )
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    
    # We will construct a beautifully styled premium dark-mode dashboard
    notebook_cards = ""
    for index, (filename, title, description) in enumerate(NOTEBOOKS):
        # Assign icons or step numbers
        notebook_cards += f"""
        <a href="{filename}" class="card">
          <div class="card-step">0{index}</div>
          <div class="card-content">
            <h3>{title}</h3>
            <p>{description}</p>
          </div>
          <div class="card-action">
            <span>Inspect</span>
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M12 5l7 7-7 7"/></svg>
          </div>
        </a>
        """

    OUTPUT.write_text(
        f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Forensic Analysis Notebooks - Incident Hub</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600;800&family=JetBrains+Mono:wght@400;700&display=swap" rel="stylesheet">
  <style>
    :root {{
      --bg-color: #080b11;
      --card-bg: rgba(17, 24, 39, 0.6);
      --border-color: rgba(255, 255, 255, 0.08);
      --text-main: #f3f4f6;
      --text-muted: #9ca3af;
      --primary-cyan: #06b6d4;
      --primary-blue: #3b82f6;
      --accent-glow: rgba(6, 182, 212, 0.15);
    }}

    * {{
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }}

    body {{
      background-color: var(--bg-color);
      color: var(--text-main);
      font-family: 'Outfit', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
      min-height: 100vh;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      padding: 2rem 1rem;
      background-image: 
        radial-gradient(circle at 10% 20%, rgba(59, 130, 246, 0.05) 0%, transparent 40%),
        radial-gradient(circle at 90% 80%, rgba(6, 182, 212, 0.05) 0%, transparent 40%);
    }}

    .container {{
      max-width: 900px;
      width: 100%;
    }}

    header {{
      text-align: center;
      margin-bottom: 3rem;
    }}

    .badge {{
      display: inline-flex;
      align-items: center;
      gap: 0.5rem;
      background: rgba(6, 182, 212, 0.1);
      border: 1px solid rgba(6, 182, 212, 0.2);
      color: var(--primary-cyan);
      padding: 0.4rem 1rem;
      border-radius: 9999px;
      font-size: 0.85rem;
      font-weight: 600;
      letter-spacing: 0.05em;
      text-transform: uppercase;
      margin-bottom: 1.5rem;
    }}

    h1 {{
      font-size: 2.75rem;
      font-weight: 800;
      line-height: 1.2;
      background: linear-gradient(135deg, #ffffff 30%, #a5f3fc 100%);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
      margin-bottom: 1rem;
      letter-spacing: -0.02em;
    }}

    .subtitle {{
      color: var(--text-muted);
      font-size: 1.15rem;
      line-height: 1.6;
      max-width: 600px;
      margin: 0 auto;
    }}

    .grid {{
      display: flex;
      flex-direction: column;
      gap: 1.25rem;
      margin-bottom: 3rem;
    }}

    .card {{
      display: flex;
      align-items: center;
      background: var(--card-bg);
      border: 1px solid var(--border-color);
      border-radius: 16px;
      padding: 1.5rem;
      text-decoration: none;
      color: inherit;
      transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
      backdrop-filter: blur(12px);
      position: relative;
      overflow: hidden;
    }}

    .card::before {{
      content: '';
      position: absolute;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      background: linear-gradient(90deg, rgba(6, 182, 212, 0.05) 0%, transparent 100%);
      opacity: 0;
      transition: opacity 0.3s ease;
    }}

    .card:hover {{
      transform: translateY(-2px);
      border-color: rgba(6, 182, 212, 0.3);
      box-shadow: 0 10px 30px -10px var(--accent-glow);
    }}

    .card:hover::before {{
      opacity: 1;
    }}

    .card-step {{
      font-family: 'JetBrains Mono', monospace;
      font-size: 1.25rem;
      font-weight: 700;
      color: var(--primary-cyan);
      margin-right: 1.5rem;
      background: rgba(6, 182, 212, 0.08);
      border: 1px solid rgba(6, 182, 212, 0.15);
      width: 48px;
      height: 48px;
      display: flex;
      align-items: center;
      justify-content: center;
      border-radius: 12px;
      flex-shrink: 0;
    }}

    .card-content {{
      flex-grow: 1;
    }}

    .card-content h3 {{
      font-size: 1.25rem;
      font-weight: 600;
      margin-bottom: 0.35rem;
      color: #ffffff;
      transition: color 0.3s ease;
    }}

    .card:hover .card-content h3 {{
      color: var(--primary-cyan);
    }}

    .card-content p {{
      color: var(--text-muted);
      font-size: 0.95rem;
      line-height: 1.5;
    }}

    .card-action {{
      display: flex;
      align-items: center;
      gap: 0.5rem;
      font-size: 0.9rem;
      font-weight: 600;
      color: var(--primary-cyan);
      opacity: 0;
      transform: translateX(-10px);
      transition: all 0.3s ease;
      flex-shrink: 0;
      margin-left: 1rem;
    }}

    .card:hover .card-action {{
      opacity: 1;
      transform: translateX(0);
    }}

    .safety-panel {{
      background: rgba(239, 68, 68, 0.03);
      border: 1px solid rgba(239, 68, 68, 0.15);
      border-radius: 16px;
      padding: 1.75rem;
      margin-top: 4rem;
      position: relative;
      overflow: hidden;
    }}

    .safety-panel::before {{
      content: '';
      position: absolute;
      left: 0;
      top: 0;
      height: 100%;
      width: 4px;
      background: #ef4444;
    }}

    .safety-panel h4 {{
      color: #ef4444;
      font-size: 1.1rem;
      font-weight: 600;
      margin-bottom: 0.75rem;
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }}

    .safety-panel p {{
      color: var(--text-muted);
      font-size: 0.95rem;
      line-height: 1.6;
    }}

    footer {{
      margin-top: 4rem;
      text-align: center;
      font-size: 0.85rem;
      color: rgba(156, 163, 175, 0.5);
    }}
  </style>
</head>
<body>
  <div class="container">
    <header>
      <div class="badge">
        <span class="pulse"></span> Technical Appendix
      </div>
      <h1>Forensic Analysis Notebooks</h1>
      <p class="subtitle">
        Static analysis pathways, evidence ledger classification, and metadata validation for the Agentic Collaboration-Plane Injection incident.
      </p>
    </header>

    <main class="grid">
      {notebook_cards}
    </main>

    <section class="safety-panel">
      <h4>
        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M10.29 3.86L1.82 18a2 2 0 0 0 1.71 3h16.94a2 2 0 0 0 1.71-3L13.71 3.86a2 2 0 0 0-3.42 0z"/><line x1="12" y1="9" x2="12" y2="13"/><line x1="12" y1="17" x2="12.01" y2="17"/></svg>
        Safety & Containment Boundary
      </h4>
      <p>
        These workbooks are compiled from reviewed static metadata fixtures, hashes, and compiler strings. In compliance with strict defensive disclosure guidelines, no execution is performed, no live network traffic is captured, and raw attacker-provided binaries are omitted.
      </p>
    </section>

    <footer>
      &copy; 2026 Incident Response Group. For defensive education only.
    </footer>
  </div>
</body>
</html>
""",
        encoding="utf-8",
    )
    print(f"Wrote {OUTPUT}")
    return 0



if __name__ == "__main__":
    raise SystemExit(main())
