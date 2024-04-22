import tkinter as tk

def button_click(symbol):
    current = display_var.get()
    if current == "Error":
        current = ""
    if symbol == "C":
        display_var.set("")
    elif symbol == "=":
        try:
            result = str(eval(current))
            display_var.set(result)
        except:
            display_var.set("Error")
    else:
        display_var.set(current + symbol)


root = tk.Tk()
root.title("Calculator")

display_var = tk.StringVar()

display = tk.Entry(root, textvariable=display_var, font=('Arial', 20), justify='right')
display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('C', 4, 1), ('=', 4, 2), ('+', 4, 3)
]

for (text, row, col) in buttons:
    button = tk.Button(root, text=text, font=('Arial', 16), width=5, height=2, command=lambda t=text: button_click(t))
    button.grid(row=row, column=col, padx=5, pady=5)

root.mainloop()