class Student:
    def __init__(self,name,address,phone,course,index_number):
        self.name = name
        self.address = address
        self.phone = phone
        self.course = course
        self.index = index_number
    
    def getinfo(self):
        print(f"Студент: {self.name}, Адреса: {self.address}, Телефон: {self.phone},  Курс: {self.course}, Бр. Индекса: {self.index}")

student_1 = Student("Иван Катанчевић", "Ниш, Драгише Цветковића 24", "+381652249239", "Департмент информатика", "23/1111")
student_2 = Student("Милан Марковић", "Нови Сад, Булевар  Европа 128", "+38164523698", "Туриѕмологија", "23/2222")
student_3 = Student("Јован Јовић", "Београд, Булевар Војводе Путника 45", "+38160235698", "Економија", "23/3333")

student_1.getinfo()
student_2.getinfo()
student_3.getinfo()


