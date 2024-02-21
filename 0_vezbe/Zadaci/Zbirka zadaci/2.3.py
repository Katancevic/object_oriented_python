

import time

def prestupna(year):
    if (year % 4 == 0 and year %100!=0) or (year%400==0):
        print('Prestupna')
    else:
        print("Nije prestupna")

        
prestupna(1996)
prestupna(2004)
prestupna(2000)
prestupna(1900)

gmt=time.gmtime()
print(gmt.tm_year)