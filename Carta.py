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
        self._colore = colore           #assegna un colore alla carta

    def visualizzaColore(self):
        return self._colore             #mostra un colore della carta

    def assegnaValore(self, valore):
        self._valore = valore           #assegna un valore alla carta

    def visualizzaValore(self):
        return self._valore             #mostra il valore della carta
