import tkinter as tk
from datetime import date

# Create the main window
window = tk.Tk()
window.title("Workshop Participant Greeting")
window.geometry("600x450")

# Instructions
title_label = tk.Label(
    window,
    text="Workshop Participant Greeting",
    font=("Arial", 20, "bold")
)
title_label.pack(pady=20)

instructions = tk.Label(
    window,
    text="Enter your name below and click Check In!",
    font=("Arial", 12)
)
instructions.pack(pady=10)

# Name entry
name_label = tk.Label(
    window,
    text="Participant Name:"
)
name_label.pack()

name_entry = tk.Entry(
    window,
    width=35,
    font=("Arial", 12)
)
name_entry.pack(pady=10)


# Function for the Check In button
def check_in():
    name = name_entry.get().strip()

    if name:
        workshop_date = date.today().strftime("%B %d, %Y")

        message = (
            f"Welcome, {name}!\n\n"
            f"We're glad to have you at the workshop.\n"
            f"Workshop Date: {workshop_date}\n\n"
            f"Have a great learning experience!"
        )

        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, message)
    else:
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, "Please enter your name before checking in.")


# Check In button
check_button = tk.Button(
    window,
    text="Check In",
    command=check_in,
    font=("Arial", 12, "bold"),
    bg="#4CAF50",
    fg="white"
)
check_button.pack(pady=15)

# Output Text widget
output_text = tk.Text(
    window,
    width=50,
    height=8,
    font=("Arial", 12),
    wrap=tk.WORD
)
output_text.pack(pady=10)

# Run the application
window.mainloop()
