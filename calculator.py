import tkinter as tk

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Calculator")

        # Create the input field
        self.input_field = tk.Entry(master, width=20, borderwidth=5, font=('Arial', 14))
        self.input_field.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        # Create the number buttons
        for i in range(10):
            tk.Button(master, text=str(i), width=5, height=2, font=('Arial', 14), command=lambda x=i: self.number_click(x)).grid(row=(i // 3) + 1, column=(i % 3), padx=5, pady=5)

        # Create the operation buttons
        tk.Button(master, text="+", width=5, height=2, font=('Arial', 14), command=lambda: self.operation_click('+')).grid(row=4, column=0, padx=5, pady=5)
        tk.Button(master, text="-", width=5, height=2, font=('Arial', 14), command=lambda: self.operation_click('-')).grid(row=4, column=1, padx=5, pady=5)
        tk.Button(master, text="*", width=5, height=2, font=('Arial', 14), command=lambda: self.operation_click('*')).grid(row=4, column=2, padx=5, pady=5)
        tk.Button(master, text="/", width=5, height=2, font=('Arial', 14), command=lambda: self.operation_click('/')).grid(row=5, column=0, padx=5, pady=5)
        tk.Button(master, text="C", width=5, height=2, font=('Arial', 14), command=self.clear_click).grid(row=5, column=1, padx=5, pady=5)
        tk.Button(master, text="=", width=5, height=2, font=('Arial', 14), command=self.equals_click).grid(row=5, column=2, padx=5, pady=5)

        # Set initial state
        self.current_value = 0
        self.operation = None
        self.result = None
        self.reset_input_field = False

    def number_click(self, number):
        if self.reset_input_field:
            self.reset_input_field = False
            self.input_field.delete(0, tk.END)
        self.input_field.insert(tk.END, number)

    def operation_click(self, operation):
        self.current_value = int(self.input_field.get())
        self.operation = operation
        self.reset_input_field = True

    def clear_click(self):
        self.input_field.delete(0, tk.END)
        self.current_value = 0
        self.operation = None
        self.result = None

    def equals_click(self):
        if self.operation is None or self.reset_input_field:
            return

        if self.operation == '+':
            self.result = self.current_value + int(self.input_field.get())
        elif self.operation == '-':
            self.result = self.current_value - int(self.input_field.get())
        elif self.operation == '*':
            self.result = self.current_value * int(self.input_field.get())
        elif self.operation == '/':
            self.result = self.current_value / int(self.input_field.get())

        self.input_field.delete(0, tk.END)
        self.input_field.insert(0, str(self.result))
        self.operation = None
        self.reset_input_field = True