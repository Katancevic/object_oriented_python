class Car:
    make = ""
    model = ""
    doorsNumber = 0
    wheels = 4
 
car = Car()
print(car.wheels)

car.make = "Audi"
print(car.make)

class Car2:
    make = ""
    model = ""
    engineType = ""
    horsePower = 1
 
car2 = Car2()

car2.make = "Audi"
car2.model = "A4"
car2.engineType = "Benzin"
car2.horsePower = "182"
print(f"My car is: \n* {car2.make} \n* {car2.model} \n* {car2.engineType} \n* {car2.horsePower} ")


car2 = Car2()

car2.make = "BMV"
car2.model = "Z5"
car2.engineType = "Dizel"
car2.horsePower = "240"
print(f"My car is: \n* {car2.make} \n* {car2.model} \n* {car2.engineType} \n* {car2.horsePower} ")

# Metoda

class Person:
    def my_func(self):
        print("Hello")
objekat_1 = Person()
objekat_1.my_func()  

# Klasa sa vise poljima- argumentima - parametrima.

class Sum:
    a = 2
    b = 5
    def calculate(self):
        print(f"Rezultat je: {self.a + self.b}")
objekat_2 = Sum()
objekat_2.calculate()

# metoda ne mora koristiti polja klase; može koristiti svoje parametre da obavi posao koji smo u prethodnom primeru pokazali, npr.:

class Calc:

    def saberi(self,a,b):
        result = a+b
        return result
calc = Calc()
res = calc.saberi(2,5)
print(f"Rezultat je: {res}")

"""Dozvoljeno je postojanje samo jednog konstruktora unutar klase. Njegovo ime mora da bude __init__, 
kako bi Python znao koji metod da izvršava prilikom kreiranja objekta. Na primer:
Ova težnja ka smanjenju broja linija koda i postizanju više automatskih operacija je upravo jedan od 
ciljeva objektno orijentisanog programiranja."""

class Car():
    made_in = ""
    model = ""
    year = ""
    seats = ""
    def __init__(self) -> str:

        print("New car is begin created")

car = Car()
car2 = Car()

# Primer specijalne metode __init__

class Calc:
    def __init__(self,a,b) -> int:
        self.a = a
        self.b = b
    def saberi(self):
        rezultat = self.a + self.b
        return rezultat
calc = Calc(2,5)
res = calc.saberi()
print(res)

# Klasa Car na nacinu sa metodama smanjujemo broj koda iz prvog primera kada smo za svaki auto definisali polja vrednosti:

class Car:
    def __init__(self, make, model, engine_type, horse_power) -> str:
        self.make = make
        self.model = model
        self.engine_type = engine_type
        self.horse_power = horse_power
    def show(self):
        print("My car is:", self.make, self.model, self.engine_type, self.horse_power)

car = Car("Audi", "A4", "Benzin", "215")
car.show()

car2 = Car("BMW", "5-ca", "Dizel", "245")
car2.show()

