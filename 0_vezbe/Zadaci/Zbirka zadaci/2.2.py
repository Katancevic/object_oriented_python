
import time

#postavljamo vrednost brojaca na 0
i=0
#petlja ce raditi sve dok je brojac i manji od 3
while i<3:
    #ucitavamo broj
    a=int(input("Unesite broj: "))
    #Ako je uneti broj manji od 1 ili veci od 5 vracamo se na pocetak petlje sto znaci da se brojac i nece povecati za 1.
    if(a<1 or a>5):
        print("Niste uneli broj izmedju 1 i 5")
        continue
    #Ako je broj izmedju 1 i 5 stopiramo program za toliko sekundi kolika je vrednost ucitanog broja
    time.sleep(a)
    #Ispisujemo ucitan broj
    print("Uneti broj je ",a)
    #Povecavamo brojac i za 1
    i=i+1