""" Polimorfizam u objektno orijentisanom programiranju znači da će se istoimeni metod u jednoj klasi različito 
ponašati od istoimenog metoda u drugoj klasi, pri čemu obe klase imaju istog roditelja
Na primer, ako bismo rekli da su pas i ptica potklase klase životinja, te da obe imaju metod kreći se, ova dva metoda, iako se isto zovu, 
imala bi potpuno drugačiju realizaciju, jer ptica leti, a pas hoda. """
# primer

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
 
class Professor(Person):
    def __init__(self,firstname,lastname,subject):
        super().__init__(firstname,lastname)
        self.subject = subject
    def show(self):
        print("Professor: ", self.firstname, self.lastname,self.subject)

person=Person("John","Davidson")
student=Student("Will","Smith","102/39")
professor=Professor("Edward","Owen","Python Programming")
 
person.show()
student.show()
professor.show()


