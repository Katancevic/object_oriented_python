
import threading


#definisanje klase
class Kvadrat:
    #definisanje konstruktora
    def __init__(self,a):
        self.a=a

    #definisanje metode obima kvadrata
    def obim_kvadrata(self): 
        print("Obim kvadrata: {}".format(4*self.a)) 
        
    #definisanje metode povrsine kvadrata
    def povrsina_kvadrata(self): 
        print("Povrsina kvadrata: {}".format(self.a*self.a)) 
  
#Proveravamo da li je pokrenuta glavna nit
if __name__ == "__main__":
   
    #istanciranje objekta
    k=Kvadrat(5)

    #prvi nacin pravljenja niti
    t1 = threading.Thread(target=Kvadrat.obim_kvadrata, args=[k])
    #Drugi nacin pravljenja niti
    t2 = threading.Thread(target=k.povrsina_kvadrata) 
    
    
    t1.start() 
    t2.start() 

    t1.join() 
    t2.join() 

    print("Gotovo!\n")
