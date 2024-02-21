import multiprocessing
import time

class Osoba:
    def __init__(self,ime, prezime, datum_rodjenja, adresa , grad, drzava, kontakt):
        self.ime=ime
        self.prezime=prezime
        self.datum_rodjenja=datum_rodjenja
        self.adresa=adresa
        self.grad=grad
        self.drzava=drzava
        self.kontakt=kontakt

    time=time.gmtime()
    year=time.tm_year
        
    def punoletna_osoba(self):
        if (self.year-int(self.datum_rodjenja[6:])>=18):
            print('Osoba je punoletna')
        else:
            print("Osoba nije punoletna")
        
class Student(Osoba):
    def __init__(self,ime, prezime, datum_rodjenja, adresa , grad, drzava, kontakt,fakultet,smer,godina_studija):
        super().__init__(ime, prezime, datum_rodjenja, adresa , grad, drzava, kontakt)
        self.fakultet=fakultet
        self.smer=smer
        self.godina_studija=godina_studija
           
  
if __name__ == "__main__": 
    student1=Student('Pera','Peric','11.05.2000','Nemanjina 5','Beograd','Srbija','06318523695','ETF','Elektronika',2)
    student2=Student('Mika','Mikic','04.11.2015','Rumenacka 11','Novi Sad','Srbija','0641233516585','FTN','Softversko inzinjerstvo i informacione tehnologije',3)
    process1 = multiprocessing.Process(target=Student.punoletna_osoba, args=(student1,))
    process2 = multiprocessing.Process(target=Student.punoletna_osoba, args=(student2,))
    
    process1.start() 
    process2.start() 
  
    process1.join() 
    process2.join() 

    print("Done!")

