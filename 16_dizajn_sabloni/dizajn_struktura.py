"""
čisto programski oblici koji imaju veze isključivo sa programskom strukturom aplikacije. U okviru ove lekcije objasnićemo šta su to dizajn šabloni;
"""
"""standardno rešenje za neki standardan programski problem. Do tog rešenja se došlo evolutivno i empirijski i njegovom upotrebom eliminišemo pojavu „izmišljanja tople vode″ u kreiranju svoje aplikacije, 
čime znatno ubrzavamo proizvodnju, naročito ukoliko se ona odvija u timskom okruženju."""

"""
Vrste dizajn šablona

U programiranju imamo tri kategorije šablona:

1. Kreacioni šabloni - Ovi šabloni bave se kreacijom objekata, na način prilagođen određenoj primeni. Posebno su važni u situacijama u kojima bi uobičajen pristup kreiranju objekata doveo do povećanja kompleksnosti projekta.
Neki od paterna koji spadaju u ovu grupu su: Singleton, Constructor, Prototype, Factory, Abstract i Builder.
2. Strukturalni šabloni - Strukturalni paterni bave se kompozicijom koda i obično predstavljaju načine za definisanje odnosa među objektima. Oni obezbeđuju da, ukoliko se dogodi promena u jednom delu sistema, ostatak sistema ne mora da se menja.
Neki od strukturalnih paterna su: Decorator, Facade, Flyweight, Adapter i Proxy.
3. Bihevioralni šabloni - Ova grupa paterna tiče se poboljšanja komunikacije između različitih objekata u sistemu.
Poznati primeri su: Iterator, Mediator, Observer i Visitor.

"""

# Singleton pattern

"""Singleton pattern garantuje da ćete u kodu napraviti samo jednu instancu određenog objekta. Pogledajmo primer:"""

# primer

class MyClass():
    pass
 
a = MyClass()
b = MyClass()
 
print(a==b)

"""Ovo je potpuno logično ponašanje navedenog programa, ali šta da se u klasi MyClass nalazi sistem za rukovanje bazom podataka? Onda bismo, 
možda, želeli da se obezbedimo od toga da korisnik može da napravi više od jedne instance objekta, jer bi u tom slučaju imao i više od jedne konekcije. 
U takvim prilikama najbolje rešenje bi bila upotreba singleton patterna:"""
class Singleton:
    __instance = None
    @staticmethod 
    def getInstance():
        if Singleton.__instance == None:
            Singleton()
        return Singleton.__instance
    def __init__(self):
        if Singleton.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            Singleton.__instance = self

s1 = Singleton()
s2 = Singleton()


"""Glavna odlika Singleton klase jeste to da je njen konstruktor privatan. Stoga u našem primeru imamo polje instance koje je privatno.
 Nakon toga je dovoljno da  u __init__ metodi proverimo da li je polje već u korišćenju tj. da li imamo instancu. Ako imamo instancu, 
 koristimo naredbu raise da prikažemo izuzetak pri svakom sledećem instanciranju klase. 
 Na ovaj način smo sigurni da će klasa biti instancirana samo jednom, jer u suprotnom dobijamo izuzetak."""


# Factory

"""Ovaj šablon koristimo kada želimo da koristimo posredničku klasu pomoću koje ćemo kreirati instancu određene klase.
 Recimo da u sistemu imamo više klasa korisnika, od kojih želimo da kreiramo jednu, na osnovu toka programa:"""

# primer

class Message(object):
 
   message = ""
   def get_message(self):
      return self.message
 
class User(Message):
   message = "Hello user!"
 
class Administrator(Message):
   message = "Hello administrator!"
 
class SuperAdministrator(Message):
   message = "Hello superadministrator!"

   """Ako bismo želeli da proveravamo koji se korisnik prijavljuje, morali bismo da instanciramo svaku klasu pojedinačno, čak i kada nema potrebe. 
   Da bismo izbegli ovakvu robusnost, uvodimo zasebnu klasu, koja će na jednom mestu vršiti selekciju i kreirati odgovarajuću instancu. Ta klasa će, zapravo, biti Factory klasa:"""

class UserFactory:
    def create_user(self, type):
        targetclass = type.capitalize()
        return globals() [targetclass]()
    
""" Ova klasa će preuzeti koji je korisnički nivo odabran i na osnovu toga sama vratiti poziv klase koja je potrebna. """

""" objekat kreiramo iz Factory klase, a tipove dodajemo naknadno, samo na jednom mestu, u Factory klasi:"""

user_obj = UserFactory()
 
user = []
input_user = input("What is your access level?")
user.append(input_user)
 
for u in user:
   print (user_obj.create_user(u).get_message())

   """Ako ukucate Director dobićete pozdravnu poruku koja je definisana u klasi Director odn. na tom nivou, isto važi i za User i Administrator klase."""


   # Adapter pattern

   """Adapter šablon pripada strukturnim šablonima; on nam omogućava da koristimo dva objekta koja u redovnim uslovima ne bi mogla da komuniciraju."""

   """Adapterom, kao i u inače, povezujemo dva nekompatiblna interfejsa. Primer ovoga iz života bi bio mobilni telefon. Želim da napunimo bateriju telefona, 
   ali imamo samo TypeC punjač a naš telefon podržava stariji standard MicroUSB. To, naravno, nije moguće sve dok nemamo neki adapter za punjač. Isti slučaj je i u programiranju, 
   gde možemo da kreiramo adapter klasu koja će nam omogućiti da se povežemo sa klasom sa kojom u suprotnom ne bismo uspeli da kreiramo konekciju."""







    