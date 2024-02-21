class Student:
    def __init__(self, id_student, ime, fakultet, broj_telefona):
        self.id_student = id_student
        self.ime = ime
        self.fakultet = fakultet
        self.broj_telefona = broj_telefona

    @classmethod   
    def input_student(cls):
        cls.id_student       =   int(input("Id_student: "))
        cls.ime              =       input("Name: ")
        cls.fakultet         =       input("Fakultet: ")
        cls.broj_telefona    =    int(input("Broj telefona: "))
        print("Uneli ste podatke: ", cls.id_student, cls.ime, cls.fakultet, cls.broj_telefona)

Student.input_student()


