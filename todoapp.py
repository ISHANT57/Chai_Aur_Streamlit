import streamlit as st
import datetime

# --- Page Configuration ---
st.set_page_config(
    page_title="Pro-Do List",
    page_icon="✅",
    layout="centered",
    initial_sidebar_state="expanded",
)

# --- Custom CSS for Styling ---
st.markdown("""
<style>
    .task-card {
        background-color: #f9f9f9;
        border-left: 5px solid #4CAF50;
        border-radius: 8px;
        padding: 10px;
        margin-bottom: 10px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
    }
    .task-completed {
        text-decoration: line-through;
        color: #888;
        border-left-color: #ccc;
    }
    .priority-high {
        color: red;
    }
    .priority-medium {
        color: orange;
    }
    .priority-low {
        color: green;
    }
</style>
""", unsafe_allow_html=True)

# --- Session State Initialization ---
if 'todos' not in st.session_state:
    st.session_state.todos = []

# --- Add New Task Function ---
def add_todo():
    task_text = st.session_state.task_input.strip()
    due_date = st.session_state.due_date
    priority = st.session_state.priority

    if task_text:
        st.session_state.todos.append({
            "task": task_text,
            "completed": False,
            "due": due_date,
            "priority": priority
        })
        st.session_state.task_input = ""

# --- Delete Task ---
def delete_task(index):
    st.session_state.todos.pop(index)

# --- Clear Completed Tasks ---
def clear_completed():
    st.session_state.todos = [t for t in st.session_state.todos if not t["completed"]]

# --- Sidebar: Add Task ---
with st.sidebar:
    st.header("➕ Add a Task")
    st.text_input("Task", key="task_input", placeholder="Enter task here...", on_change=add_todo)
    st.date_input("Due Date", key="due_date", value=datetime.date.today())
    st.selectbox("Priority", ["High", "Medium", "Low"], key="priority")
    st.button("Add Task", on_click=add_todo)
    st.markdown("---")
    st.button("🧹 Clear Completed", on_click=clear_completed)

# --- Filters ---
st.subheader("📌 Filters")
filter_priority = st.selectbox("Filter by Priority", ["All", "High", "Medium", "Low"])
filter_status = st.radio("Filter by Status", ["All", "Active", "Completed"], horizontal=True)
st.write("---")

# --- Display Tasks ---
filtered_tasks = []

for i, task in enumerate(st.session_state.todos):
    matches_priority = filter_priority == "All" or task["priority"] == filter_priority
    matches_status = (
        filter_status == "All" or
        (filter_status == "Active" and not task["completed"]) or
        (filter_status == "Completed" and task["completed"])
    )
    if matches_priority and matches_status:
        filtered_tasks.append((i, task))

if not filtered_tasks:
    st.info("No tasks match the selected filters.")
else:
    for i, task in filtered_tasks:
        col1, col2 = st.columns([0.85, 0.15])
        with col1:
            checked = st.checkbox(
                f"{task['task']} (Due: {task['due']}, Priority: {task['priority']})",
                value=task["completed"],
                key=f"task_{i}"
            )
            st.session_state.todos[i]["completed"] = checked
        with col2:
            if st.button("🗑️", key=f"delete_{i}"):
                delete_task(i)
                st.rerun()


# --- Footer --
st.markdown("---")
st.caption("✅ Pro-Do List • Made with Streamlit By Ishant")


