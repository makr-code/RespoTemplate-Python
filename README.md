# Python AI Workspace Template

Generisches Template für Python-Projekte mit **AI Vibe Coding** (GitHub Copilot Agents + GitHub Workflows).

## Ziele

- Klare, wiederverwendbare Workspace-Struktur
- Copilot-/Agent-Konventionen im Repository verankert
- Standardisierte CI-Pipeline für Python-Qualität und Security
- Persistenter KI-Wissensbereich (`wiki/`) für langfristigen Kontext

## Enthaltene Bausteine

- `AGENTS.md` und `CLAUDE.md` als Agent-Schema und Konventionen
- `.github/copilot-instructions.md` + `.github/instructions/*` für Coding-/CI-Regeln
- Workflows für:
  - `ruff check`
  - `ruff format --check`
  - `mypy`
  - `pytest --cov`
  - CodeQL (Python)
  - Auto-Label `ai-generated`
- Beispiel-Package unter `src/workspace_template/`
- Beispieltests unter `tests/template/`
- Struktur für langfristigen KI-Kontext: `wiki/`, `raw/`, `ai_context/`, `ai_working/`

## Workspace-Struktur

```text
.
├── .github/
│   ├── copilot-instructions.md
│   ├── instructions/
│   └── workflows/
├── src/
│   └── workspace_template/
├── tests/
│   └── template/
├── wiki/
├── raw/
├── ai_context/
├── ai_working/
├── AGENTS.md
├── CLAUDE.md
└── pyproject.toml
```

## Schnellstart

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
```

## Lokale Qualitätssicherung

```bash
ruff check src tests/template
ruff format --check src tests/template
mypy src tests/template
pytest --cov
```

## Anpassung für dein Projekt

1. Paketnamen unter `src/workspace_template/` umbenennen
2. `pyproject.toml` (`[project]` + Coverage/Mypy) anpassen
3. Repository-spezifische Inhalte in `ai_context/` und `wiki/` ergänzen
4. Nicht benötigte Verzeichnisse entfernen

## Lizenz

MIT
