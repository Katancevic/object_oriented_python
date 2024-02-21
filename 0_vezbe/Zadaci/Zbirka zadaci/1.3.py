#definisanje klase
class Osoba:
    #definisanje konstruktora
    def __init__(self,ime,prezime,adresa,grad,kontakt,godiste):
        self.ime=ime
        self.prezime=prezime
        self.adresa=adresa
        self.grad=grad
        self.kontakt=kontakt
        self.godiste=godiste
    
    #Prvi nacin ispisa    
    def ispis(self):
        print('Osoba: ime: {}\nPrezime: {}\nAdresa: {}\nGrad: {}\nKontakt: {}\nGodiste: {}\n'.format(self.ime,self.prezime,self.adresa,self.grad,self.kontakt,self.godiste))
        
    #Drugi nacin ispisa
    def ispis2(self):
        print(f'Osoba: ime: {self.ime}\nPrezime: {self.prezime}\nAdresa: {self.adresa}\n,Grad: {self.grad}\nKontakt: {self.kontakt}\nGodiste: {self.godiste}\n')    
    
#instanciranje objekta
osoba1=Osoba('Pera','Peric','Nemanjina 15','Beograd','011 548562',1996)

#poziv metode nad objektom
osoba1.ispis()

#poziv metode2 nad objektom
osoba1.ispis2()
