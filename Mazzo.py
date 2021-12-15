"""
Classe Mazzo
"""

from Carta import Carta
import random

class Mazzo:
    _carteDaGiocare = []
    _carteGiocate = []
    _colori = ["blu", "rosso", "verde", "giallo"]

    def __init__(self):
        self.setMazzo()

    def setMazzo(self):
        for colore in self._colori:
            for _ in range(2):
                for numero in range(1, 10):
                    self._carteDaGiocare.append(Carta(colore, str(numero)))

                self._carteDaGiocare.append(Carta(colore, "pesca_due"))
                self._carteDaGiocare.append(Carta(colore, "inverti"))
                self._carteDaGiocare.append(Carta(colore, "stop"))

            self._carteDaGiocare.append(Carta(colore, str(0)))

        for _ in range(4):
            self._carteDaGiocare.append(Carta("nero", "cambio_colore"))
            self._carteDaGiocare.append(Carta("nero", "pesca_quattro"))

        random.shuffle(self._carteDaGiocare)

        return self._carteDaGiocare

    def getMazzo(self):
        return self._carteDaGiocare

    def pesca(self, numero, mano):
        for index in range(numero):
            mano.append(self._carteDaGiocare[index])

        for carta in mano:
            self._carteDaGiocare.remove(carta)
            
        return mano

    def giocaCarta(self, carte):
        for carta in carte:
            self._carteGiocate.append(carta)

    def ultimaCarta(self):
        return self._carteGiocate[-1]
