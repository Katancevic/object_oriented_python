"""Napraviti apstraktnu klasu Taxi, koja sadrži apstraktnu metodu cena_voznje.  Klasu Taxi nasleđuju klase PinkTaxi, NaxisTaxi I ZutiTaxi.  
Svaka od ovih klasa treba da nasledi metodu cena_voznje I da ispiše cenu voznje po kilometru za svaki taxi. Cena vožnje se definiše kao polje unutar svake od klasa. 
Instancirati objekat za svaki taxi I pozvati metodu cena_voznje nad njima."""

import abc

class Taxi(abc.ABC):
    @abc.abstractmethod
    def cena_voznje(self):
        pass

class PinkTaxi(Taxi):
    cena = 150
    def cena_voznje(self):
        print(f"Cena vožnje PinkTaxi je {self.cena} din po kilometru")

class NaxisTaxi(Taxi):
    cena = 140
    def cena_voznje(self):
        print(f"Cena vožnje NaxisTaxi je {self.cena} din po kliometru")

class ZutiTaxi(Taxi):
    cena = 120
    def cena_voznje(self):
        print(f"Cena vožnje ZutiTaxi je {self.cena} din po kilometru")

pink = PinkTaxi()
pink.cena_voznje()

naxis = NaxisTaxi()
naxis.cena_voznje()

zuti = ZutiTaxi()
zuti.cena_voznje()