import tkinter as tk
from tkinter import messagebox

TASKS_FILE = "tasks.txt"

def load_tasks():
    try:
        with open(TASKS_FILE, "r") as file:
            tasks = file.readlines()
            for task in tasks:
                task_listbox.insert(tk.END, task.strip())
    except FileNotFoundError:
        open(TASKS_FILE, "w").close()  # Create file if it doesn't exist

def save_tasks():
    tasks = task_listbox.get(0, tk.END)
    with open(TASKS_FILE, "w") as file:
        for task in tasks:
            file.write(task + "\n")

def add_task():
    task = task_entry.get()
    if task:
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
        save_tasks()
    else:
        messagebox.showwarning("Warning", "Task cannot be empty!")

def delete_task():
    try:
        selected_task_index = task_listbox.curselection()[0]
        task_listbox.delete(selected_task_index)
        save_tasks()
    except IndexError:
        messagebox.showwarning("Warning", "No task selected!")

# Create the main window
root = tk.Tk()
root.title("To-Do List App Made by Jabbar Jatoi 📝")
root.geometry("400x400")
root.config(bg="#f0f0f0")

# Task Entry Frame
frame = tk.Frame(root, bg="#f0f0f0")
frame.pack(pady=10)

task_entry = tk.Entry(frame, width=30, font=("Arial", 12))
task_entry.grid(row=0, column=0, padx=5)

add_button = tk.Button(frame, text="Add Task", command=add_task, bg="#4CAF50", fg="white", font=("Arial", 10))
add_button.grid(row=0, column=1, padx=5)

# Task Listbox
task_listbox = tk.Listbox(root, width=40, height=15, font=("Arial", 12), selectbackground="#a6a6a6")
task_listbox.pack(pady=10)

# Delete Button
delete_button = tk.Button(root, text="Delete Task", command=delete_task, bg="#FF4C4C", fg="white", font=("Arial", 10))
delete_button.pack(pady=5)

# Load tasks from file when the app starts
load_tasks()

# Run the application
root.mainloop()
