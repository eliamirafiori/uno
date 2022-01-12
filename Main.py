"""
Main 2.0.0
"""

def generaMazzo():
    mazzo = []
    
    for colore in _colori:
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
        print("Inserisci un intero!")
        generaGiocatori()
        return "Inserisci un intero!"

    if numeroGiocatori < 2 or numeroGiocatori > 10:
        print("I giocatori devono essere tra 2 e 10")
        generaGiocatori()
        return "I giocatori devono essere tra 2 e 10"

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

def organizzaCarteGiocatore(mano):
    manoOrganizzata = []

    for colore in _colori:
        for carta in mano:
            if carta.visualizzaColore() == colore:
                manoOrganizzata.append(carta)

    #TODO organizza per valore
    return manoOrganizzata

def aggiungiCarteGiocatore(giocatore):
    mano = []
    for _ in range(_carteDaPescare):
        mano.append(pescaCarta())

    giocatore.assegnaMano(organizzaCarteGiocatore(mano))

def assegnaCarteIniziali():
    _carteDaPescare = 7
    for giocatore in _giocatori:
        aggiungiCarteGiocatore(giocatore)

    _carteDaPescare = 0
    assegnaCartaIniziale()

def assegnaCartaIniziale():
    carteSpeciali = ["pesca_due", "pesca_quattro", "inverti", "stop", "cambio_colore"]
    
    while len(_cimitero) == 0 or _cimitero[len(_cimitero) - 1].visualizzaValore() in carteSpeciali:
        _cimitero.append(pescaCarta())

    print(_cimitero[len(_cimitero) - 1].visualizzaValore())

def visualizzaTurno(turno):
    return turno % len(_giocatori)

def controlloCarta(carta, ultimaCartaCimitero, dovrebbeRispondere = False):
    if dovrebbeRispondere:
        if (carta.visualizzaValore() == "pesca_quattro"
            or carta.visualizzaValore() == ultimaCartaCimitero.visualizzaValore()):
            return True

    else:
        if (carta.visualizzaColore() == ultimaCartaCimitero.visualizzaColore()
            or carta.visualizzaValore() == ultimaCartaCimitero.visualizzaValore()
            or carta.visualizzaColore() == "nero"):
            return True

    return False

def puoGiocare(giocatore, ultimaCartaCimitero):
    for carta in giocatore.visualizzaMano():
        if controlloCarta(carta, ultimaCartaCimitero):
            return True

    return False

def puoRispondere(giocatore, ultimaCartaCimitero):
    for carta in giocatore.visualizzaMano():
        if controlloCarta(carta, ultimaCartaCimitero, True):
            return True
    
    return False

def visualizzaManoGiocatore(giocatore, visualizzaPerRispondere = False, ultimaCartaCimitero = None):
    if visualizzaPerRispondere:
        for carta in giocatore.visualizzaMano():
            if (carta.visualizzaValore() == "pesca_quattro"
                or carta.visualizzaValore() == ultimaCartaCimitero.visualizzaValore()):
                print('|' + carta.visualizzaColore() + ' ' + carta.visualizzaValore() + '|')

    else:
        for carta in giocatore.visualizzaMano():
            print('|' + carta.visualizzaColore() + ' ' + carta.visualizzaValore() + '|')

def invertiTurno():
    _giocatori = _giocatori[::-1]
    _turno = (len(_giocatori) - _turno) + 1 #TODO capire se ci va il "+ 1" o no
            
    print("L'ordine dei giocatori ora sarà: ")
    for giocatore in _giocatori:
        print(giocatore.visualizzaNome())

def scegliColore():
    print("Scegli un colore:")
    index = 1
    for colore in _colori:
        print(index + " - " + colore.capitalize())

    colore = input("Indice colore: ")

    try:
        colore = int(colore)
    except:
        print("Inserisci un intero!")
        scegliColore()
        return "Inserisci un intero!"

    return colore

def giocaCarta(giocatore, ultimaCartaCimitero):
    indiceCarta = input("Scegli una carta da giocare: ")

    try:
        indiceCarta = int(indiceCarta)
    except:
        print("Inserisci un intero!")
        giocaCarte(mano, ultimaCartaCimitero)
        return "Inserisci un intero!"

    if numeroGiocatori < 0 or numeroGiocatori > (len(mano) - 1):
        print("Scegli una carta esistente!")
        giocaCarte(mano, ultimaCartaCimitero)
        return "Scegli una carta esistente!"

    mano = giocatore.visualizzaMano()
    carta = mano[indiceCarta]

    if controlloCarta(carta, ultimaCartaCimitero):
        _cimitero.append(carta)
        mano.pop(indiceCarta)
        giocatore.assegnaMano(mano)

        if carta.visualizzaValore() == "pesca_due":
            _carteDaPescare += 2

        elif carta.visualizzaValore() == "pesca_quattro":
            _carteDaPescare += 4

        elif carta.visualizzaValore() == "stop":
            _carteSaltaTurno += 1

        elif carta.visualizzaValore() == "inverti":
            invertiTurno()

        elif carta.visualizzaValore() == "cambio_colore":
            _cimitero.append(Carta(_colori[scegliColore()], "dummy")) #Carta per "tenere" il colore
            #TODO quando riutilizzo il _cimitero e lo rimetto nel mazzo devo togliere le carte "dummy"

    else:
        print("Scegli una carta valida!")
        giocaCarte(mano, ultimaCartaCimitero)
        return "Scegli una carta valida!"

def inizioGioco():
    while True:
        _turno += _carteSaltaTurno
        _carteSaltaTurno = 0

        giocatore = _giocatori[visualizzaTurno(_turno)]
        ultimaCartaCimitero = _cimitero[len(_cimitero) - 1]

        #Visualizza la mano del giocatore
        visualizzaManoGiocatore(giocatore)

        #Controllo della mano del giocatore per vedere se può giocare
        if puoGiocare(giocatore, ultimaCartaCimitero): #Se il giocatore può giocare con le carte che ha in mano
            
            #Controllo se ci sono carte da pescare dai turni precedenti
            if _carteDaPescare > 0: #Se ci sono carte da pescare dai turni precedenti

                #Controllo della mano del giocatore per vedere se può rispondere
                if puoRispondere(giocatore, ultimaCartaCimitero): #Se il giocatore può rispondere con le carte che ha in mano

                    #Proposta per rispondere o pescare
                    #Se vuole rispondere o se non specifica la risposta è True
                    #Se non vuole rispondere è False
                    vuoleRispondere = True if str(input("Hai la possibilità di rispondere, vuoi farlo? (S/n)\n")).strip().lower() != 'n' else False

                    #Controllo la scelta del giocatore se rispondere o pescare
                    if vuoleRispondere: #Se la scelta è quella di rispondere
                        visualizzaManoGiocatore(giocatore, True, ultimaCartaCimitero) #Visualizza la mano con cui può rispondere il giocatore
                        giocaCarta(giocatore, ultimaCartaCimitero)
                        #TODO risponde solo con le carte con cui può farlo

                    else: #Se la scelta è quella di pescare
                        aggiungiCarteGiocatore(giocatore) #Il giocatore pesca _carteDaPescare carte
                        _carteDaPescare = 0 #Reset di _carteDaPescare

                        visualizzaManoGiocatore(giocatore) #Visualizza la mano del giocatore
                        giocaCarta(giocatore, ultimaCartaCimitero)
                        #TODO controllo più carte da giocare

                else: #Se il giocatore NON può rispondere allora pesca _carteDaPescare carte
                    aggiungiCarteGiocatore(giocatore) #Il giocatore pesca _carteDaPescare carte
                    _carteDaPescare = 0 #Reset di _carteDaPescare

                    visualizzaManoGiocatore(giocatore) #Visualizza la mano del giocatore
                    giocaCarta(giocatore, ultimaCartaCimitero)
                    #TODO controllo più carte da giocare

            else: #Se NON ci sono carte da pescare dai turni precedenti
                visualizzaManoGiocatore(giocatore) #Visualizza la mano del giocatore
                giocaCarta(giocatore, ultimaCartaCimitero)
                #TODO controllo più carte da giocare
                pass

        else: #Se il giocatore NON può giocare con le carte che ha in mano
            #TODO possibilità: pescare (done) -> controlloMano (done) -> giocare o passare
            if _carteDaPescare == 0: _carteDaPescare = 1

            aggiungiCarteGiocatore(giocatore) #Il giocatore pesca _carteDaPescare carte
            _carteDaPescare = 0 #Reset di _carteDaPescare

            #Controllo della mano del giocatore per vedere se può giocare dopo aver pescato
            if puoGiocare(giocatore, ultimaCartaCimitero): #Se il giocatore può giocare con le carte che ha in mano
                visualizzaManoGiocatore(giocatore) #Visualizza la mano del giocatore
                giocaCarta(giocatore, ultimaCartaCimitero)
                #TODO controllo più carte da giocare

        _turno += 1


if __name__ == "__main__":
    from Carta import Carta
    from Giocatore import Giocatore
    import random

    #TODO commentare tutto
    
    _colori = ["blu", "rosso", "verde", "giallo" , "nero"]
    _mazzo = generaMazzo()
    _cimitero = [] #iughioh eazter eggg
    _giocatori = generaGiocatori()

    _turno = 0
    _carteDaPescare = 0
    _carteSaltaTurno = 0

    assegnaCarteIniziali()
