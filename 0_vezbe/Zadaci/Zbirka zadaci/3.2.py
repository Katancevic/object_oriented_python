
class Osoba:
    ime="Nemanja"
    
    def ispisi_ime(self):
        print(self.ime)
        

decak=Osoba()

print("Ime pre menjanja: ")
decak.ispisi_ime()

#Dinamicka promena vrednosti
setattr(decak,'ime','Milos')

print("Ime posle menjanja: ")
decak.ispisi_ime()
