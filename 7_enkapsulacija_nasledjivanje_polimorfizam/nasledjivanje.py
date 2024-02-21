"""Nasleđivanje je mehanizam koji nam omogućava da već napisan kod iskoristimo veći broj puta. 
Tada nasleđivanjem klase iskorišćavamo kod te klase u nekoj drugoj. 
Ako ovo definišemo kroz objektni pristup, nasleđivanje predstavlja mehanizam klase da podeli svoje članove (metode i polja) 
sa nekom drugom klasom tokom izvršavanja pograma."""

# primer nasledjivanja

# Base class
class Animal:
 
    # Class attribute
    species = 'mammal'
    name = " "
    age = 0
 
    # Instance attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age
 
    # instance method
    def description(self):
        return "{} is {} years old".format(self.name, self.age)
 
    # instance method
    def speak(self, sound):
        return "{} says {}".format(self.name, sound)
    

    """U prvom delu koda imamo definisanu klasu Animal i ona predstavlja našu roditeljsku klasu.
      U njoj već imamo definisane podatke za jednu životinju i ta životinja može imati vrstu kojoj pripada, visinu i starost. 
      Pored toga imamo tri metode u njoj: init da obavimo unos parametara i dve instancne metode – description i speak. 
      Obe ispisuju neke podatke na osnovu onoga što unesemo. Nakon toga, u drugom delu programa:"""


# Derived class (inherits from Animal class)
class Dog(Animal):
    def run(self, speed):
        return "{} runs {}".format(self.name, speed)
 
# Derived class inherits attributes from the parent class
 
rex = Dog("Rex", 10)
print(rex.description())
 
# Derived class has specific attributes and behavior as well
print(rex.run("slowly"))

# Funkcija super() Funkcija kojom se u decijim klasama prepisuje metoda roditeljske klase
# primer:

class Person:
    def __init__(self,firstname,lastname):
        self.firstname = firstname
        self.lastname = lastname
    def show(self):
        print("Person: ", self.firstname, self.lastname)
    
class Student(Person):
    def __init__(self,firstname,lastname,indexnumber):
        super().__init__(firstname,lastname)
        self.indexnumber = indexnumber
    
    def show(self):
        print("Student: ", self.firstname, self.lastname,self.indexnumber)


st = Student("John","Smith","120/001")
st.show()

""" roditeljska klasa Person prikuplja i ispisuje ime i prezime osobe, dok Student klasa nasleđuje podatke i metode Person klase i dodaje broj indeksa. 
Specifična situacija je sa metodom show. Ona se pojavljuje u obe klase i prepisuje se tako da je aktivna samo metoda show iz dete-klase, 
što možemo videti i na ispisu, gde će biti ispisani svi podaci uključujući i broj indeksa, koji se pojavljuje samo u Student klasi."""


"""u slučaju da nam je potreban metod iz roditeljske klase, koji je sada prepisan? Iako smo prepisali roditeljski metod, to ne znači da je on bespovratno izgubljen, 
odnosno, da je stvarno prepisan. Ukoliko nam zatreba, možemo doći do njega pomoću funkcije super."""


class Person:
    def __init__(self,firstname,lastname):
        self.firstname = firstname
        self.lastname = lastname
    def show(self):
        print("Person: ", self.firstname, self.lastname)
    
class Student(Person):
    def __init__(self,firstname,lastname,indexnumber):
        super().__init__(firstname,lastname)
        self.indexnumber = indexnumber
    
    def show(self):
        print("Student: ", self.firstname, self.lastname,self.indexnumber)
        super().show()


st = Student("John","Smith","120/001")
st.show()

# primer_2

class Person:
  def __init__(self):
    pass
 
# Single level inheritance
class Employee(Person):
  def __init__(self):
    pass
 
# Multi-level inheritance
class Manager(Employee):
  def __init__(self):
    pass
 
# Multiple inheritance
"""class Enterprenaur(Person, Employee):
  def __init__(self):
    pass
"""




