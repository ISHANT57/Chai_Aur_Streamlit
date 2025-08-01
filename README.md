# ☕ Chai Aur Streamlit: My Learning Journey

Welcome to my "Chai Aur Streamlit" repository! This project documents my journey of learning Streamlit from the ground up. What started as a simple exploration has culminated in a feature-rich, professional To-Do list application. This README serves as a guide to the project, the concepts I've learned, and the final application.

![Pro-Do List Screenshot](C:\Users\ishan\Downloads\STREAMLIT\chai_streamlit\Screenshot 2025-08-01 161841.png)
*Replace this with a screenshot of your final To-Do app!*

---

## 🚀 About The Project

The goal of this project was to learn the fundamentals of building interactive web applications entirely in Python using Streamlit. The **Pro-Do List** application is the practical outcome of this learning process. It's designed to be a functional, stylish, and user-friendly task manager that showcases the power and simplicity of Streamlit.

---

## 🌟 Features of the Pro-Do App

The final application includes a comprehensive set of features, demonstrating a wide range of Streamlit's capabilities:

* **📝 Add & Manage Tasks:** Easily add tasks with descriptions, due dates, and priority levels.
* **✅ Mark as Complete:** Check off tasks to move them from the "Active" list to a clean, collapsed "Completed" section.
* **🗑️ Delete Tasks:** Remove tasks you no longer need with a single click.
* **🧹 Clear Completed:** A dedicated button to clear all completed tasks at once.
* **🔍 Powerful Filtering:**
    * Filter tasks by **Priority** (High, Medium, Low).
    * Filter tasks by **Status** (All, Active, Completed).
* **📅 Due Dates:** Assign a due date to each task to stay on schedule.
* **🎨 Custom Styling:** Injected CSS to create a professional and modern user interface.
* **💾 Persistent Session:** Uses `st.session_state` to ensure your to-do list remains active as you interact with the app.

---

## 💡 Key Streamlit Concepts Learned

This project was a hands-on way to master the following Streamlit concepts:

* **Basic Widgets:** `st.button`, `st.text_input`, `st.checkbox`, `st.selectbox`, `st.radio`, `st.date_input`.
* **Layout & Structure:** Using `st.sidebar` for inputs and `st.columns` to align elements.
* **State Management:** The critical use of `st.session_state` to hold data across app reruns.
* **App Logic & Control Flow:** How to trigger functions with `on_click` and `on_change`, and how to force an update with `st.rerun()`.
* **Dynamic UI:** Generating UI elements in a loop to display the list of tasks.
* **Customization:** Using `st.markdown` with `unsafe_allow_html=True` to inject custom CSS for unique styling.
* **Page Configuration:** Setting up a professional page look with `st.set_page_config`.

---

## 🛠️ Getting Started

To get a local copy up and running, follow these simple steps.

### Prerequisites

Ensure you have Python 3.7+ installed.

### Installation

1.  **Clone the repo:**
    ```bash
    git clone [https://github.com/ISHANT57/Chai_Aur_Streamlit.git](https://github.com/ISHANT57/Chai_Aur_Streamlit.git)
    ```
2.  **Navigate to the project directory:**
    ```bash
    cd Chai_Aur_Streamlit
    ```
3.  **Install Streamlit:**
    ```bash
    pip install streamlit
    ```

### Running the App

1.  Run the application from your terminal:
    ```bash
    streamlit run app.py
    ```
2.  Open your browser and navigate to the local URL provided (e.g., `http://localhost:8501`).

---

## 👤 Author

* **Ishant** - [ISHANT57](https://github.com/ISHANT57)

---

## 📄 License

This project is open-source. Consider adding an MIT License file to define permissions for others.
