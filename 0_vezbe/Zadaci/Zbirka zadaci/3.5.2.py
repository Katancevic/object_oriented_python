klasa = type('X',(),{"sabiranje":lambda self,a,b,c,d,e:a+b+c+d+e})

a=klasa()
print(a.sabiranje(1,2,3,4,5))
