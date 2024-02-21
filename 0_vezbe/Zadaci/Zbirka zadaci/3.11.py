class Season_message:
    message = ""
    def get_message(self):
        return self.message

class Prolece(Season_message):
   message = "Stiglo je prolece!"

class Leto(Season_message):
   message = "Stiglo je leto!"

class Jesen(Season_message):
       message = "Stigla je jesen!"
       
class Zima(Season_message):
       message = "Stigla je zima!"


class Season:
    def create_season(self, name_of_season):
        targetclass = name_of_season.capitalize()
        return globals()[targetclass]()


season_obj = Season()

season = []
godisnje_doba = input("Unesite godisnje doba: ")
season.append(godisnje_doba)

for u in season:
   print (season_obj.create_season(u).get_message())
