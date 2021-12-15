"""
Main
"""

def setGiocatori(giocatori, mazzo):
    numeroGiocatori = int(input("Inserisci il numero di giocatori: "))

    for numero in range(numeroGiocatori):
        nome = str(input("Nome del giocatore " + str(numero + 1) + ": "))
        
        giocatori.append(Giocatore(nome, mazzo.pesca(7, [])))

    random.shuffle(giocatori)

def gameOn(giocatori, mazzo):
    carteSpeciali = ["pesca_due", "pesca_quattro", "inverti", "stop", "cambio_colore"]
    
    while True:
        mazzo.giocaCarta(mazzo.pesca(1, []))
        if mazzo.ultimaCarta().getValore() not in carteSpeciali: break

    index = 0
    while True:
        print("Ultima carta: " + mazzo.ultimaCarta().getValore() + " " + mazzo.ultimaCarta().getColore())
        
        if mazzo.ultimaCarta().getValore() == "stop":
            index += 1
            
        elif mazzo.ultimaCarta().getValore() == "inverti":
            giocatori = giocatori[::-1]
            index = (len(giocatori) - index) + 1
        
        turno = getTurno(index, giocatori)
        giocatore = giocatori[turno]
        
        input("\n\nTocca al giocatore " + giocatore.getNome() + ", non sbirciate teste di cazzo! ")
        
        if mazzo.ultimaCarta().getValore() in carteSpeciali:
            scelta = str(input("Vuoi giocare una carta speciale o preferisci pescare? "))
        
        print(visualizzaManoGiocatore(giocatore))
        mazzo.giocaCarta(sceltaCartaDaGiocare(giocatore, mazzo.ultimaCarta()))
        print(visualizzaManoGiocatore(giocatore))
        index += 1

def getTurno(turno, giocatori):
    return turno % len(giocatori)

def visualizzaManoGiocatore(giocatore):
    return giocatore.visualizzaMano()

def sceltaCartaDaGiocare(giocatore, ultimaCarta):
    index = int(input("Index carta da giocare: ")) - 1
    mano = giocatore.getMano()
    
    if index < len(mano) and index >= 0:
        cartaDaGiocare = mano[index]

        if controlloCarte(ultimaCarta, cartaDaGiocare):
            mano.pop(index)

            giocatore.setMano(mano)

            return [cartaDaGiocare]
        else:
            print("Scegli un'altra carta! Mona!")
            return sceltaCartaDaGiocare(giocatore, ultimaCarta)
        
    else:
        print("Non hai tutte queste carte! Poraccio...")
        return sceltaCartaDaGiocare(giocatore, ultimaCarta)

def controlloCarte(ultimaCarta, cartaDaGiocare):
    if (ultimaCarta.getColore() == cartaDaGiocare.getColore()
    or ultimaCarta.getValore() == cartaDaGiocare.getValore()
    or cartaDaGiocare.getColore() == "nero"):
        return True
    else:
        return False

if __name__ == "__main__":
    from Giocatore import Giocatore
    from Mazzo import Mazzo
    from Carta import Carta
    import random

    _giocatori = []
    _mazzo = Mazzo()
    
    setGiocatori(_giocatori, _mazzo)

    gameOn(_giocatori, _mazzo)

    
