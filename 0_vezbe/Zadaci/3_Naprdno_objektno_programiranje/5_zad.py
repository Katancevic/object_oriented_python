"""Napraviti klasu generisanjem novog tipa. Klasa je potrebno da ima naziv Y, definisanu metodu deljenje koja pomoću lambda izraza vraća količnik 
ako je vrednost drugog argumenta različit od 0 ili ispis greške ako je vrednost 0. """

calc = type("Y", (),{"deljenje":lambda self, a , b: a / b if b != 0 else "Greška, ne može se deliti sa nulom"}) # sintaksa za generisanje tipa i lambda izraz

kolicnik = calc()

print(kolicnik.deljenje(10,5))
print(kolicnik.deljenje(10,0))
