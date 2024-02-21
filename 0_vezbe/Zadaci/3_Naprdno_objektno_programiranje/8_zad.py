"""Kreirati klasu Osoba gde se pomoću konstruktora čuvaju podaci: ime, prezime, datum_rodjenja, adresa,  grad, drzava, kontakt. Svi podaci su tekstualnog tipa. 
Potrebno je da klasa student sadrži metodu punoletna_osoba u kojoj ispituje da li je osoba punoletna. 
Definisati klasu Student koja nasleđuje klasu Osoba i sadrži dodatne podatke o imenu fakulteta,
smeru i godini studiranja. Potrebno je da svi podaci budu tekstualnog tipa osim godine studija koja treba da bude ceo broj. 
Instancirati 2 objekta klase Student. Napraviti proces sa metodom punoletna_osoba za oba objekta,  
prvo izvršavati proces za prvi instanciran objekat, pa nakon uspešno završenog  prvog procesa izvršiti drugi. """

import multiprocessing
import time

class Osoba():
    def __init__(self, ime, prezime, datum_rodjenja, adresa, grad, drzava, kontakt) -> str:
        self.ime = ime
        self.prezime = prezime
        self.datum_rodjenja = datum_rodjenja
        self.adresa = adresa
        self.grad = grad
        self.drzava = drzava
        self.kontakt = kontakt
    
    time = time.gmtime()
    year = time.tm_year

    def punoletna_osoba(self):
       if self.year - int(self.datum_rodjenja[6:]) >= 18:
            print("Osoba je punoletna.")
       else:
            print("Osoba je maloletna.")



class Student(Osoba):
    def __init__(self, ime, prezime, datum_rodjenja, adresa, grad, drzava, kontakt,ime_fakulteta,smer,godina_studiranja):
        super().__init__(ime, prezime, datum_rodjenja, adresa,grad, drzava, kontakt)
        self.ime_fakulteta = ime_fakulteta
        self.smer = smer
        self.godina_studiranja = godina_studiranja



if __name__ == "__main__":

    student_1 = Student("Ivan", "Katančević", "12.10.1988", "Dragiše Cvetkovića 24", "Niš", "Srbija", "065-2249239", "Prirodno Matematički fakultet", "Informatika", "2007")

    student_2 = Student("Marko", "Marković", "15.12.2020", "Rajka Mitića 8","Beogad", "Srbija", "062-526987","Elektronski fakultet", "Računarstvo", "2007" )


    process_1 = multiprocessing.Process(target= student_1.punoletna_osoba)
    process_2 = multiprocessing.Process(target=student_2.punoletna_osoba)


    process_1.start()
    process_2.start()

    process_1.join()
    process_2.join()

    print("Done")

