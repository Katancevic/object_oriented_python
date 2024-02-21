
def prost(n):
    #ako je broj 1 broj je prost i vracamo True
    if n==1:
        return True
    #U drugom slucaju delicemo broj sa brojevima od 2 do ucitanog broja, ako je ucitan broj deljiv sa nekim brojem nije prost i vracamo False
    for i in range(2,n):
        if(n%i==0):
            return False
    #U drugom slucaju ako ucitan broj nije deljiv ni sa jednim brojem u petlji znaci da je prost pa vracamo True
    return True
   
#ucitavamo broj
a=int(input("Unesite broj: "))
#Ako je broj prost funkcija ce vrati True pa ce if uslov biti tacan
if(prost(a)):
    print("Da")
#Ako broj nije prost funkcija ce vratiti False pa ce if uslov biti netacan
else:
    print("Ne")

