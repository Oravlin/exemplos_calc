from tkinter import *

class Application:
    def __init__(self, master=None):
        global valorVisor
        valorVisor = ""

        global numeroAtual
        numeroAtual = ""

        padxBotoes = 2
        padyBotoes = 2
        widthBotoes = 4
        heightBotoes = 2

        self.janela = Frame(master)
        self.janela.pack() 
        
        self.visor = Entry(self.janela, width=24, justify="right")
        self.visor.grid(row=0, column=0, columnspan=4, padx=5, pady=5)


        # Botões da linha 1
        self.btnC = Button(self.janela, text="C", width=widthBotoes, height=heightBotoes, command=self.apagarTudo)
        self.btnC.grid(row=1, column=0, padx=padxBotoes, pady=padyBotoes)

        self.btnBackspace = Button(self.janela, text="⌫", width=widthBotoes, height=heightBotoes, command=self.apagarUltimo)
        self.btnBackspace.grid(row=1, column=1, padx=padxBotoes, pady=padyBotoes)
        
        self.btnDivisao = Button(self.janela, text="÷", width=widthBotoes, height=heightBotoes, command=lambda: self.inserirOperador("÷"))
        self.btnDivisao.grid(row=1, column=2, padx=padxBotoes, pady=padyBotoes)
        
        self.btnSubtracao = Button(self.janela, text="-", width=widthBotoes, height=heightBotoes, command=lambda: self.inserirOperador("-"))
        self.btnSubtracao.grid(row=1, column=3, padx=padxBotoes, pady=padyBotoes)


        # Botões da linha 2
        self.btnUm = Button(self.janela, text="1", width=widthBotoes, height=heightBotoes, command=lambda: self.digitar(1))
        self.btnUm.grid(row=2, column=0, padx=padxBotoes, pady=padyBotoes)
        
        self.btnDois = Button(self.janela, text="2", width=widthBotoes, height=heightBotoes, command=lambda: self.digitar(2))
        self.btnDois.grid(row=2, column=1, padx=padxBotoes, pady=padyBotoes)
                
        self.btnTres = Button(self.janela, text="3", width=widthBotoes, height=heightBotoes, command=lambda: self.digitar(3))
        self.btnTres.grid(row=2, column=2, padx=padxBotoes, pady=padyBotoes)
                
        self.btnMulti = Button(self.janela, text="*", width=widthBotoes, height=heightBotoes, command=lambda: self.inserirOperador("*"))
        self.btnMulti.grid(row=2, column=3, padx=padxBotoes, pady=padyBotoes)


        # Botões da linha 3
        self.btnQuatro = Button(self.janela, text="4", width=widthBotoes, height=heightBotoes, command=lambda: self.digitar(4))
        self.btnQuatro.grid(row=3, column=0, padx=padxBotoes, pady=padyBotoes)
                
        self.btnCinco = Button(self.janela, text="5", width=widthBotoes, height=heightBotoes, command=lambda: self.digitar(5))
        self.btnCinco.grid(row=3, column=1, padx=padxBotoes, pady=padyBotoes)
                        
        self.btnSeis = Button(self.janela, text="6", width=widthBotoes, height=heightBotoes, command=lambda: self.digitar(6))
        self.btnSeis.grid(row=3, column=2, padx=padxBotoes, pady=padyBotoes)
                        
        self.btnSoma = Button(self.janela, text="+", width=widthBotoes, height=heightBotoes, command=lambda: self.inserirOperador("+"))
        self.btnSoma.grid(row=3, column=3, padx=padxBotoes, pady=padyBotoes)


        # Botões da linha 4
        self.btnSete = Button(self.janela, text="7", width=widthBotoes, height=heightBotoes, command=lambda: self.digitar(7))
        self.btnSete.grid(row=4, column=0, padx=padxBotoes, pady=padyBotoes)
                
        self.btnOito = Button(self.janela, text="8", width=widthBotoes, height=heightBotoes, command=lambda: self.digitar(8))
        self.btnOito.grid(row=4, column=1, padx=padxBotoes, pady=padyBotoes)
                        
        self.btnNove = Button(self.janela, text="9", width=widthBotoes, height=heightBotoes, command=lambda: self.digitar(9))
        self.btnNove.grid(row=4, column=2, padx=padxBotoes, pady=padyBotoes)

        self.btnIgual = Button(self.janela, text="=", width=widthBotoes, height=heightBotoes * 2 + 1, command=lambda: self.calcular())
        self.btnIgual.grid(row=4, column=3, rowspan=2, padx=padxBotoes, pady=padyBotoes)

        # Botões da linha 5
        self.btnZero = Button(self.janela, text="0", width=widthBotoes * 2 + 2, height=heightBotoes, command=lambda: self.digitar(0))
        self.btnZero.grid(row=5, column=0, columnspan=2, padx=padxBotoes, pady=padyBotoes)
                
        self.btnPonto = Button(self.janela, text=".", width=widthBotoes, height=heightBotoes, command=lambda: self.inserirOperador("."))
        self.btnPonto.grid(row=5, column=2, padx=padxBotoes, pady=padyBotoes)

    # Funções dos botões
    def digitar(self, numero: int):
        global valorVisor
        self.visor.insert(END, str(numero))
        valorVisor += str(numero)

        print(valorVisor)
        
    def apagarTudo(self):
        global valorVisor
        self.visor.delete(0, END)
        valorVisor = ""

    def apagarUltimo(self):
        global valorVisor
        ultimoNumero = self.visor.index(END) - 1
        if ultimoNumero >= 0:
            self.visor.delete(ultimoNumero)
            valorVisor = valorVisor[:-1]
            print(valorVisor)

    def inserirOperador(self, operador):
        global valorVisor
        conteudo = self.visor.get()
        if conteudo and conteudo[-1] not in "+-*÷.":
            self.visor.insert(END, operador)
            valorVisor += operador
            print(valorVisor)

    def calcular(self):

        pass


root = Tk()
root.title("Calculadora")
Application(root)
root.mainloop()
