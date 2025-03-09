# 📝 Task Manager

A simple Django-based Task Manager application that allows users to create, view, and manage tasks. Each task has a title, description, due date, and status.

## 📌 Features

- ✅ Create new tasks
- 📋 View a list of tasks
- ✏️ Edit existing tasks
- ⏳ Automatically mark tasks as overdue if the due date has passed

## 📊 Models

### 🗂️ Task Model

The `Task` model represents a task with the following fields:

- `title`: The title of the task (CharField)
- `description`: A detailed description of the task (TextField)
- `due_date`: The due date for the task (DateField, nullable and blank)
- `status`: The status of the task (CharField, default: 'pending')

## 📄 Forms

The task creation and editing forms are built using Django forms and rendered through the `task_form.html` template.

## 🎨 Templates

### `task_form.html`

This template is responsible for rendering the form to create and edit tasks. It uses **Bootstrap** for styling to provide a clean and responsive layout.

## 🚀 Getting Started

Follow these steps to set up and run the Task Manager locally:

### 1. Set Up a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 2. Apply Migrations

```bash
python manage.py migrate
```

### 3. Run the Development Server

```bash
python manage.py runserver
```

### 4. Access the Application

Open your browser and navigate to: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

## 📘 Usage

- Add Task: Click the "Add Task" button and fill out the form.
- View Tasks: Browse the task list page to see all tasks.
- Edit Task: Click on a task title to update its details.
- Overdue Tasks: Tasks will automatically be marked as overdue if the due date has passed.

Prerequisites

Ensure you have the following installed:

XAMPP (for database)

Python (for running Django)

Visual Studio Code (code editor)

## Getting Started

1. **Start XAMPP Services:**
    - Open the XAMPP Control Panel.
    - Click*Start on both Apache and MySQL modules.

2. **Run the Application:**
    - Open Visual Studio Code (or your preferred terminal).
    - Navigate to your project directory using:
      ```bash
      cd path/to/your/project
      ```
    - Run the following command to start the development server:
      ```bash
      python manage.py runserver
      ```

3. **Access the Application:**
    - Open your browser and go to:
      ```
      http://localhost:8000
      ```
