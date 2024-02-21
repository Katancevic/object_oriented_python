"""Napraviti funkciju koja ispituje da li je godina prestupna ili ne. Posle poziva funkcije metodom time modula ispisati trenutnu godinu."""
import datetime
def prestupna_god():
    n = int(input("Unesite godinu: "))
    if (n % 4 == 0 and n % 100 != 0) or (n % 400 == 0): # ispitivanje da li je godina prestupna
        print(f"Godina koju ste uneli {n} je prestupna.")
    else:
        print(f"Godina koju ste uneli {n} nije prestupna.")
    
    todey = datetime.datetime.now()
    print(todey)

prestupna_god()
    