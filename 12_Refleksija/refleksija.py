""" Refleksija može biti korisna kada naša aplikacija koristi klase koje mi slabo poznajemo. 
Tada možemo napisati logiku da naš program sazna koja polja postoje u klasi i koje metode klase možemo koristiti."""
"""Refleksiju u našim programima realizujmo pre svega ugrađenim funkcijama za analizu objekata u Pythonu. 
Nama najbitnije ugrađene funkcije za analizu objekata su: dir, id, type, isinstance, issubclass i callable."""

# Funkcija ID
"""Korišćenjem ove funkcije nad objektom dobijamo njegov jedinstveni identifikator i to tokom trajanja programa."""
class A:
    x = 10
    y = 15

a = A()
b = A()

print(id(a))
print(id(b))

print(id(a.x))
print(id(b.x))

"""Funkciju id možemo koristiti kada želimo da proverimo da li postoji preklapanje u adresama koje je 
izazvala pogrešno napisana logika ili greška prilikom spajanja više dokumenata. ID zasnovan na memorijskoj 
adresi Python koristi za svoju internu upotrebu, naročito kod operatora is."""

# Funkcija dir

"""Funkcija dir() je jedna od najmoćnih funkcija koje su ugrađene u Python. Ova funkcija vraća listu svih 
atributa i metoda jednog objekta, bilo to da je taj objekat funkcija, ceo modul, string, lista itd."""

class Example:
    first_field = 13
 
new_object = Example()
print(dir(new_object))
"""Ovo je ujedno i jedna od funkcija koje su nam značajne za refleksiju, jer pomoću nje dobijamo uvid u to šta nam je dostupno kroz objekat, 
čak i kada ne znamo koja je to klasa, već samo imamo njen objekat. Često se koristi i u svrhu debugovanja programa, pa čak i u velikim timovima developera"""

"""Takođe, kada koristimo neki novi modul sa kojim nismo imali iskustva, dir funkcijom možemo proveriti šta se tačno nalazi u njemu; na taj način lakše testiramo
 njegove opcije i ujedno učimo brže. Primer je izlistavanja paketa za rad sa grafičkim interfejsom u okviru Pythona:"""
import tkinter as tk

class Applications(tk.Frame):
    pass

object = Applications()
print(dir(object))

# type()

"""Još jedna funkcija koja se koristi u debugging svrhe je funkcija type(). Pomoću ove funkcije dobijamo tip objekta prosleđenog kao parametar."""

class Example2:
    pass

new_object = Example2()

t1 = type(Example2)
t2 = type(new_object)

print(t1)
print(t2)
####
calc = type('X',(),{"a":0,"b":0,"add":lambda self,a,b:a+b})

"""U okviru ove promenljive imamo naizgled potpuno nečitljiv kod, ali u okviru linije dešava se defincija klase X, koja ima polje a sa vrednošću
 0 i polje b sa vrednošću 0. Sledi definicija metode pod nazivom add, koja uzima parametre a i b i vraća njihov zbir. Ako dodamo sledeći kod:"""

c = calc()
print(c.add(4,5))
print(type(c))

"""Pre svega, tri parametra ove funkcije su:

1. naziv;
2. lista klasa koje naša klasa nasleđuje; ako nema nasleđivanja, ostaju prazne zagrade;
3. rečnik koji kreira telo klase; u njemu navodimo sva polja i metode.
"""

"""Ovom jednom linijom i type funkcijom smo zamenili sledeće linije:"""

class X:
    a = 0
    b = 0
    def add(self,a,b):
        self.a=a
        self.b=b
        return self.a+self.b
    
    # Funkcija is
"""Dva najznačajnija predstavnika is funkcija su: isinstance i issubclass."""
"""Funkcija isinstance nam omogućava proveru da li je neka vrednost određenog tipa. 
Prvi parametar je promenljiva koja se proverava, dok je drugi parametar tip koji proveravamo."""

x = "13"
 
if isinstance(x,int):
    print(x*x)
else:
    print("Not a number")

    """U okviru if strukture želimo da proverimo da li je promenljiva x tipa int; ako jeste, 
    množimo je sa samom sobom. Ukoliko nije tipa int, ispisujemo Not a number. Kako je broj 13 prosleđen kao string, dobijamo ispis poruke."""

"""Funkcijom issubclass proveravamo da li je neka klasa potklasa neke klase. Npr.:"""

class Top:
    pass

class Example(Top):
    pass

print(issubclass(Top,Example)) #false
print(issubclass(Example,Top)) #true

#Funkcija callable

"""Primena funkcije callable je jednostavna; njome proveravamo da li se objekat može pozvati. Uzima jedan parametar, 
koji je upravo objekat koji se proverava. Provera vraća informaciju da je objekat funkcija ili metoda kao True, a ako se vrednost ne može pozvati, vraća False:"""

def x():
  a = 5
 
num1 = 5
num2 = 2
 
z = num1+num2
 
print(callable(x))
print(callable(z))

#  setattr() funkcija

"""Dinamičko dodavanje metode ili polja klasi postižemo ugrađenom setattr() funkcijom."""

#setattr(object, name, value)

"""gde je parametar object objekat koji želimo da setujemo, dakle objekat kojem menjamo ili dodajemo polja i metode.

Parametrom name definišemo naziv svojstva (člana klase).

Parametrom value definišeno vrednost svojstva.

na jednom primeru sintaksa bi bila:"""

class Person:
    name = 'John'
 
new_person = Person()
print('Before name changing:', new_person.name)
 
setattr(new_person, 'name', 'David')
 
print('After name changing:', new_person.name)

# getattr() funkcija

"""Ukoliko želimo da samo dobavimo neko polje ili metode, tada koristimo funkciju getatt"""

class Example:
    pass
obj = Example()
 
def new_method(self): # Have to add self since this will become a method
    print('Hello world!')
 
setattr(Example, 'show_text', new_method)
 
obj.show_text()

# Instanciranje klasa u refleksiji

"""Refleksija omogućava instanciranje klase i startovanje njenih metoda na osnovu stringova. 
Ovo omogućava da klasa za nas bude potpuno nepoznata, sve dok znamo parametre koji su nam potrebni 
za njeno instanciranje i eventualno pozivanje njenih metoda."""










