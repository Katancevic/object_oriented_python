"""Učitati 2 cela broja. Podeliti ih I ispisati rezultat. Ako je drugi 0 izbaciti izuzetak ZeroDvisionError."""

a = int(input("Unesi prvi ceo broj: "))
b = int(input("Unesi drugi ceo broj: "))
try:
    c = a / b

    print(f"Rezultat deljenja dva broja je: {c}")

except ZeroDivisionError:
    print(f"Uneli ste drugi količnik {b}, ne može se deliti sa nulom.")