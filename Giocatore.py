"""
Classe Giocatore
"""
from Carta import Carta

class Giocatore:
    _nome = ""
    _mano = []

    def __init__(self, nome):
        self.assegnaNome(nome)

    def assegnaNome(self, nome):
        self._nome = nome.capitalize()      #assegna un nome al giocatore

    def visualizzaNome(self):
        return self._nome                   #mostra il nome del giocatore

    def assegnaMano(self, mano):
        self._mano = mano                   #assegna la mano al giocatore

    def visualizzaMano(self):
        return self._mano                   #mostra la mano del giocatore
