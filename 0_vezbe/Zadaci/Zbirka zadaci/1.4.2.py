class Brojevi:
    def __init__(self,prvi_broj,drugi_broj):
        self.a=prvi_broj
        self.b=drugi_broj
        
    def sabiranje(self):
        sabirak=self.a+self.b
        return sabirak

    def oduzimanje(self):
        razlika=self.a-self.b
        return razlika
    
    def mnozenje(self):
        proizvod=self.a*self.b
        return proizvod

    def deljenje(self):
        if self.b==0:
            return "Deljenje sa 0 nije dozvoljeno!!!!"
        else:
            kolicnik=self.a//self.b
            return kolicnik
    
E1=Brojevi(7,5)
print("Sabirak je: ",E1.sabiranje())
print("Razlika je: ",E1.oduzimanje())
print("Proizvod je: ",E1.mnozenje())
print("Kolicnik je: ",E1.deljenje())
E2=Brojevi(7,0)
print("Kolicnik je: ",E2.deljenje())