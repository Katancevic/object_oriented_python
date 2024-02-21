
import threading
import math


#definisanje klase
class Krug:
    #definisanje konstruktora
    def __init__(self,r):
        self.r=r

    #definisanje metode obima kruga
    def obim_kruga(self): 
        print("Obim kruga: {}".format(2*self.r*math.pi)) 
  
#Proveravamo da li je pokrenuta glavna nit
if __name__ == "__main__":
   
    #istanciranje 2 objekta
    a=Krug(3)
    b=Krug(4)
    
    #prvi nacin pravljenja niti
    t1 = threading.Thread(target=Krug.obim_kruga, args=[a])
    #Drugi nacin pravljenja niti
    t2 = threading.Thread(target=b.obim_kruga) 
    
    
    t1.start() 
    t2.start() 

    t1.join() 
    t2.join() 

    print("Gotovo!\n")
