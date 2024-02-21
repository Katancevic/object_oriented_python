"""Kreirati klasu Car koja ima definisano polje klase potrosnja a unutar konstruktora definisane vrednosti za polja marka,model I godina proizvodnje. 
Definisati metodu potrosnja_goriva koja ispisuje vrednosti polja. Instancirati objekat klase I pozvati metodu potrosnja_goriva nad objektom. 
Ispisati jedinstveni identifikator objekta I klase, iskoristiti funkciju dir nad klasom. Ispitati da li vrednost polja godina instanciranog objekta predstavljena tipom celi broj."""

class Car:
    potrosnja = 0
    def __init__(self, marka, model, godina_proizvodnje):
        self.marka = marka
        self.model = model
        self.godina_proizvodnje = godina_proizvodnje
    def potrosnja_goriva(self, potrosnja):
        self.potrosnja = potrosnja
        print(f"Marka: {self.marka} \nModel: {self.model} \nGodina proizvodnje: {self.godina_proizvodnje} \
              \nPotrošnja goriva: {potrosnja}")
        

auto_1 = Car("Audi", "A4", 2010)

auto_1.potrosnja_goriva("7L/100km")

# Indetifikator objekta
print(id(auto_1))
# Indetifikator klase
print(id(Car))

# Funkcija dir nad klasom
print(dir(Car))

# ispitivanje instanciranog objekta koji je tip

if isinstance(auto_1.godina_proizvodnje, int):
    print("Godina, objekta auto_1 je tipa integer")
else:
    print("Godina, objekta auto_1 nije tipa integer")

if isinstance(auto_1.potrosnja_goriva, int):
    print("Potrosnja goriva, auto_1 je tipa integer")
else:
    print("Potrosnja goriva, objekta auto_1 nije tipa integer")


 



        