# Improvvisare con la Chitarra

Appunti in italiano per imparare a improvvisare con la chitarra. Il progetto
usa Sphinx e il tema Shibuya; Read the Docs pubblica il libro sul web e prepara
le versioni scaricabili in PDF ed ePub.

## Struttura

```text
.
├── .readthedocs.yaml       # configurazione della pubblicazione
├── requirements-docs.txt   # dipendenze per costruire il libro
├── Docs/
│   ├── conf.py             # configurazione Sphinx
│   ├── index.md            # indice e ordine dei capitoli
│   ├── capitoli/           # appunti organizzati per argomento
│   └── adr/                # decisioni architetturali per agent e collaboratori
└── README.md
```

## Anteprima locale

Con Python 3.12 o successivo:

```bash
./avvia-docs.sh
```

Lo script crea `.venv` e installa le dipendenze al primo avvio, poi apre il sito
su `http://127.0.0.1:8000`. Lascia il terminale aperto mentre scrivi: Sphinx
ricostruisce le pagine e ricarica il browser quando salvi modifiche. Interrompi
il server con `Ctrl+C`.

Per installare o aggiornare manualmente le dipendenze:

```bash
python3 -m venv .venv  # solo al primo avvio
.venv/bin/python -m pip install -r requirements-docs.txt
```

Per generare localmente l'ePub usa
`.venv/bin/sphinx-build -b epub Docs _build/epub`. La generazione PDF in locale
richiede una distribuzione LaTeX con XeLaTeX; Read the Docs gestisce questa
fase durante la pubblicazione.

## Pubblicazione

Collega il repository a [Read the Docs](https://readthedocs.org/). La
configurazione in `.readthedocs.yaml` indica la lingua italiana, la radice
Sphinx in `Docs/conf.py` e la creazione di HTML, PDF ed ePub. Imposta anche
l'italiano come lingua del progetto nel pannello Read the Docs.

## Scrivere e collaborare

- Aggiungi o aggiorna i capitoli in `Docs/capitoli/` e inseriscili nella
  sequenza in `Docs/index.md`.
- Mantieni il testo del libro in italiano; conserva i termini musicali
  internazionali quando sono d'uso comune e spiegali alla prima occorrenza.
- Per decisioni che influenzano struttura o convenzioni, usa il modello in
  `Docs/adr/modello.md` e aggiorna l'indice ADR.
- Prima di modificare il progetto, gli agenti di coding dovrebbero leggere
  questo README e le ADR pertinenti.
