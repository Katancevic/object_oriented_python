"""generički tipovi i generičko programiranje nešto što predstavlja možda i najkompleksnije principe rada u objektnom pristupu. 
Kao takvi, oni nisu često u realnoj upotrebi i nisu presudni za uspešno programiranje aplikacija u Pythonu. Naravno,
pravilno korišćenje generičkih tipova može znatno olakšati rad i ubrzati proces pisanja koda; 
koriste se prema potrebni i u zavisnosti od toga sa kojim podacima radimo."""

""" Pod pojmom generičkog programiranja podrazumeva se izrada programskog koda koji se u nepromenjenom obliku može primeniti na različite tipove podataka."""
""" Generički tip definiše skup tipova dobijenih za različite vrednosti parametra."""

"""ealitivno novi modul koji se prvi put pojavio u Python verziji 3.5. Reč je o typing modulu, koji nam obezbeđuje lako proveravanje tipova objekata i ujedno 
omogućava korišćenje sintakse za kreiranje generičkih tipova, kako varijabli tako i klasa i metoda."""

import typing
from typing import TypeVar


T = TypeVar('T') # Nakon toga definišemo promenljivu kao:

"""TypeVar kao parametar uzima string sa karakterom T i to se sve čuva u promenljivoj. Razlog je to što postoji konvencija o imenovanju tipova kod generičkog programiranja. 
Karakter T kao parametar u stvari predstavlja vrednost tip – dakle ne string, ne int već tip. Stoga će promenljiva T biti tipa tip"""

"""Konvencije za Nazive parametre tipova
E	element
K	ključ
N	broj
T	tip
V	vrednost
S, U, V	drugi, treći i četvrti tip"""

# Generičke funkcije i metode

"""Tipski parametri u funkcijama služe za to da deklarišu koji se tip podatka vraća korisniku i da se ponašaju kao placeholderi tipova koji se prosleđuju generičkoj metodi."""
from typing import TypeVar
 
T = TypeVar('T')      # Declare type variable
 
def do_nothing(one_arg:T,other_arg:T) -> None:
    pass
 
do_nothing(1,2)
#do_nothing("abc",UserID(42))

"""Dakle, ponovo smo definisali tipsku promenljivu i zatim smo nju postavili kao dva parametra funkcije - funkcije koja vraća None.
    Dakle, koristimo funkciju samo da preuzme informacije. Ako pozovemo generičku funkciju, možemo joj proslediti bilo koji parametar. 
    Tako smo u prvom slučaju proslediti dva broja, dakle dva podatka tip int, ali smo u drugom slučaju prosledili string i objekat neke klase. 
    Funkcija napisana na ovaj način će uzeti bilo koji podatak dat kao parametar jer smo koristili generičku promenljivu."""

""" Važno je odmah napomenuti da generičke metode i tipovi nemaju klasičnu primenu, recimo da u prethodnom primeru uzmemo unete parametre i obavljamo neke operacije nad njima; 
    unkcije napisane na ovaj način koristimo da skladištimo podatke i da ih zatim prosledimo negde."""

# Generičke klase

"""Pogledajmo jedan od najčešćih primera upotrebe generičkog programiranja i ujedno ćete videti kako kreiramo jednu generičku klasu.

Pretpostavimo da radimo sa nekim skupom objekata koje želimo da nekako organizujemo. U tom slučaju koriste se klase koje se označavaju kao kolekcije (kolekcija=zbirka, skupljanje).

One definišu objekte koji se koriste za organizaciju drugih objekata odgovarajućeg tipa u kolekcije na odgovarajući način. Moguće je u kolekciju dodavati objekte različitog tipa, ali onda 
imamo problem utvrđivanja tipa objekta prilikom njegovog korišćenja. Ako pokušamo da neki objekat iz ove kolekcije upotrebimo kao objekat neke druge klase, nailazimo na problem.

Ovo je upravo jedan od najčešćih slučajeva korišćenja generičkih tipova; pogledajmo jedan primer gde koristimo listu za skladištenje podataka:"""

from typing import TypeVar, Generic

T = TypeVar('T')

class Stack(Generic[T]):
    def __init__(self) -> None:
        # Create an empty list with items of type T
        #self.items: List[T] = []
        pass

    def push(self, item: T) -> None:
        self.items.append(item)

    def pop(self) -> T:
        return self.items.pop()
    

stack = Stack()
stack.push("text")
stack.push(123)
stack.push([2])
stack.push(UserWarning())
stack.push(stack)

"""Pre svega, važno je napomenuti da za kreiranje generičke klase koristimo posebnu klasu Generic iz modula typing, koju naša klasa nasleđuje.
   Samim tim ona postaje generička i radi sa generičkim parametrima.
    U okviru koda možemo videti da kreiramo jednu praznu listu, koja za tip podatka koji čuva dobija T, dakle dobiće generički tip. Nakon toga smo definisali metodu push,
    koja služi za dodavanje elementa u kolekciju, i metodu pop, koja služi za preuzimanje vrednosti elementa.

    Nakon toga instanciramo klasu stack i u nastavku koristimo njen objekat da prosleđujemo tipove. Generički tipovi ovde pokazuju svoju moć: prosleđujemo razne tipove podataka, 
    preko klasičnih sve do drugih klasa, pa čak i samoj listi prosleđujemo sebe kao element. Ovo su nam omogućili generički tipovi."""

# primer 2

from typing import TypeVar

T = TypeVar('T', bound='Shape')

class Shape:
    def set_scale(self: T, scale: float) -> T:
        self.scale = scale
        return self

class Circle(Shape):
    def set_radius(self, r: float) -> 'Circle':
        self.radius = r
        return self

class Square(Shape):
    def set_width(self, w: float) -> 'Square':
        self.width = w
        return self

circle = Circle().set_scale(0.5).set_radius(2.7)
square = Square().set_scale(0.5).set_width(3.2)

"""Dakle, imamo dve klase: Circle i Square; svaka ima svoja polja odgovarajuća za geometrijsku figuru o kojoj je reč i jedno zajedničko polje scale. 
Ako bismo koristili klasični pristup, svaka od ovih klasa bi trebalo da ima metodu kojom postavljamo vrednosti za polje scale (setter), 
a već napisane setter metode bi morale da imaju polja za posebne parametre, za radius i width. I to je jedini pristup, jer nam tako diktiraju njihovi tipovi.
Upotrebom generičke klase Shape, dobijamo mogućnost da nad jednim objektom pozovemo dve metode koje uzimaju različite tipove podatka. Dakle, objekat tipa Circle i objekat tipa Square."""



