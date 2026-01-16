import tkinter as tk
from tkinter import ttk, messagebox
import requests

class CurrencyConverter:
    def __init__(self, root):
        self.root = root
        self.root.title("Currency Converter")
        self.root.geometry("420x300")
        self.root.resizable(False, False)

        self.currencies = ["USD", "EUR", "GBP", "JPY", "AUD", "CAD", "CHF", "INR", "AED", "PKR"]


        self.create_gui()

    def create_gui(self):
        tk.Label(self.root, text="Currency Converter", font=("Arial", 16, "bold")).pack(pady=10)

        frame = tk.Frame(self.root)
        frame.pack(pady=10)

        tk.Label(frame, text="From Currency").grid(row=0, column=0, padx=10, pady=5)
        tk.Label(frame, text="To Currency").grid(row=1, column=0, padx=10, pady=5)
        tk.Label(frame, text="Amount").grid(row=2, column=0, padx=10, pady=5)

        self.from_currency = ttk.Combobox(frame, values=self.currencies, state="readonly")
        self.from_currency.grid(row=0, column=1)
        self.from_currency.set("USD")

        self.to_currency = ttk.Combobox(frame, values=self.currencies, state="readonly")
        self.to_currency.grid(row=1, column=1)
        self.to_currency.set("EUR")

        self.amount_entry = tk.Entry(frame)
        self.amount_entry.grid(row=2, column=1)

        self.result_label = tk.Label(self.root, text="", font=("Arial", 12))
        self.result_label.pack(pady=10)

        btns = tk.Frame(self.root)
        btns.pack(pady=10)

        tk.Button(btns, text="Convert", width=12, command=self.convert).grid(row=0, column=0, padx=5)
        tk.Button(btns, text="Swap", width=12, command=self.swap).grid(row=0, column=1, padx=5)
        tk.Button(btns, text="Clear", width=12, command=self.clear).grid(row=0, column=2, padx=5)

    def convert(self):
        try:
            amount = float(self.amount_entry.get())
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number.")
            return

        base = self.from_currency.get()
        target = self.to_currency.get()

        url = f"https://open.er-api.com/v6/latest/{base}"
        response = requests.get(url)
        data = response.json()

        if data["result"] != "success":
            messagebox.showerror("Error", "Failed to fetch exchange rates.")
            return

        rate = data["rates"].get(target)
        if rate is None:
            messagebox.showerror("Error", "Currency not found.")
            return

        converted = amount * rate
        self.result_label.config(text=f"{amount} {base} = {converted:.2f} {target}")

    def swap(self):
        a = self.from_currency.get()
        b = self.to_currency.get()
        self.from_currency.set(b)
        self.to_currency.set(a)

    def clear(self):
        self.amount_entry.delete(0, tk.END)
        self.result_label.config(text="")

if __name__ == "__main__":
    root = tk.Tk()
    app = CurrencyConverter(root)
    root.mainloop()
