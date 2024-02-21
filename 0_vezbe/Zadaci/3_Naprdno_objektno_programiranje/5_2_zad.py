"""Napraviti klasu generisanjem novog tipa. Klasa je potrebno da ima naziv X, definisanu metodu sabiranje koja pomoću lambda izraza vraća sabirak argumenata. """

klasa = type("X", (),{"sabiranje": lambda self,a,b,c,d,e,: a+b+c+d+e})

a = klasa()
print(a.sabiranje(1,2,3,4,5))