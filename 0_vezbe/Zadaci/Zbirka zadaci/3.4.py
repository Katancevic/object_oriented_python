class Car:
    def __init__(self,marka,model,godina):
        self.marka=marka
        self.model=model
        self.godina=godina
    
    potrosnja=6
    
    def potrosnja_goriva(self):
        print('Automobil marke {} model {} godiste {} trosi {}l na 100km'.format(self.marka,self.model,self.godina,self.potrosnja))
        
        
auto1=Car('BMW','5',2009)
auto1.potrosnja_goriva()

#Identifikator objekta i klase
print(id(auto1))
print(id(Car))

print(dir(Car))

if isinstance(auto1.godina,int):
    print('Godina objekta je tipa int')
else:
    print('Godina objekta nije tipa int')