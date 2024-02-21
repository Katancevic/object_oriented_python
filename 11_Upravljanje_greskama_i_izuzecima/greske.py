# softverske greske u osnovi mogu biti sintakstne i logicne takodje mozemo ih podeliti kao greske u prevodjenju i greske u izvrsavanju

# sintakstne greske prilikom kucanje kodova upoznati sa ovim

# logicne greske ne postoji probelm sa sintaksom ali ne bojemo dobar rezultat

a = float(input("Number1: "))
b = float(input("Number2: "))

c = a+b/2

print("srednja vrednost: ", c)

# Hvatanje greske try/exept

try:
    x = 125
    y = 0
    print(x/y)

except NameError:
    print("You wan't see me!")

except ZeroDivisionError:
    print("Can't division by zero")

except Exception:
    print("Error is here!")

finally:
    print("Value of: ",y)

    # rucno izbacivanje izuzetaka, mozemo u bilo kom delu izvrsavanje programa
    # da mozemo da prekinemo program i vratimo gresku

    # primer
"""
    a = "123"

    if not type(a) is int:
        raise TypeError("Wrong type!")
"""
    
    # kreirati izuzetke primer
class Not_a_number_exeption(Exception):
    pass
class Zero_division_exeption(Exception):
    pass
class Invalid_operationExeption(Exception):
    pass

class Calculator():
     @staticmethod
     def calculate(a,b,op):
        if not isinstance(a,int) or not isinstance(b,int):
            raise Not_a_number_exeption()
        if b == 0:
            raise Zero_division_exeption()
        if not op in ["+", "-", "*", "/"]:
            raise Invalid_operationExeption()
        
        if op == "+":
            return a + b
        if op == "-":
            return a - b
        if op == "*":
            return a * b
        if op == "/":
            return a / b
        
try:
    x= Calculator.calculate(3,2,"+")
    print(x)
except Not_a_number_exeption:
    print("Nije broj")
except Zero_division_exeption:
    print("deljenje sa nulom")
except Invalid_operationExeption:
    print("los operator")
except Exception:
    print("Error Found")

        
