"""Napraviti program koji ispisuje različite verzije Datuma.
a) Trenutni datum I vreme
b) Trenutna godina
c) Mesec u godini
d) Broj nedelje u godini
e) Ime dana u nedelji
f) Dan u godini
g) Dan u mesecu
h) Dan u nedelji"""

import datetime

trenutni_datum = datetime.datetime.now()
print(f"Trenutni datum i vreme: {trenutni_datum}")

trenutna_godina = datetime.date.today().strftime("%Y") # sintaksa za ispis perioda u vremenu
print(f"Trenutna godina: {trenutna_godina}")

mesec_u_godini = datetime.date.today().strftime("%B")
print(f"trenutni mesec: {mesec_u_godini}")

br_nedelja_u_god = datetime.date.today().strftime("%W")
print(f"Broj nedelja u godini: {br_nedelja_u_god}")

br_dana_u_ned = datetime.date.today().strftime("%w")
print(f"Redni broj dana u nedelji: {br_dana_u_ned}")

dan_u_god =  datetime.date.today().strftime("%j")
print(f"Dan u godini: {dan_u_god}")

dan_u_mescu = datetime.date.today().strftime("%d")
print(f"Dan u mesecu: {dan_u_mescu}")

dan_u_nedelju = datetime.date.today().strftime("%A")
print(f"Dan u nedelju: {dan_u_nedelju}")

