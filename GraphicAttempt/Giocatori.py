"""
Classe Giocatore
"""
from Carta import Carta

class Giocatore:
    _nome = ""
    _mano = []

    def __init__(self, nome, mano):
        self.assegnaNome(nome)
        self.assegnaMano(mano)

    def assegnaNome(self, nome):
        self._nome = nome.capitalize()

    def visualizzaNome(self):
        return self._nome

    def assegnaMano(self, mano):
        self._mano = mano

    def visualizzaMano(self):
        return self._mano

    def visualizzaMano(self):
        mano = []
        for carta in self._mano:
            mano.append(carta.visualizzaValore() + " " + carta.visualizzaColore())
        return mano

    def sceltaCartaDaGiocare(self, mazzo):
        return None #questo metodo verrà sovrascritto dai metodi delle subclassi
    
    def numeroCarteInMano(self):
        return len(self._mano)
    
    def vuoleRispondere(self):
        return True

class Giocatore_Umano(Giocatore):
    super().__init__(self, nome, mano)

    def sceltaCartaDaGiocare(self):
            print("Scegli una carta da giocare: ")
            indiceCarta = chiediCarta(self).replace(',', '').split()
            mano = giocatore.visualizzaMano()

            if len(indiceCarta)==1:
                try:
                    indiceCarta = int(indiceCarta)
                except:
                    print("Inserisci un intero!")
                    giocaCarte(mano, ultimaCartaCimitero)
                    self.sceltaCarta()

                if indiceCarta < 0 or indiceCarta > (len(mano) - 1):
                    print("Scegli una carta esistente!")
                    giocaCarte(mano, ultimaCartaCimitero)
                    self.sceltaCarta()

            else:
                for i in range(len(indiceCarta)):
                    try:
                        indiceCarta = int(indiceCarta)
                    except:
                        print("Inserisci un intero!")
                        giocaCarte(mano, ultimaCartaCimitero)
                        self.sceltaCarta()

                if indiceCarta < 0 or indiceCarta > (len(mano) - 1):
                    print("Scegli una carta esistente!")
                    giocaCarte(mano, ultimaCartaCimitero)
                    self.sceltaCarta()
            carta = [mano[indice] for indice in indiceCarta]

            return carta
        
    def scegliColore(self):
            global _colori
            print("Scegli un colore:")
            indiceCarta = 0

            for colore in _colori:
                print(str(indiceCarta) + " - " + colore.capitalize())
                indiceCarta += 1
            colore = input("Inserisci indice del colore scelto: ")

            try:
                colore = int(colore)
            except:
                print("Inserisci un intero!")
                self.scegliColore()

            if colore < 0 or colore > 3:
                print('Inserisci un intero corrispondente ad uno degli indici delle carte!')
                self.scegliColore()

            return colore
        
    def vuoleRispondere(self):
        vuoleRispondere = True if str(input("Hai la possibilità di rispondere, vuoi farlo? (S/n)\n")).strip().lower() != 'n' else False

        return vuoleRispondere

class Giocatore_IA(Giocatore):
    '''
    carte_speciali = ["pesca_quattro", "pesca_due", "inverti", "stop", "cambio_colore"]
    carte_normali = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    colori = ['nero', 'blu',  'giallo', 'rosso','verde'].    blu rosso verde giallo
    '''
    def __init__(self):
        super().__init__(self, nome, mano, cleverness)
        self._mano = self.ordinaMano()
        self._furbo = furbo #True per un IA human-like (che quindi applicherà strategie di ottimizzazione)
                                  #False altrimenti
    def Furbo(self):
        return self._furbo

    def assegnaFurbo(self, cleverness):
        self.furbo = cleverness

    def scegliColore(self):
        global _colori

        if not self.Furbo():
            colore = _colori[random.randint(0, 4)] #se l'IA non è furba sceglie un colore casuale
        else:
            blu, rosso, verde, giallo = [0, 'blu'], [0,'rosso'], [0, 'verde'], [0, 'giallo'] #sonst sceglie il colore che ha più (/meno) abbondante in mano
            for carta in self.visualizzaMano():
                if carta.getColore() == blu: blu[0] +=1
                elif carta.getColore() == rosso: rosso[0] +=1
                elif carta.getColore() == verde: verde[0] +=1
                elif carta.getColore() == giallo: giallo[0] +=1
        colore = max(blu, rosso, verde, giallo)[1]

        return colore

    '''ora inserisco tutta una serie di metodi che consentono all'IA di procedere in maniera intelligente e adottare strategie di gioco'''
    def CarteProssimoGiocatores(self):
        #controlla quante carte ha il giocatore successivo
        prossimo_turno = visualizzaTurno(turno, giocatori)+1
        giocatore = _giocatori[prossimo_turno]
        return giocatore.numeroCarteInMano()
        
    def ordinaMano(self):
       #l'algoritmo a inizio partita ordina le carte della mano secondo il seguente ordiamento:
       #prima compaiono le carte speciali ["pesca_quattro", "pesca_due", "inverti", "stop", "cambio_colore"]
       #poi le carte normali ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'].
       #All'interno di ciascuna sottosezione è ripettato l'ordine['nero', 'blu',  'giallo', 'rosso','verde']
       #in questo modo poi per la scelta della carta da giocare sarà necessario un numero minore di operazioni e minor memoria
       mano = self.visualizzaMano()
       # assegno a ciascuna carta due punteggi : uno legato al colore e uno legato al valore
       for i in range(1, len(mano)):
           punteggio_valore = carte_speciali.index[mano[i].visualizzaValore()] if mano[i].visualizzaValore() in carte_speciali else carte_normali.index[mano[i].visualizzaValore()]+5
           punteggio_colore = colori.index[mano[i].visualizzaColore()]
           carta = mano[i]
           #con un algoritmo ispirato all'Insertion Sort riposiziono le carte nella mano
           #l'operazione sarà computazionalmente intensiva con la mano iniziale, poi a sforzo computazionale minimo
           #in virtuù della natura quasi ordinata delle carte della mano
           j = i
           punteggio_valore_J-1 == carte_speciali.index[mano[j-1].visualizzaValore()] if mano[j-1].visualizzaValore() in carte_speciali else carte_normali.index[mano[j-1].visualizzaValore()]+5
           punteggio_colore_J-1 == colori.index[mano[j-1].visualizzaColore()]

           while j > 0 and punteggio_valore_J-1 >= punteggio_valore_J-1 and punteggio_colore_J-1 > punteggio_colore:
               mano[j] = mano[j-1]
               j = j-1
               mano[j] = carta

    def Buttabili(self, mazzo):
        #buttabili ritorna un dizionario con come chiave i valori e come valore una lista [indice_prima_comparsa, n_carte_buttabili]
        mano = self.visualizzaMano()
        ultima_carta_colore , ultima_carta_valore = ultimaCartaCimitero.visualizzaColore(), ultimaCartaCimitero.visualizzaValore()
        buttabili = {}
        for carta in mano: buttabili[carta.visualizzaValore()]=[] if carta.visualizzaValore() not in buttabili i_esimo = 0

        while i_esimo in range(len(mano)):
            carta = mano[i_esimo]
            valore = carta.visualizzaValore()

            if valore == ultima_carta_valore:
                buttabili[valore].append(i_esimo)
                n_carte = 1
                j_esimo = i_esimo + 1
                while j_esimo <len(mano) and mano[j_esimo]==valore:
                    n_carte += 1
                buttabili[valore].append(n_carte)
                i_esimo  += n_carte
                colore = carta.visualizzaColore()

            elif colore == ultima_carta_colore:
                if buttabili[valore]==[]:
                    buttabili[valore] += [i_esimo, 1]
                i_esimo +=1

            else: i_esimo +=1

    def maxButtabili(self, type_carte):
        # type_carte = 'normali' o 'speciali'
        buttabili = self.Buttabili(mano)
        valori_carte = carte_normali if type_carte =='normali' else carte_speciali+carte_normali
        valore = ''

        for chiave in valori_carte:
            if key in buttabili:
                if buttabili[chiave][1] > n_carte:
                    valore = chiave
                elif buttabili[chiave][1] == n_carte:
                    valore = [valore].append(key)

        if valore == '':
            return ()
        elif type(valore)==str:
            return (valore, buttabili[valore][0],buttabili[valore][1])
        else:
            return ([val for val in valore], [buttabili[val][0] for val in valore], buttabili[valore[0]][1])

    def buttaColoreAbbondante(self):
        colore = self.scegliColore()
        i = 0
        mano = self.visualizzaMano()

        while i in range(len(mano)):
            if mano[i].colore == colore:
                return mano[i]
            else:
                i += 1

    def scegliColore(self):
        '''visto che nel gioco ho delle IA sviluppo la funzione
        come metodo della classe giocatore:
        il giocatore umano manterrà la funzione già data,
        l'IA userà questo'''
        if not self.Furbo:
            colore = random.choice(_colori)
        else:
            '''il sistema furbo consiste nel segliere il colore più presente nella mano'''
            mano = self.visualizzaMano()
            colori_carte = {}
            for carta in mano:
                if carta.colore not in colori_carte:
                    colori_carte[carta.colore] = 1
                else:
                    colori_carte[carta.colore] += 1
            colore = max(colori_carte)
        return colore

    def sceltaCartaDaGiocare():
        carteSpeciali = ["pesca_due", "pesca_quattro", "inverti", "stop", "cambio_colore"] #meglio metterlo variabile globale
        mano = self.visualizzaMano()
        ultimaCartaCimitero = _cimitero[-1]

        #se non ricordo male in controlloCarta(), dovrebbeRispondere = (ultimaCartaCimitero.visualizzaValore() in carteSpeciali)
        dovrebbeRispondere = (ultimaCartaCimitero.visualizzaValore() in carteSpeciali)

        if not self.Furbo():
            for index in range(len(mano), 0, -1):
                carta = mano[index]
                if controlloCarta(carta, ultimaCartaCimitero, dovrebbeRispondere):
                    mano.pop(index)
                    self.assegnaMano(mano)
                    return [carta]
            carta =  pesca()

            while not controlloCarta(carta, ultimaCartaCimitero, dovrebbeRispondere):
                carta =  pesca()

            return [carta]

        else:
            mano = self.ordinaMano()
            # se è furbo, usa le seguenti strategie, nel seguente ordine:
            # 1. se il giocatore successivo ha <3/4 carte, quante più carte possibili partendo da quelle speciali
            # 2. altrimenti lo fa partendo dalle carte normali
            # 3. butta la prima carta utile appartenente al colore PIù rappresentato della mano
            # 4. butta la prima carta utile
            carte_giocatore_successivo = self.CarteProssimoGiocatore()
            tupla = self.maxButtabili('speciali')

            if carte_giocatore_successivo < 4:
                if tupla != None and type(tupla[0])!=list:
                   carte = []
                   for i in range(tupla[1], tupla[1]+tupla[2]+1): carte.append(mano.pop[i])

                   return carte

                elif tupla != None and type(tupla[0])==list:
                    #creo un mini "codice di priorità" a seconda che il giocatore successivo abbia solo una carta o 2 o 3
                    emergency = (len(tupla[0])%carte_next_players) - 1
                    carte = []
                    for i in range(tupla[1][emergency], tupla[1][emergency]+tupla[2]+1): carte.append(mano.pop[i])
                    
                    return carte
                   
                else:
                    cartaDaGiocare = pescaCarte()
                    # counter = 1
                    return sceltaCartaDaGiocare(self, cartaDaGiocare)

            else:
                if tupla != None and type(tupla[0])!=list and tupla[2]!=1:
                   carte = []
                   for i in range(tupla[1], tupla[1]+tupla[2]+1): carte.append(mano.pop[i])
                   return carte

                elif tupla != None and tupla[2]==1:
                   return buttaColoreAbbondante(self)            
                else:
                   pescaCarte()
                   return sceltaCartaDaGiocare(self, ultimaCartaCimitero)