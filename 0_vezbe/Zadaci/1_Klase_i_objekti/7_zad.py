"""Napraviti klasu Racun koja ima metode uplata, isplata i stanje Računa. Klasa treba da sadrži konstruktor koji postavlja stanje računa (polje stanje) na 0. 
Instanciranjem objekta klase se otvara račun. Uplatiti 500e pozivom metode uplata, ispisati stanje računa pozivom metode stanjeRacuna,  
isplatiti 250e metodom isplata ako postoje stredstva na računu, ispisati stanje racuna metodom stanjeRacuna. Ako ima sredstava isplatiti 350e I ispisati stanje računa metodom stanjeRacuna"""

class Racun():
    def __init__(self):
        self.stanje = 0
    
    def uplata(self, kolicina):
       self.stanje += kolicina
    
    def isplata(self, kolicina):
        if self.stanje < kolicina:
            self.kolicina = kolicina
            print(f"Nemate dovoljno sredstava na racunu! (Vaš zahtev je da podignete {self.kolicina})")
        else:
            self.stanje -= kolicina
            print(f"Uspešno ste podigli vaš novac {self.stanje}")
    
    def stanje_racuna(self):
        print(f"Vaše trenutno stanje računa je: {self.stanje}")

racun = Racun()

racun.uplata(500)
racun.stanje_racuna()
racun.isplata(250)
racun.stanje_racuna()
racun.isplata(350)
racun.stanje_racuna()
