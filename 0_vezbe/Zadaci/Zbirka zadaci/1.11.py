'''Zadatak 1.11 Napraviti klasu Osoba koja sadrži podatak ime I koja sadrži metodu ispis_imena koja ispisuje ime. 
Napraviti klase Tata I Mama koje nasleđuju klasu Osoba I gde svaka klasa sadrži metodu rodbinski_odnosi u kojoj se
poziva metoda ispis_imena iz roditeljke klase I u kojoj je ispisuje rodbinski odnos te osobe. Instancirati objekte za klase Mama I Tata.'''


class Osoba:
    def __init__(self,ime):
        self.ime=ime
        
    def ispis_imena(self):
        print("Moje ime je ",self.ime)
        

class Tata(Osoba):
    def rodbinski_odnosi(self):
        super().ispis_imena()
        print("Ja sam tata")
        
class Mama(Osoba):
    def rodbinski_odnosi(self):
        super().ispis_imena()
        print("Ja sam mama")
        

tata=Tata('Milos')
tata.rodbinski_odnosi()

mama=Mama('Ana')
mama.rodbinski_odnosi()
