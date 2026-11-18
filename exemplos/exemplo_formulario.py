import tkinter as tk
from tkinter import messagebox

janela = tk.Tk()
janela.title("Cadastro de Clientes")
janela.geometry("500x350")

clientes = []
# nome
tk.Label(janela, text="Nome:").grid(row=1, column=0, padx=10, pady=5)

ent_nome = tk.Entry(janela, width=40)
ent_nome.grid(row=1, column=1, padx=10, pady=5)
# cpf
tk.Label(janela, text="CPF:").grid(row=2, column=0, padx=10, pady=5)

ent_cpf = tk.Entry(janela, width=40)

ent_cpf.grid(row=2, column=1, padx=10, pady=5)
# telefone
tk.Label(janela, text="Telefone:").grid(row=3, column=0, padx=10, pady=5)

ent_telefone = tk.Entry(janela, width=40)

ent_telefone.grid(row=3, column=1, padx=10, pady=5)
# email
tk.Label(janela, text="E-Mail:").grid(row=4, column=0, padx=10, pady=5)

ent_email = tk.Entry(janela, width=40)

ent_email.grid(row=4, column=1, padx=10, pady=5)
# cidade
tk.Label(janela, text="Cidade:").grid(row=5, column=0, padx=10, pady=5)

ent_cidade = tk.Entry(janela, width=40)

ent_cidade.grid(row=5, column=1, padx=10, pady=5)

#funções dos botões
def salvar():
    nome = ent_nome.get()
    cpf = ent_cpf.get()
    telefone = ent_telefone.get()
    email = ent_email.get()
    cidade = ent_cidade.get()

    if nome == "":
        messagebox.showwarning("Atenção", "Informe o nome do cliente!")
        return
    if cpf == "":
        messagebox.showwarning("Atenção", "Informe o CPF do cliente!")
        return
    if telefone == "":
        messagebox.showwarning("Atenção", "Informe o telefone do cliente!")
        return
    if email == "":
        messagebox.showwarning("Atenção", "Informe o email do cliente!")
        return
    if cidade == "":
        messagebox.showwarning("Atenção", "Informe a cidade do cliente!")
        return

    cliente = {
        "nome": nome,
        "cpf": cpf,
        "telefone": telefone,
        "email": email,
        "cidade": cidade
    }

    messagebox.showinfo(
        "Sucesso",
        "Cliente cadastrado com sucesso!"
    )

def limpar():
    ent_nome.delete(0, tk.END)
    ent_email.delete(0, tk.END)
    ent_telefone.delete(0, tk.END)
    ent_cidade.delete(0, tk.END)
    ent_cpf.delete(0, tk.END)
    
    ent_nome.focus()


# botões
btn_salvar = tk.Button(
    janela,
    text="Salvar",
    command=salvar
)

btn_salvar.grid(
    row=6,
    column=1,
    pady=20
)

btn_limpar = tk.Button(
    janela,
    text="Limpar",
    command=limpar
)

btn_limpar.grid(
    row=6,
    column=2,
    pady=20
)

janela.mainloop()
