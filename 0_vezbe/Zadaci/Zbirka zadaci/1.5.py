
class Zivotinja:
    def __init__(self,ime):
        self.ime=ime
    
    def stampaj_ime(self):
        print("Moje ime je: " + self.ime)
        

class Macka(Zivotinja):
    def oglasi_se(self):
        print("Mjau mjau")
        
class Pas(Zivotinja):
    def oglasi_se(self):
        print("Av av")
        

#instanciranje klase Pas
kuca=Pas('Zuca')
#metoda spampaj_ime je metoda klase Zivotinja koju mozemo pozvati nad objektom klase Pas jer je to dete klase Zivotinja
kuca.stampaj_ime()
#poziv metode oglasi_se klase Pas
kuca.oglasi_se()

maca=Macka('Cica')
#metoda spampaj_ime je metoda klase Zivotinja koju mozemo pozvati nad objektom klase Macka jer je to dete klase Zivotinja
maca.stampaj_ime()
#poziv metode oglasi_se klase Macka
maca.oglasi_se()