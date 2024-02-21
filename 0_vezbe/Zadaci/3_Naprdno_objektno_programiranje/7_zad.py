"""Kreirati klasu Brojevi gde se pomoću konstruktora čuvaju vrednosti za dva cela broja u različitim poljima. 
Definisati jednu metodu koja izračunava i ispisuje sabirak na standardni izlaz, dok druga metoda ispisuje razliku. 
Instancirati objekat klase Brojevi. Jednu metodu postaviti u jedan proces  a drugu metodu u drugi proces, 
prvo izvršavati proces koji sadrži metodu sabiranja, pa nakon uspešno završenog  prvog proces izvršiti drugi. """

import multiprocessing # za procese importovati ovu funkciju

class Brojevi():
    def __init__(self, a , b) -> int:
        self.a = a
        self.b = b
    def sabiranje(self):
        sab = self.a + self.b
        print(sab)
    def oduzimanje(self):
        raz = self.a - self.b
        print(raz)

if  __name__ == "__main__": # postavljanje procesa
    brojevi = Brojevi(10,5)

    process_sab = multiprocessing.Process(target = brojevi.sabiranje)
    process_raz = multiprocessing.Process(target = brojevi.oduzimanje)

    process_sab.start()
    process_raz.start()

    process_sab.join()
    process_raz.join()

