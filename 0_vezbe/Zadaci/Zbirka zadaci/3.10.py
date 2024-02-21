import time

class Pas:
    __instance = None
    @staticmethod 
    def getInstance():
        if Pas.__instance == None:
            Pas()
        return Pas.__instance
    
    def __init__(self,ime):
        if Pas.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            Pas.__instance = self
            self.ime=ime
        
    def oglasavanje(self):
        print('Ja sam pas i ja se oglasavam sa av av ')

s1 = Pas('Zucko')
s1.oglasavanje()

time.sleep(3)

s2 = Pas('Maca')
s2.oglasavanje()
