# Family Budget – Gestione Risparmi Familiari con Python e Tkinter

Questa è un'applicazione desktop sviluppata in Python con `Tkinter` per la GUI e `SQLite` come database locale. 
Il progetto ha lo scopo di registrare e analizzare le spese familiari, suddividendole automaticamente per categoria e sotto-categoria, con possibilità di importare dati da file Excel.

## 🚀 Stato attuale

L'applicazione è in fase di sviluppo iniziale ma già funzionante nelle seguenti aree:

- Inserimento manuale delle spese (data e importo mentre categoria e sotto-categoria vanno ancora abbinate ai rispettivi db)
- Gestione delle categorie e sotto-categorie.
- Importazione di movimenti da file Excel in un’area di archivio.
- Salvataggio dati in un database SQLite
- Maschera per definire regole di matching automatico tra descrizioni movimenti e categorie.
- Interfaccia utente sviluppata con `Tkinter`

---

## 🗂 Struttura del progetto

- `main.py`: interfaccia principale dell'app, con inserimento spese, gestione categorie e pulsanti placeholder.
- `UICategories.py`: finestra per aggiungere e gestire categorie e sotto-categorie.
- `db.py`: script di utilità per la gestione del database (creazione/modifica tabelle, test query)
- `database/database.db`: database SQLite in cui vengono salvati i dati.
- `Family savings - tables structure.xlsx`: schema di riferimento delle tabelle, usato per progettare la struttura del database.
- `UIArc_Imp.py` → Maschera Archive: importa movimenti da Excel (elenco.xlsx), li visualizza in TreeView e permette l’assegnazione di categorie/sotto-categorie.
- `UIMatching.py` → Gestione regole di matching automatico tra stringhe di descrizione e categorie/sotto-categorie.
- `elenco.xlsx` → File Excel di esempio con movimenti da importare.

---

## ⚙️ Funzionalità implementate

✅ Interfaccia principale (main.py)
Inserimento spesa manuale: data, importo, categoria e sotto-categoria.
Accesso diretto a:

Archivio movimenti (importazione Excel)

Gestione categorie

Gestione regole di matching

✅ Archivio movimenti (UIArc_Imp.py)
Importa i movimenti da elenco.xlsx e li visualizza in tabella.

Assegnazione manuale di categorie e sotto-categorie.

Visualizzazione descrizione operazione selezionata.

Pre-matching automatico basato sulle regole salvate.

✅ Gestione categorie (UICategories.py)
Creazione categorie e sotto-categorie collegate.

Controllo duplicati con messaggi di conferma.

Visualizzazione in TreeView gerarchica (categorie → sotto-categorie).

✅ Matching categorie (UIMatching.py)
Creazione regole che associano una stringa di testo a una coppia categoria/sotto-categoria.

Visualizzazione e gestione regole esistenti.

---

## 🛠 Database (SQLite)

Tabelle attualmente in uso:

- `categories(id_cat, category)`
- `sub_categories(id_subcat, id_cat, cod_subcat, subcategory)`
- `record(id_record, date, amount, id_cat, id_subcat)`
- *(Nota: tabelle come `matching` sono previste ma non ancora usate)*

---

## 📌 TODO / Funzionalità future

- [ ] Importazione automatica da file Excel (`pandas`)
- [ ] Collegamento dinamico di categorie e sotto-categorie nel form principale
- [ ] Visualizzazione spese per periodo/categoria
- [ ] Aggiunta campo "attivo" per disattivare categorie obsolete
- [ ] Matching automatico categorie ↔ descrizione testuale
- [ ] Archiviazione record storici

---

## ▶️ Esecuzione

Assicurati che la cartella `database/` contenga il file `database.db`, poi avvia l'app con:

```bash
python main.py
