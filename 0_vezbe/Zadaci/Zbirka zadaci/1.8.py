def pametno_deljenje(func):
    def inner(a, b):
        print("Delim broj ", a, " sa ", b)
        if b == 0:
            print("Joj. Broj b je 0, ne mogu da podelim sa 0")
            return #Ovaj return sluzi kao break jer ako je b 0 ne zelimo da delimo pa samo nagovestimo da se vraca prazna vrednost

        return func(a, b) #ovaj return sluzi da ustvari pozovemo funkciju koju smo prosledili, funkciju deljenje gde se vraca povratna vrednost sa kolicnikom prosledjenih brojeva
    return inner #Dekorator pravimo tako sto imamo spoljasnju i unutrasnju funkciju i uvek vracamo unutrasnju funkciju kao povratnu vrednost kako bismo videli sta smo menjali odn. sta smo uradili tom dekoratorskom funkcijom.


@pametno_deljenje
def deljenje(a, b):
    print(a/b)
    
#pozivi funkcije deljenje
deljenje(5,2)
deljenje(5,0)