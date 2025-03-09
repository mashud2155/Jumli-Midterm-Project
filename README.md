📝 Task Manager

A simple Django-based Task Manager application that allows users to create, view, and manage tasks. Each task has a title, description, due date, and status.

📌 Features

- ✅ Create new tasks
- 📋 View a list of tasks
- ✏️ Edit existing tasks
- ⏳ Automatically mark tasks as overdue if the due date has passed

📊 Models

🗂️ Task Model

The `Task` model represents a task with the following fields:

- `title`: The title of the task *(CharField)*
- `description`: A detailed description of the task *(TextField)*
- `due_date`: The due date for the task *(DateField, nullable and blank)*
- `status`: The status of the task *(CharField, default: 'pending')*

#### Key Methods:

- `__str__`: Returns the title of the task
- `save`: Custom save method with additional behavior
- `check_and_update_overdue_status`: Checks if the task is overdue and updates the status

## 📄 Forms

The task creation and editing forms are built using Django forms and rendered through the `task_form.html` template.

## 🎨 Templates

### `task_form.html`

This template is responsible for rendering the form to create and edit tasks. It uses **Bootstrap** for styling to provide a clean and responsive layout.

## 🚀 Getting Started

Follow these steps to set up and run the Task Manager locally:

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/task_manager.git
cd task_manager
```

### 2. Set Up a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Apply Migrations

```bash
python manage.py migrate
```

### 5. Run the Development Server

```bash
python manage.py runserver
```

### 6. Access the Application

Open your browser and navigate to: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

 📘 Usage

- Add Task: Click the "Add Task" button and fill out the form.
- View Tasks: Browse the task list page to see all tasks.
- Edit Task: Click on a task title to update its details.
- Overdue Tasks: Tasks will automatically be marked as overdue if the due date has passed.

## 📜 License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for more information.

---

💡 *Contributions are welcome! Feel free to open issues and submit pull requests.*

