""" Napraviti listu koja sadrži imena država. Uneti ceo broj I ispisati koji grad se nalazi na toj poziciji. 
Ako podatak na toj poziciji ne postoji podići IndexError izuzetak."""


lista = ["Srbija", "Spanija", "Italija", "Grcka", "Francuska"]

broj = int(input("Unesi ceo broj: "))


try:
    print(f"Grad ne postoji {broj} je {lista[broj]}")

except IndexError:
    print("Index pod tim brojem ne postoji u listi")