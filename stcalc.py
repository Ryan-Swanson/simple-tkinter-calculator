import tkinter as tk
import math

class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Advanced Calculator")
        self.create_widgets()
        self.center_window()

    def create_widgets(self):
        container = tk.Frame(self)
        container.pack(expand=True, fill=tk.BOTH)

        self.result_var = tk.StringVar()

        # Entry widget to display the result
        result_entry = tk.Entry(container, textvariable=self.result_var, font=("Arial", 24), justify="right", bd=30, bg="light blue")
        result_entry.grid(row=0, column=0, columnspan=5, sticky="nsew")

        # Buttons
        buttons = [
            ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3), ("sqrt", 1, 4),
            ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3), ("^", 2, 4),
            ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3), ("(", 3, 4),
            ("0", 4, 0), (".", 4, 1), ("+", 4, 2), ("=", 4, 3), (")", 4, 4),
            ("C", 5, 0), ("sin", 5, 1), ("cos", 5, 2), ("tan", 5, 3), ("log", 5, 4),
        ]

        for (text, row, col) in buttons:
            button = tk.Button(container, text=text, font=("Arial", 18), command=lambda t=text: self.on_button_click(t))
            button.grid(row=row, column=col, sticky="nsew")

        for i in range(6):
            container.grid_rowconfigure(i, weight=1)
            container.grid_columnconfigure(i, weight=1)

    def on_button_click(self, text):
        if text == "=":
            try:
                expression = self.result_var.get()
                result = self.evaluate_expression(expression)
                self.result_var.set(result)
            except Exception as e:
                self.result_var.set("Error")
        elif text == "C":
            self.result_var.set("")
        else:
            current_text = self.result_var.get()
            self.result_var.set(current_text + text)

    def evaluate_expression(self, expression):
        # Replace symbols for math functions
        expression = expression.replace("sqrt", "math.sqrt")
        expression = expression.replace("^", "**")
        expression = expression.replace("sin", "math.sin")
        expression = expression.replace("cos", "math.cos")
        expression = expression.replace("tan", "math.tan")
        expression = expression.replace("log", "math.log")

        # Evaluate the expression
        result = eval(expression)
        return result

    def center_window(self):
        self.update_idletasks()
        width = self.winfo_width()
        height = self.winfo_height()
        x_offset = (self.winfo_screenwidth() // 2) - (width // 2)
        y_offset = (self.winfo_screenheight() // 2) - (height // 2)
        self.geometry(f"{width}x{height}+{x_offset}+{y_offset}")

if __name__ == "__main__":
    app = Calculator()
    app.mainloop()
