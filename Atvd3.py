from tkinter import *
import os

class Campos:
    def __init__(self, master=None):
        self.fonte1 = ("Arial"), ("10")

        self.espaço1 = Frame(master)
        self.espaço1["pady"] = 10
        self.espaço1.pack()

        self.espaço2 = Frame(master)
        self.espaço2["padx"] = 20
        self.espaço2.pack()

        self.espaço3 = Frame(master)
        self.espaço3["padx"] = 20
        self.espaço3.pack()

        self.espaço4 = Frame(master)
        self.espaço4["padx"] = 20
        self.espaço4.pack()

        self.espaço5 = Frame(master)
        self.espaço5["padx"] = 20
        self.espaço5.pack()

        self.espaço6 = Frame(master)
        self.espaço6["padx"] = 20
        self.espaço6.pack()

        self.espaço7 = Frame(master)
        self.espaço7["padx"] = 20
        self.espaço7.pack()

        self.espaço8 = Frame(master)
        self.espaço8["padx"] = 20
        self.espaço8.pack()

        self.espaço9 = Frame(master)
        self.espaço9["padx"] = 20
        self.espaço9.pack()


        self.nome = Label(self.espaço1, text="Calculadora IMC!!!")
        self.nome["font"] = ("Arial", "10", "bold")
        self.nome.pack()

        self.digitoLabel = Label(self.espaço2, text="Nome:", bg="red", font=("Arial", "10", "bold"))
        self.digitoLabel.pack(side=LEFT)

        self.digito = Entry(self.espaço2)
        self.digito["width"] = 30
        self.digito["font"] = self.fonte1
        self.digito.pack(side=LEFT)

        self.digitoLabel = Label(self.espaço3, text="Endereço:", bg="brown", font=("Arial", "10", "bold"))
        self.digitoLabel.pack(side=LEFT)

        self.digito = Entry(self.espaço3)
        self.digito["width"] = 30
        self.digito["font"] = self.fonte1
        self.digito.pack(side=LEFT)


        self.digitoLabel = Label(self.espaço4, text="Peso:", bg="green" , font=("Arial", "10", "bold"))
        self.digitoLabel.pack(side=LEFT)

        self.digito = Entry(self.espaço4)
        self.digito["width"] = 30
        self.digito["font"] = self.fonte1
        self.digito.pack(side=LEFT)

        self.digito2Label = Label(self.espaço5, text="Altura:", bg="blue" , font=("Arial", "10", "bold"))
        self.digito2Label.pack(side=LEFT)

        self.digito2 = Entry(self.espaço5)
        self.digito2["width"] = 30
        self.digito2["font"] = self.fonte1
        self.digito2.pack(side=LEFT)


        self.imcLabel = Label(self.espaço6, text="Resultado:", font=("Arial", "10", "bold"))
        self.imcLabel.pack(side=LEFT)

        self.imcValor = Label(self.espaço7, text="", font=self.fonte1)
        self.imcValor.pack(side=RIGHT)


        self.exec = Button(self.espaço8)
        self.exec["text"] = "Executar"
        self.exec["font"] = ("Arial", "10", "bold")
        self.exec["width"] = 12
        self.exec["command"] = self.calcula
        self.exec.pack()

        self.sair = Button(self.espaço9)
        self.sair["text"] = "Sair"
        self.sair["font"] = ("Arial", "10", "bold")
        self.sair["width"] = 12
        self.sair["command"] = self.exit
        self.sair.pack()



    def exit(self):
        exit()

    def calcula(self):
        peso = self.digito.get()
        altura = self.digito2.get()
        peso = peso.replace(",", ".")
        altura = altura.replace(",", ".")

        resp = (float(peso)) / (float(altura) * float(altura))

        if peso:
                self.imcValor["text"] = resp

        if (resp < 17):
                self.imcValor["text"] = (f"Muito abaixo do peso, seu IMC é: {resp}")
        elif (resp < 18.49):
                self.imcValor["text"] =(f"Abaixo do peso, seu IMC é:{resp}")
        elif (resp >= 18.50 and resp <= 24.99):
                self.imcValor["text"] =(f"Peso normal, seu IMC é:{resp}")
        elif (resp >= 25 and resp <= 29.99):
                self.imcValor["text"] =(f"Acima do peso, seu IMC é:{resp}")
        elif (resp >= 30 and resp <= 34.99):
                self.imcValor["text"] =(f"Obesidade I, seu IMC é:{resp}")
        elif (resp >= 35 and resp <= 39.99):
                self.imcValor["text"] =(f"Obesidade  II, seu IMC é:{resp}")
        elif (resp > 40):
                self.imcValor["text"] =(f"Obesidade III, seu IMC é:{resp}")

root = Tk()
Campos(root)
root.mainloop()

