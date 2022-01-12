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

def organizzaCarteGiocatore(mano):
    manoOrganizzata = []
    colori = ["blu", "rosso", "verde", "giallo" , "nero"]

    for colore in colori:
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

def visualizzaManoGiocatore(giocatore, visualizzaPerRispondere = False, ultimaCartaCimitero = None):
    if visualizzaPerRispondere:
        for carta in giocatore.visualizzaMano():
            if (carta.visualizzaValore() == "pesca_quattro"
                or carta.visualizzaValore() == ultimaCartaCimitero.visualizzaValore()):
                print('|' + carta.visualizzaColore() + ' ' + carta.visualizzaValore() + '|')

    else:
        for carta in giocatore.visualizzaMano():
            print('|' + carta.visualizzaColore() + ' ' + carta.visualizzaValore() + '|')

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
        turno += _carteSaltaTurno
        _carteSaltaTurno = 0

        giocatore = _giocatori[visualizzaTurno(turno)]
        ultimaCartaCimitero = _cimitero[len(_cimitero) - 1]

        puoGiocare = False
        for carta in giocatore.visualizzaMano():
            if controlloCarta(carta, ultimaCartaCimitero):
                puoGiocare = True
                return

        #Visualizza la mano del giocatore
        visualizzaManoGiocatore(giocatore)

        if puoGiocare:
            #Se ci sono carte da pescare dai turni precedenti
            if _carteDaPescare > 0:

                #Controllo della mano del giocatore per vedere se può rispondere
                puoRispondere = False
                for carta in giocatore.visualizzaMano():
                    if controlloCarta(carta, ultimaCartaCimitero, True):
                        puoRispondere = True
                        return

                #Se il giocatore può rispondere con le carte che ha in mano
                if puoRispondere:

                    #Proposta per rispondere o pescare
                    scelta = str(input("Hai la possibilità di rispondere, vuoi farlo? (S/n)\n")).strip().lower()

                    #Continua a comparire il messaggio d'errore e la proposta fintantochè la scelta non è valida
                    while scelta not in ['s', 'n']:
                        print("Inserisci una risposta valida")
                        scelta = str(input("Hai la possibilità di rispondere, vuoi farlo? (S/n)\n")).strip().lower()

                    #Se la scelta è quella di rispondere
                    if scelta == 's':
                        #TODO risponde solo con le carte con cui può farlo
                        #Visualizza la mano con cui può rispondere il giocatore
                        visualizzaManoGiocatore(giocatore, True, ultimaCartaCimitero)

                    #Se la scelta è quella di pescare
                    else:
                        aggiungiCarteGiocatore(giocatore)
                        #TODO dopo aver pescato gioca

                #Se il giocatore non può rispondere allo pesca _carteDaPescare carte
                else:
                    aggiungiCarteGiocatore(giocatore)

            #TODO possibilità: giocare
            #TODO controllo più carte da giocare
            pass
        else:
            #TODO possibilità: pescare -> controlloMano -> giocare o passare
            pass

        turno += 1


if __name__ == "__main__":
    from Carta import Carta
    from Giocatore import Giocatore
    import random
    
    _mazzo = generaMazzo()
    _cimitero = [] #iughioh eazter eggg
    _giocatori = generaGiocatori()

    _carteDaPescare = 0
    _carteSaltaTurno = 0

    assegnaCarteIniziali()
