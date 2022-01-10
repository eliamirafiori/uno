"""
Classe Giocatore
"""

#proposta di codice:
#mi sono resa conto che trattare i giocatori umani diversamente dalle IA potrebbe rendere la cosa
#macchinosa, quindi propongo di fare una superclasse Giocatore con 2 subclassi:
#Giocatore_Umano e Giocatore_IA. In questo modo è più facile ovviare a cose come
#il fatto che il codice per scegliere la carta o il tipo di strategie utilizzabili
#saranno inevitabilmente diverse

#propongo anche/quindi di inserire il metodo SceltaCartaDaGiocatore (al moento nel Main)
#direttamente tra i metodi del giocatore
from Carta import Carta

class Giocatore:
    _nome = ""
    '''_giocatori=[] #idea stupida ma la butto giù'''
    _mano = []

    def __init__(self, nome, mano):
        self.assegnaNome(nome)
        self.assegnaMano(mano)
        '''_giocatori.append(self)'''

    def assegnaNome(self, nome):
        self._nome = nome.capitalize()

    def visualizzaNome(self):
        return self._nome

    def assegnaMano(self, mano):
        self._mano = mano

    def assegnaMano(self):
        return self._mano

    def visualizzaMano(self):
        mano = []
        for carta in self._mano:
            mano.append(carta.visualizzaValore() + " " + carta.visualizzaColore())
        return mano

    def sceltaCartaDaGiocare(self, mazzo):
        return None #questo metodo verrà sovrascritto dai metodi delle subclassi

   ''' def giocatori():
        return _giocatori'''

class Giocatore_Umano(Giocatore):
    super().__init__(self, nome, mano)

    def sceltaCartaDaGiocare(self, mazzo):
        index = int(input("Index carta da giocare: ")) - 1
        mano = self.visualizzaMano()
    
        if index < len(mano) and index >= 0:
            cartaDaGiocare = mano[index]

            if controlloCarte(mazzo.ultimaCarta(), cartaDaGiocare):
                mano.pop(index)

                self.assegnaMano(mano)
            
                #controllo che sia un cambio colore o +4, nel caso faccio funzione per cambiare colore

                return [cartaDaGiocare]
        
            else:
                print("Scegli un'altra carta! Mona!")
                return sceltaCartaDaGiocare(self, mazzo.ultimaCarta())
        
        elif index == -1:
            pescaCarte(self, mazzo, 1)
            return [mazzo.ultimaCarta()]
        
        else:
            print("Non hai tutte queste carte! Poraccio...")
            return sceltaCartaDaGiocare(self, mazzo.ultimaCarta())

class Giocatore_IA(Giocatore):

    #forse devo farle maiuscole?
    carte_speciali = ["pesca_quattro", "pesca_due", "inverti", "stop", "cambio_colore"]
    carte_normali = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    colori = ['nero', 'blu',  'giallo', 'rosso','verde']


    super().__init__(self, nome, mano, cleverness):
        self._mano = self.ordinaMano()
        self._furbo = furbo #True per un IA human-like (che quindi applicherà strategie di ottimizzazione)
                                  #False altrimenti

    def Furbo(self):
        return self._furbo

    '''ora inserisco tutta una serie di metodi che consentono all'IA di procedere in maniera intelligente e adottare strategie di gioco'''

   def CarteProssimoGiocatores(self):
        #controlla quante carte ha il giocatore successivo
        prossimo_turno = visualizzaTurno(turno, giocatori)+1
        giocatore = _giocatori[prossimo_turno]
        return len(giocatore.visualizzaMano())

    '''def visualizzaSpecial(self):
        #cerca quante carte speciali (+4, +2, inverti, cambia colore) si abbiano e le memorizza in un dizionario, assieme alla posizione
        speciali = {}
        carteSpeciali = ["pesca_quattro", "pesca_due", "inverti", "stop", "cambio_colore"]
        mano = self.visualizzaMano()
        for special in carteSpeciali:
            speciali[special]=[]
            for index in len(mano):
                if mano[index].visualizzaValore()==special:
                    speciali[special].append(index)
        return speciali

    def visualizzaMultipleSpecial(self):
        #cerca se è possibile giocare 2 carte, e se è possibile ritorna quali sono (colore, valore, index)
        #il criterio è questo: vale doppia se entrambe le carte hanno lo stesso valore e almeno una di esse ha lo stesso colore dell'ultima carta
        color = mazzo.ultimaCarta().visualizzaColore()
        mano = self.visualizzaMano()
        multipleSpecial = False
        #per prima cosa controllo tra le carte speciali
        speciali = self.visualizzaSpecial()
        while multiple==False:
            for speciale in speciali:
                elements = speciale[speciali]
                if len(elements)>1:
                    for i in range(len(elements)):
                        if mano[elemets[i]].visualizzaColore()==color:
                            multiple = tuple(mano[elements[i]], mano[elements[(i+1)//len(elements)])
                            return multiple
                        else: continue
            break
        return multipleSpecial
        #adesso controllo tra quelle normali

    def visualizzaMultiple(self):
        color = mazzo.ultimaCarta().visualizzaColore()
        mano = self.visualizzaMano()
        multiple = False
        while multiple==False:
            for index in range(len(mano)):
                if mano[i].get
                Colore()==color:
                    valore = mano[i].getValore()
                    for j in range(len(mano)):
                        if mano[j].getValore()==valore:
                            multiple = tuple(mano[i], mano[j])
                            return multiple
                        else: continue
            break
        return multiple

    def coloriNellaMano(self):
        blu, rosso, verde, giallo = 0, 0, 0, 0
        mano = self.getMano()
        for carta in mano:
            if carta.getColore() == 'blu':
                blu +=1
            elif carta.getColore() == 'rosso':
                rosso +=1
            elif carta.getColore() == 'verde':
                verde += 1
            elif carta.getColore() == 'giallo':
                giallo += 1
            else:
                continue
        return (blu, rosso, verde, giallo)
                        
    def sceltaCartaDaGiocare(self, mazzo):
        mano = self.getMano()
        clever = self.isClever()

        if not clever:
            for index in len(mano):
                #controlla tra tutte le carte se ce ne sono di accettabili, e butta la prima buona
                cartaDaGiocare = mano[index]
                if controlloCarte(mazzo.ultimaCarta(), cartaDaGiocare):
                    mano.pop(index)
                    self.setMano(mano)
                    return [cartaDaGiocare]
            #se non trova una carta accettabile, continua a pescare fino a quando non ne trova una buona
            cartaDaGiocare =  self.pesca(1, mano)
            while not controlloCarte(mazzo.ultimaCarta(), cartaDaGiocare):
                cartaDaGiocare =  self.pesca(1, mano)
            return [cartaDaGiocare]
        else:
            #se è furbo, usa le seguenti strategie, nel seguente ordine:
            # 1. se il giocatore successivo ha <3/4 carte, butta un +2/+4 2 volte
            # 2. se possibile, butta un +2/+4/...
            # 3. butta 2 carte
            # 4. butta la prima carta utile appartenente al colore MENO rappresentato della mano
            # 5. butta la prima carta utile
            multipleSpecial, carteNextPlayer = self.getMultipleSpecial(), self.CarteNextPlayers(self)
            if (multipleSpecial) != False and (carteNextPlayer < 4):
                cartaDaGiocare_1, cartaDaGiocare_2 = mano[multipleSpecial[1]], mano[multipleSpecial[2]]
                return [cartaDaGiocare_1, cartaDaGiocare_2]
            
            special = self.getSpecial()    
            elif (special !={}) and (carteNextPlayer < 4):
                for key in special:
                    for index in special[key]:
                        cartaDaGiocare = mano[index]
                        if controlloCarte(mazzo.ultimaCarta(), cartaDaGiocare):
                            return [cartaDaGiocare]
                    
            multiple = self.getMultiple()
            elif multiple != False:
                cartaDaGiocare_1, cartaDaGiocare_2 = mano[multiple[1]], mano[multiple[2]]
                return [cartaDaGiocare_1, cartaDaGiocare_2]

            else:
                #implemento assieme i punti 4 e 5
                #il programma memorizza l'ultimo indice utile la cui carta non sia del colore meno rappresentato della mano
                #e se alla fine non trova una carta di tale colore sceglie l'ultima utile
                #se non ce ne sono di utili, pesca

                colori = self.ColoriNellaMano()
                colore = colori.index(min(colori))
                lastUsefulIndex = None
                for index in range(len(mano)):
                    cartaDaGiocare = mano[index]
                    if controlloCarte(mazzo.ultimaCarta(), cartaDaGiocare):
                        lastUsefulIndex = index                      
                        if cartaDaGiocare.visualizzaColore() == colore:
                            return [cartaDaGiocare]
                if lastUsefulIndex != None:
                    cartaDaGiocare = mano[lastUsefulIndex]
                    return [cartaDaGiocare]
                else:
                    pescaCarte(self, mazzo, 1)
                    return sceltaCartaDaGiocare(self, mazzo.ultimaCarta())
                    '''
   
   def ordinaMano(self):

       #l'algoritmo a inizio partita ordina le carte della mano secondo il seguente ordiamento:
       #prima compaiono le carte speciali ["pesca_quattro", "pesca_due", "inverti", "stop", "cambio_colore"]
       #poi le carte normali ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'].
       #All'interno di ciascuna sottosezione è ripettato l'ordine['nero', 'blu',  'giallo', 'rosso','verde']
       #in questo modo poi per la scelta della carta da giocare sarà necessario un numero minore di operazioni e minor memoria

       mano = self.visualizzaMano()
       
       ''' mi sono stufata, le uso un sacco, le salvo a inizio classe!

       carte_speciali = ["pesca_quattro", "pesca_due", "inverti", "stop", "cambio_colore"]
       carte_normali = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
       colori = ['nero', 'blu',  'giallo', 'rosso','verde']'''

       # l'ordinamento in questione è sostanzialmente una variante di BubbleSort, con ordine determinato prima da se una carta è speciale o meno
       # e poi dal suo colore.

       # PROBLEMA : BubbleSort smette di essere efficiente nel giro di relativamente poco. Potrebbe essere utile risistemare il tutto in modo che si basi
       # su InsertionSort, CocktailShakerSort (BubbleSort ma che passa da inizio a fine e poi da fine a inizio) o GnomeSort.
       # 2 considerazioni su una possibile ed eventuale implementazione di ciò:
       # 1. come farlo con un sistema a 2 confronti?
       # 2. vale la pena affidarsi ad un codice di quelli complessi se poi per sostanzialmente tutto il gioco si ha a che fare con una mano QUASI ORDINATA
       # (== dove soltanto un elemento è fuori posto)?
        ''' CODICE USATO COME GUIDA PER L'IMPLEMENTAZIONE IN INSERTIONSORT ! 
    def insertsort(array):
                for removed_index in range(1, len(array)):
                removed_value = array[removed_index]
                insert_index = removed_index
                while insert_index > 0 and array[insert_index - 1] > removed_value:
                    array[insert_index] = array[insert_index - 1]
                    insert_index = insert_index - 1
                    array[insert_index] = removed_value '''


       for i in range(1, len(mano)):
           punteggio_valore = carte_speciali.index[mano[i].visualizzaValore()] if mano[i].visualizzaValore() in carte_speciali else carte_normali.index[mano[i].visualizzaValore()]+5
           punteggio_colore = colori.index[mano[i].visualizzaColore()]
           carta = mano[i]

           j = i
           punteggio_valore_J-1 = carte_speciali.index[mano[j-1].visualizzaValore()] if mano[j-1].visualizzaValore() in carte_speciali else carte_normali.index[mano[j-1].visualizzaValore()]+5
           punteggio_colore_J-1 = colori.index[mano[j-1].visualizzaColore()]
           while j > 0 and punteggio_valore_J-1 >= punteggio_valore_J-1 and punteggio_colore_J-1 > punteggio_colore:
               mano[j] = mano[j-1]
               j = j-1
               mano[j] = carta
           
    ### CODICE ORIGINALE IN BUBBLESORT !!!
    ###for i in range(len(mano)-1):
    ###    for j in range(0, n-i-1):

               #ad ogni carta è associato un doppio punteggio numerico (valore_numerico_carta , valore_numerico_colore)
               # ["pesca_quattro", "pesca_due", "inverti", "stop", "cambio_colore",'0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
               # = [0                 1           2          3        4             5    6    7    8    9    10   11   12   13   14]

               # ['nero', 'blu',  'giallo', 'rosso','verde']
               #    0      1        2         3       4
    ###        valore_carta_J = carte_speciali.index[mano[j].visualizzaValore()] if mano[j].visualizzaValore() in carte_speciali else carte_normali.index[mano[j].visualizzaValore()]+5
    ###        valore_colore_J = colori.index[mano[j].visualizzaColore()]

    ###        valore_carta_J+1 = carte_speciali.index[mano[j+1].visualizzaValore()] if mano[j+1].visualizzaValore() in carte_speciali else carte_normali.index[mano[j+1].visualizzaValore()]+5
    ###        valore_colore_J+1 = colori.index[mano[j+1].visualizzaColore()]

    ###        if (valore_carta_J >= valore_carta_J+1) and (valore_colore_J+1 >  valore_colore_J+1):
    ###            mano[j], mano[j+1] = mano[j+1], mano[j]
    ### return mano

            
    def Buttabili(self, mazzo):
        #ho pensato "ho troppi problemi! Mi creo una struttura di supporto per un metodo successivo!
        #buttabili ritorna un dizionario con come chiave i valori e come valore una lista [indice_prima_comparsa, n_carte_buttabili]
        mano = self.visualizzaMano()
        ultima_carta_colore , ultima_carta_valore = ultimaCartaCimitero.visualizzaColore(), ultimaCartaCimitero.visualizzaValore()
        buttabili = {}
        for carta in mano: buttabili[carta.visualizzaValore()]=[] if carta.visualizzaValore() not in buttabili
        i_esimo = 0
        
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
        #mi sono scazzata. Ho usato il dizionario come struttura di supporto e ho differenziato la ricerca tra carte normali e speciali
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
        #prima ordina i colori in una lista dal più frequente al meno frequente
        # e poi, in presenza di più blocchi di carte buttabili, seleziona quello col maggior numero di carte di colore frequente
        mano = self.visualizzaMano()
        riferimento = self.maxButtabili('normali')

        conta_colore = {}
        for colore in colori[1:]: conta_colore[colore] = 0
        for carta in mano:
            conta_colore[carta.visualizzaColore()] += 1
        colori_ordinati = colori[1:]
        for i in range(1, len(colori_ordinati)):
            for j in range(i, len(colori_ordinati)):
                if conta_colore[colori_ordinati[j]) < conta_colore[colori_ordinati[j-1]):
                    colori_ordinati[j], colori_ordinati[j-1] = colori_ordinati[j-1], colori_ordinati[j]
        del(color_counter)

        for colore in colori_ordinati:
            lunghezza = riferimento[0]
            for i in range(len(lunghezza)):
                if mano[riferimento[1][i]].visualizzaColore()==colore:
                    return mano[riferimento[1][i]]
        return mano[riferimento[1][-1]]
                
    def sceltaCartaDaGiocare(self, mazzo):
        mano = self.visualizzaMano()
        furbo = self.Furbo()
        ultimaCartaCimitero = (_cimitero[len(_cimitero) - 1]

        if not furbo:
            for index in range(len(mano), 0, -1):
                #controlla tra tutte le carte se ce ne sono di accettabili, e butta la prima buona
                cartaDaGiocare = mano[index]
                if controlloCarte(ultimaCartaCimitero, cartaDaGiocare):
                    mano.pop(index)
                    self.assegnaMano(mano)
                    return [cartaDaGiocare]
            #se non trova una carta accettabile, continua a pescare fino a quando non ne trova una buona
            cartaDaGiocare =  self.pesca(1, mano)
            while not controlloCarte(ultimaCartaCimitero, cartaDaGiocare):
                cartaDaGiocare =  self.pesca(1, mano)
            return [cartaDaGiocare]
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
                    pescaCarte(self, mazzo, 1)
                    # counter = 1
                    return sceltaCartaDaGiocare(self, ultimaCartaCimitero)
                    ''' PROBLEMA!!!! Va avanti a ripetizione! fino a quando non trova una carta buttabile. Va bene?'''
            else:
                if tupla != None and and type(tupla[0])!=list and tupla[2]!=1:
                    carte = []
                    for i in range(tupla[1], tupla[1]+tupla[2]+1): carte.append(mano.pop[i])
                    return carte
                elif tupla != None and and type(tupla[0])==list: #DA SISTEMARE
                elif tupla != None and tupla[2]==1:
                    return buttaColoreAbbondante(self)            
                else:
                    pescaCarte(self, mazzo, 1)
                    # counter = 1
                    return sceltaCartaDaGiocare(self, ultimaCartaCimitero)
                    
                    
                
                
                
            
        
            
       
                    
                
            
                    
                    
            
    
