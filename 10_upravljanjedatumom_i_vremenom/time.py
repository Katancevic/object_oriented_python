import time # modul za vereme

# Funkcija sleep()

print("Hello...")
time.sleep(5)
print("Hello")

"""for i in range(1,6):
    print("Hello")
    time.sleep(i+1) # funkcija sleep
"""

print(time.time()) # Prvi deo, broj 1601382673, predstavlja broj sekundi od 01. 01. 1970. - referentna tacka (pocetak vremena za Python)

# Ono što nam je zapravo potrebno da bismo radili sa vremenom jeste trenutni broj milisekundi koje su protekle od 01. 01. 1970. godine.

miliseconds=round(time.time()*1000)
print(miliseconds)

# Funkcija gmtime/localtime

gmt = time.gmtime() # vremenski objekat
print(f"Current date is: {gmt.tm_mday}.{gmt.tm_mon}.{gmt.tm_year}")
#localtime
gmt = time.localtime()

print(f"Current time is: {gmt.tm_hour}:{gmt.tm_min}")

"""U okviru nove promenljive smo sačuvali poziv funkcije gmtime i nakon toga možemo koristiti njene parametre za prikaz određenih vrednosti, 
pa smo ovde iskoristili ispis dana (tm_mday), meseca (tm_mon) i godine (tm_year). 
Ova funkcija sadrži još parametara, uključujući i veoma često korišćene parametre za vreme: tm_hour, tm_min i tm_sec."""

# primer

import time
gmt = time.gmtime(631152000)
print("Current date is: ",gmt.tm_mday,gmt.tm_mon,gmt.tm_year)

"""Na primer, sledeći kod će generisati vremenski objekat (gmt) za datum 01. 01. 1990. godine, što je godina kada je stvoren Python.
 Mana ove funkcije je što generiše datum i vreme bez upotrebe vremenskih zona. U praksi ćemo najčešće koristiti vreme i 
 datum sa vremenskom zonom i prva funkcija koja nam to omogućava je funkcija localtime."""
"""Funkcija localtime se ponaša identično kao i funkcija gmtime, samo što, umesto univerzalnog, prikazuje vreme za zonu koja je podešena na računaru:"""

"""while True:
    print("Exact time is: ")
    my_time = time.localtime(time.time())
    print(my_time.tm_hour,"hours",my_time.tm_min,"minutes")
    time.sleep(60)

    U prethodnim primerima smo ručno navodili koje podatke želimo, dakle odvojeno za dane, godine, sate i minute. 
    Python nam pruža dve funkcije koje možemo koristiti da daleko lakše i brže formatiramo prikaz datuma i vremena. To su funkcije srftime i strptime:"""

my_time = time.localtime()

my_time_parsed = time.strftime("Month: %b Day: %d Year: %Y",my_time )

print(my_time_parsed)

# strptime vremesnki objekat

entry_time = "2023-02-07 02:43:15"

time_obj = time.strptime(entry_time, "%Y-%m-%d %H:%M:%S")

print("Entry created in the year: ", time_obj.tm_year)

# najmocniji modul sa radom vremena datetime modul
import datetime

date_1 = datetime.datetime(2023,11,2,3,5,29)
date_2 = datetime.datetime.now # vraca lokalno vreme sa sekundama i milisekundama
date_3 = datetime.datetime.fromtimestamp(time.time())

print(date_1)
print(date_2)
print(date_3)





