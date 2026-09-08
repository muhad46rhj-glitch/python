import tkinter as tk

window = tk.Tk()
window.title("ATM PIN Setup")
window.geometry("420x500")
window.configure(bg="white")

# Heading
heading = tk.Label(
    window,
    text="ATM PIN SETUP",
    font=("Arial", 22, "bold"),
    bg="navy",
    fg="white",
    width=25
)
heading.pack(pady=15)

# Account information
account_frame = tk.Frame(window, bg="white")
account_frame.pack()

tk.Label(
    account_frame,
    text="Customer Name:",
    bg="white"
).grid(row=0, column=0, padx=5, pady=8)

name = tk.Entry(account_frame, width=25)
name.grid(row=0, column=1)

tk.Label(
    account_frame,
    text="Account Number:",
    bg="white"
).grid(row=1, column=0, padx=5, pady=8)

account = tk.Entry(account_frame, width=25)
account.grid(row=1, column=1)

# PIN
tk.Label(
    window,
    text="Enter PIN",
    font=("Arial", 12, "bold"),
    bg="white"
).pack(pady=10)

pin = tk.Entry(
    window,
    width=15,
    show="*",
    justify="center",
    font=("Arial", 16)
)
pin.pack()

# Functions
def number(n):
    pin.insert(tk.END, n)

def remove():
    pin.delete(0, tk.END)

def save():
    result.delete("1.0", tk.END)

    result.insert(
        tk.END,
        "ACCOUNT DETAILS\n"
        "----------------------\n"
        "Name: " + name.get() + "\n"
        "Account: " + account.get() + "\n"
        "PIN: " + "*" * len(pin.get())
    )

# Keypad
keypad = tk.Frame(
    window,
    bg="gray",
    padx=8,
    pady=8
)
keypad.pack(pady=15)

keys = [
    "1", "2", "3",
    "4", "5", "6",
    "7", "8", "9",
    "Clear", "0", "Save"
]

for i, key in enumerate(keys):
    row = i // 3
    column = i % 3

    if key == "Clear":
        action = remove
    elif key == "Save":
        action = save
    else:
        action = lambda x=key: number(x)

    tk.Button(
        keypad,
        text=key,
        width=8,
        height=2,
        command=action
    ).grid(
        row=row,
        column=column,
        padx=3,
        pady=3
    )

# Output
result = tk.Text(
    window,
    width=40,
    height=6
)
result.pack(pady=10)

window.mainloop()
