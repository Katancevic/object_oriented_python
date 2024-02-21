"""Napraviti klasu Osoba koja sadrži podatak ime I koja sadrži metodu ispis_imena koja služi za ispis imena. 
Napraviti klase Tata I Mama koje nasleđuju klasu Osoba I gde svaka klasa sadrži metodu rodbinski_odnosi u kojoj 
se poziva metoda ispis_imena iz roditeljke klase I u kojoj je ispisuje rodbinski odnos te osobe. Instancirati objekte za klase Mama I Tata I pozvati metodu rodbinski_odnosi nad njima"""

class Osoba:
    def __init__(self, ime):
        self.ime = ime

    def ispis_ime(self):
        print(f"Ime: {self.ime}")

class Tata(Osoba):
    def rodbinski_odnos(self):
        super().ispis_ime() # funkcija super poziva metodu roditeljske klase 
        print(f"Otac, glava porodice.")

class Mama(Osoba):
    def rodbinski_odnos(self):
        super().ispis_ime()
        print(f"Majka, stub porodice.")

tata = Tata("Ivan")
tata.rodbinski_odnos()

mama = Mama("Verica")
mama.rodbinski_odnos()