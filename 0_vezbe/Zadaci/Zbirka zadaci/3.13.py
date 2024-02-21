import multiprocessing

class Slovo:
    def __init__(self,a):
        self.slovo=a
        
    def veliko_slovo(self): 
        print(self.slovo.upper()) 
        
    def malo_slovo(self): 
        print(self.slovo.lower()) 
        
if __name__ == "__main__": 
    s=Slovo('a')
    #prvi nacin pravljenja procesa
    process1 = multiprocessing.Process(target=Slovo.veliko_slovo, args=(s,))
    #drugi nacin pravljenja procesa
    process2 = multiprocessing.Process(target=s.malo_slovo) 
    
    process1.start() 
    process2.start() 
  
    process1.join() 
    process2.join() 

    print("Done!")

