import tkinter as tk
from tkinter import ttk

janela = tk.Tk()
janela.title("Financiamento de imóveis")
janela.geometry("400x200") # Largura x altura em pixels

label = ttk.Label(janela, text="Login", font=("Arial", 20) )
label.pack(pady=20, padx=20)
texto = tk.Entry(janela, width=20)
texto.pack(pady=20)

janela.mainloop()
