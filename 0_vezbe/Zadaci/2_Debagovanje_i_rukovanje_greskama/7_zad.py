"""Otvoriti fajl izrazi.txt I ispisati podatke iz fajla. Ako fajl ne postoji izbaciti izuzetak. Izuzetak za nepostojanje fajla je IOError."""

try:
    f =  open("izrazi.txt", "r")
    
    c = f.read()
  
    f.close()

except IOError:
    print("Greska prilikom otvaranja")