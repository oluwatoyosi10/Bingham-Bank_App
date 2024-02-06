import tkinter as tk
from tkinter import messagebox

def add_task():
    task = entry_task.get()
    if task:
        listbox_tasks.insert(tk.END, task)
        entry_task.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Please enter a task.")

def remove_task():
    try:
        selected_task_index = listbox_tasks.curselection()[0]
        listbox_tasks.delete(selected_task_index)
    except IndexError:
        messagebox.showwarning("Selection Error", "Please select a task to remove.")

def clear_tasks():
    listbox_tasks.delete(0, tk.END)

def main():
    root = tk.Tk()
    root.title("To-Do List")
    root.geometry("400x300")
    root.configure(bg="light gray")

    label_title = tk.Label(root, text="To-Do List", font=("Helvetica", 20), bg="light gray")
    label_title.pack(pady=10)

    entry_task = tk.Entry(root, font=("Helvetica", 12))
    entry_task.pack(pady=10)

    button_add = tk.Button(root, text="Add Task", command=add_task, bg="green", fg="white")
    button_add.pack()

    listbox_tasks = tk.Listbox(root, font=("Helvetica", 12), selectbackground="light blue")
    listbox_tasks.pack(pady=10)

    button_remove = tk.Button(root, text="Remove Task", command=remove_task, bg="red", fg="white")
    button_remove.pack()

    button_clear = tk.Button(root, text="Clear All", command=clear_tasks, bg="orange", fg="white")
    button_clear.pack()

    root.mainloop()
