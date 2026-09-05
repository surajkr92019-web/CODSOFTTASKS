import tkinter as tk


# -----------------------------
# Create main window
# -----------------------------
window = tk.Tk()
window.title("Calculator")
window.geometry("360x520")
window.resizable(False, False)
window.configure(bg="#202020")


# -----------------------------
# Display
# -----------------------------
display = tk.Entry(
    window,
    font=("Arial", 30),
    justify="right",
    bg="#111111",
    fg="white",
    insertbackground="white",
    bd=0
)

display.pack(
    padx=15,
    pady=20,
    ipady=15,
    fill="x"
)


# -----------------------------
# Functions
# -----------------------------

def press(value):
    """Add a number or operator to the display."""

    current = display.get()

    # If display contains Error, start again
    if current == "Error":
        display.delete(0, tk.END)

    display.insert(tk.END, value)


def clear():
    """Clear the calculator."""

    display.delete(0, tk.END)


def delete():
    """Delete the last character."""

    current = display.get()

    display.delete(0, tk.END)
    display.insert(0, current[:-1])


def calculate():
    """Calculate the expression."""

    try:
        expression = display.get()

        # Convert percentage
        expression = expression.replace("%", "/100")

        # Calculate result
        result = eval(expression)

        # Remove unnecessary .0
        if isinstance(result, float) and result.is_integer():
            result = int(result)

        display.delete(0, tk.END)
        display.insert(0, str(result))

    except ZeroDivisionError:
        display.delete(0, tk.END)
        display.insert(0, "Cannot divide by 0")

    except:
        display.delete(0, tk.END)
        display.insert(0, "Error")


# -----------------------------
# Button Frame
# -----------------------------

button_frame = tk.Frame(
    window,
    bg="#202020"
)

button_frame.pack(
    padx=10,
    pady=5,
    fill="both",
    expand=True
)


# -----------------------------
# Button settings
# -----------------------------

buttons = [
    ("C", 0, 0, "#e74c3c"),
    ("⌫", 0, 1, "#555555"),
    ("%", 0, 2, "#555555"),
    ("÷", 0, 3, "#ff9500"),

    ("7", 1, 0, "#444444"),
    ("8", 1, 1, "#444444"),
    ("9", 1, 2, "#444444"),
    ("×", 1, 3, "#ff9500"),

    ("4", 2, 0, "#444444"),
    ("5", 2, 1, "#444444"),
    ("6", 2, 2, "#444444"),
    ("−", 2, 3, "#ff9500"),

    ("1", 3, 0, "#444444"),
    ("2", 3, 1, "#444444"),
    ("3", 3, 2, "#444444"),
    ("+", 3, 3, "#ff9500"),

    ("0", 4, 0, "#444444"),
    (".", 4, 1, "#444444"),
    ("=", 4, 2, "#27ae60"),
]


# -----------------------------
# Create buttons
# -----------------------------

for text, row, column, color in buttons:

    # Special buttons
    if text == "C":
        command = clear

    elif text == "⌫":
        command = delete

    elif text == "=":
        command = calculate

    else:
        # Convert display symbols to Python operators
        value = text

        if value == "÷":
            value = "/"

        elif value == "×":
            value = "*"

        elif value == "−":
            value = "-"

        command = lambda v=value: press(v)

    button = tk.Button(
        button_frame,
        text=text,
        command=command,
        font=("Arial", 20),
        bg=color,
        fg="white",
        activebackground="#777777",
        activeforeground="white",
        bd=0,
        relief="flat"
    )

    button.grid(
        row=row,
        column=column,
        padx=5,
        pady=5,
        sticky="nsew"
    )


# -----------------------------
# Make buttons resize properly
# -----------------------------

for i in range(4):
    button_frame.columnconfigure(i, weight=1)

for i in range(5):
    button_frame.rowconfigure(i, weight=1)


# -----------------------------
# Keyboard support
# -----------------------------

def keyboard_input(event):

    key = event.keysym
    char = event.char

    if char in "0123456789.+-*/%":
        press(char)

    elif key == "Return":
        calculate()

    elif key == "BackSpace":
        delete()

    elif key == "Escape":
        clear()


window.bind("<Key>", keyboard_input)


# -----------------------------
# Start calculator
# -----------------------------

window.mainloop()
