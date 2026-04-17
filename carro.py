from os import system as lt
lt("cls")
import os

class Carro:
    """
    Essa classe cria carros da HotWhells
    """
    def __init__(self, cor: str, fabricante: str, potencia: float, ano: str, modelo: str):
        self.cor = cor
        self.fabricante = fabricante
        self.potencia = potencia
        self.ano = ano
        self.modelo = modelo
        self.status = False
        self.velocidade = 0
        self.farol = False

    def ligar(self):
        if self.status == False:
            self.status = True
        return f"Seu carro está ligado. :)"
    
    def desligar(self):
        if self.status == True:
            self.status = False
        return f"Seu carro está desligado. :("

    def acelerar(self):
        if self.velocidade < 100 and self.status == True:
            self.velocidade += 5
        else:
            self.velocidade = 100
            return f"Você deve ligar seu carro antes de operá-lo."
        return f"Seu carro está a {self.velocidade} Km/h"

    def desacelerar(self):
        if self.velocidade > 0 and self.status == True:
            self.velocidade -= 5
        else:
            self.velocidade = 0
            return f"Você deve ligar seu carro antes de operá-lo."
        return f"Seu carro está a {self.velocidade} Km/h"

    def freiar():
        pass

    def ligar_farol(self):
        if self.farol:
            return "O farol está ligado."

        self.farol = True
        return "Farol ligado. 💡"

    def desligar_farol(self):
        if not self.farol:
            return "O farol já está desligado."

        self.farol = False
        return "Farol desligado."


# print("Insira os dados do seu carro abaixo.")
cor_carro = "vermelho"
fab_carro = "Chevrolet"
pot_carro = 200
ano_carro = 1985
modelo_carro = "Fusca"


veiculo1 = Carro(cor_carro, fab_carro, pot_carro, ano_carro, modelo_carro)

while True:
    op = input("O que deseja fazer?\n1 - Ligar carro\n2 - Desligar carro\
\n3 - Acelerar\n4 - desacelerar\n5 - Ligar farol\n6 - Desligar farol\n-> ")
    match op:
        case "1":
            print(veiculo1.ligar())
        case "2":
            print(veiculo1.desligar())
        case "3":
            print(veiculo1.acelerar())
        case "4":
            print(veiculo1.desacelerar())
        case "5":
            print(veiculo1.ligar_farol())
        case "6":
            print(veiculo1.desligar_farol())



    print()