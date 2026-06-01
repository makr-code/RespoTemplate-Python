# CI Logic Instructions

## Pflichtprüfungen für C++-Änderungen

- `clang-format` muss sauber laufen
- `clang-tidy` darf keine neuen kritischen Findings erzeugen
- CodeQL muss ohne offene High/Critical Findings durchlaufen
- Sanitizer-Build (ASan) muss grün sein

## PR-Verhalten

- KI-generierte PRs mit Label `ai-generated` kennzeichnen
- Ohne grüne CI und menschliche Freigabe kein Merge
