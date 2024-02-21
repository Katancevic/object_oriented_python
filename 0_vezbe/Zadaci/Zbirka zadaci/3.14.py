class Experience_message:
    message = ""
    def get_message(self):
        return self.message

class Junior(Experience_message):
   message = "Ja sam junior programer!"

class Medior(Experience_message):
   message = "Ja sam medior programer!"

class Senior(Experience_message):
       message = "Ja sam senior programer!"



class Experience:
    def create_season(self, experience_level):
        targetclass = experience_level.capitalize()
        return globals()[targetclass]()


experience_obj = Experience()

experience = []
level = input("Unesite nivo iskustva: ")
experience.append(level)

for u in experience:
   print (experience_obj.create_season(u).get_message())
