"""Enkapsulaciju smo definisali kao pojam koji koristimo da opišemo način na koji je interfejs razdvojen od implementacije. 
Enkapsulaciju možemo posmatrati i kao način sakrivanja podataka, gde dozvoljavamo da određeni delovi koda budu vidljivi, dok ostali ostaju sakriveni. 
Ovo donosi prednosti u radu i korišćenju, kako za korisnika tako i za programera.

Mnogi jezici, npr. C++ i Java, imaju koncept modifikatora pristupa. Npr. C++ ima modifikator pristupa private. 
On određuje da metodama i svojstvima može da pristupi samo klasa u okviru koje su definisani. Protected modifikator pristupa određuje da 
samo deca klase mogu da pristupe, a public modifikator da bilo koja klasa može da pristupi svim elementima.
Ovo, nažalost, nije moguće u Pythonu, ali i dalje imamo mogućnost enkapsulacije koda, samo što se to realizuje na drugi način.
Python koristi modifikaciju pristupa, ali ne na način da zabrani pristup, već tako da zaštićene vrednosti promeni tako da je do njih teže doći i da 
jasno naglasi programeru da ne bi trebalo da ih koristi.

U Pythonu imamo dva načina da zaštitimo vrednost: da ona bude zaštićena i da bude privatna. """

# Zaštićene (protected) vrednosti

"""Zaštićeni članovi predstavljaju vrednosti koje treba koristiti samo u okviru klase i njene dece.
 Da bismo ovo realizovali, u Pythonu ispred naziva svojstva ili polja navodimo jednu donju crtu (underscore): _.

 Važno je napomenuti da, kao što smo rekli ranije, Python ne sprečava pristup, već programeru daje 
 napomenu da ne bi trebalo da koristi zaštićenu i privatnu vrednost. """

 # primer zasticene klase

class Example():
    def __init__(self):
        self._protectedAtribute= 702991
 
    def _protectedMethod(self):
        print("Hello from protected method")
 
p1 = Example()
p1._protectedMethod()
print(p1._protectedAtribute)

"""U primeru možemo videti da smo u okviru klase postavili dve metode. Prva je, naravno, init, sa kojoj smo se upoznali ranije, 
ali ova metoda u sebi ima zaštićenu vrednost. Dakle, koristili smo jednu donju crtu da naglasimo da je vrednost zaštićena. Nakon toga u 
kodu imamo još jednu metodu (pod proizvoljnim nazivom protectedMethod) i, kao što vidite, i ona je zaštićena korišćenjem donje crte.
 Ako instanciramo klasu, možemo videti da imamo pristup i metodi i atributu i možda se sada pitate – pa koja je onda poenta svega ovoga ako i dalje mogu da pristupim svemu?

Upravo je donja crta jasan indikator čemu pristupate, jer morate i donju crtu navesti ispred naziva kada pozivate metode i vrednosti.
 Ovo je jasan indikator da svesno navodite nešto što ste ili vi ili neki drugi programer zaštitili prilikom pisanja klase. 
 
 Ako sklonimo donje crte ispred naziva, dakle pokušamo da zavaramo Python, dobićemo poruke o greškama, jer se nazivi više neće poklapati. """

# Privatne (private) vrednosti
"""Privatni članovi su slični zaštićenim; razlika je u tome što polje klase koje je proglašeno privatnim uopšte ne treba koristiti van klase,
pa ni u klasama koje su deca roditeljske klase. Da bismo ovo realizovali, u Pythonu ispred naziva svojstva ili polja navodimo dve donje crte (double underscore): __."""

class Example():
    def __init__(self):
        self.__privateAtribute= 702991
 
    def __privateMethod(self):
        print("Hello from private method")
 
p1 = Example()
p1.__privateMethod()
 
print(p1.__privateAtribute)

"""Dakle, imamo privatno polje __privateAtribute i privatnu metodu __privateMethod. Ako pokušamo da pokrenemo kod, kao što smo uradili i ranije, dobijamo sledeći ispis:

Traceback (most recent call last):
AttributeError: 'Example' object has no attribute '__privateMethod'

Dakle dobijamo ispis greške gde se navodi da Example objekat nema atribut privateMethod, iako jasno možemo videti da je pravilno definisan. 
Ovo se dešava zbog upotrebe __ ispred naziva metode. Tada Python menja naziv metode tako da joj redovnim pozivom ne možemo pristupiti i na 
taj način štiti metodu od slučajnog korišćenja ili slučajne izmene njene vrednosti."""

"""Upotreba jedne donje crte programeru naglašava da ne bi trebalo da koristi svojstva ili polja klase van same klase ili njene dece.
 Ne sprečava nas da ih koristimo, ali služi kao napomena, dok upotrebom dve donje crte u stvari kreiramo privatnu 
 vrednost kojoj ne možemo pristupiti redovnim metodama i Python vraća grešku ukoliko probamo da je koristimo. 
 Ovo su dve metode pomoću kojih možemo zaštititi, tj. enkapsulirati naš kod."""

"""Geteri i seteri su metode koje se koriste za kontrolisano pristupanje privatnim poljima klase. 
Polja koja su izložena kroz getere i setere nazivaju se svojstva, tj. properties. 
"""
# Primer geter i seter

class Point:
    def __init__(self):
        self.a=0
        self.b=0
    def move(self):
        self.a+=1
        self.b+=1
#  možemo nepravilnom upotrebom izazvati klasu da napravi problem u izvršavanju, zbog izloženosti njenih ključnih polja (a,b). Npr.:

class Point:
    def __init__(self):
        self.a=0
        self.b=0
    def move(self):
        self.a+=1
        self.b+=1
 
pt = Point()
pt.b="Hello"
pt.move()

"""Klasa bi očekivala da polje b bude integer, ali mi smo „greškom” prosledili string. U ovom slučaju, umesto nekog adekvatnog odgovora klase, dobijamo:

TypeError: can only concatenate str (not "int") to str

Ova greška onda prekida rad kompletnog programa zbog pogrešno prosleđenog parametra."""

"""Korišćenjem getter i setter metoda možemo kontrolisati kako se važnim poljima 
pristupa i kako se može promeniti njihova vrednost. Pogledajmo isti primer, ali sa implementacijom getter i setter metoda za jedno od polja:"""


class Point:
    def __init__(self):
        self.__a=0
 
    def get_a(self):
        return self.__a
    def set_a(self,a):
        if not isinstance(a,int):
            return
        self.__a = a
    def move(self):
        self.__a+=1
 
pt = Point()
pt.set_a = "Hello"
pt.move()

"""Sada imamo dve nove metode: get_a, koja će predstavljati getter metodu, i set_a, koja će predstavljati setter metodu. 
Metoda get_a, kao što joj samo ime govori, preuzima vrednost, dok setter metoda setuje, dakle kreira vrednost. 
Ovde imamo uslove da ukoliko tip podataka u inicijalizaciji nije int, program ne radi ništa, a ako jeste – čuva vrednost. 
Ako sada pokrenemo program sa pogrešno prosleđenim parametrom, videćemo da ne postoji prekid rada programa i nema prijave greške, 
jer smo definisali šta se događa i kako se promenljiva obrađuje u slučaju pogrešnog unosa. Naravno, ako prosledimo broj, dobićemo normalan, tj. predviđen rad programa."""

#Primer_2

class Point:
    def __init__(self):
        self.__a=0 # privatno polje
        
    @property    
    def a(self):
        return self.__a
    
    @a.setter    
    def a(self,a):
        if not isinstance(a,int):
            return
        self.__a=a
    
    def move(self):
        self.__a+=1

pt=Point()
print(pt.a) #Pozivamo getter metodu 

pt.move()  #Pomocu metode move povecavamo vrednost promenljive __a za 1
print(pt.a) 

pt.a=5  #Pozivamo setter metodu
print(pt.a)
