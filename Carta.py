"""
Classe Carta
"""

class Carta:
    _colore = ""
    _valore = ""

    def __init__(self, colore, valore):
        self.setColore(colore)
        self.setValore(valore)

    def setColore(self, colore):
        self._colore = colore

    def getColore(self):
        return self._colore

    def setValore(self, valore):
        self._valore = valore

    def getValore(self):
        return self._valore
