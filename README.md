# DecodeLabs-Python-Programming-Internship
# 📝 To-Do List Application

A simple **command-line To-Do List application developed using Python**. This project allows users to add tasks, view their tasks, delete tasks, and exit the application through a simple menu-driven interface.

## 🚀 Features

* ➕ Add new tasks
* 📋 View all added tasks
* 🗑️ Delete a task using its task number
* 🚪 Exit the application
* ⚠️ Displays a message for invalid choices
* 🔄 Menu repeats until the user exits

## 🛠️ Technologies Used

* **Python 3**
* Python Lists
* `while` Loop
* `if-elif-else` Statements
* `input()` and `print()`
* List methods: `append()` and `pop()`

## 📂 Project Structure

```text
To-Do-List/
│
├── todo_list.py
├── README.md
├── screenshot1.png
└── screenshot2.png
```

## ▶️ How to Run

### 1. Install Python

Make sure Python 3 is installed on your computer.

### 2. Clone the Repository

```bash
git clone <your-github-repository-link>
```

### 3. Open the Project Folder

```bash
cd To-Do-List
```

### 4. Run the Program

```bash
python todo_list.py
```

## 💻 How the Program Works

When the program starts, it displays the following menu:

```text
========== TO-DO LIST ==========
1. Python
2. SQL
3. Tableau
4. Power BI
```

The user can enter a choice to perform different operations.

### 1️⃣ Add Task

Select **option 1** and enter the task you want to add.

Example:

```text
Enter your choice: 1
Enter your task: SQL
Task Added Successfully!
```

The task is stored in a Python list using the `append()` method.

### 2️⃣ View Tasks

Select **option 2** to view all currently added tasks.

Example:

```text
Your Tasks:
1. SQL
2. Python
3. Power BI
```

If no tasks are available, the program displays:

```text
No tasks available.
```

The program uses a `for` loop to display the tasks with their numbers.

### 3️⃣ Delete Task

Select **option 3** to delete a task.

The program first displays the available tasks and asks for the task number.

Example:

```text
Enter task number to delete: 2
Python deleted successfully!
```

The selected task is removed using the `pop()` method.

### 4️⃣ Exit

Select **option 4** to exit the application.

```text
Thank You!
```

The program uses the `break` statement to stop the loop and end the application.

## 🔄 Program Flow

```text
        START
          ↓
   Display Main Menu
          ↓
     Enter Choice
          ↓
   ┌──────┼───────┬────────┐
   ↓      ↓       ↓        ↓
 Add    View    Delete    Exit
 Task   Tasks    Task      ↓
   ↓      ↓       ↓       END
   └──────┴───────┘
          ↓
    Display Menu Again
          ↓
        Repeat
```

## 📸 Screenshots

### ➕ Adding Tasks

This screenshot shows tasks being added successfully through the Python program.

![Adding Tasks](screenshot1.png)

### 🗑️ Viewing and Deleting Tasks

This screenshot shows the list of tasks, deleting a selected task, and displaying the remaining tasks.

![Viewing and Deleting Tasks](screenshot2.png)

## 📚 Learning Outcomes

By developing this project, I learned:

* How to create a menu-driven Python program
* How to use Python lists
* How to take input from users
* How to use `while` and `for` loops
* How to use conditional statements
* How to add and remove items from a list
* How to handle invalid choices
* How to run and test a Python program using VS Code

## 🔮 Future Improvements

The application can be improved in the future by adding:

* ✅ Mark tasks as completed
* ✏️ Edit existing tasks
* 💾 Save tasks permanently
* 📅 Add deadlines
* 🏷️ Add task categories
* 🔍 Search for tasks
* 🖥️ Create a graphical user interface

## 👩‍💻 Author

**Shravani**

---


