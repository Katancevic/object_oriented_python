"""Napraviti lambda funkciju koja filtrira elemente liste u zavinosti da li su negativni ili ne.
Potrebno je da funkcija vrati listu pozitivnih elemenata početne liste."""

lista = [5,12,13,18,24,29,18,17, -5,-89,-25,-6]

positive = list(filter(lambda x : (x > 0), lista))

print(f"Pozitivna lista: {positive}")