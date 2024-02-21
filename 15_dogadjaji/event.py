"""Događaji su jedan od ključnih koncepata u programiranju GUI (Graphical User Interface) aplikacija, 
dakle aplikacija sa kojima korisnik vrši interakciju kroz neke korisničke kontrole putem tastera, prozora, polja i slično"""

"""Programiranje koje podrazumeva praćenje i obradu događaja u toku izvršenja aplikacije naziva se event-based (ili event-driven) programiranje"""

"""uzimo jedan primer iz života. Recimo da želimo da se vozimo automobilom kome rezervoar nije pun. Imali bismo dva načina da budemo sigurni da nam neće nestati goriva tokom vožnje. 
Jedan je da konstantno proveravamo stanje u rezervoaru, a drugi da se oslonimo na indikator rezerve goriva."""

# primer dogadjaja

class Reservoir:
    def __init__(self):
        self.reserveLimit = 10
        self.totalAmount = 100

    def reserveIndicator(self):
        print("Warning, low fuel level!")

    def getFuel(self):
        self.totalAmount -=1
        
        if self.totalAmount <=self.reserveLimit:
            self.reserveIndicator()
        print(self.totalAmount)

res = Reservoir()


for i in range(100):
    res.getFuel()

    """Sam rezervoar je svestan ulaska u rezervu, ali svet oko njega nije. Unutar main metode, ne znamo da je rezervoar „na rezervi” jer je događaj identifikovan i 
    obrađen samo unutar objekta klase. Dakle, to nam je isto kao da indikator rezerve goriva stoji na samom rezervoaru unutar šasije automobila i vozač ne može da ga vidi. 
    Indikator će raditi, ali to je svejedno jer vozač ne može da ga vidi i reaguje na događaj.

Sa ovom analogijom dolazimo do Distributer/Subscriber modela. On podrazumeva sledeće:

Da bi događaj bio vidljiv za objekte izvan objekta u kome se dogodio (distributera), oni se moraju pretplatiti na njega. 
A da bi se objekat pretplatio na događaj drugog objekta, mora ispuniti uslove. Ti uslovi podrazumevaju postojanje odgovarajućeg metoda na objektu pretplatniku.

U trenutku pretplate, objekat distributer prijavljuje pretplatnika na događaj (stavlja ga u listu pretplatnika). Prilikom detektovanja događaja, 
distributer prolazi kroz listu pretplatnika i svima im šalje informaciju da je došlo do događaja. Ovaj koncept poznat je i pod nazivom observer šablon."""

# Slušač događaja (event listener)
    
    """Prvi korak u procesu definicije događaja je konstrukcija slušača događaja. Slušač predstavlja metodu koja očekuje pojavu događaja. 
    U samom kodu slušač događaja je najčešće apstrakcija koja ima jedan ili više metoda za koje će znati distributer i pretplatnici. 
    Slušač događaja je nešto što treba da bude logički vezano za klasu koja će generisati događaj (ili više događaja)."""
# primer
    
import abc
class EventListener(abc.ABC):
    @abc.abstractmethod
    def reserve_reached(self,sender):
        pass

# Distributer događaja

"""Sledeći je distributer događaja. To je klasa u kojoj se događaj dogodio. Da bi bila distributer, ova klasa mora imati određene delove: 

listu slušača;
mehanizam za pridruživanje slušača listi (add_listener); 
mehanizam za uklanjanje slušača (remove_listener); 
mehanizam za obaveštavanje slušača."""

# primer

class Reservoir:
    def __init__(self):
        self.current_state = 100
        self.reserve_limit = 50
        self.listeners = []
 
    def add_listener(self, listener):
        self.listeners.append(listener)
 
    def remove_listener(self, listener):  
        self.listeners.remove(listener)
 
    def distribute_event(self):
        for listener in self.listeners:
            if isinstance(listener, EventListener):
                listener.reserve_reached(self)

# Aktivacija događaja
                
"""Kada postoji kompletan mehanizam za upravljanje događajima unutar klase, samu aktivaciju događaja treba vršiti po potrebi. 
U našem slučaju se aktivacija događaja obavlja samom logikom potrošnje goriva:"""

def consume_fuel(self):
        print(f"Fuel consumed. {self.current_state} liters remaining")
        self.current_state -= 1
        if self.current_state < self.reserve_limit:
            self.distribute_event()

"""Dakle, metodom consume_fuel ispisujemo koliko je goriva ostalo, umanjujemo stanje goriva i aktiviramo događaj."""
# if self.current_state < self.reserve_limit:
#    self.distribute_event()

# Pretplata na događaj 

"""Dakle, do sada imamo svu potrebnu logiku, distributera koji šalje informacije i način da aktiviramo događaj. 
Ova logika nas ponovo dovodi na sam početak. Događaj se odvija, ali niko ne vidi da se događa
"""

# primer

class MyListener(EventListener):
    def reserve_reached(self,sender):
        print("Warning, Low fuel level")
 
res = Reservoir()
res.add_listener(MyListener())

"""Sada novom klasom nasleđujemo klasu EventListener, definišemo obaveznu metodu reserve_reached (zbog apstrakcije) i koristimo nju za prikaz upozorenja."""

"""Sa ovim smo realizovali kompletnu funkcionalnost; sada svi delovi našeg koda mogu pratiti jedan događaj. Kompletan kod primera sa ispisom podataka bi mogao da glasi:"""

import abc

class EventListener(abc.ABC):
    @abc.abstractmethod
    def reserve_reached(self,sender):
        pass
 
class Reservoir:
    def __init__(self):
        self.current_state = 100
        self.reserve_limit = 50
        self.listeners = []  
 
    def add_listener(self, listener):
        self.listeners.append(listener)
 
    def remove_listener(self, listener):  
        self.listeners.remove(listener)
 
    def distribute_event(self):
        for listener in self.listeners:
            if isinstance(listener, EventListener):
                listener.reserve_reached(self)
     
    def consume_fuel(self):
        print(f"Fuel consumed. {self.current_state} liters remaining")
        self.current_state -= 1
        if self.current_state < self.reserve_limit:
            self.distribute_event() 
 
class MyListener(EventListener):
    def reserve_reached(self,sender):
        print("Warning, Low fuel level")
 
res = Reservoir()
res.add_listener(MyListener())
 
for i in range(0,100):
    res.consume_fuel()

"""Ako uzmemo kod primera i odstranimo sve vezano za logiku primera, ostaje šablon za kreiranje modela za rad sa događajima: """

# primer kada koristimo sablon rezervoar

"""
import abc
class EventListener(abc.ABC):
    @abc.abstractmethod
#activate event logic 
 
class EventHandler:
    def __init__(self):
        #fields
        self.listeners = []  
 
    def add_listener(self, listener):
        self.listeners.append(listener)
 
    def remove_listener(self, listener):  
        self.listeners.remove(listener)
 
    def distribute_event(self):
        for listener in self.listeners:
            if isinstance(listener, EventListener):
                #activate listener 
     
    def DoSomething(self):
        # logic for doing something
        if: #event occurs activate distributer
            self.distribute_event() 
             
class MyListener(EventListener):
    # define event
 
objectEvent = EventHandler()
objectEvent.add_listener(MyListener())

"""