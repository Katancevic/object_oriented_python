drzave=['Srbija','Crna Gora','Bosna i Hercegovina','Hrvatska','Bugarska','Makedonija','Rumunija']

a=int(input("Unesite ceo broj: "))

try:
    print("Grad na poziciji ",a,' je ',drzave[a])
except IndexError:
    print("Taj indeks ne postoji")

