"""Napraviti klasu Zivotinja koja kao podatak sadrži ime I metodu stampaj_ime, koji štampa ime.
Napraviti klase Biljojed, Mesojed I Svastojed koje nasleđuju klasu Zivotinja gde svaka sadrži metodu ishrana kojom se ispisuje šta ko jede. 
Instancirati 3 objekta gde je jedna životinja biljojed, jedna mesojed a jedna svaštojed. Pozvati metode stampaj_ime I ishrana nad svim objektima.
"""

class Zivotinja():
    def __init__(self, ime):
        self.ime = ime
    
    def stampaj_ime(self):
        print(f"Ime zivotinje: {self.ime}")
    
class Biljojed(Zivotinja):
    def ishrana(self):
        print(f"{self.ime} pase travu.")

class Mesojed(Zivotinja):
    def ishrana(self):
        print(f"Zivotinja {self.ime} jede meso.")

class Svastojed(Zivotinja):
    def ishrana(self):
        print(f"Zivotinja {self.ime} jede svasta!")

zivotinja1 = Biljojed("Krava")
zivotinja1.stampaj_ime()
zivotinja1.ishrana()

zivotinja2 = Mesojed("Lav")
zivotinja2.stampaj_ime()
zivotinja2.ishrana()

zivotinja3 = Svastojed("Svinja")
zivotinja3.stampaj_ime()
zivotinja3.ishrana()