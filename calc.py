import tkinter as tk
from tkinter import *

def on_click(button_value):
    current = entry_var.get()

    if button_value == "=":
        try:
            result = str(eval(current))
            entry_var.set(result)
        except Exception as e:
            entry_var.set("Error")
    elif button_value == "C":
        entry_var.set("")
    elif button_value == "x²":
        entry_var.set(str(float(current) ** 2))
    elif button_value == "√":
        entry_var.set(str(float(current) ** 0.5))
    else:
        entry_var.set(current + button_value)

def key_press(event):
    key = event.char
    if key.isdigit() or key in "+-*/.":
        on_click(key)
    elif key == '\r':  # Check for Enter key
        on_click("=")

window = Tk()
window.title("Calculator")
window.geometry("400x600")

# Create an entry widget for the calculator screen
entry_var = StringVar()
entry = Entry(window, textvariable=entry_var, justify="right", font=("Arial", 24), bd=10, relief=tk.GROOVE)
entry.grid(row=0, column=0, columnspan=4, pady=10, sticky="nsew")

# Create a label for the calculator screen
screen_label = Label(window, text="Calculator", font=("Arial", 32, "bold"))
screen_label.grid(row=1, column=0, columnspan=4, pady=20, sticky="nsew")

button1 = Button(text="C", height=3, width=7, font=("Arial", 16, "bold"), command=lambda: on_click("C"))
button2 = Button(text="x²", height=3, width=7, font=("Arial", 16, "bold"), command=lambda: on_click("x²"))
button3 = Button(text="√", height=3, width=7, font=("Arial", 16, "bold"), command=lambda: on_click("√"))
button4 = Button(text="/", height=3, width=7, font=("Arial", 16, "bold"), command=lambda: on_click("/"))

button5 = Button(text="7", height=3, width=7, font=("Arial", 16, "bold"), command=lambda: on_click("7"))
button6 = Button(text="8", height=3, width=7, font=("Arial", 16, "bold"), command=lambda: on_click("8"))
button7 = Button(text="9", height=3, width=7, font=("Arial", 16, "bold"), command=lambda: on_click("9"))
button8 = Button(text="*", height=3, width=7, font=("Arial", 16, "bold"), command=lambda: on_click("*"))

button9 = Button(text="4", height=3, width=7, font=("Arial", 16, "bold"), command=lambda: on_click("4"))
button10 = Button(text="5", height=3, width=7, font=("Arial", 16, "bold"), command=lambda: on_click("5"))
button11 = Button(text="6", height=3, width=7, font=("Arial", 16, "bold"), command=lambda: on_click("6"))
button12 = Button(text="-", height=3, width=7, font=("Arial", 16, "bold"), command=lambda: on_click("-"))

button13 = Button(text="1", height=3, width=7, font=("Arial", 16, "bold"), command=lambda: on_click("1"))
button14 = Button(text="2", height=3, width=7, font=("Arial", 16, "bold"), command=lambda: on_click("2"))
button15 = Button(text="3", height=3, width=7, font=("Arial", 16, "bold"), command=lambda: on_click("3"))
button16 = Button(text="+", height=3, width=7, font=("Arial", 16, "bold"), command=lambda: on_click("+"))

button17 = Button(text="0", height=3, width=7, font=("Arial", 16, "bold"), command=lambda: on_click("0"))
button18 = Button(text=".", height=3, width=7, font=("Arial", 16, "bold"), command=lambda: on_click("."))
button19 = Button(text="=", height=3, width=7, font=("Arial", 16, "bold"), command=lambda: on_click("="))

# Grid buttons and entry
button1.grid(row=2, column=0, pady=5, padx=5, sticky="nsew")
button2.grid(row=2, column=1, pady=5, padx=5, sticky="nsew")
button3.grid(row=2, column=2, pady=5, padx=5, sticky="nsew")
button4.grid(row=2, column=3, pady=5, padx=5, sticky="nsew")

button5.grid(row=3, column=0, pady=5, padx=5, sticky="nsew")
button6.grid(row=3, column=1, pady=5, padx=5, sticky="nsew")
button7.grid(row=3, column=2, pady=5, padx=5, sticky="nsew")
button8.grid(row=3, column=3, pady=5, padx=5, sticky="nsew")

button9.grid(row=4, column=0, pady=5, padx=5, sticky="nsew")
button10.grid(row=4, column=1, pady=5, padx=5, sticky="nsew")
button11.grid(row=4, column=2, pady=5, padx=5, sticky="nsew")
button12.grid(row=4, column=3, pady=5, padx=5, sticky="nsew")

button13.grid(row=5, column=0, pady=5, padx=5, sticky="nsew")
button14.grid(row=5, column=1, pady=5, padx=5, sticky="nsew")
button15.grid(row=5, column=2, pady=5, padx=5, sticky="nsew")
button16.grid(row=5, column=3, pady=5, padx=5, sticky="nsew")

button17.grid(row=6, column=1, pady=5, padx=5, sticky="nsew")
button18.grid(row=6, column=2, pady=5, padx=5, sticky="nsew")
button19.grid(row=6, column=3, pady=5, padx=5, sticky="nsew")

# Make rows and columns expandable
for i in range(7):
    window.grid_rowconfigure(i, weight=1)
    window.grid_columnconfigure(i, weight=1)

# Bind keyboard events
window.bind('<Key>', key_press)

window.mainloop()
