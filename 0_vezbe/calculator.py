class Calculator:
    number1 = 0.0
    number2 = 0.0
    def add(self):
        return self.number1 + self.number2
    def sub(self):
        return self.number1 - self.number2
    def mul(self):
        return self.number1 * self.number2
    def div(self):
        return self.number1 / self.number2

calc = Calculator()
calc.number1 = 3
calc.number2 = 2
print(calc.add())
print(calc.sub())
print(calc.mul())
print(calc.div())