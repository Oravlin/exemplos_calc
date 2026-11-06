import tkinter as tk

def digitar(numero:int):
    visor.insert(tk.END, str(numero))
    
def apagar():
    visor.delete(0,tk.END)
    
janela = tk.Tk()
janela.title("Primeiros botões")

visor = tk.Entry(janela, width=24, justify="right")
visor.grid(row=0, column=0, columnspan=3, padx=5, pady=5)

btn7 = tk.Button(janela, text="7", width=6, command=lambda: digitar(7))
btn7.grid(row=1, column=0, padx=2, pady=2)

btn8 = tk.Button(janela, text="8", width=6, command=lambda: digitar(8))
btn8.grid(row=1, column=1, padx=2, pady=2)

btnC = tk.Button(janela, text="C", width=6, command=apagar)
btnC.grid(row=1, column=2, padx=2, pady=2)

janela.mainloop()