"""
Classe Carta
"""

class Carta:
    _colore = ""
    _valore = ""

    def __init__(self, colore, valore):
        self.assegnaColore(colore)
        self.assegnaValore(valore)

    def assegnaColore(self, colore):
        self._colore = colore

    def visualizzaColore(self):
        return self._colore

    def assegnaValore(self, valore):
        self._valore = valore

    def visualizzaValore(self):
        return self._valore
