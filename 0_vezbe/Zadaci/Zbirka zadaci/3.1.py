class Vozilo:

    def __init__(self,v,g,d):
        self.vlasnik=v
        self.godina_proizvodnje=g
        self.datum_poslednje_registracije=d
    

class Plovilo(Vozilo):
    
    def __init__(self,v,g,d,m):
        super().__init__(v, g,d)
        self.max_brzina=m
        
        
    def ispis_podataka(self):
        print("Vlasnik: ",self.vlasnik,', Godina_proizvodnje: ',self.godina_proizvodnje,", Datum datum_poslednje_registracije ",self.datum_poslednje_registracije,', Maximalna brzina: ',self.max_brzina)
        
        
    def kretanje(self):
        print("Ja sam plovilo i krecem se po vodi\n")




class Letelica(Vozilo):
    
    def __init__(self,v,g,d,m):
        super().__init__(v, g,d)
        self.max_brzina=m
        
        
    def ispis_podataka(self):
        print("Vlasnik: ",self.vlasnik,', Godina_proizvodnje: ',self.godina_proizvodnje,", Datum datum_poslednje_registracije ",self.datum_poslednje_registracije,', Maximalna brzina: ',self.max_brzina)
        

    def kretanje(self):        
        print("Ja sam letelica i krecem se u vazduhu\n")


class Kopneno(Vozilo):
    
    def __init__(self,v,g,d,m,t):
        super().__init__(v, g,d)
        self.max_brzina=m
        self.br_tockova=t
        
        
    def ispis_podataka(self):
        print("Vlasnik: ",self.vlasnik,', Godina_proizvodnje: ',self.godina_proizvodnje,", Datum datum_poslednje_registracije ",self.datum_poslednje_registracije,', Maximalna brzina: ',self.max_brzina,"Broj tockova: ",self.br_tockova)
        

    def kretanje(self):        
        print("Ja sam kopneno vozilo i krecem se po kopnu\n")




Brod1=Plovilo('Petar',2008,'02.03.2019',120)
Brod1.ispis_podataka()
Brod1.kretanje()

Avion1=Letelica('Milos',2017,'05.07.2020',2000)
Avion1.ispis_podataka()
Avion1.kretanje()

Auto1=Kopneno('Andrej',2019,'15.10.2020',250,4)
Auto1.ispis_podataka()
Auto1.kretanje()