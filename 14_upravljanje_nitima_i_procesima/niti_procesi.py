""" Kako biste razumeli zbog čega dolazi do blokada izvršavanja koda i zašto dođe do usporavanja izvršavanja koda,
neophodno je razumeti na koji način se obavlja izvršavanje programa, odnosno aplikacija od strane hardvera posredstvom operativnog sistema kompjutera.
U očima operativnog sistema, jedna aplikacija, odnosno program, može biti sačinjena iz više procesa, a svaki proces unutar sebe može imati proizvoljan broj niti"""

"""
* Procesi su način na koji operativni sistem izoluje i razdvaja izvršavanje programa. Uprošćeno se može reći da su procesi zapravo programi ili njihovi delovi koji se 
posredstvom operativnog sistema izvršavaju na nekom kompjuteru.
* Nit je najmanja izvršna jedinica koja može postojati unutar procesa. Svaki proces sastoji se iz jedne ili više niti. Procesi poseduju minimalno jednu nit, 
koja se kreira prilikom nastanka procesa i koja se drugačija naziva primarna nit. Jedno jezgro kompjuterskog procesora u jednom trenutku može da izvršava samo jednu nit.
"""

# Da bismo, pre svega, povezali modul sa našim fajlom, koristimo:

import threading

"""Kada imamo omogućen modul, kreiranje nove niti postižemo objektom Thread klase, koja je deo paketa threading. Instanciranje klase zahteva dva argumenta:

target: u okviru target parametra navodimo funkciju (metodu koja se izvršava u novoj niti);
args: u okviru args parametra navodimo sve argumente koji su funkciji ili metodi potrebni da bi funkcionisala."""

def calculate_cube(num): 
    print("Cube: {}".format(num * num * num)) 
  
def calculate_square(num): 
    print("Square: {}".format(num * num)) 
  
if __name__ == "__main__": # if the main program started do this:
    # creating thread 
    t1 = threading.Thread(target=calculate_square, args=(10,)) # kreiramo nit
    t2 = threading.Thread(target=calculate_cube, args=(10,)) 
  
    # start thread 1 
    t1.start() 
    # start thread 2 
    t2.start() 
  
    # wait until thread 1 is completely executed 
    t1.join() 
    # wait until thread 2 is completely executed 
    t2.join() 
  
    # both threads completely executed 
    print("Done!")

    #  rad niti nad objektima.

    import threading
 
class Osoba:
    def __init__(self,ime,prezime,godine):
        self.ime=ime
        self.prezime=prezime
        self.godine=godine
         
    def ispis_imena(self):
        print("Osoba se zove : ",self.ime, " ", self.prezime)
     
    def ispis_godina(self):
        print("Osoba ima ",self.godine,' godina')
         
 
osoba1=Osoba('Pera','Peric',19)
if __name__ == "__main__": 
    t1 = threading.Thread(target=Osoba.ispis_imena, args=(osoba1,)) 
    t2 = threading.Thread(target=osoba1.ispis_godina) 
   
    t1.start() 
    t2.start()
     
    t1.join()
    t2.join()

    # Multiprocessing

"""Kao što i sam naziv govori, ovaj princip nam daje mogućnost kreiranja više procesa, koji će tada imati svoje niti. 
To nam omogućava da imamo operacije koje se izvršavaju istovremeno, umesto da čekaju jedna na drugu.
Ovaj princip je u osnovi funkcionisanja samog operativnog sistema; iz tog razloga možemo uporedo da koristimo npr. 
Google Chrome i Microsoft Word. Jedan proces brine o jednoj aplikaciji, a drugi o drugoj. Naravno, ovo je veoma uprošćeno, ali to je upravo osnovni princip."""

"""Da bismo, pre svega, povezali modul sa našim fajlom, koristimo:"""

import multiprocessing


def calculate_cube(num): 
    print("Cube: {}".format(num * num * num)) 
  
def calculate_square(num): 
    print("Square: {}".format(num * num)) 
  
if __name__ == "__main__": 
    process1 = multiprocessing.Process(target=calculate_square, args=(10,))

    process2 = multiprocessing.Process(target=calculate_cube, args=(10,)) 
    process1.start() 
    process2.start() 
  
    process1.join() 
    process2.join() 

    print("Done!")
    # ovo znacajno ubrzava rad programa (aplikacije)
