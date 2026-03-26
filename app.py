import streamlit as st

# Title
st.title("🏠 Home Management System")

# Session state to store tasks
if "tasks" not in st.session_state:
    st.session_state.tasks = []

# Input box
task = st.text_input("Enter a task")

# Add button
if st.button("Add Task"):
    if task:
        st.session_state.tasks.append(task)

# Display tasks
st.subheader("Your Tasks")

for i, t in enumerate(st.session_state.tasks):
    col1, col2 = st.columns([4, 1])

    with col1:
        st.write(t)

    with col2:
        if st.button("❌", key=i):
            st.session_state.tasks.pop(i)
            st.rerun()