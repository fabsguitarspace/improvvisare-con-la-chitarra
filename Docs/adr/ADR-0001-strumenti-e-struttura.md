# ADR-0001: Strumenti e struttura iniziale

- **Stato:** Accettata
- **Data:** 2026-10-07
- **Sostituisce:** nessuna

## Contesto

Il progetto raccoglie in italiano un libro di appunti intitolato
«Improvvisare con la Chitarra». Deve essere pubblicato su Read the Docs e
scaricabile in PDF ed ePub. Le decisioni e le convenzioni devono essere
consultabili anche dagli agenti di coding che contribuiranno al repository.

## Decisione

- Usare Sphinx per costruire il libro e Read the Docs per pubblicarlo.
- Usare il tema Shibuya per il sito HTML.
- Scrivere i capitoli in Markdown con l'estensione MyST per Sphinx.
- Tenere sorgenti e configurazione Sphinx in `Docs/` e le decisioni in
  `Docs/adr/`.
- Generare HTML, PDF ed ePub su Read the Docs; impostare l'italiano come lingua
  dei contenuti e usare XeLaTeX per il PDF.

## Conseguenze

- Le nuove pagine del libro vanno aggiunte alla toctree di `Docs/index.md`.
- Le ADR restano escluse dall'output destinato ai lettori.
- Le dipendenze Sphinx, Shibuya e MyST sono dichiarate in
  `requirements-docs.txt`.
- Le dipendenze hanno limiti di versione compatibili, ma non sono ancora
  bloccate a versioni puntuali.

## Alternative considerate

- Usare reStructuredText come formato dei capitoli; è il formato nativo di
  Sphinx, ma Markdown è più immediato per appunti e collaborazione.
- Tenere gli appunti fuori dalla radice Sphinx; la cartella `Docs/` mantiene
  invece insieme libro e ADR, escludendo queste ultime dalla pubblicazione.
