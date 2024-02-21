class Auto:

    #Definisanje konstruktora
    def __init__(self, proizvodjac, model, max):
        self.proizvodjac = proizvodjac
        self.model = model
        self.max = max

    #Metoda koja sluzi za postavljanje vrednosti polja proizvodjac
    def postavi_proizvodjaca(self,x):
        self.proizvodjac=x
        
    def postavi_model(self,x):
        self.model=x
        
    def postavi_max_brzinu(self,x):
        self.maxBrzina=x

    #Metoda za ispis podataka        
    def ispis(self):
        print("Proizvodjac: ",self.proizvodjac,', Model: ',self.model,', Maximalna brzina: ',self.maxBrzina)

#Instanciranje objekta klase Auto
auto1=Auto('fdf','fd',5)

#Poziv metoda
auto1.postavi_proizvodjaca("BMW")
auto1.postavi_model("5")
auto1.postavi_max_brzinu(250)
auto1.ispis()
