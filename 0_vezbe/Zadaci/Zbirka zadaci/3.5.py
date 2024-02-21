calc = type('Y',(),{"deljenje":lambda self,a,b:a/b if (b!=0) else 'Greska, b ima vrednos 0'})

c=calc()

print(c.deljenje(1,1))
print(c.deljenje(1,0))