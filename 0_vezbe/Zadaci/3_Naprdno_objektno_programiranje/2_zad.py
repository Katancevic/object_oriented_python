"""Napraviti klasu Osoba. Neka klasa sadrži polje ime koji ima vrednost Nemanja. 
   Takođe neka klasa sadrži metodu ispiši_ime koja ispisuje ime. 
   Dinamički promeniti da ime ima vrednost Miloš."""

class Osoba:
    ime = "Nemanja"
    def ispisi_ime(self):
        print(f"Ime: {self.ime}")
    
ime_promeni = Osoba()

print(f"Ime koje je definisano u polju klase: ")
ime_promeni.ispisi_ime()

setattr(ime_promeni, "ime", "Ivan") # Funkcija "setattr() "Dinamicki promena imena u toku izvrsenja programa.

print(f"Ime koje smo promenili u toku izvršenja programa: ")
ime_promeni.ispisi_ime()