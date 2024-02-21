
class Zivotinja:
    
    def __init__(self,ime):
        self.ime=ime
        
    def stampaj_ime(self):
        print("Moje ime je "+self.ime)


class Biljojed(Zivotinja):
    def ishrana(self):
        print("Ja jedem biljke")
        
class Mesojed(Zivotinja):
    def ishrana(self):
        print("Ja jedem meso")
        
class Svastojed(Zivotinja):
    def ishrana(self):
        print("Ja jedem i biljke i meso")
        
        


srna = Biljojed("Bambi")
srna.stampaj_ime()
srna.ishrana()

lav = Mesojed("Simba")
lav.stampaj_ime()
lav.ishrana()

medved=Svastojed("Bruno")
medved.stampaj_ime()
medved.ishrana()
