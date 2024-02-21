class City:
    country = "Serbia"
    population = ""
    mayor = ""
    
    @staticmethod
    def what_country():
        print(City.country)


City.what_country()