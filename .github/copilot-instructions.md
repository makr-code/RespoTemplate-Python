# Copilot Instructions (C++)

## Sprache & Analyse

- Verwende bei Symbolsuche und Referenzanalyse zuerst C++-Sprachwerkzeuge, nicht reine Textsuche.
- Berücksichtige aktive CMake-Presets und Build-Konfigurationen.

## Modern C++ (C++20/23)

- Ownership explizit modellieren: `std::unique_ptr` und `std::shared_ptr`.
- Nicht-ownende Eingaben bevorzugt über `std::string_view` und `std::span`.
- Templates mit Concepts einschränken.
- Datenpipelines bevorzugt mit Ranges implementieren.
- Coroutinen nur mit klaren Promise-Typen und nachvollziehbarer Fehlerbehandlung.

## Architekturprinzipien

- RAII ist obligatorisch.
- Vermeide unnötige Abstraktionen und implizite Ownership.
- Schreibe Code, der testbar und sanitizierbar bleibt.

## Beispiele

### Bevorzugt

- Ressourcen in RAII-Objekten kapseln.
- APIs mit klarer Ownership und Lebensdauer dokumentieren.
- Build- und Test-Targets in CMake explizit definieren.

### Vermeiden

- Rohe Zeiger als primärer Ownership-Mechanismus.
- Versteckte globale Zustände.
- Komplexität ohne klaren Wartungsnutzen.
