
a = int(input("Unesite broj: "))
b = int(input("Unesite broj: "))
try:
    print(a/b)
except ZeroDivisionError:
    print("Ne moze se deliti sa 0")