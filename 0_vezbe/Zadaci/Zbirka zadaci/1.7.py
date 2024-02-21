
class Racun:
    def __init__(self):
        self.stanje=0
        
    def uplata(self,kolicina):
        self.stanje=self.stanje+kolicina
        
    def isplata(self,kolicina):
        #Ukoliko je polje stanje manje od kolicine koja je potrebno da se podigne sa racuna ispisujemo da nema dovoljno sredstava
        #Ukoliko je polje stanje vece ili jednako od kolicine koja je potrebno da se podigne sa racuna oduzima se ta vrednost sa racuna
        if(self.stanje<kolicina):
            print("Nemate dovoljno novca na racunu")
        else:
            self.stanje=self.stanje-kolicina
            
    def stanjeRacuna(self):
        print("Stanje racuna je ",self.stanje)

racun=Racun()
racun.uplata(500)
racun.stanjeRacuna()
racun.isplata(250)
racun.stanjeRacuna()
racun.isplata(350)
racun.stanjeRacuna()

