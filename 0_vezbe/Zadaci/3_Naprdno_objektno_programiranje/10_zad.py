"""Napraviti klasu Pas pomoću Singleton pattern-a. Potrebno je definisati ime psa I metodu oglašavanje koja ispisuje oglašavanje psa. 
Instancirati jedan objekat klase Pas, pozvati metodu oglašavanje, stopirati program na 3 sekunde pa instancirati još jedan objekat 
I pozvati metodu oglašavanje nad njim."""

import time

class Pas:
    __instance = None
    @staticmethod
    def get_instance():
        if Pas.__instance == None:
            Pas()
        return Pas.__instance
    
    def __init__(self, ime) -> None:
        if Pas.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            Pas.__instance = self
            self.ime = ime

    def oglasavanje(self):
        print("Pas. oglasavam se sa av,av...")


obj1 = Pas("Zucko")
obj1.oglasavanje()

time.sleep(3)

obj2 = Pas("Macka")
obj2.oglasavanje()

    