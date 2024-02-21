"""Apstrakcija u Pythonu predstavlja proces sakrivanja realizacije same aplikacije od korisnika i fokusiranje na samo korišćenje aplikacije. 
Važno je napomenuti da korisnik može biti i drugi programer koji radi u našem timu, gde apstrakcija sprečava bespotrebno korišćenje delova koda - ili čak štetno, 
gde drugi programer može koristiti neke elemente klasa ili metode koje ne bi trebalo da koristi."""
#  U Pythonu možemo imati apstraktne klase i metode. 
"""Apstraktne klase možemo posmatrati kao, jednostavno, šablone za kreiranje drugih klasa. Njihova osnovna osobina je da se ne mogu instancirati, 
već jedino naslediti ili koristiti u statičkom kontekstu."""

# primer

class Product:
    def __init__(self,name,price):
        self.name=name
        self.price=price
    def tax(self):
        return self.price * 1.2
    def buy(self):
        print("You bought a product",self.name,"with a price",self.tax(),"dollars")
 
p = Product("Shoes",100)
p.buy()

"""proizvod je previše apstraktan, jer nam ne govori sta tacno kupujemo. 
Ideja apstraktne klase jeste da nikada ne instanciramo direktno klasu Product, 
već da instanciramo neku drugu klasu, npr. Shoes, koja se koristi kao šablon klase Product.
Python u osnovi ne poznaje apstraktne klase, ali se one mogu simulirati paketom abc (abstract base classes)."""

import abc # kada u kodu umamo apstraknu klasu (abstracte base classes)

import abc
class Product(abc.ABC): # Da bi sama klasa imala mogućnost apstrakcije, potrebno je da nasleđuje klasu ABC iz paketa abc.
    pass

"""Pythonu, da bi jedna klasa mogla da postane apstraktna, ona mora sadržati makar jedan apstraktan metod. 
Da bismo definisali jednu apstraktnu metodu, koristimo dekorator abstractmethod iz istog paketa."""

# primer_2/1

import abc
class Product(abc.ABC):
    def __init__(self,name,price):
        self.name=name
        self.price=price

    @abc.abstractmethod
    def tax(self):
        return self.price * 1.2
    def buy(self):
        print("You bought a product",self.name,"with a price",self.tax(),"dollars")


p = Product("Shoes",100)
p.buy()

# primer 2/2

import abc
class Product(abc.ABC):
    def __init__(self,name,price):
        self.name=name
        self.price=price
 
    @abc.abstractmethod
    def tax(self):
        pass
    def buy(self):
        print("You bought:", self.name,"with a price",self.tax(),"dollars")
 
class Shoes(Product):
    def tax(self):
        return self.price * 1.2
 
p = Shoes("Nike Airmax",100)
p.buy()

# Abstraktne metode

"""Apstraktan metod možemo posmatrati kao vrstu ugovora između apstraktne klase i klase koja je nasleđuje. 
On garantuje da će klasa koja nasleđuje ispoštovati uslove za učešće u ostatku sistema."""
# primer 2/1
import abc

class BaseStation(abc.ABC):
    @abc.abstractmethod
    def fillCar(self):
        pass

# primer 2/2
    
import abc
class BaseStation(abc.ABC):
    @abc.abstractmethod
    def fillCar(self):
        pass
class ShellGasStation(BaseStation):
    pass
new_station = ShellGasStation()

"""prilikom instanciranja bi se pojavio problem: Razlog toga je što nismo ispoštovali ugovor/dogovor 
i nismo implementirali apstraktan metod fillCar()."""

# primer 2/3

import abc 
class BaseStation(abc.ABC):
    @abc.abstractmethod
    def fillCar(self):
        pass

class ShellGasStation(BaseStation):
    def fillCar(self):
        print("Filling car with water")

new_station = ShellGasStation()
new_station.fillCar()


