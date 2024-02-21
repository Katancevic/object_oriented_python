"""Napraviti apstraktnu klasu Polygon, koja sadrži apstraktnu metodu broj_stranica. 
Klasu Polygon nasleđuju klase Triangle, Pentagon, Hexagon,  Quadrilateral. 
Svaka od ovih klasa treba da nasledi metodu broj_stranica I da ispiše broj_stranica za svaki oblik. 
Instancirati objekat za svaki oblik I pozvati metodu broj_stranica nad njima."""

import abc

class Polygon(abc.ABC):
    @abc.abstractmethod
    def broj_stranica(self):
        pass

class Triangle(Polygon):
    def broj_stranica(self):
        print("Ovaj oblik ima 3 stranice.")

class Pentagon(Polygon):
    def broj_stranica(self):
        print("Ovaj oblik ima 5 stranice.")
class Hexagon(Polygon):
    def broj_stranica(self):
        print("Ovaj oblik ima 6 stranice.")

class Qudrilateral(Polygon):
    def broj_stranica(self):
        print("Ovaj oblik ima 4 stranice")

triangle = Triangle()
triangle.broj_stranica()

pentagon = Pentagon()
pentagon.broj_stranica()

hexagon = Hexagon()
hexagon.broj_stranica()

qudrilateral = Qudrilateral()
qudrilateral.broj_stranica()