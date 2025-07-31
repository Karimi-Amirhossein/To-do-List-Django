# My Django To-Do App

Welcome! This is a fully functional To-Do List application I built from scratch to practice and showcase my backend development skills with Python and Django.


---

### About This Project

I built this project as a core piece of my portfolio to master the fundamentals of web development. The goal was to go beyond a simple script and create a real, multi-user web application with a secure authentication system, a database, and a clean, interactive frontend. It was a fantastic learning experience where I tackled everything from database design to user interface styling.

---

### What Can It Do? 🚀

This isn't just a simple checklist. Here are the key features I implemented:

* **Secure User Accounts:** Users can register for a new account and log in securely. The app keeps every user's task list completely private.
* **Full Task Management (CRUD):** You can easily **C**reate new tasks, **R**ead your list, **U**pdate tasks (e.g., mark them as complete or edit the title), and **D**elete them.
* **Clean, Modern UI:** The interface is styled with Bootstrap 5 to be responsive and easy to use on any device.
* **User-Specific Experience:** The app greets you by name and always knows which tasks belong to you.

---

### My Tech Stack 💻

* **Backend:** Python, Django
* **Frontend:** HTML, CSS, Bootstrap 5
* **Database:** SQLite3
* **Version Control:** Git & GitHub

---

### How to Run This Project Locally

Interested in running the app on your own machine? Here’s how:

1.  **Clone the repository:**
    ```sh
    git clone [https://github.com/Amir_Karimi2002/django-todo-app.git](https://github.com/Amir_Karimi2002/django-todo-app.git)
    cd django-todo-app
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
* Deploying the application to a live server.
* Adding a search/filter functionality for tasks.
* Implementing email notifications for task due dates.

Thanks for checking out my project!