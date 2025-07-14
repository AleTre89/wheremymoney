# 💰 Family Budget – Gestione Risparmi Familiari con Python e Tkinter

Questa è un'applicazione desktop sviluppata in Python con `Tkinter` per la GUI e `SQLite` come database locale. 
Il progetto ha lo scopo di registrare e analizzare le spese familiari, suddividendole per categoria e sotto-categoria, con possibilità future di importare dati da file Excel.

## 🚀 Stato attuale

L'applicazione è in fase di sviluppo iniziale ma già funzionante nelle seguenti aree:

- Inserimento manuale delle spese (data e importo mentre categoria e sotto-categoria vanno ancora abbinate ai rispettivi db)
- Gestione delle categorie e sotto-categorie. Per le categorie è in funzione l'aggiornamento con interfaccia grafica
- Salvataggio dati in un database SQLite
- Interfaccia utente sviluppata con `Tkinter`

---

## 🗂 Struttura del progetto

- `main.py`: interfaccia principale dell'app, con inserimento spese, gestione categorie e pulsanti placeholder.
- `UICategories.py`: finestra per aggiungere e gestire categorie e sotto-categorie.
- `db.py`: script di gestione e modifica tabelle (es. rimozione colonne).
- `database/database.db`: database SQLite in cui vengono salvati i dati.
- `Family savings - tables structure.xlsx`: schema di riferimento delle tabelle, usato per progettare la struttura del database.

---

## ⚙️ Funzionalità implementate

### ✅ Interfaccia principale (`main.py`)
- Campi per **data** e **importo**
- Selezione manuale di **categoria** e **sotto-categoria**
- **Inserimento spesa** nel database (`record` table)
- Pulsanti per: 
  - importazione (non ancora implementata)
  - archivio (non ancora implementato)
  - gestione categorie
  - future funzioni di matching (non ancora implementato)

### ✅ Gestione categorie (`UICategories.py`)
- Aggiunta **nuove categorie**
- Aggiunta **nuove sotto-categorie** collegate a una categoria
- **Controllo duplicati** e inserimento condizionato
- Visualizzazione **lista categorie** in `TreeView` (le subcategorie verranno aggiunte in futuro)

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
