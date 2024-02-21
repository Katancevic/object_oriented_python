"""Napraviti klasu Stan koja pomoću konstruktora cuva podatke o broju stana I sifru alarma. 
Napraviti metod ispisi_broj_stana koji ispisuje koji je broj stana I napraviti privatnu metodu ispisi_sifru_alarma koja ispisuje šifru alarma. 
Instancirati objekat I pozvati obe metode na objektom. Prilikom pokretanja programa mozemo videti da se dobija greska jer pristupamo privatnoj metodi."""

class Stan():
    def __init__(self, broj_stana, sifra_alarma):
        self.broj_stana = broj_stana
        self.sifra_alarma = sifra_alarma

    def ispisi_broj_stana(self):
        print(f"Broj stana: {self.broj_stana}")
    
    def __ispisi_sifru_alarma(self):
        print(f"šifra alarma je: {self.sifra_alarma}")

stan = Stan(24, 123456)

stan.ispisi_broj_stana()

stan.ispisi_sifru_alarma()

