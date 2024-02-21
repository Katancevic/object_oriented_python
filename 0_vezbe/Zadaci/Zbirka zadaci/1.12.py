import abc
  
class Polygon(abc.ABC): 
  
    @abc.abstractmethod
    def broj_stranica(self): 
        pass
  
class Triangle(Polygon): 
    def broj_stranica(self): 
        print("Ja imam 3 strane") 
  
class Pentagon(Polygon): 
    def broj_stranica(self): 
        print("Ja imam 5 strana") 
  
class Hexagon(Polygon): 
    def broj_stranica(self): 
        print("Ja imam 6 strane") 
  
class Quadrilateral(Polygon): 
    def broj_stranica(self): 
        print("Ja imam 4 strane") 
  


R = Triangle() 
R.broj_stranica() 
  
K = Quadrilateral() 
K.broj_stranica() 
  
R = Pentagon() 
R.broj_stranica() 
  
K = Hexagon() 
K.broj_stranica() 


