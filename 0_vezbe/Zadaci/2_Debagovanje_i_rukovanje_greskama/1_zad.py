"""Napraviti funkciju koja ispituje da li je broj prost (broj je prost ako je deljiv s
amo sa 1 I sa samim sobom) . Učitati broj I pozvati funkciju za učitani broj."""
broj = int(input("Unesi broj: "))

def prost_broj(n):
    if n == 1:
        return True
    for i in range(2,n):

        if n % i == 0:
            return False
    return True

if(prost_broj(broj)):
    print(f"Broj {broj} je prost broj.")
else:
    print(f"broj {broj} Nije prost broj.")