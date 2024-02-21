"""Napraviti klasu Osoba koja sadrži polja: ime (string), prezime(string), adresu (string), grad (string), kontakt telefon (string), godište(ceo broj). 
Definisati metodu ispis koja ispisuje podatke objekta na standardni izlaz. Instancirati jedan objekat sa proizvoljenim podacima I pozvati metodu ispis nad objektom. """

class Osoba():
    ime = ""
    prezime = ""
    adresa = ""
    grad = ""
    kontakt = ""
    godiste = 0
    def __init__(self, ime, prezime, adresa, grad, kontakt, godiste):
        self.ime = ime
        self.prezime = prezime
        self.adresa = adresa
        self.grad = grad
        self.kontakt = kontakt
        self.godiste = godiste
    def ispis_nad_objektima(self):
        print(f"Ime: {self.ime} \nPrezime: {self.prezime} \nAdresa: {self.adresa} \nGrad: {self.grad} \nKontakt: {self.kontakt} \nGodište: {self.godiste}")

osoba = Osoba("Ivan", "Katančević", "Dragiše Cvetkovića 24", "Niš", "+381 65 2249239", 1988)

osoba.ispis_nad_objektima()