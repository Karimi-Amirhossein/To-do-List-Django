# My Django To-Do App

Welcome! This is a fully functional To-Do List application I built from scratch to practice and showcase my backend development skills with Python and Django.

## 🚀 Live Demo

This application is fully deployed and accessible online. You can test it here:
**[https://amirhosseinkarimi.pythonanywhere.com/](https://amirhosseinkarimi.pythonanywhere.com/)**

---

### About This Project

I built this project as a core piece of my portfolio to master the fundamentals of web development. The goal was to go beyond a simple script and create a real, multi-user web application with a secure authentication system, a database, a clean, interactive frontend, and deploy it to a live server.

---

### What Can It Do? ✨

* **Secure User Accounts:** Users can register for a new account and log in securely. The app keeps every user's task list completely private.
* **Full Task Management (CRUD):** You can easily **C**reate new tasks, **R**ead your list, **U**pdate tasks (e.g., mark them as complete or edit the title), and **D**elete them.
* **Clean, Modern & Responsive UI:** The interface is styled with Bootstrap 5 and `django-crispy-forms` to be user-friendly and responsive on any device.
* **User Feedback System:** The app provides clear error and success messages using Django's messaging framework.

---

### My Tech Stack 💻

* **Backend:** Python, Django
* **Frontend:** HTML, CSS, Bootstrap 5
* **Forms:** `django-crispy-forms`
* **Database:** SQLite3
* **Deployment:** PythonAnywhere
* **Version Control:** Git & GitHub

---

### How to Run This Project Locally

1.  **Clone the repository:**
    ```sh
    git clone [https://github.com/karimi-amirhossein/To-do-List-Django.git](https://github.com/karimi-amirhossein/To-do-List-Django.git)
    cd To-do-List-Django
    ```
2.  **Set up your environment:**
    ```sh
    # Create and activate a virtual environment
    python -m venv venv
    .\venv\Scripts\activate

    # Install all the necessary packages
    pip install -r requirements.txt
    ```
3.  **Prepare the database and run:**
    ```sh
    # Apply database migrations
    python manage.py migrate

    # Start the server!
    python manage.py runserver
    ```
    The app will be running at `http://127.0.0.1:8000/`.

---

### What's Next?

I'm proud of how this project turned out, but I'm always thinking about what's next. Some ideas for future improvements include:
* Adding a search/filter functionality for tasks.
* Implementing due dates and priority levels for tasks.
* Using AJAX to update tasks without a full page reload.

Thanks for checking out my project!