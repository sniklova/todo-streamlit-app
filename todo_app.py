import streamlit as st
import json
from datetime import datetime

# Soubor pro ukládání úkolů
TODO_FILE = "todos.json"

# Načtení úkolů ze souboru
def load_todos():
    try:
        with open(TODO_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

# Uložení úkolů do souboru
def save_todos(todos):
    with open(TODO_FILE, "w", encoding="utf-8") as f:
        json.dump(todos, f, ensure_ascii=False, indent=2)

# Inicializace
st.set_page_config(page_title="Můj To-Do List", page_icon="📝")
st.title("📝 Můj To-Do List")
st.write("Zde si můžeš zapisovat a spravovat své úkoly.")

# Načtení úkolů
todos = load_todos()

# Formulář pro přidání nového úkolu
with st.form("new_task_form"):
    col1, col2 = st.columns([3, 1])
    with col1:
        new_task = st.text_input("Přidat nový úkol")
    with col2:
        emoji = st.text_input("Emoji", max_chars=2)

    col3, col4 = st.columns([1, 1])
    with col3:
        person = st.text_input("S kým?", placeholder="Jméno osoby")
    with col4:
        due_date = st.date_input("Do kdy?")

    submitted = st.form_submit_button("➕ Přidat")
    if submitted and new_task:
        task = {
            "task": new_task,
            "emoji": emoji,
            "person": person,
            "due_date": due_date.strftime("%Y-%m-%d"),
            "created": datetime.now().strftime("%Y-%m-%d %H:%M")
        }
        todos.append(task)
        save_todos(todos)
        st.experimental_rerun()

# Výpis úkolů
st.subheader("📋
