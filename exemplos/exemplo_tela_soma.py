import tkinter as tk
def somar():
    n1 = float(entrada1.get())
    n2 = float(entrada2.get())
    
    resultado = n1 + n2
    
    lbl_resultado.config(text=f"Resultado: {resultado}")
    
# cria a janela
janela = tk.Tk()
janela.title("calculadora")
janela.geometry("350x250")

# cria texto e entrada do n1
lbl_numero1 = tk.Label(janela, text="Primeiro número:")
lbl_numero1.pack()

entrada1 = tk.Entry(janela)
entrada1.pack()

#cria texto e entrada do n2
lbl_numero1 = tk.Label(janela, text="Segundo número:")
lbl_numero1.pack()

entrada2 = tk.Entry(janela)
entrada2.pack()

# criando botão de soma
botao_somar = tk.Button(
    janela,
    text="Somar",
    command=somar
)
botao_somar.pack(pady=15) #adiciona espaço vertical, o padding.

lbl_resultado = tk.Label(janela, text="Resultado:")
lbl_resultado.pack()

janela.mainloop()