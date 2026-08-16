# FrancoPedia deployment map

This document describes the currently deployed educational pilot without recording credentials, passwords, tokens, or user data.

## Public path

- **Landing:** GitHub Pages serves this repository from the `main` branch root. `index.html` routes visitors to `landing/`; `CNAME` declares `francopedia.is-a.dev`.
- **Guide:** the launch button targets `https://agents-mac-mini.tail1339c4.ts.net:10000`.
- **Ingress:** Tailscale Funnel terminates public HTTPS and proxies only to Open WebUI at `127.0.0.1:3030`. The Hermes API remains loopback-only at `127.0.0.1:8664`; no router port is opened.

## Services

| Component | LaunchAgent | Local endpoint | Role |
| --- | --- | --- | --- |
| Hermes vascular API | `ai.hermes.vascular-share-api` | `http://127.0.0.1:8664` | Provides the visible `vascular-intern-guide` model |
| Open WebUI | `ai.hermes.vascular-share-webui` | `http://127.0.0.1:3030` | Dedicated Python 3.12 educational workspace |

Both user LaunchAgents use `KeepAlive` and `RunAtLoad`.

The backend model is pinned to `deepseek/deepseek-v4-flash-0731` through a profile-scoped OpenRouter credential. Image pre-analysis uses `google/gemini-3.7-flash`; the visible DeepSeek specialist remains the final-answer author. Credentials are intentionally not represented here.

## Operational boundaries

The release is an invite-only, deidentified educational pilot. It does not accept PHI and is not for emergency care, patient-specific decisions, EHR integration, or institutional clinical deployment. Self-registered users begin pending and require owner approval before model/chat access.

## Acceptance evidence locations

The live deployment's reproducible, sanitized acceptance artifacts are maintained with the deployment:

- `acceptance/modern_workspace_acceptance.py` and `acceptance/result.json` — private workspace/isolation acceptance suite
- `acceptance/format_svs_vision_acceptance.py` and `acceptance/format-svs-vision-result.json` — formatting, SVS retrieval, and vision acceptance suite

The authoritative operator runbook is maintained with the runtime deployment; this public repository deliberately contains only this sanitized map.

## Read-only health checks

```sh
curl -fsS http://127.0.0.1:8664/health
curl -fsS http://127.0.0.1:3030/health
tailscale serve status
```

Do not expose the loopback services directly or copy runtime credentials into this repository.
