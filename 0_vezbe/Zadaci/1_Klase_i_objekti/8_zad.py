"""Napraviti funkciju deljenje koja vraća realni količnik 2 broja. 
Ovu funkciju dekorisati funkcijom pametno_deljenje koja proverava da li pri deljenju dolazi do greške odnosno da li je drugi argument 0.
Ako dolazi do greške ispisati gresku a ako ne dolazi do greške vratiti količnik. Pozvati funkciju deljenje."""

def pametno_deljenje(func):
    def inner(a, b):
        print(f"Deljenje broja {a} i broja {b}")

        if b == 0:
            print(f"Drugi broj je {b} ne može se deliti sa nulom!")
            return
        
        return func(a,b)
    return inner

@pametno_deljenje
def deljenje(a, b):
    print(a / b)

deljenje(8, 2)
deljenje(5, 0)