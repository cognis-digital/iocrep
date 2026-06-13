<a name="top"></a>
<div align="center">

<img src="https://capsule-render.vercel.app/api?type=rect&color=0:6b46c1,100:2b6cb0&height=120&section=header&text=IOCREP&fontSize=48&fontColor=ffffff&fontAlignY=58" width="100%" alt="IOCREP"/>

# IOCREP

### Score IOCs against offline reputation/allow lists with explainable verdicts

<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=18&duration=3500&pause=1000&color=6B46C1&center=true&vCenter=true&width=720&lines=Score+IOCs+against+offline+reputationallow+lists+with+explai;Self-hostable+%C2%B7+MCP-native+%C2%B7+CI-ready+%C2%B7+polyglot" width="720"/>

[![PyPI](https://img.shields.io/pypi/v/cognis-iocrep.svg?color=6b46c1)](https://pypi.org/project/cognis-iocrep/) [![CI](https://github.com/cognis-digital/iocrep/actions/workflows/ci.yml/badge.svg)](https://github.com/cognis-digital/iocrep/actions) [![License: COCL 1.0](https://img.shields.io/badge/License-COCL%201.0-2b6cb0.svg)](LICENSE) [![Suite](https://img.shields.io/badge/Cognis-Neural%20Suite-6b46c1.svg)](https://github.com/cognis-digital)

*Part of the Cognis Neural Suite.*

</div>

```bash
pip install cognis-iocrep
iocrep scan .            # → prioritized findings in seconds
```

## Usage — step by step

1. **Install:**

   ```bash
   pip install iocrep
   ```

2. **Score indicators** — pass IOCs (IP, domain, URL, hash, email; defanged forms accepted) against the offline reputation DB:

   ```bash
   iocrep score 198.51.100.7 evil.example[.]com d41d8cd98f00b204e9800998ecf8427e
   ```

   Each verdict carries a score, severity, and the explainable top reason.

3. **Score a file of indicators** and supply your own reputation/allow list:

   ```bash
   iocrep score --infile iocs.txt --db reputation.json
   ```

4. **Read the output** — table, JSON, or a standalone HTML report written to a file:

   ```bash
   iocrep score --infile iocs.txt --format json -o verdicts.json
   iocrep score --infile iocs.txt --format html -o report.html
   ```

5. **CI / triage gate** — exit non-zero at/above a severity (default `medium`):

   ```bash
   iocrep score --infile iocs.txt --fail-on high
   ```

## Contents

- [Why iocrep?](#why) · [Features](#features) · [Quick start](#quick-start) · [Example](#example) · [Architecture](#architecture) · [AI stack](#ai-stack) · [How it compares](#how-it-compares) · [Integrations](#integrations) · [Install anywhere](#install-anywhere) · [Related](#related) · [Contributing](#contributing)

<a name="why"></a>
## Why iocrep?

Score IOCs against offline reputation/allow lists with explainable verdicts — without standing up heavyweight infrastructure.

`iocrep` is single-purpose, scriptable, and self-hostable: point it at a target, get prioritized results in the format your workflow already speaks (table · JSON · SARIF), gate CI on it, and let agents drive it over MCP.

<div align="right"><a href="#top">↑ back to top</a></div>

<a name="features"></a>
## Features

- ✅ Refang
- ✅ Classify Indicator
- ✅ Score Indicator
- ✅ Score Batch
- ✅ Runs on Linux/macOS/Windows · Docker · devcontainer
- ✅ Ports in Python, JavaScript, Go, and Rust (`ports/`)

<div align="right"><a href="#top">↑ back to top</a></div>

<a name="quick-start"></a>
## Quick start

```bash
pip install cognis-iocrep
iocrep --version
iocrep scan .                       # scan current project
iocrep scan . --format json         # machine-readable
iocrep scan . --fail-on high        # CI gate (non-zero exit)
```

<div align="right"><a href="#top">↑ back to top</a></div>

<a name="example"></a>
## Example

```text
$ iocrep scan .
  [HIGH    ] IOC-001  example finding             (./src/app.py)
  [MEDIUM  ] IOC-002  another signal              (./config.yaml)

  2 findings · risk score 5 · 38ms
```

<div align="right"><a href="#top">↑ back to top</a></div>

<a name="architecture"></a>
## Architecture

```mermaid
flowchart LR
  IN[input] --> P[iocrep<br/>analyze + score]
  P --> OUT[report]
```

<div align="right"><a href="#top">↑ back to top</a></div>

<a name="ai-stack"></a>
## Use it from any AI stack

`iocrep` is interoperable with every popular way of using AI:

- **MCP server** — `iocrep mcp` (Claude Desktop, Cursor, Cognis.Studio, [uncensored-fleet](https://github.com/cognis-digital/uncensored-fleet))
- **OpenAI-compatible / JSON** — pipe `iocrep scan . --format json` into any agent or LLM
- **LangChain · CrewAI · AutoGen · LlamaIndex** — wrap the CLI/JSON as a tool in one line
- **CI / scripts** — exit codes + SARIF for non-AI pipelines

<div align="right"><a href="#top">↑ back to top</a></div>

<a name="how-it-compares"></a>
## How it compares

| | **Cognis iocrep** | typical tools |
|---|:---:|:---:|
| Self-hostable, no account | ✅ | varies |
| Single command, zero config | ✅ | ⚠️ |
| JSON + SARIF for CI | ✅ | varies |
| MCP-native (AI agents) | ✅ | ❌ |
| Polyglot ports (JS/Go/Rust) | ✅ | ❌ |
| Open license | ✅ COCL | varies |
<div align="right"><a href="#top">↑ back to top</a></div>

<a name="integrations"></a>
## Integrations

Pipes into your stack: **SARIF** for code-scanning, **JSON** for anything, an **MCP server** (`iocrep mcp`) for AI agents, and a webhook forwarder for SIEM/Slack/Jira. See [`docs/INTEGRATIONS.md`](docs/INTEGRATIONS.md).

<div align="right"><a href="#top">↑ back to top</a></div>

<a name="install-anywhere"></a>
## Install — every way, every platform

```bash
pip install "git+https://github.com/cognis-digital/iocrep.git"    # pip (works today)
pipx install "git+https://github.com/cognis-digital/iocrep.git"   # isolated CLI
uv tool install "git+https://github.com/cognis-digital/iocrep.git" # uv
pip install cognis-iocrep                                          # PyPI (when published)
docker run --rm ghcr.io/cognis-digital/iocrep:latest --help        # Docker
brew install cognis-digital/tap/iocrep                             # Homebrew tap
curl -fsSL https://raw.githubusercontent.com/cognis-digital/iocrep/main/install.sh | sh
```

| Linux | macOS | Windows | Docker | Cloud |
|---|---|---|---|---|
| `scripts/setup-linux.sh` | `scripts/setup-macos.sh` | `scripts/setup-windows.ps1` | `docker run ghcr.io/cognis-digital/iocrep` | [DEPLOY.md](docs/DEPLOY.md) (AWS/Azure/GCP/k8s) |

<div align="right"><a href="#top">↑ back to top</a></div>

<a name="related"></a>
## Related Cognis tools


**Explore the suite →** [🗂️ all 170+ tools](https://github.com/cognis-digital/cognis-neural-suite) · [⭐ awesome-cognis](https://github.com/cognis-digital/awesome-cognis) · [🔗 cognis-sources](https://github.com/cognis-digital/cognis-sources) · [🤖 uncensored-fleet](https://github.com/cognis-digital/uncensored-fleet) · [🧠 engram](https://github.com/cognis-digital/engram)

<div align="right"><a href="#top">↑ back to top</a></div>

<a name="contributing"></a>
## Contributing

PRs, new rules, and demo scenarios are welcome under the collaboration-pull model — see [CONTRIBUTING.md](CONTRIBUTING.md) and [SECURITY.md](SECURITY.md).

> ### ⭐ If `iocrep` saved you time, **star it** — it genuinely helps others find it.

## License

Source-available under the **Cognis Open Collaboration License (COCL) v1.0** — free for personal, internal-evaluation, research, and educational use; **commercial / production use requires a license** (licensing@cognis.digital). See [LICENSE](LICENSE).

---

<div align="center"><sub><b><a href="https://cognis.digital">Cognis Digital</a></b> · one of 170+ tools in the <a href="https://github.com/cognis-digital/cognis-neural-suite">Cognis Neural Suite</a> · <i>Making Tomorrow Better Today</i></sub></div>
