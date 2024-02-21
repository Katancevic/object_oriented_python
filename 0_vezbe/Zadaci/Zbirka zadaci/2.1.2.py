import time

def trocifren(a):
    if a>=100 and a<=999:
        print("Broj je trocifren")
    else:
        print("Broj nije trocifren")

t1=time.time()  
broj=int(input('Unesite ceo broj: '))
trocifren(broj)
t2=time.time()
#Razlika vremana nam daje vreme koliko je potrebno da se ucita broj i funkcija vrati ispis
print("Vreme: ",t2-t1)