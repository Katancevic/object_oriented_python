""" Napraviti program koji traži od korisnika da unese broj I pogodi koji broj je zamišljen. 
Zamišljen broj definisati u programu. Napraviti svoje izuzetke. Kada se broj pogodi prekinuti program."""
import random
class Error(Exception):
    pass

class ValueTooSmallError(Error):
    pass

class ValueTooLargeError(Error):
    pass

number = random.randint(0,100)
n = 3
while True:
    try:

        broj = int(input("Unesi ceo broj: "))

        if broj < number:
            raise ValueTooSmallError
        elif broj > number:
            raise ValueTooLargeError
        else:
            break

    except ValueTooSmallError:
        print("Broj koji ste uneli je manji od zamisljenog broja. Pokusajte ponovo!")
    except ValueTooLargeError:
        print("Broj koji ste uneli je veci od zamisljenog broja. Pokusajte ponovo!")
    n +=1

print("Cestitamo pogodili ste zamisljen broj")
