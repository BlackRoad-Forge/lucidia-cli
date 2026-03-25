<!-- BlackRoad SEO Enhanced -->

# lucidia cli

> Part of **[BlackRoad OS](https://blackroad.io)** — Sovereign Computing for Everyone

[![BlackRoad OS](https://img.shields.io/badge/BlackRoad-OS-ff1d6c?style=for-the-badge)](https://blackroad.io)
[![BlackRoad Forge](https://img.shields.io/badge/Org-BlackRoad-Forge-2979ff?style=for-the-badge)](https://github.com/BlackRoad-Forge)
[![License](https://img.shields.io/badge/License-Proprietary-f5a623?style=for-the-badge)](LICENSE)

**lucidia cli** is part of the **BlackRoad OS** ecosystem — a sovereign, distributed operating system built on edge computing, local AI, and mesh networking by **BlackRoad OS, Inc.**

## About BlackRoad OS

BlackRoad OS is a sovereign computing platform that runs AI locally on your own hardware. No cloud dependencies. No API keys. No surveillance. Built by [BlackRoad OS, Inc.](https://github.com/BlackRoad-OS-Inc), a Delaware C-Corp founded in 2025.

### Key Features
- **Local AI** — Run LLMs on Raspberry Pi, Hailo-8, and commodity hardware
- **Mesh Networking** — WireGuard VPN, NATS pub/sub, peer-to-peer communication
- **Edge Computing** — 52 TOPS of AI acceleration across a Pi fleet
- **Self-Hosted Everything** — Git, DNS, storage, CI/CD, chat — all sovereign
- **Zero Cloud Dependencies** — Your data stays on your hardware

### The BlackRoad Ecosystem
| Organization | Focus |
|---|---|
| [BlackRoad OS](https://github.com/BlackRoad-OS) | Core platform and applications |
| [BlackRoad OS, Inc.](https://github.com/BlackRoad-OS-Inc) | Corporate and enterprise |
| [BlackRoad AI](https://github.com/BlackRoad-AI) | Artificial intelligence and ML |
| [BlackRoad Hardware](https://github.com/BlackRoad-Hardware) | Edge hardware and IoT |
| [BlackRoad Security](https://github.com/BlackRoad-Security) | Cybersecurity and auditing |
| [BlackRoad Quantum](https://github.com/BlackRoad-Quantum) | Quantum computing research |
| [BlackRoad Agents](https://github.com/BlackRoad-Agents) | Autonomous AI agents |
| [BlackRoad Network](https://github.com/BlackRoad-Network) | Mesh and distributed networking |
| [BlackRoad Education](https://github.com/BlackRoad-Education) | Learning and tutoring platforms |
| [BlackRoad Labs](https://github.com/BlackRoad-Labs) | Research and experiments |
| [BlackRoad Cloud](https://github.com/BlackRoad-Cloud) | Self-hosted cloud infrastructure |
| [BlackRoad Forge](https://github.com/BlackRoad-Forge) | Developer tools and utilities |

### Links
- **Website**: [blackroad.io](https://blackroad.io)
- **Documentation**: [docs.blackroad.io](https://docs.blackroad.io)
- **Chat**: [chat.blackroad.io](https://chat.blackroad.io)
- **Search**: [search.blackroad.io](https://search.blackroad.io)

---


[![CI](https://github.com/blackboxprogramming/lucidia-cli/actions/workflows/ci.yml/badge.svg)](https://github.com/blackboxprogramming/lucidia-cli/actions/workflows/ci.yml)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-3776AB.svg)](https://python.org)
[![License](https://img.shields.io/badge/license-Proprietary-9c27b0)](LICENSE)

A terminal operating system built on Textual and Rich. Multi-tab TUI with a web browser, sandboxed filesystem, AI agents, mini applications, and background process management.

## Components

### Web Engine
Terminal web browser with HTML-to-Rich markup parser, link extraction and navigation, browsing history, and DuckDuckGo search integration.

### Virtual Filesystem
Sandboxed at `~/.lucidia/vfs`. Standard operations: `ls`, `cd`, `cat`, `write`, `mkdir`, `rm`. Persistent across sessions.

### AI Agents
Ollama-powered agents with distinct personalities: lucidia, alice, octavia, cece, operator. Council mode runs multi-agent discussions where agents debate and synthesize answers.

### Mini Apps
- `calc` -- safe expression evaluator
- `btc` / `eth` -- live crypto prices
- `weather` -- wttr.in integration
- `fortune` -- random wisdom
- `time` / `date` / `unix` -- clock utilities
- `whoami` / `neofetch` -- system info

### Process Manager
Async background task spawning with PID tracking. `ps` to list, `kill` to stop.

## Architecture

```
lucidia.py (main TUI)
    |
    +-- components/
    |       web_engine.py     HTML parser + browser
    |       virtual_fs.py     Sandboxed filesystem
    |       agents.py         Ollama AI integration
    |       apps.py           Calculator, crypto, weather
    |       process_mgr.py    Background task manager
    |
    +-- config/
            settings.json     User preferences
```

## Keybindings

| Key | Action |
|-----|--------|
| Ctrl+1 | Shell |
| Ctrl+2 | Web browser |
| Ctrl+3 | Files |
| Ctrl+4 | AI Agents |
| Ctrl+5 | Apps |
| Ctrl+Q | Quit |

## Install and Run

```bash
pip install textual rich
python lucidia.py
```

For AI agents, Ollama must be running locally.

## Development

```bash
pip install -r requirements.txt
pytest tests/ -v
```

## License

Proprietary -- BlackRoad OS, Inc.
