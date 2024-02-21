"""Napraviti klasu Brojevi, koja sadrži 2 polja koja predstavljaju  cele brojeve. Koristiti konstruktor klase. 
Napraviti metode sabiranje, oduzimanje, množenje I deljenje(celobrojno) koje vraćaju rezultat svake od operacija. 
Instancirati jedan objekat I pozvati metode nad njim. """

class Brojevi():
    def __init__(self, broj1, broj2) -> int:
        self.broj1 = broj1
        self.broj2 = broj2
    def sabiranje(self):
        zbir = self.broj1 + self.broj2
        print(f"Zbir dva broja je: {zbir}")
        return zbir
    def oduzimanje(self):
        razlika = self.broj1 - self.broj2
        print(f"Razlika dva broja je: {razlika}")
        return razlika
    def mnozenje(self):
        mnoz = self.broj1 * self.broj2
        print(f"Množenje dva broja je: {mnoz}")
        return mnoz
    def deljenje(self):
        delje = self.broj1 - self.broj2
        print(f"Deljenje dva broja je: {delje}")
        return delje
    
obj = Brojevi(15,3)

obj.sabiranje()
obj.oduzimanje()
obj.mnozenje()
obj.deljenje()