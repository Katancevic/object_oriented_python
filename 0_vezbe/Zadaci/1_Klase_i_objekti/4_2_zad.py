"""Napraviti klasu Brojevi, koja sadrži 2 polja koja predstavljaju cele brojeve. Koristiti konstruktor klase. 
Napraviti metode sabiranje, oduzimanje, množenje I deljenje(celobrojno) koje vraćaju rezultat svake od operacija. 
Ako je drugi broj 0 potrebno je da metoda deljenje vraca poruku o gresci umesto rezultata. Instancirati jedan objekat I pozvati metode nad njim. """

class Brojevi():
    def __init__(self, broj_1, broj_2) -> int:
        self.broj_1 = broj_1
        self.broj_2 = broj_2
    def sabiranje(self):
        zbir = self.broj_1 + self.broj_2
        print(f"zbir dva broja je: {zbir}")
        return zbir
    def oduzimanje(self):
        razlika = self.broj_1 - self.broj_2
        print(f"Razlika dva broja je: {razlika}")
        return razlika
    def mnozenje(self):
        mnozi = self.broj_1 * self.broj_2
        print(f"Rezultat mnozenje dva broja je: {mnozi}")
        return mnozi
    def deljenje(self):
        if self.broj_2 == 0:
            print(f"Nije moguče obaviti operaciju deljenja!!! \nDrugi broj koji je unešen je: {self.broj_2}")
            return 
        else: 
            delje = self.broj_1 / self.broj_2
            print(f"Rezultat deljenje dva broja je: {delje}")
        return delje
    
obj = Brojevi(15,0)

obj.sabiranje()
obj.oduzimanje()
obj.mnozenje()
obj.deljenje()

        

