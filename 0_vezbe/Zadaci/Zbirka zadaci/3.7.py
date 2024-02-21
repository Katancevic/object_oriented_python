import multiprocessing

class Brojevi:
    def __init__(self,a,b):
        self.a=a
        self.b=b 
        
    def sabiranje(self): 
        print(self.a+self.b) 
        
    def oduzimanje(self): 
        print(self.a-self.b)
  
if __name__ == "__main__": 
    brojevi=Brojevi(1,2)
    #prvi nacin pravljenja procesa
    process1 = multiprocessing.Process(target=Brojevi.sabiranje, args=(brojevi,))
    #drugi nacin pravljenja procesa
    process2 = multiprocessing.Process(target=brojevi.oduzimanje) 
    
    process1.start() 
    process2.start() 
  
    process1.join() 
    process2.join() 

    print("Done!")

