import pygame
import tkinter as tk 
from Giocatori import Giocatore
from Carta import Carta

pygame.init()
pygame.font.init()
FONT = pygame.font.SysFont('Comic Sans MS', 30)
TIPO_FILE = '.PNG' # stabilisco già la tipologia d'immagine che verrà usata nel progetto

#inizializzo lo SCHERMO, con colore di default verde
pygame.display.init()
WIDTH, HEIGHT = 1100, 800
SCHERMO = pygame.display.set_mode((WIDTH, HEIGHT))
RED_VALUE , GREEN_VALUE, BLUE_VALUE = 0, 127, 0
SCHERMO.fill((RED_VALUE, GREEN_VALUE, BLUE_VALUE))
pygame.display.flip()


def visualizzaGiocatori():
  '''la funzione collega i giocatori alla posizione in lista
  in modo da identificarne univocamente la posizione sul campo
  e a seconda che sia il suo turno oppure no o che abbia carte oppure no
  visualizza le carte (una carta coperta + il numero di carte avute dal giocatore)
  più una bordatura rossa per il giocatore turnante '''
  #CARTA_COPERTA = 'blablaname.png'
  alto, sinistra = 200, 100
  altezza = 50
  turno = visualizzaTurno(_turno)
  for i in range(len(_giocatori)):
    giocatore= _giocatori[i]
    n_carte = giocatore.numeroCarteInMano()
    if n_carte > 0:
        x, y = sinistra, alto+i*altezza #ricavo le coordinate di dove mettere le carte
        text = giocatore.visualizzaNome()+': '+str(n_carte)
        testo = FONT.render(text, False, (255, 0, 0)) #ci scrive sopra in rosso il numero di carte del giocatore
        SCHERMO.blit(testo, (x, y)) 
        if turno == i:
            pygame.draw.line(SCHERMO, (255, 255, 0), (x-5, y-5), (x-5, y+5), 7) #se è il turno del giocatore, a sx compare una linea gialla spessa

def mostraCartaButtata(carta):
    #se c'è una sola carta da buttare carica la rispettiva immagine
    if type(carta) != list:
        nome_carta = carta.visualizzaColore()+carta.visualizzaValore()+TIPO_FILE
        immagine_carta = pygame.image.load(nome_carta)
        SCHERMO.blit(immagine_carta, (500, 200))
        return pygame.display.update()
        pygame.time.wait(1500) #prima di aggiornare lo SCHERMO a eventuali carte successive aspetta un secondo e mezzo
    else:
        #altrimenti la funzione si applica in maniera ricorsiva
        #stampando le carte dall'ultima alla prima
        while type(carta) != list:
            mostraCartaButtata(carta[:-1])
            
def mostraMazzo():
    nome_carta = str("retro_carta"+TIPO_FILE)
    immagine_carta = pygame.image.load(nome_carta)
    SCHERMO.blit(immagine_carta, (700, 200))
    return pygame.display.update()
  
def visualizzaTesto(testo):
    testo = FONT.render(text, False, (0, 0, 0))
    SCHERMO.blit(testo, 500, 300)
    SCHERMO.wait(1500)
    
def visualizzaTestoSpeciale(testo):
    FONT = pygame.font.SysFont('Comic Sans MS', 60)
    testo = FONT.render(text, False, (255, 255, 0))
    SCHERMO.blit(testo, 500, 300)
    SCHERMO.wait(1500)
    FONT = pygame.font.SysFont('Comic Sans MS', 30)
    testo = FONT.render(text, False, (0, 0, 0))
  
        
def visualizzaCarteGiocatore(giocatore):
    mano=giocatore.visualizzaMano()
    x, y =320, 550
    slittamento = 50
    for i in range(len(mano)):
        carta = mano[i]
        nome_carta = carta.visualizzaColore()+carta.visualizzaValore()+TIPO_FILE
        immagine_carta = pygame.image.load(nome_carta)
        if i <= 15:
            SCHERMO.blit(immagine_carta, (x+slittamento*i, y))
            testo = FONT.render(str(i), False, (0, 0, 0)) #ci scrive sotto in rosso il numero di carte del giocatore
            SCHERMO.blit(testo, (x+slittamento*i, y+170))
        else:
            SCHERMO.blit(immagine_carta, (x+slittamento*(i-15), y-200))
            testo = FONT.render(str(i), False, (0, 0, 0)) #ci scrive sotto in rosso il numero di carte del giocatore
            SCHERMO.blit(testo, (x+slittamento*(i-15), y-30))
    return pygame.display.update()

def chiediCarta(giocatore):
    text = 'Digita il numero della carta che vuoi giocare: '
    testo = FONT.render(text, False, (0, 0, 0))
    SCHERMO.blit(testo, 500, 300)

    radice = tk.Tk()
    radice.geometry("200x120")

    def getTextInput():
        result=textExample.get(1.0, tk.END+"-1c")
        print(result)

    testoEsempio=tk.Text(radice, height=10)
    testoEsempio.pack()
    bottone=tk.Button(radice, height=1, width=10, text="Read", command=getTextInput)
    bottone.pack()
    radice.mainloop()
    return testoEsempio
  
  
def inizioGiocoGrafico():
    global _turno,  _carteDaPescare, _carteSaltaTurno

    while True:
        _turno += _carteSaltaTurno
        _carteSaltaTurno = 0
        #Visualizzo i giocatori sul campo
        visualizzaGiocatori()
        mostraMazzo()

        giocatore = _giocatori[visualizzaTurno(_turno)]
        ultimaCartaCimitero = _cimitero[len(_cimitero) - 1]
        #Visualizzo sia il mazzo che l'ultima carta buttata
        mostraCartaButtata(ultimaCartaCimitero)
        

        #Mostro il turni
        text = "\n\nE' il turno di " + giocatore.visualizzaNome()
        print(text)
        visualizzaTesto(text)

        #Indico l'ultima carta in tavolo
        text = "Ultima carta in tavola: " + ultimaCartaCimitero.visualizzaColore() + " " + ultimaCartaCimitero.visualizzaValore()
        print(text)
        visualizzaTesto(text)
        
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
                    text = giocatore.visualizzaNome() + " dovresti pescare " + str(_carteDaPescare)
                    print(text)
                    visualizzaTesto(text)
                    vuoleRispondere = giocatore.vuoleRispondere()

                    #Inserisco la parte grafica
                    mostraManoGiocatore()
                    text = giocatore.visualizzaNome() + " dovresti pescare " + str(_carteDaPescare)
                    print(text)
                    visualizzaTesto(text)
                    
                    #Controllo la scelta del giocatore se rispondere o pescare
                    if vuoleRispondere: #Se la scelta è quella di rispondere
                        text = giocatore.visualizzaNome() + " hai scelto di rispondere"
                        print(text)
                        visualizzaTesto(text)
                        visualizzaManoGiocatore(giocatore, True, ultimaCartaCimitero) #Visualizza la mano con cui può rispondere il giocatore
                        visualizzaCarteGiocatore(giocatore)
                        carta = giocaCarta(giocatore, ultimaCartaCimitero)
                        ultimaCartaCimitero = carta
                        visualizzaTesto("Scegli una carta da giocare")
                        mostraCartaButtata(carta)
                        

                    else: #Se la scelta è quella di pescare

                        #Inserisco ancora la parte grafica
                        text = giocatore.visualizzaNome() + " hai scelto di pescare e poi rispondere"
                        print(text)
                        visualizzaTesto(text)
                        
                        aggiungiCarteGiocatore(giocatore) #Il giocatore pesca _carteDaPescare carte
                        _carteDaPescare = 0 #Reset di _carteDaPescare
                        visualizzaManoGiocatore(giocatore) #Visualizza la mano del giocatore
                        visualizzaCarteGiocatore(text)
                        carta = giocaCarta(giocatore, ultimaCartaCimitero)
                        ultimaCartaCimitero = carta
                        mostraCartaButtata(carta)


                else: #Se il giocatore NON può rispondere allora pesca _carteDaPescare carte
                    text = giocatore.visualizzaNome() + " hai pescato " + str(_carteDaPescare) + ", ora puoi giocare"
                    print(text)
                    visualizzaTesto(text)
                    aggiungiCarteGiocatore(giocatore) #Il giocatore pesca _carteDaPescare carte
                    _carteDaPescare = 0 #Reset di _carteDaPescare

                    visualizzaManoGiocatore(giocatore) #Visualizza la mano del giocatore
                    visualizzaCarteGiocatore(giocatore)
                    carta = giocaCarta(giocatore, ultimaCartaCimitero)
                    ultimaCartaCimitero = carta
                    mostraCartaButtata(carta)
                    #TODO controllo più carte da giocare

            else: #Se NON ci sono carte da pescare dai turni precedenti
                visualizzaManoGiocatore(giocatore) #Visualizza la mano del giocatore
                visualizzaCarteGiocatore(giocatore)
                carta = giocaCarta(giocatore, ultimaCartaCimitero)
                ultimaCartaCimitero = carta
                mostraCartaButtata(carta)
                
                #TODO controllo più carte da giocare

        else: #Se il giocatore NON può giocare con le carte che ha in mano
            if _carteDaPescare == 0: _carteDaPescare = 1

            text = giocatore.visualizzaNome() + " non hai carte con cui giocare, ora peschi " + str(_carteDaPescare) + " carte"
            print(text)
            visualizzaTesto(text)
            aggiungiCarteGiocatore(giocatore) #Il giocatore pesca _carteDaPescare carte
            _carteDaPescare = 0 #Reset di _carteDaPescare

            #Controllo della mano del giocatore per vedere se può giocare dopo aver pescato
            if puoGiocare(giocatore, ultimaCartaCimitero): #Se il giocatore può giocare con le carte che ha in mano
                visualizzaManoGiocatore(giocatore) #Visualizza la mano del giocatore
                visualizzaCarteGiocatore(giocatore)
                carta = giocaCarta(giocatore, ultimaCartaCimitero)
                ultimaCartaCimitero = carta
                mostraCartaButtata(carta)
                
                #TODO controllo più carte da giocare

        if len(giocatore.visualizzaMano()) == 0:
            text = giocatore.visualizzaNome() + " HA VINTO!!"
            print(text)
            visualizzaTestoSpeciale(text)
            return
        elif len(giocatore.visualizzaMano()) == 1:
            text = giocatore.visualizzaNome() + " urla UNO!!"
            print(text)
            visualizzaTestoSpeciale(text)

        _turno += 1 

      
    
    
   
