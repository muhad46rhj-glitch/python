class pakistan():
    def capital(self):
        print("The capital of Pakistan is Islamabad")

    def language(self):
        print("The official language of Pakistan is Urdu")

    def type(self):
        print("Pakistan is a developing country")


class USA():
    def capital(self):
        print("The capital of USA is Washington D.C.")

    def language(self):
        print("The official language of USA is English")

    def type(self):
        print("USA is a developed country")

obj_pak = pakistan()
obj_usa = USA()

for country in (obj_pak, obj_usa):
    country.capital()
    country.language()
    country.type()
