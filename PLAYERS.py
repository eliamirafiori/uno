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
        self.setNome(nome)
        self.setMano(mano)
        '''_giocatori.append(self)'''

    def setNome(self, nome):
        self._nome = nome.capitalize()

    def getNome(self):
        return self._nome

    def setMano(self, mano):
        self._mano = mano

    def getMano(self):
        return self._mano

    def visualizzaMano(self):
        mano = []
        for carta in self._mano:
            mano.append(carta.getValore() + " " + carta.getColore())
        return mano

    def sceltaCartaDaGiocare(self, mazzo):
        return None #questo metodo verrà sovrascritto dai metodi delle subclassi

   ''' def giocatori():
        return _giocatori'''

class Giocatore_Umano(Giocatore):
    super().__init__(self, nome, mano)

    def sceltaCartaDaGiocare(self, mazzo):
        index = int(input("Index carta da giocare: ")) - 1
        mano = self.getMano()
    
        if index < len(mano) and index >= 0:
            cartaDaGiocare = mano[index]

            if controlloCarte(mazzo.ultimaCarta(), cartaDaGiocare):
                mano.pop(index)

                self.setMano(mano)
            
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

    def __init__(self, mano, nome, cleverness):
        self._mano = mano
        self._nome = nome
        self._cleverness = clever #True per un IA human-like (che quindi applicherà strategie di ottimizzazione)
                                  #False altrimenti

    def isClever(self):
        return self._cleverness

    '''ora inserisco tutta una serie di metodi che consentono all'IA di procedere in maniera intelligente e adottare strategie di gioco'''

    def CarteNextPlayers(self):
        #controlla quante carte ha il giocatore successivo
        next_turno = getTurno(turno, giocatori)+1
        giocatore = _giocatori[next_turno]
        return len(giocatore.getMano())

    def getSpecial(self):
        #cerca quante carte speciali (+4, +2, inverti, cambia colore) si abbiano e le memorizza in un dizionario, assieme alla posizione
        speciali = {}
        carteSpeciali = ["pesca_quattro", "pesca_due", "inverti", "stop", "cambio_colore"]
        mano = self.getMano()
        for special in carteSpeciali:
            speciali[special]=[]
            for index in len(mano):
                if mano[index].getValore()==special:
                    speciali[special].append(index)
        return speciali

    def getMultipleSpecial(self):
        #cerca se è possibile giocare 2 carte, e se è possibile ritorna quali sono (colore, valore, index)
        #il criterio è questo: vale doppia se entrambe le carte hanno lo stesso valore e almeno una di esse ha lo stesso colore dell'ultima carta
        color = mazzo.ultimaCarta().getColore()
        mano = self.getMano()
        multipleSpecial = False
        #per prima cosa controllo tra le carte speciali
        speciali = self.getSpecial()
        while multiple==False:
            for speciale in speciali:
                elements = speciale[speciali]
                if len(elements)>1:
                    for i in range(len(elements)):
                        if mano[elemets[i]].getColore()==color:
                            multiple = tuple(mano[elements[i]], mano[elements[(i+1)//len(elements)])
                            return multiple
                        else: continue
            break
        return multipleSpecial
        #adesso controllo tra quelle normali

    def getMultiple(self):
        color = mazzo.ultimaCarta().getColore()
        mano = self.getMano()
        multiple = False
        while multiple==False:
            for index in range(len(mano)):
                if mano[i].getColore()==color:
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
                        if cartaDaGiocare.getColore() == colore:
                            return [cartaDaGiocare]
                if lastUsefulIndex != None:
                    cartaDaGiocare = mano[lastUsefulIndex]
                    return [cartaDaGiocare]
                else:
                    pescaCarte(self, mazzo, 1)
                    return sceltaCartaDaGiocare(self, mazzo.ultimaCarta())
                    
                
            
                    
                    
            
    
