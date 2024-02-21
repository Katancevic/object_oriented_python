import abc 
class Taxi(abc.ABC):
    @abc.abstractmethod
    def cena_voznje(self):
        pass

class PinkTaxi(Taxi):
    cena=100
    def cena_voznje(self):
        print("Cena km za Pink taxi je {} dinara".format(self.cena))
        
class NaxisTaxi(Taxi):
    cena=105
    def cena_voznje(self):
        print("Cena km za Naxis taxi {} dinara".format(self.cena))

class ZutiTaxi(Taxi):
    cena=110
    def cena_voznje(self):
        print("Cena km za Zuti taxi {} dinara".format(self.cena))

pink = PinkTaxi()
pink.cena_voznje()

naxi = NaxisTaxi()
naxi.cena_voznje()

zuti = ZutiTaxi()
zuti.cena_voznje()