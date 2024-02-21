"""Kreirati klasu koja će se koristiti za instanciranje objekata kruga, pomoću konstruktora definisati podatak poluprečnika.
Definisati jednu metodu koja izračunava i ispisuje obima kruga na standardni izlaz. 
Instancirati 2 objekata i jednu metodu postaviti u jednu nit a metodu za drugi objekat u drugi nit, nitima prvo izvršavati prvu metodu,
pa nakon uspešno završene niti prve metode izvršiti drugu.  Tokom ovoga procesa, glavna nit mora biti stopirana. """

import threading # importovati ovu funkciju kada radis sa nitima
import math

class Krug:
    def __init__(self, r) -> float:
        self.r = r
    def obim_kruga(self):
        pi = 3.14
        O = 2 * self.r * pi
        print(f"Obi kruga je: {round(O, 2)} cm")
        #Drugi nacin preko math biblioteke
        #O = 2 * self.r * math.pi

#Proveravamo da li je pokrenuta glavna nit
if __name__ == "__main__":
    
    r_1 = Krug(5)
    r_2 = Krug(10)

    
    t2 = threading.Thread(target=r_2.obim_kruga())
    t1 = threading.Thread(target=r_1.obim_kruga())
    
    t1.start()
    t2.start() 
    
    t1.join() 
    t2.join()

 

    print("Gotovo!\n")

