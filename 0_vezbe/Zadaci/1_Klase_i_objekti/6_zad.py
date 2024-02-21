"""Napisati klasu Automobil koja sadrži podatke o automobilu. Informacije o automobilu su naziv proizvođača (string), model (string) I maksimalna brzina (ceo broj) kojom se automobil kreće. 
Definisati polja ove klase unutar konstruktora. Klasa treba sadržati metodu ispis koji će odštampati podatke kao I metode postavi_proizvodjaca, 
postavi_model I postavi_max_brzinu koje služe za čuvanje podataka u promenljive polja. Instancirati jedan objekat i pozvati sve metode nad njim."""

class Automobil():
    def __init__(self, proizvodjac, model, maksimalna_brzina):
        self.proizvodjac = proizvodjac
        self.model = model
        self.maksimalna_brzina = maksimalna_brzina
   
    def ispis(self):
        print(f"Proizvođač: {self.proizvodjac} \nModel: {self.model} \nMaksimalna brzina: {self.maksimalna_brzina}")
    
    def postavi_proizvodjaca(self, proizodjac):
        self.proizvodjac = proizodjac
   
    def postavi_model(self, model):
        self.model = model
    
    def postavi_max_brzinu(self, max_brzina):
        self.maksimalna_brzina = max_brzina

automobil1 = Automobil("fdf", "fd", 5)

automobil1.postavi_proizvodjaca("Audi")
automobil1.postavi_model("A4")
automobil1.postavi_max_brzinu(240)
automobil1.ispis()