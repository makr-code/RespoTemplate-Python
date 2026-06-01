# C++ Tools Instructions

## Tooling Priorität

1. Nutze C++ Symbol- und Sprachwerkzeuge zuerst
2. Nutze `grep`/Textsuche nur als Fallback

## Codierstandards (C++20/23)

- RAII ist verpflichtend
- Bevorzuge `std::unique_ptr`/`std::shared_ptr` gegenüber rohen Zeigern
- Verwende `std::string_view` und `std::span` für nicht-ownende Parameter
- Verwende Concepts zur Einschränkung generischer APIs
- Nutze Ranges für deklarative Datenverarbeitung
- Nutze Coroutinen mit klar definierten Promise-Typen

## Qualitätsgrenzen

- Keine unnötigen, cleveren Abstraktionen
- Lesbarkeit und Wartbarkeit haben Vorrang vor Mikro-Optimierungen
