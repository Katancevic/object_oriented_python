
class Calc:
    number_1 = ""
    number_2 = ""

    def add(self):
        zbir = self.number_1 + self.number_2
        return zbir
    
    def sub(self):
        razlika = self.number_1 - self.number_2
        return razlika
    
    def mul(self):
        proizvod = self.number_1 * self.number_2
        return proizvod
    
    def div(self):
        kolicnik = self.number_1 / self.number_2
        return kolicnik
    
calc = Calc()
calc.number_1 = 8
calc.number_2 = 2

print(f"Rezultat sabiranja:  {calc.add()}")
print(f"Rezultat oduzimanja: {calc.sub()}")
print(f"Rezultat množenja:   {calc.mul()}")
print(f"Rezultat deljenja:   {calc.div()}")