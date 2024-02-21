"""Napraviti klasu Serija sa poljima ime, zanr I godina. Instancirati dva objekta. """

class Serija():
    def __init__(self, ime, zanr, godina) -> str:
        self.ime = ime
        self.zanr = zanr
        self.godina = godina

obj1 = Serija("Two and a Half Men", "Komedija", 2002)
obj2 = Serija("Game of Throns", "Adventure", 2015)


     