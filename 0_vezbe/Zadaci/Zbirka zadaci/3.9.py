import abc

# slusac 
class EventListener(abc.ABC):
    @abc.abstractmethod
    def dostignut_limit(self,sender):
        pass
 
class Bankomat:
    def __init__(self,stanje):
        self.current_state = stanje
        self.reserve_limit = 100
        self.listeners = []  
 
    def add_listener(self, listener):
        self.listeners.append(listener)
 
    def remove_listener(self, listener):  
        self.listeners.remove(listener)
 
    def distribute_event(self):
        for listener in self.listeners:
            if isinstance(listener, EventListener):
                listener.dostignut_limit(self)
     
    #Ako je stanje na kartici vece od prosledjene svote smanjujemo stanje za vrednost svotu, ispisujemo stanje na kartici i ako je novo stanje manje od limita aktiviramo dogadjaj
    #Ako je stanje na kartici manje od prosledjene svote ispisujemo samo stanje na kartici
    def isplata(self,svota):
        if self.current_state>=svota:
            self.current_state -= svota
            print("Svota {} je skinuta sa kartice. Na kartici je ostalo {}".format(svota, self.current_state))
            if self.current_state < self.reserve_limit:
                self.distribute_event() 
        else:
            print('Na kartici nema dovoljno sredstava, stanje na kartici je {}'.format(self.current_state))

class MyListener(EventListener):
    def dostignut_limit(self,sender):
        print("Upozorenje, na kartici se nalazi mala svota novca")


#Postavljanje pocetnog stanja 
stanje=int(input('Unesite svotu novca na karticu:'))
res = Bankomat(stanje)
#Pridruzivanje slusaca listi
res.add_listener(MyListener())

#Sve dok je stanje a kartici vece od 0 unosimo svotu za isplatu
while(res.current_state>0):
    res.isplata(int(input('Unesite koliku svotu novca zelite da podignete sa kartice: ')))