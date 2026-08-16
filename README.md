# FrancoPedia

**FrancoPedia is the Vascular Intern Guide** — a focused, private educational workspace for navigating vascular evidence.

> Educational and deidentified pilot only. It is not for PHI, emergencies, patient-specific decisions, EHR use, or institutional clinical deployment.

## Launch

The canonical public landing page is <https://momomojo.github.io/francopedia/>. Launch the guide at <https://agents-mac-mini.tail1339c4.ts.net:10000>.

## Architecture map

```text
GitHub Pages landing page
        │
        └── Launch FrancoPedia ──> Tailscale Funnel HTTPS
                                      │
                                      └── Open WebUI (127.0.0.1:3030)
                                             │
                                             └── Hermes vascular-share API (127.0.0.1:8664)
                                                    └── OpenRouter: deepseek/deepseek-v4-flash-0731
```

The landing page is static and deployed from the repository's `main` branch root through GitHub Pages. Deployment details, service boundaries, and acceptance-suite locations are in [docs/DEPLOYMENT.md](docs/DEPLOYMENT.md).

## Repository layout

- `landing/` — responsive dark-theme landing page
- `docs/` — deployment and operations documentation (sanitized)
- `env.example` — intentionally non-functional environment variable placeholders

## Local preview

No build step is required. From the repository root, run a static server such as `python3 -m http.server`, then open `landing/` in a browser.

## License

MIT. See [LICENSE](LICENSE).
