import tkinter as tk
root = tk.Tk()
root.title("Python Calculator")
root.geometry("360x520")
root.config(bg="#1f1f2e")
root.resizable(False, False)
expression = ""
def press(key):
    global expression
    if key == "=":
        try:
            result = str(eval(expression))
            equation.set(result)
            expression = result
        except:
            equation.set("Error")
            expression = ""
    elif key == "C":
        expression = ""
        equation.set("")
    else:
        expression += str(key)
        equation.set(expression)
equation = tk.StringVar()
input_field = tk.Entry(root, textvariable=equation, font=("Arial", 24), bd=10,
                       insertwidth=2, width=18, borderwidth=4,
                       bg="#ffffff", fg="#000000", justify='right')
input_field.grid(row=0, column=0, columnspan=4, pady=20, padx=10)
buttons = [
    ['C', '%', '/', '*'],
    ['7', '8', '9', '-'],
    ['4', '5', '6', '+'],
    ['1', '2', '3', '='],
    ['0', '.', '', '']
]
for r, row in enumerate(buttons, 1):
    for c, char in enumerate(row):
        if char != '':
            tk.Button(root, text=char, font=("Arial", 18), padx=10, pady=10,
                      width=4, bg="#33334d", fg="#ffffff", activebackground="#4d4d66",
                      command=lambda ch=char: press(ch)).grid(row=r, column=c, padx=5, pady=5)

root.mainloop()
