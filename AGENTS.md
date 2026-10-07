# Istruzioni per gli agenti

## Scopo e lingua

- Questo repository contiene appunti per il libro «Improvvisare con la
  Chitarra».
- Scrivi in italiano tutti i contenuti rivolti ai lettori. Mantieni i termini
  musicali internazionali quando sono d'uso comune e spiegali alla prima
  occorrenza.
- Quando introduci un nuovo termine tecnico o specifico, aggiungilo anche a
  `Docs/glossario.md` con una definizione breve e chiara. Mantieni le voci in
  ordine alfabetico.

## Struttura del libro

- Le pagine sorgente sono in Markdown con MyST e si trovano sotto `Docs/`.
- Se aggiungi una pagina del libro, inseriscila nella toctree di
  `Docs/index.md` nell'ordine di lettura desiderato.
- Le decisioni architetturali sono in `Docs/adr/`. Consulta quelle pertinenti
  prima di cambiare convenzioni o struttura; per una nuova decisione usa
  `Docs/adr/modello.md`.
- Le ADR sono materiale di lavoro e restano escluse dal libro pubblicato.

## Configurazione e risorse

- Read the Docs usa `Docs/conf.py` e genera HTML, PDF ed ePub.
- Il logo della testata Shibuya è `Docs/_static/logo_256.png`; la homepage usa
  `Docs/_static/logo.png`.
- Le personalizzazioni CSS vanno in `Docs/_static/custom.css`, già collegato
  tramite `html_css_files`.
- Per avviare l'anteprima locale usa `./avvia-docs.sh`.
