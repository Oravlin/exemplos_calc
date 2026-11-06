import tkinter as tk

janela = tk.Tk()
janela.title("Teclado Calculadora")

botao_7 = tk.Button(janela, text='7', width=6)
botao_7.grid(row=0, column=0)

botao_8 = tk.Button(janela, text='8', width=6)
botao_8.grid(row=0, column=1)

botao_9 = tk.Button(janela, text='9', width=6)
botao_9.grid(row=0, column=2)

janela.mainloop()