from os import system as lt 
lt("cls")

class Lampada:
    def avisar(self):
        print("Cuidado! Quente!")

minha_lampada = Lampada()
minha_lampada.avisar()