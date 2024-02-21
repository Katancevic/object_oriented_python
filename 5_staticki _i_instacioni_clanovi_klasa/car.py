class Car:

    make = "Audi" # polje klase sa vrednoscu Audi

    def __init__(self, name, speed_limit): # metoda klase car sa konstruktorom __init__
        self.name = name # instanca promenljive name
        self.speed_limit = speed_limit # instanca promenljive speed_limit

car1 = Car("fiat", "220")
car2 = Car("Mazda", "240")

print(car1.make)
print(car2.make)

print(car1.name)
print(car2.name)

print(car1.speed_limit)
print(car2.speed_limit)

""" Pored polja, kao članove klase možemo imati i metode. Metode prema tipu možemo podeliti na:
1. instancne, 
2. statičke,
3. klasne metode. 
"""
# Instancne metode

"""Da bi metoda bila instancna, ona mora imati jedan parametar u koji će se prilikom 
poziva automatski proslediti referenca na objekat nad kojim je metoda pozvana (ovaj parametar se obično imenuje kao self)."""

# primer 1
class Car:
    model = ""
    def set_model(self):
        self.model = "R8"
 
car = Car()
car.set_model()
print(car.model)


# primer 2

class Student:
 
    def __init__(self, a, b):
        self.a = a
        self.b = b
 
    def avg(self):
        return (self.a + self.b) / 2
 
 
s1 = Student(10, 20)
print( s1.avg() )

# Staticke metode
"""Statičke metode se definišu kao i druge metode, ali se pozivaju direktno putem klase, a ne preko njene instance, tj. objekta. 
Mogu se, ali ne moraju, označiti posebnim dekoratorom @staticmethod."""

# primer

class Car:
    make=""
    model=""
    wheels=4

    @staticmethod
    def HowManyWheels():
        print(Car.wheels)

Car.HowManyWheels()

"""U primeru možete videti da metodu HowManyWheels deklarišemo statičkom upotrebom posebne funkcije/dekoratora.
 Dekorator spečava instanciranje metode i njoj se pristupa putem klase, što možemo videti u poslednjoj liniji koda."""

# Klasne metode

"""Klasne metode se prosleđuju direktno klasi, za razliku od instancnih metoda koje se prosleđuju pomoću samog objekta.
Da bi metoda bila klasna, ona mora imati jedan parametar u koji će se prilikom poziva automatski proslediti referenca na 
klasu nad kojom je metoda pozvana (ovaj parametar se obično imenuje kao cls).
Klasni metodi se definišu kao i drugi metodi i označavaju se posebnim @classmethod"""

"""Klasni metodi se definišu kao i drugi metodi i označavaju se posebnim dekoratorom @classmethod."""

class User:
    name = ""
    userid = ""
    number = ""
 
    def __init__(self, name, userid, number):
        self.name = name
        self.userid = userid
        self.number = number
        print (self.name,self.userid,self.number)
 
new_user = User("John","34734",12356)

"""Ovaj princip je apsolutno ispravan i objektno orijentisan, ali dolazimo do problema kada 
želimo da obavljamo unos putem npr. input funkcija. Tada kod izgleda ovako:"""

class User:
 
    def __init__(self, name, userid, number):
        self.name = name
        self.userid = userid
        self.number = number
        print (self.name,self.userid,self.number)
 
new_user = User("John","34734",12356)
input('Name: '),
int(input('User ID: ')),
int(input('Phone number: ')),

"""Dakle, prilikom instanciranja, sada kao parametre prosleđujemo inpute i problem je što ove tri linije koda moramo
proslediti za svako dodavanje korisnika.Ovo sada odstupa od naše želje za što većom automatizacijom procesa. 
Tu na scenu nastupa klasna metoda. Sada klasnu metodu možemo upotrebiti da pišemo u polja klase, umesto preko objekta. 
Primer klasne metode za ovaj problem možete videti u nastavku:"""

class User:
 
    def __init__(self, name, userid, number):
        self.name = name
        self.userid = userid
        self.number = number
 
    @classmethod
    def input_user(cls):
        cls.name   = input('Name: ')
        cls.userid   = int(input('User ID: '))
        cls.number = int(input('Phone number: '))
        return (cls.name,cls.userid,cls.number)
    
"""Ovde smo sada definisali novu klasnu metodu input_user. Parametrom cls čuvamo sve vrednosti koje korisnik unosi i koje vraćamo iz metode u klasu."""
# poziv klasne metode
User.input_user()
# ili iako nije potrebno mozemo i preko objekta klase User
new_user = User.input_user()
print(new_user)








