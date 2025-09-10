import streamlit as st

st.set_page_config(page_title="To-Do List", page_icon="✅", layout="centered")

st.title("📝 Můj To-Do List")
st.write("Zde si můžeš zapisovat a spravovat své úkoly.")

if "tasks" not in st.session_state:
    st.session_state.tasks = []

new_task = st.text_input("Přidat nový úkol", placeholder="Např. Udělat domácí úkol...")

if st.button("➕ Přidat"):
    if new_task.strip():
        st.session_state.tasks.append({"text": new_task, "done": False})
        st.experimental_rerun()

if st.session_state.tasks:
    st.subheader("📋 Seznam úkolů")

    for i, task in enumerate(st.session_state.tasks):
        col1, col2 = st.columns([0.1, 0.9])
        done = col1.checkbox("", value=task["done"], key=f"task_{i}")
        if done != task["done"]:
            st.session_state.tasks[i]["done"] = done

        if task["done"]:
            col2.markdown(f"~~{task['text']}~~")
        else:
            col2.markdown(task["text"])

    if st.button("🗑️ Odstranit hotové úkoly"):
        st.session_state.tasks = [task for task in st.session_state.tasks if not task["done"]]
        st.experimental_rerun()
else:
    st.info("Zatím nemáš žádné úkoly. Přidej si nějaký výše.")
