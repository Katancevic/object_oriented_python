

class Error(Exception):
    pass


class ValueTooSmallError(Error):
    """Raised when the input value is too small"""
    pass


class ValueTooLargeError(Error):
    """Raised when the input value is too large"""
    pass

#zamisljen broj
number = 10

#Beskonacna petlja koja ce da se vrti sve dok se ne pogodi zamisljeni broj odn. sve dok je uneti broj razlicit od zamisljenog broja
while True:
    try:
        #unos broja
        i_num = int(input("Unesite ceo broj: "))
        #Ako je uneti broj manji od zamisljenog dizemo izuzetak ValueTooSmallError
        if i_num < number:
            raise ValueTooSmallError
        #Ako je uneti broj veci od zamisljenog dizemo izuzetak ValueTooLargeError
        elif i_num > number:
            raise ValueTooLargeError
        else:
            break
    
    except ValueTooSmallError:
        print("Ova vrednost je previse mala, probajte opet!")
    
    except ValueTooLargeError:
        print("Ova vrednost je previse velika, probajte opet!")
        

print("Bravo! Pogodili ste broj")
