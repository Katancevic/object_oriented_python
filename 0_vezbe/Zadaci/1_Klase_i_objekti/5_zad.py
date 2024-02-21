"""Napraviti klasu Zivotinja koja sadrži polje ime (string) I metodu stampaj_ime koja štampa podatak ime. 
Napravitu klasu Pas I Macka koje nasleđuju klasu Zivotinja. Klase Pas I Macka je potrebno da sadrže matodu Oglasavam_se koja ispisuje oglašavanje te životinje. 
Instancirati 2 objekta, objekat klase Pas I objekat klase Macka I pozvati metodu Oglasavam_se nad njima."""

class Zivotinja():
    def __init__(self,ime) -> str:
        self.ime = ime
    def stampa(self):
        print(f"Ime zivotinje je: {self.ime}")

class Pas(Zivotinja):
    def oglasavam_se_pas(self):
        print(f"Zivotina {self.ime} se oglasava: Av,av,av,av...!!!")
class Macka(Zivotinja):
    def oglasavam_se_macka(self):
        print(f"Zivotinja {self.ime} se oglasva; Mjau, mjau,mjau...!!!")

obj_pas = Pas("Zuca")
obj_macka = Macka("Snesko")

obj_pas.stampa()
obj_pas.oglasavam_se_pas()

obj_macka.stampa()
obj_macka.oglasavam_se_macka()

