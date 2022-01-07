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
        self._nome = nome.capitalize()

    def visualizzaNome(self):
        return self._nome

    def assegnaMano(self, mano):
        self._mano = mano

    def visualizzaMano(self):
        return self._mano
