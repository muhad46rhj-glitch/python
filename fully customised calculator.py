import tkinter as tk
import math

def click(value):
    entry.insert(tk.END, value)

def clear():
    entry.delete(0, tk.END)

def backspace():
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current[:-1])

def square():
    try:
        num = float(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(num ** 2))
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

def root():
    try:
        num = float(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(math.sqrt(num)))
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

def calculate():
    try:
        expression = entry.get().replace("%", "/100")
        result = eval(expression)
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

app = tk.Tk()
app.title("Advanced Calculator")
app.geometry("350x500")

entry = tk.Entry(app, font=("Arial", 20), justify="right")
entry.pack(fill="both", padx=10, pady=10)

buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "0", ".", "%", "+",
    "(", ")", "√", "x²"
]

frame = tk.Frame(app)
frame.pack()

row = 0
col = 0

for button in buttons:

    if button == "√":
        cmd = root
    elif button == "x²":
        cmd = square
    else:
        cmd = lambda b=button: click(b)

    tk.Button(
        frame,
        text=button,
        width=5,
        height=2,
        font=("Arial", 16),
        command=cmd
    ).grid(row=row, column=col)

    col += 1
    if col > 3:
        col = 0
        row += 1

tk.Button(
    app,
    text="=",
    font=("Arial", 16),
    command=calculate
).pack(fill="both", padx=10, pady=5)

tk.Button(
    app,
    text="⌫",
    font=("Arial", 16),
    command=backspace
).pack(fill="both", padx=10, pady=5)

def clear_all():
    entry.delete(0, tk.END)
history_box = tk.Listbox(app, height=8)
history_box.pack(fill="both", padx=10, pady=5)
tk.Button(app, text="C", font=("Arial", 16), command=clear).pack(fill="both", padx=10, pady=5)
def clear_entry():
    current = entry.get()
    if current:
        entry.delete(len(current)-1, tk.END)

def clear_all():
    entry.delete(0, tk.END)
def clear_all():
    entry.delete(0, tk.END)
app.mainloop()
def clear_all():
    entry.delete(0, tk.END)

def clear_entry():
    current = entry.get()
    if current:
        entry.delete(len(current)-1, tk.END)

app.configure(bg="#1e1e1e")

entry = tk.Entry(
    app,
    font=("Arial", 20),
    justify="right",
    bg="#2d2d2d",
    fg="white",
    insertbackground="red"
)
bg="#ff9500"
fg="white"
math.sqrt(25)      # 5
math.sin(math.radians(30))  # 0.5
math.cos(math.radians(60))  # 0.5
math.log10(100)    # 2
math.factorial(5)  # 120
math.pi            # 3.14159...
math.e             # 2.71828...

app.bind("<Return>", lambda event: calculate())
history = []
def calculate():
    try:
        expression = entry.get()
        result = eval(expression)

        history.append(f"{expression} = {result}")
        history_box.insert(tk.END, f"{expression} = {result}")

        entry.delete(0, tk.END)
        entry.insert(0, str(result))

    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

def clear_history():
    history.clear()
    history_box.delete(0, tk.END)

tk.Button(
    app,
    text="Clear History",
    font=("Arial", 14),
    command=clear_history
).pack(fill="both", padx=10, pady=5)
def use_history(event):
    selected = history_box.get(history_box.curselection())
    expression = selected.split("=")[0].strip()

    entry.delete(0, tk.END)
    entry.insert(0, expression)

history_box.bind("<Double-Button-1>", use_history)
result = eval(entry.get())
safe_dict = {
    "sqrt": math.sqrt,
    "sin": math.sin,
    "cos": math.cos,
    "tan": math.tan,
    "log": math.log10,
    "ln": math.log,
    "pi": math.pi,
    "e": math.e,
    "factorial": math.factorial,
}

result = eval(entry.get(), {"__builtins__": None}, safe_dict)
import matplotlib.pyplot as plt
import numpy as np
def plot_graph():
    try:
        expression = entry.get()

        x = np.linspace(-10, 10, 400)

        expression = expression.replace("^", "**")

        y = eval(
            expression,
            {
                "__builtins__": None,
                "x": x,
                "sin": np.sin,
                "cos": np.cos,
                "tan": np.tan,
                "sqrt": np.sqrt,
                "log": np.log10,
                "pi": np.pi,
                "e": np.e
            }
        )

        plt.figure(figsize=(6, 4))
        plt.plot(x, y)
        plt.grid(True)
        plt.xlabel("x")
        plt.ylabel("y")
        plt.title(f"y = {expression}")
        plt.show()

    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "Graph Error")
Add ("Graph Button")
tk.Button(
    app,
    text="Graph",
    font=("Arial", 16),
    command=plot_graph
).pack(fill="both", padx=10, pady=5)
history_box.insert(tk.END, f"(expression) = {result}")
def calculate():
    try:
        expression = entry.get()
        result = eval(expression)

        history_box.insert(
            tk.END,
            f"{expression} = {result}"
        )

        entry.delete(0, tk.END)
        entry.insert(0, str(result))

    except Exception as e:
        print(e)

history_box = tk.Listbox(frame)
history_box = tk.Listbox(app, height=8)
history_box.pack(fill="both", padx=10, pady=5)
exceptExceptionase:print(e)
history = []

history_box = tk.Listbox(app, height=8)
history_box.pack()
history.append(f"(expression) = {result}")
history_box.insert(tk.END, f"(expression) = {result}")
history_box = []
history = []
history_box = tk.Listbox(app)
import tkinter as tk 

def click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(number))

def clear():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

app = tk.Tk()
app.title("Calculator")
app.geometry("300x400")

entry = tk.Entry(app, font=("Arial", 20), justify="right")
entry.pack(fill="both", padx=10, pady=10)

buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "0", ".", "=", "+"
]

frame = tk.Frame(app)
frame.pack()

row = 0
col = 0

for button in buttons:
    if button == "=":
        cmd = calculate
    else:
        cmd = lambda b=button: click(b)

    tk.Button(
        frame,
        text=button,
        width=5,
        height=2,
        font=("Arial", 16),
        command=cmd
    ).grid(row=row, column=col)

    col += 1
    if col > 3:
        col = 0
        row += 1

tk.Button(
    app,
    text="Clear",
    font=("Arial", 16),
    command=clear
).pack(fill="both", padx=10, pady=10)

app.mainloop()



import tkinter as tk
import math

def click(value):
    entry.insert(tk.END, value)

def clear():
    entry.delete(0, tk.END)

def backspace():
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current[:-1])

def square():
    try:
        num = float(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(num ** 2))
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

def root():
    try:
        num = float(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(math.sqrt(num)))
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

def calculate():
    try:
        expression = entry.get().replace("%", "/100")
        result = eval(expression)
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

app = tk.Tk()
app.title("Advanced Calculator")
app.geometry("350x500")

entry = tk.Entry(app, font=("Arial", 20), justify="right")
entry.pack(fill="both", padx=10, pady=10)

buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "0", ".", "%", "+",
    "(", ")", "√", "x²"
]

frame = tk.Frame(app)
frame.pack()

row = 0
col = 0

for button in buttons:

    if button == "√":
        cmd = root
    elif button == "x²":
        cmd = square
    else:
        cmd = lambda b=button: click(b)

    tk.Button(
        frame,
        text=button,
        width=5,
        height=2,
        font=("Arial", 16),
        command=cmd
    ).grid(row=row, column=col)

    col += 1
    if col > 3:
        col = 0
        row += 1

tk.Button(
    app,
    text="=",
    font=("Arial", 16),
    command=calculate
).pack(fill="both", padx=10, pady=5)

tk.Button(
    app,
    text="⌫",
    font=("Arial", 16),
    command=backspace
).pack(fill="both", padx=10, pady=5)

tk.Button(
    app,
    text="Clear",
    font=("Arial", 16),
    command=clear
).pack(fill="both", padx=10, pady=5)
entry = tk.Entry(app)
entry.pack()

entry = tk.Entry(app)
entry.pack()

def clear():
    entry.delete(0, tk.END)

app.mainloop
entry = tk.Entry(app)
entry.pack()

tk.Button(
    app,
    text="Clear",
    font=("Arial", 16),
    command=clear
).pack(fill="both", padx=10, pady=10)

def clear_all():
    entry.delete(0, tk.END)

def clear_entry():
    current = entry.get()
    if current:
        entry.delete(len(current)-1, tk.END)


app.configure(bg="#1e1e1e")

entry = tk.Entry(
    app,
    font=("Arial", 20),
    justify="right",
    bg="#2d2d2d",
    fg="white",
    insertbackground="white"
)


tk.Button(
    frame,
    text=button,
    width=5,
    height=2,
    font=("Arial", 16),
    bg="#3c3f41",
    fg="white",
    activebackground="#505354",
    activeforeground="white",
    command=cmd
).grid(row=row, column=col, padx=2, pady=2)


bg="#ff9500"
fg="white"
app


import math


math.sqrt(25)      # 5
math.sin(math.radians(30))  # 0.5
math.cos(math.radians(60))  # 0.5
math.log10(100)    # 2
math.factorial(5)  # 120
math.pi            # 3.14159...
math.e             # 2.71828...

app.bind("<Return>", lambda event: calculate())


def calculate():
    try:
        expression = entry.get()
        result = eval(expression)

        history.append(f"{expression} = {result}")
        history_box.insert(tk.END, f"{expression} = {result}")

        entry.delete(0, tk.END)
        entry.insert(0, str(result))

    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")


def clear_history():
    history.clear()
    history_box.delete(0, tk.END)


tk.Button(
    app,
    text="Clear History",
    font=("Arial", 14),
    command=clear_history
).pack(fill="both", padx=10, pady=5)


def use_history(event):
    selected = history_box.get(history_box.curselection())
    expression = selected.split("=")[0].strip()

    entry.delete(0, tk.END)
    entry.insert(0, expression)


result = eval(entry.get())



safe_dict = {
    "sqrt": math.sqrt,
    "sin": math.sin,
    "cos": math.cos,
    "tan": math.tan,
    "log": math.log10,
    "ln": math.log,
    "pi": math.pi,
    "e": math.e,
    "factorial": math.factorial,
}

result = eval(entry.get(), {"__builtins__": None}, safe_dict)

import matplotlib.pyplot as plt
import numpy as np
def plot_graph():
    try:
        expression = entry.get()

        x = np.linspace(-10, 10, 400)

        expression = expression.replace("^", "**")

        y = eval(
            expression,
            {
                "__builtins__": None,
                "x": x,
                "sin": np.sin,
                "cos": np.cos,
                "tan": np.tan,
                "sqrt": np.sqrt,
                "log": np.log10,
                "pi": np.pi,
                "e": np.e
            }
        )

        plt.figure(figsize=(6, 4))
        plt.plot(x, y)
        plt.grid(True)
        plt.xlabel("x")
        plt.ylabel("y")
        plt.title(f"y = {expression}")
        plt.show()

    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "Graph Error")
tk.Button(
    app,
    text="Graph",
    font=("Arial", 16),
    command=plot_graph
).pack(fill="both", padx=10, pady=5)

y=x

history_box = tk.Listbox(app, height=8)
history_box.pack()



history_box.insert(tk.END, f"{expression} = {result}")



def calculate():
    try:
        expression = entry.get()
        result = eval(expression)

        history_box.insert(
            tk.END,
            f"{expression} = {result}"
        )

        entry.delete(0, tk.END)
        entry.insert(0, str(result))

    except Exception as e:
        print(e)

def calculate():
    try:
        expression = entry.get()
        result = eval(expression)

        history_box.insert(tk.END, f"{expression} = {result}")

        entry.delete(0, tk.END)
        entry.insert(0, str(result))

    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")
        
history_box = tk.Listbox(app, height=8)
history_box.pack(fill="both", padx=10, pady=5)

def clear():
    entry.delete(0, tk.END)
app.mainloop() 
