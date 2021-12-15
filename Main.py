"""
Main
"""

def printTutorial():
    #TODO
    print("Benvenuti in UNO")
    print("Per pescare digita 0")

def setGiocatori(giocatori, mazzo):
    numeroGiocatori = int(input("Inserisci il numero di giocatori: "))

    for numero in range(numeroGiocatori):
        nome = str(input("Nome del giocatore " + str(numero + 1) + ": "))
        
        giocatori.append(Giocatore(nome, mazzo.pesca(7, [])))

    random.shuffle(giocatori)
    
    print("L'ordine dei giocatori sarà: ")
    for giocatore in giocatori:
        print(giocatore.getNome())

def gameOn(giocatori, mazzo):
    carteSpeciali = ["pesca_due", "pesca_quattro", "inverti", "stop", "cambio_colore"]
    
    while True:
        mazzo.giocaCarta(mazzo.pesca(1, []))
        if mazzo.ultimaCarta().getValore() not in carteSpeciali: break

    index = 0
    carteDaPescare = 0
    while True:
        print("\n\nUltima carta: " + mazzo.ultimaCarta().getValore() + " " + mazzo.ultimaCarta().getColore())
        
        if mazzo.ultimaCarta().getValore() == "stop":
            turno = getTurno(index, giocatori)
            giocatore = giocatori[turno]
            input("Il giocatore " + giocatore.getNome() + " salta il turno! ")
            
            index += 1
            
        elif mazzo.ultimaCarta().getValore() == "inverti":
            giocatori = giocatori[::-1]
            index = (len(giocatori) - index) + 1
            
            print("L'ordine dei giocatori ora sarà: ")
            for giocatore in giocatori:
                print(giocatore.getNome())
        
        turno = getTurno(index, giocatori)
        giocatore = giocatori[turno]
        
        input("Tocca al giocatore " + giocatore.getNome() + ", non sbirciate teste di cazzo! ")
        
        if mazzo.ultimaCarta().getValore() in ["pesca_due", "pesca_quattro"]:
            if mazzo.ultimaCarta().getValore() == "pesca_due":
                    carteDaPescare += 2
            elif mazzo.ultimaCarta().getValore() == "pesca_quattro":
                    carteDaPescare += 4
                    
            #func per controllare se ha +2 o +4
                    
            scelta = str(input("Vuoi giocare una carta speciale o preferisci pescare?(G/P) "))
            
            if scelta == 'P':
                if mazzo.ultimaCarta().getValore() == "pesca_due":
                    pescaCarte(giocatore, mazzo, carteDaPescare + 2)
                elif mazzo.ultimaCarta().getValore() == "pesca_quattro":
                    pescaCarte(giocatore, mazzo, carteDaPescare + 4)
                    
                carteDaPescare = 0
        
        print(visualizzaManoGiocatore(giocatore))
        mazzo.giocaCarta(sceltaCartaDaGiocare(giocatore, mazzo))
        print(visualizzaManoGiocatore(giocatore))
        index += 1

def getTurno(turno, giocatori):
    return turno % len(giocatori)

def visualizzaManoGiocatore(giocatore):
    return giocatore.visualizzaMano()

def sceltaCartaDaGiocare(giocatore, mazzo):
    index = int(input("Index carta da giocare: ")) - 1
    mano = giocatore.getMano()
    
    if index < len(mano) and index >= 0:
        cartaDaGiocare = mano[index]

        if controlloCarte(mazzo.ultimaCarta(), cartaDaGiocare):
            mano.pop(index)

            giocatore.setMano(mano)
            
            #controllo che sia un cambio colore o +4, nel caso faccio funzione per cambiare colore

            return [cartaDaGiocare]
        
        else:
            print("Scegli un'altra carta! Mona!")
            return sceltaCartaDaGiocare(giocatore, mazzo.ultimaCarta())
        
    elif index == -1:
        pescaCarte(giocatore, mazzo, 1)
        return [mazzo.ultimaCarta()]
        
    else:
        print("Non hai tutte queste carte! Poraccio...")
        return sceltaCartaDaGiocare(giocatore, mazzo.ultimaCarta())

def controlloCarte(ultimaCarta, cartaDaGiocare):
    if (ultimaCarta.getColore() == cartaDaGiocare.getColore()
    or ultimaCarta.getValore() == cartaDaGiocare.getValore()
    or cartaDaGiocare.getColore() == "nero"):
        return True
    else:
        return False
    
def pescaCarte(giocatore, mazzo, numeroCarte):
    mano = giocatore.getMano()
    giocatore.setMano(mazzo.pesca(numeroCarte, mano))
    

if __name__ == "__main__":
    from Giocatore import Giocatore
    from Mazzo import Mazzo
    from Carta import Carta
    import random

    _giocatori = []
    _mazzo = Mazzo()
    
    printTutorial()
    
    setGiocatori(_giocatori, _mazzo)

    gameOn(_giocatori, _mazzo)

    
