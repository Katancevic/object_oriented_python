""" Napraviti zadatak koji učitava ceo broj 3 puta koristeći while petlju. Broj bi trebalo da se nalazi između 1 I 5. Ako broj nije između 1 I 5, uneti
ponovo broj. Pre nego što program ispiše uneti broj, program treba da sačeka toliko sekundi kolika je vrednost ucitanog broja. """

import time


i = 0
while i <3:
    broj = int(input("Unesi broj: "))

    if (broj < 1 or broj > 5):
        print(f"Broj koji je unesen {broj} nije u opsegu između 1-5, pokušajte ponovo.")
        continue
    time.sleep(broj)

    print(f"Uneti broj je {broj}")

    i += 1




