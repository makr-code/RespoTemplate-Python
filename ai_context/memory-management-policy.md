# Memory Management Policy (C++)

## Ziele

- Speicherlecks, Dangling Pointer und Double-Free vermeiden
- Ownership explizit dokumentieren
- RAII als Standard durchsetzen

## Regeln

1. Verwende `std::unique_ptr` für eindeutige Ownership.
2. Verwende `std::shared_ptr` nur bei echter geteilter Ownership.
3. Übergib nicht-ownende Daten über Referenzen, `std::span` oder `std::string_view`.
4. Vermeide rohe `new`/`delete` im Applikationscode.
5. Jede API beschreibt Ownership und Lebensdauer der Parameter und Rückgaben.
