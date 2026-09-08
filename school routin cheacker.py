import tkinter as tk

root = tk.Tk()
root.title("After School Routine")
root.geometry("450x350")
root.configure(bg="lightblue")

tasks = ["Homework", "Snack", "Exercise", "Read a book", "Prepare school bag"]
index = 0

def typed(event):
    if event.char:
        typed_label.config(text="Last character: " + event.char)

def area_click(event):
    click_label.config(text="Routine area clicked!")

def check_task():
    global index

    task = entry.get().strip()

    if task == "":
        warning.config(text="Please enter a task!", fg="red")
    else:
        warning.config(text="Task accepted!", fg="green")
        next_task.config(text="Next task: " + tasks[index])
        index = (index + 1) % len(tasks)

title = tk.Label(
    root,
    text="After-School Routine Checker",
    font=("Arial", 20, "bold"),
    bg="lightblue"
)
title.pack(pady=15)

entry = tk.Entry(root, width=30, font=("Arial", 13))
entry.pack(pady=10)

typed_label = tk.Label(
    root,
    text="Last character: None",
    bg="lightblue"
)
typed_label.pack()

routine = tk.Label(
    root,
    text="CLICK HERE FOR ROUTINE",
    width=30,
    height=3,
    bg="orange",
    relief="raised"
)
routine.pack(pady=15)

routine.bind("<Button-1>", area_click)

click_label = tk.Label(root, text="", bg="lightblue")
click_label.pack()

button = tk.Button(
    root,
    text="Check Task",
    command=check_task,
    bg="green",
    fg="white"
)
button.pack(pady=10)

warning = tk.Label(root, text="", bg="lightblue")
warning.pack()

next_task = tk.Label(
    root,
    text="Next task: Homework",
    font=("Arial", 12, "bold"),
    bg="lightblue"
)
next_task.pack(pady=15)

root.bind("<Key>", typed)

root.mainloop()
