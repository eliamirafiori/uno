"""
Classe Giocatore
"""
from Carta import Carta

class Giocatore:
    _nome = ""
    _mano = []

    def __init__(self, nome, mano):
        self.setNome(nome)
        self.setMano(mano)

    def setNome(self, nome):
        self._nome = nome.capitalize()

    def getNome(self):
        return self._nome

    def setMano(self, mano):
        self._mano = mano

    def getMano(self):
        return self._mano

    def visualizzaMano(self):
        mano = []
        for carta in self._mano:
            mano.append(carta.getValore() + " " + carta.getColore())
        return mano
