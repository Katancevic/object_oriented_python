"""Napraviti funkciju koja ispituje da li je uneti broj trocifren. Učitati broj I pozvati funkciju za učitani broj. 
Izračunati koliko sekundi je potrebno da se učita broj I funkcija vrati ispis."""

import time 

def trocifreni(broj):
    if broj >= 100 and broj <= 999:
        print(f"Broj {broj} je trocifreni")
    else:
        print(f"Broj {broj} nije trocifrni")

t1 = time.time()

broj_unos = int(input("Unesi broj: "))
trocifreni(broj_unos)

t2 = time.time()
print(f"Vreme izvrsenja programa: {t2-t1}")
        
