class Tier:
    def __init__(self, laut):
        self.laut = laut
        self.laut_geben()
        
    def laut_geben(self):
        print(self.laut)

class Hund(Tier):
    def __init__(self):
        self.laut = "Wuff"
    def laut_geben(self):
        Tier(self.laut)

class Katze(Tier):
    def __init__(self):
        self.laut = "Miau"
    def laut_geben(self):
        Tier(self.laut)

dackel = Hund()
dackel.laut_geben()
katze = Katze()
katze.laut_geben()