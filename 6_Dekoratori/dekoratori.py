"""Uprošćeno, funkcija dekoratora jeste da preuzme funkciju i doda neki kod ili funkcionalnost i da vrati funkciju. Ovaj način rada se naziva metaprogramiranjem, 
jer deo programa pokušava da promeni neki drugi deo u trenutku izvršavanja programa."""

# Dekoratori se mogu u osnovi podeliti na dva tipa: ugrađene i korisnički definisani.
#Dekorator možemo prepoznati po oznaci @ ispred naziva i prema poziciji.


# primer 1 dekorater procedualni pristup


def make_pretty(func): # ovako se pise dekorator korisnicki
    def inner():
        print("I got decorated")
        func()
    return inner


def ordinary(): # poziva funkicju make_pretty()
    print("I am ordinary")


ordinary() #prints I am ordinary ne promenjena funkija ispis

 # sa dekoraterem , oko funkcije pisemo dekorater a ne menjamo samo funkicju
pretty = make_pretty(ordinary) # jednu funkicju pozivamo i kao parametar je druga funkcija

pretty()

"""U našem primeru dekorator je upravo funkcija make_pretty. Ovaj dekorator kao parametar uzima promenljivu func, 
koja predstavlja funkciju koja će se proslediti dektoratoru. Ta logika se nalazi u okviru unutrašnje funkcije dekoratora, g
de imamo ispis (koji će predstavljati promenu pozvane funkcije). Nakon toga imamo poziv funkcije i vraćanje podataka dekoratoru.
Druga funkcija, pod nazivom ordinary, predstavlja funkciju koju ćemo promeniti pomoću dekoratora; u sebi sadrži samo ispis da je obična. 
Promene uviđamo pozivanjem funkcija i njihovim izvršavanjem: """

# Upotreba @ 

def make_pretty(func):
    def inner():
        print("I got decorated")
        func()
    return inner
 
 
@make_pretty
def ordinary():
    print("I am ordinary")
 
 
ordinary()


# primer_2 dekorater procedualni pristup

def decorator(operation):
    def inner(funcion):
        if operation == "+":
            return lambda a,b: a+b
        elif operation == "-":
            return lambda a,b: a-b
        return funcion
    return inner


@decorator("+")
def function(a,b):
    pass

@decorator("-")
def function2(a,b):
    pass

print(function(4,3))
print(function2(4,3))


# primer 1 objektno orijentican nacin pisanja dekoratora (dekorator klase)

class decorator:
    def __init__(self, operation) -> int:
        self.operation = operation

    def __call__(self,funcion):
        if self.operation == "+":
            return lambda a,b: a+b
        elif self.operation == "-":
            return lambda a,b: a-b


@decorator("+")
def function(a,b):
    pass

@decorator("-")
def function2(a,b):
    pass

print(function(4,3))
print(function2(4,3))

