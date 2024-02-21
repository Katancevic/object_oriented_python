class Stan:
    
    def __init__(self,broj_stana,sifra_alarma):
        self.broj_stana=broj_stana
        self.sifra_alarma=sifra_alarma
        
    def ispisi_broj_stana(self):
        print("Broj stana je :",self.broj_stana)
        
    def __ispisi_sifru_alarma(self):
        print("Sifra alarma je : ",self.sifra_alarma)
        
moj_stan=Stan(12,157856)
moj_stan.ispisi_broj_stana()

#Dolazi do greske jer pristupamo privatnoj metodi
moj_stan.ispisi_sifru_alarma()