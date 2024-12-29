import tkinter as tk
from tkinter import ttk
from forex_python.converter import CurrencyRates, CurrencyCodes
from googletrans import Translator

class CurrencyConverter(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Currency Converter with Translation")
        self.geometry("400x300")

        # Create tabs
        self.tab_control = ttk.Notebook(self)
        self.currency_tab = ttk.Frame(self.tab_control)
        self.translation_tab = ttk.Frame(self.tab_control)
        self.tab_control.add(self.currency_tab, text='Currency Converter')
        self.tab_control.add(self.translation_tab, text='Language Translator')
        self.tab_control.pack(expand=1, fill="both")

        # Currency Converter tab
        self.currency_label = tk.Label(self.currency_tab, text="Currency Converter")
        self.currency_label.pack()

        self.amount_label = tk.Label(self.currency_tab, text="Amount:")
        self.amount_label.pack()
        self.amount_entry = tk.Entry(self.currency_tab)
        self.amount_entry.pack()

        self.from_label = tk.Label(self.currency_tab, text="From:")
        self.from_label.pack()
        self.from_var = tk.StringVar()
        self.from_option = ttk.Combobox(self.currency_tab, textvariable=self.from_var)
        self.from_option['values'] = ('USD', 'EUR', 'GBP', 'INR', 'AUD')
        self.from_option.pack()

        self.to_label = tk.Label(self.currency_tab, text="To:")
        self.to_label.pack()
        self.to_var = tk.StringVar()
        self.to_option = ttk.Combobox(self.currency_tab, textvariable=self.to_var)
        self.to_option['values'] = ('USD', 'EUR', 'GBP', 'INR', 'AUD')
        self.to_option.pack()

        self.convert_button = tk.Button(self.currency_tab, text="Convert", command=self.convert_currency)
        self.convert_button.pack()

        self.result_label = tk.Label(self.currency_tab, text="Result:")
        self.result_label.pack()
        self.result_text = tk.Text(self.currency_tab, height=5)
        self.result_text.pack()

        # Language Translator tab
        self.translation_label = tk.Label(self.translation_tab, text="Language Translator")
        self.translation_label.pack()

        self.text_label = tk.Label(self.translation_tab, text="Text:")
        self.text_label.pack()
        self.text_entry = tk.Text(self.translation_tab, height=10)
        self.text_entry.pack()

        self.lang_label = tk.Label(self.translation_tab, text="Language:")
        self.lang_label.pack()
        self.lang_var = tk.StringVar()
        self.lang_option = ttk.Combobox(self.translation_tab, textvariable=self.lang_var)
        self.lang_option['values'] = ('en', 'fr', 'es', 'de', 'zh-cn')
        self.lang_option.pack()

        self.translate_button = tk.Button(self.translation_tab, text="Translate", command=self.translate_text)
        self.translate_button.pack()

        self.translated_text = tk.Text(self.translation_tab, height=10)
        self.translated_text.pack()

    def convert_currency(self):
        amount = float(self.amount_entry.get())
        from_currency = self.from_var.get()
        to_currency = self.to_var.get()
        c = CurrencyRates()
        result = c.convert(from_currency, to_currency, amount)
        self.result_text.delete(1.0, tk.END)
        self.result_text.insert(tk.END, f"{amount} {from_currency} = {result} {to_currency}")

    def translate_text(self):
        text = self.text_entry.get("1.0", tk.END)
        lang = self.lang_var.get()
        translator = Translator()
        translation = translator.translate(text, dest=lang)
        self.translated_text.delete(1.0, tk.END)
        self.translated_text.insert(tk.END, translation.text)


if __name__ == "__main__":
    app = CurrencyConverter()
    app.mainloop()