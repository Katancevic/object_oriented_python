
class Firma:
    #definisanje polja
    ime=''
    vrsta_poslovanja=''
    adresa=''
    grad=''
    kontakt=''

    #definisanje konstruktora
    def __init__(self,ime,poslovanje,adresa,grad,kontakt):
        self.ime=ime
        self.vrsta_poslovanja=poslovanje
        self.adresa=adresa
        self.grad=grad
        self.kontakt=kontakt

#instanciranje objekta
ITA=Firma('IT akademija','IT','Cara Dusana 34','Beograd','011 4011200')
#izdvajanje polja grad objekta
print(ITA.grad)