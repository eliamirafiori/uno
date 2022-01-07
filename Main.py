"""
Main 2.0.0
"""

def generaMazzo():
    colori = ["blu", "rosso", "verde", "giallo"]
    mazzo = []
    
    for colore in colori:
        for _ in range(2):
            for numero in range(1, 10):
                mazzo.append(Carta(colore, str(numero)))

            mazzo.append(Carta(colore, "pesca_due"))
            mazzo.append(Carta(colore, "inverti"))
            mazzo.append(Carta(colore, "stop"))

        mazzo.append(Carta(colore, str(0)))

    for _ in range(4):
        mazzo.append(Carta("nero", "cambio_colore"))
        mazzo.append(Carta("nero", "pesca_quattro"))

    random.shuffle(mazzo)

    return mazzo

def generaGiocatori():
    giocatori = []
    numeroGiocatori = input("Inserisci il numero di giocatori: ")

    try:
        numeroGiocatori = int(numeroGiocatori)
    except:
        print("Sei ritardato, metti un intero!")
        generaGiocatori()
        return "Sei ritardato, metti un intero!"

    if numeroGiocatori < 2 or numeroGiocatori > 10:
        print("Troppi o troppo pochi, cazzo mene")
        generaGiocatori()
        return "Troppi o troppo pochi, cazzo mene"

    for numero in range(numeroGiocatori):
        nome = str(input("Nome del giocatore " + str(numero + 1) + ": "))
        
        giocatori.append(Giocatore(nome))

    random.shuffle(giocatori)
    
    print("L'ordine dei giocatori sarà: ")
    for giocatore in giocatori:
        print(giocatore.visualizzaNome())

    return giocatori

def pescaCarta():
    carta = _mazzo[len(_mazzo) - 1]
    _mazzo.remove(_mazzo[len(_mazzo) - 1])
    return carta

def assegnaCarteIniziali():
    for giocatore in _giocatori:
        mano = []
        for _ in range(7):
            mano.append(pescaCarta())

        giocatore.assegnaMano(mano)

    assegnaCartaIniziale()

def assegnaCartaIniziale():
    carteSpeciali = ["pesca_due", "pesca_quattro", "inverti", "stop", "cambio_colore"]
    
    while len(_cimitero) == 0 or _cimitero[len(_cimitero) - 1].visualizzaValore() in carteSpeciali:
        _cimitero.append(pescaCarta())

    print(_cimitero[len(_cimitero) - 1].visualizzaValore())

def visualizzaTurno(turno):
    return turno % len(_giocatori)

def controlloManoGiocatore(mano, ultimaCartaCimitero):
    puoGiocare = False
    for carta in mano:
        if carta.visualiizaColore() == ultimaCartaCimitero.visualiizaColore():
            puoGiocare = True
            return
        
        if carta.visualiizaValore() == ultimaCartaCimitero.visualiizaValore():
            puoGiocare = True
            return

    return puoGiocare

def controlloCarta(carta, ultimaCartaCimitero):
    #TODO controllo carte speciali
     if carta.visualiizaColore() == ultimaCartaCimitero.visualiizaColore():
        return True
        
    if carta.visualiizaValore() == ultimaCartaCimitero.visualiizaValore():
        return True

    return False

def giocaCarta(giocatore, ultimaCartaCimitero):
    indiceCarta = input("Scegli una carta da giocare: ")

    try:
        indiceCarta = int(indiceCarta)
    except:
        print("Sei ritardato, metti un intero!")
        giocaCarte(mano, ultimaCartaCimitero)
        return "Sei ritardato, metti un intero!"

    if numeroGiocatori < 0 or numeroGiocatori > (len(mano) - 1):
        print("Scegli una carta esistente")
        giocaCarte(mano, ultimaCartaCimitero)
        return "Scegli una carta esistente"

    mano = giocatore.visualizzaMano()
    carta = mano[indiceCarta]

    if controlloCarta(carta, ultimaCartaCimitero):
        _cimitero.append(carta)
        mano.pop(indiceCarta)
        giocatore.assegnaMano(mano)
        
    else:
        print("Scegli una carta valida")
        giocaCarte(mano, ultimaCartaCimitero)
        return "Scegli una carta valida"

def inizioGioco():
    turno = 0
    while True:
        giocatore = _giocatori[visualizzaTurno(turno)]
        ultimaCartaCimitero = (_cimitero[len(_cimitero) - 1]

        #TODO controllo saltaTurno o pescaCarte != 0

        puoGiocare = False
        for carta in giocatore.visualizzaMano():
            if controlloCarta(carta, ultimaCartaCimitero):
                puoGiocare = True
                return
        
        if puoGiocare:
            #possibilità: giocare
            #TODO controllo più carte da giocare
        else:
            #possibilità: pescare -> controlloMano -> giocare o passare

if __name__ == "__main__":
    from Carta import Carta
    from Giocatore import Giocatore
    import random
    
    _mazzo = generaMazzo()
    _cimitero = [] #iughioh eazter eggg
    _giocatori = generaGiocatori()

    _carteDaPescare = 0
    _saltaTurno = False

    assegnaCarteIniziali()
