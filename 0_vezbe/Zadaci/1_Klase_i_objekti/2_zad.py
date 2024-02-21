"""Napraviti klasu Firma koja sadrži polja: ime (string), vrstu poslovanja (string), adresu (string), grad (string), kontakt telefon (string). 
Instancirati objekat, proslediti konstruktoru stvarne podatke I na standardni izlaz ispisati vrednost polja grad tog objekta"""

class Firma:
    ime = " "
    vrsta_poslovanja = " "
    adresa = " "
    grad = " "
    kontakt_telefon = " "
    def __init__(self, ime, vrsta_poslovanja, adresa, grad, kontakt_telefon) -> str:
        self.ime = ime
        self.vrsta_poslovanja = vrsta_poslovanja
        self.adresa = adresa
        self.grad = grad
        self.kontakt_tel = kontakt_telefon

obj = Firma("DMV", "Proizvodnja", "Kraljevića Marka bb", "Niš", "018 4591-556")

print(f"Grad: {obj.grad}")
print(f"Vrsta poslovanja: {obj.vrsta_poslovanja}")

