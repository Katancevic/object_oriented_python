"""Napraviti klasu Vozilo. Klasa vozilo sadrži podatke ime vlasnika, godinu_proizvodnje i datum_poslednje_registracije. 
Napraviti klase Plovilo, Letelica i Zemljano_vozilo koje nasleđuju klasu Vozilo. Neka svaka od ovih klasa sadrži metodu koja ispisuje način kretanja. 
Zemljano_vozilo treba da ima podatak o broju točkova I max_brzini, Plovilo I Letelica treba da sadrže samo podatak o maximalnoj brzini. 
Instancirati 3 objekta, svaki neka bude drugačiji tip vozila. """

class Vozilo():
   def __init__(self, tip,vlasnik_vozila, godina_proizvodnje, datum_poslednje_registracije):
        self.tip = tip
        self.vlasnik_vozila = vlasnik_vozila
        self.godina_proizvodnje = godina_proizvodnje
        self.datum_poslednje_registracije = datum_poslednje_registracije

class Plovilo(Vozilo):
    def nacin_kretanja(self, max_brzina):
        self.max_brzina = max_brzina
        print(f"Maksimalna brzina plovila: {max_brzina}")
        print("--------------------")
    def podaci(self):
        print(f"Tip vozila: {self.tip} \nVlasnik: {self.vlasnik_vozila} \nGodina proizvodnje: {self.godina_proizvodnje} \
                \nDatum poslednje registracije: {self.datum_poslednje_registracije}")
     

class Letelica(Vozilo):
    def nacin_kretanja(self, max_brzina):
        self.max_brzina = max_brzina
        print(f"Maksimalna brzina letalice: {max_brzina}")
        print("--------------------")
    def podaci(self):
        print(f"Tip vozila: {self.tip} \nVlasnik: {self.vlasnik_vozila} \nGodina proizvodnje {self.godina_proizvodnje} \
                \nDatum poslednje registracije: {self.datum_poslednje_registracije}")
        

class Zemljino_vozilo(Vozilo):
    def nacin_kretanja(self, broj_tockova, max_brzina):
        self.broj_tockova = broj_tockova
        self.max_brzina = max_brzina
        print(f"Broj točkova: {broj_tockova} \nMaksimalna brzina vozila: {max_brzina}")

    def podaci(self):
        print(f"Tip vozila: {self.tip} \nVlasnik: {self.vlasnik_vozila} \nGodina proizvodnje: {self.godina_proizvodnje} \
                \nDatum poslednje registracije: {self.datum_poslednje_registracije}")
    

brod = Plovilo("Plovilo", "Ivan", "2020", "30.11.2023")
brod.podaci()
brod.nacin_kretanja("80km\h")

avion = Letelica("Letelica", "Ivan", "2010", "25.08.2018")
avion.podaci()
avion.nacin_kretanja("450km\h")

auto = Zemljino_vozilo("Auto", "Ivan", "2009", "29.12.2023")
auto.podaci()
auto.nacin_kretanja("4", "240km\h")
