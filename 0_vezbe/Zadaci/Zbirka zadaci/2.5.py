
import datetime

print("Trenutni datum I vreme: " , datetime.datetime.now())
print("Trenutna godina: ", datetime.date.today().strftime("%Y"))
print("Mesec u godini: ", datetime.date.today().strftime("%B"))
print("Broj nedelje u godini: ", datetime.date.today().strftime("%W"))
print("Redni broj dana u nedelji: ", datetime.date.today().strftime("%w"))
print("Dan u godini: ", datetime.date.today().strftime("%j"))
print("Dan u mesecu: ", datetime.date.today().strftime("%d"))
print("Dan u nedelji: ", datetime.date.today().strftime("%A"))

