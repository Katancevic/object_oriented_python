try:
    with open("izrazi.txt",'r') as f:
        c=f.read()
        for l in c:
            print(l,end="")
    
except IOError:
  print("Greska pri otvaranju fajla")

