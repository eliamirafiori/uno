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
        tipo = str(input("Tipologia di giocatore - U per il giocatore umano, C per il giocatore virtuale: ").strip().upper())
        while tipo not in ['U', 'C']:
            tipo = str(input("Errore! Inserire tipologia di giocatore - U per il giocatore umano, C per il giocatore virtuale: ").strip().upper())
        if tipo == 'U':
            giocatore = Giocatore_Umano(nome)
            giocatori.append(giocatore)
        else:
            furbo = str(input("Il giocatore virtuale deve essere intelligente? Premere spazio per no, digitare qualcosa per sì: ").strip())
            giocatore = Giocatore_IA(nome)
            giocatore.assegnaFurbo(furbo == '')
            giocatori.append(giocatore)
            
    random.shuffle(giocatori)
    
    print("L'ordine dei giocatori sarà: ")
    for giocatore in giocatori:
        print(giocatore.visualizzaNome())

    return giocatori

def pescaCarta():
    global _mazzo

    carta = _mazzo[len(_mazzo) - 1]
    _mazzo.remove(_mazzo[len(_mazzo) - 1])
    return carta

def organizzaCarteGiocatore(mano):
    manoOrganizzata = []

    for colore in ["blu", "rosso", "verde", "giallo", "nero"]:
        for carta in mano:
            if carta.visualizzaColore() == colore:
                manoOrganizzata.append(carta)

    #TODO organizza per valore
    return manoOrganizzata

def aggiungiCarteGiocatore(giocatore):
    global _carteDaPescare

    mano = []

    for carta in giocatore.visualizzaMano():
        mano.append(carta)

    for _ in range(_carteDaPescare):
        mano.append(pescaCarta())

    giocatore.assegnaMano(organizzaCarteGiocatore(mano))

def assegnaCarteIniziali():
    global _carteDaPescare, _giocatori

    _carteDaPescare = 7
    for giocatore in _giocatori:
        aggiungiCarteGiocatore(giocatore)

    _carteDaPescare = 0
    assegnaCartaIniziale()

def assegnaCartaIniziale():
    global _cimitero

    carteSpeciali = ["pesca_due", "pesca_quattro", "inverti", "stop", "cambio_colore"]
    
    while len(_cimitero) == 0 or _cimitero[len(_cimitero) - 1].visualizzaValore() in carteSpeciali:
        _cimitero.append(pescaCarta())

    inizioGioco()

def visualizzaTurno(turno):
    global _giocatori

    return turno % len(_giocatori)

def controlloCarta(carta, ultimaCartaCimitero, dovrebbeRispondere = False):
    if dovrebbeRispondere:
        if len(carta)==1:
            if (carta.visualizzaValore() == "pesca_quattro" or carta.visualizzaValore() == ultimaCartaCimitero.visualizzaValore()):
                    return True
    
        else:
            controlloCarta(carta[:-1], carta[0], dovrebbeRispondere)
        return False
    else:
        if len(carta)==1:
            if (carta.visualizzaColore() == ultimaCartaCimitero.visualizzaColore() or carta.visualizzaValore() == ultimaCartaCimitero.visualizzaValore() or carta.visualizzaColore() == "nero"):
                return True
        else:
            controlloCarta(carta[:-1], carta[0], dovrebbeRispondere)
        return False
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
        indiceCarta = 0
        for carta in giocatore.visualizzaMano():
            if (carta.visualizzaValore() == "pesca_quattro"
                or carta.visualizzaValore() == ultimaCartaCimitero.visualizzaValore()):
                print(str(indiceCarta) + ' |' + carta.visualizzaColore() + ' ' + carta.visualizzaValore() + '|')
            indiceCarta +=1

    else:
        indiceCarta = 0
        for carta in giocatore.visualizzaMano():
            print(str(indiceCarta) + ' |' + carta.visualizzaColore() + ' ' + carta.visualizzaValore() + '|')
            indiceCarta +=1

def invertiTurno():
    global _giocatori, _turno

    _giocatori = _giocatori[::-1]
    _turno = (len(_giocatori) - _turno) + 1 #TODO capire se ci va il "+ 1" o no
            
    print("L'ordine dei giocatori ora sarà: ")
    for giocatore in _giocatori:
        print(giocatore.visualizzaNome())

def scegliColore():
    global _colori

    print("Scegli un colore:")
    indiceCarta = 0
    for colore in _colori:
        print(str(indiceCarta) + " - " + colore.capitalize())
        indiceCarta += 1

    colore = input("Indice colore: ")

    try:
        colore = int(colore)
    except:
        print("Inserisci un intero!")
        scegliColore()
        return "Inserisci un intero!"

    return colore

def giocaCarta(giocatore, ultimaCartaCimitero):
    global _cimitero, _carteDaPescare, _carteSaltaTurno, _colori

    print("Scegli una carta da giocare!")
    mano = giocatore.visualizzaMano()
    carta = giocatore.scegliCarta()
    return carta

    if controlloCarta(carta, ultimaCartaCimitero):
        _cimitero.append(carta)
        mano.pop(indiceCarta)
        giocatore.assegnaMano(mano)

        if carta.visualizzaValore() == "pesca_due":
            _carteDaPescare += 2

        elif carta.visualizzaValore() == "pesca_quattro":
            _carteDaPescare += 4
            _cimitero.append(Carta(_colori[scegliColore()], "dummy")) #Carta per "tenere" il colore

        elif carta.visualizzaValore() == "stop":
            _carteSaltaTurno += 1

        elif carta.visualizzaValore() == "inverti":
            invertiTurno()

        elif carta.visualizzaValore() == "cambio_colore":
            _cimitero.append(Carta(_colori[scegliColore()], "dummy")) #Carta per "tenere" il colore
            #TODO quando riutilizzo il _cimitero e lo rimetto nel mazzo devo togliere le carte "dummy"

    else:
        print("Scegli una carta valida!")
        giocaCarta(giocatore, ultimaCartaCimitero)
        return "Scegli una carta valida!"
    
    carta = mano[indiceCarta]
    carteUguali = []
    indiciCarteUguali = []
    if controlloCarta(carta, ultimaCartaCimitero):
        for indice in range(len(mano)) and indice != indiceCarta:
            if mano[indice].visualizzaValore() == carta.visualizzaValore() and mano[indice].visualizzaValore() not in carteSpeciali:
                carteUguali += mano[indice]
                indici += indice
            if carteUguali == []:
                _cimitero.append(carta)
                mano.pop(indiceCarta)
                giocatore.assegnaMano(mano)
            else:
                altreCarte = input('Vuoi giocare anche altre carte? Rispondi S per sì e N per no: ')
                if altreCarte.strip() in ['s', 'S']:
                    if len(carteUguali) > 1:
                        for cartaUguale in carteUguali:
                            print(cartaUguale.visualizzaValore()+' '+cartaUguale.visualizzaColore(), end = '  ')
                        try:
                            indiceUltimaCarta = int(input("Qual è l'ultima carta che vuoi giocare? ").strip())
                        except:
                            indiceUltimaCarta = int(input("Inserisci un numero compatibile! Qual è l'ultima carta che vuoi giocare? ").strip())
                        carteUguali = carteUguali[:indiceUltimaCarta]+carteUguali[indiceUltimaCarta+1:]+carteUguali[indiceUltimaCarta]
                        carteUguali.insert(carta, 0)
                        _cimitero.append(carteUguali)
                        for indice in indici:
                            mano.pop(indice)
                            giocatore.assegnaMano(mano)
                                                    

def inizioGioco():
    global _turno,  _carteDaPescare, _carteSaltaTurno

    while True:
        _turno += _carteSaltaTurno
        _carteSaltaTurno = 0

        giocatore = _giocatori[visualizzaTurno(_turno)]
        ultimaCartaCimitero = _cimitero[len(_cimitero) - 1]

        print("\n\nE' il turno di " + giocatore.visualizzaNome())
        print("Ultima carta in tavola: " + ultimaCartaCimitero.visualizzaColore() + " " + ultimaCartaCimitero.visualizzaValore())

        #Visualizza la mano del giocatore
        #visualizzaManoGiocatore(giocatore)

        #Controllo della mano del giocatore per vedere se può giocare
        if puoGiocare(giocatore, ultimaCartaCimitero): #Se il giocatore può giocare con le carte che ha in mano
            
            #Controllo se ci sono carte da pescare dai turni precedenti
            if _carteDaPescare > 0: #Se ci sono carte da pescare dai turni precedenti

                #Controllo della mano del giocatore per vedere se può rispondere
                if puoRispondere(giocatore, ultimaCartaCimitero): #Se il giocatore può rispondere con le carte che ha in mano

                    #Proposta per rispondere o pescare
                    #Se vuole rispondere o se non specifica la risposta è True
                    #Se non vuole rispondere è False
                    print(giocatore.visualizzaNome() + " dovresti pescare " + str(_carteDaPescare))
                    vuoleRispondere = vuoleRispondere()

                    #Controllo la scelta del giocatore se rispondere o pescare
                    if vuoleRispondere: #Se la scelta è quella di rispondere
                        print(giocatore.visualizzaNome() + " hai scelto di rispondere")
                        visualizzaManoGiocatore(giocatore, True, ultimaCartaCimitero) #Visualizza la mano con cui può rispondere il giocatore
                        giocaCarta(giocatore, ultimaCartaCimitero)
                        #TODO risponde solo con le carte con cui può farlo

                    else: #Se la scelta è quella di pescare
                        print(giocatore.visualizzaNome() + " hai scelto di pescare e poi rispondere")
                        aggiungiCarteGiocatore(giocatore) #Il giocatore pesca _carteDaPescare carte
                        _carteDaPescare = 0 #Reset di _carteDaPescare

                        visualizzaManoGiocatore(giocatore) #Visualizza la mano del giocatore
                        giocaCarta(giocatore, ultimaCartaCimitero)
                        #TODO controllo più carte da giocare

                else: #Se il giocatore NON può rispondere allora pesca _carteDaPescare carte
                    print(giocatore.visualizzaNome() + " hai pescato " + str(_carteDaPescare) + ", ora puoi giocare")
                    aggiungiCarteGiocatore(giocatore) #Il giocatore pesca _carteDaPescare carte
                    _carteDaPescare = 0 #Reset di _carteDaPescare

                    visualizzaManoGiocatore(giocatore) #Visualizza la mano del giocatore
                    giocaCarta(giocatore, ultimaCartaCimitero)
                    #TODO controllo più carte da giocare

            else: #Se NON ci sono carte da pescare dai turni precedenti
                visualizzaManoGiocatore(giocatore) #Visualizza la mano del giocatore
                giocaCarta(giocatore, ultimaCartaCimitero)
                #TODO controllo più carte da giocare

        else: #Se il giocatore NON può giocare con le carte che ha in mano
            if _carteDaPescare == 0: _carteDaPescare = 1

            print(giocatore.visualizzaNome() + " non hai carte con cui giocare, ora peschi " + str(_carteDaPescare) + " carte")
            aggiungiCarteGiocatore(giocatore) #Il giocatore pesca _carteDaPescare carte
            _carteDaPescare = 0 #Reset di _carteDaPescare

            #Controllo della mano del giocatore per vedere se può giocare dopo aver pescato
            if puoGiocare(giocatore, ultimaCartaCimitero): #Se il giocatore può giocare con le carte che ha in mano
                visualizzaManoGiocatore(giocatore) #Visualizza la mano del giocatore
                giocaCarta(giocatore, ultimaCartaCimitero)
                #TODO controllo più carte da giocare

        if len(giocatore.visualizzaMano()) == 0:
            print(giocatore.visualizzaNome() + " HA VINTO!!")
            return
        elif len(giocatore.visualizzaMano()) == 1:
            print(giocatore.visualizzaNome() + " urla UNO!!")

        _turno += 1


if __name__ == "__main__":
    from Carta import Carta
    from Giocatore import Giocatore
    import random

    #TODO commentare tutto
    
    _colori = ["blu", "rosso", "verde", "giallo"]
    _mazzo = generaMazzo()
    _cimitero = [] #iughioh eazter eggg
    _giocatori = generaGiocatori()

    _turno = 0
    _carteDaPescare = 0
    _carteSaltaTurno = 0

    assegnaCarteIniziali()
