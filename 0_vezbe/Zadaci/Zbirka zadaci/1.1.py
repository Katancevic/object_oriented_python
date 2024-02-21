
#definisanje klase
class Serija:
    #definisanje konstruktora
    def __init__(self,ime,zanr,godina):
        #definisanje polja klase
        self.ime=ime
        self.zanr=zanr
        self.godina=godina

#instanciranje objekata 
Game_of_Thrones=Serija('Game of Thrones','Adventure',2011)
Chernobyl=Serija('Chernobyl','Drama',2019)
