class Zeitreisemaschine:
    def __init__(self):
        self.zielJahr = 0
        self.herkunftJahr = 2023

    def zieljahr(self, ziel):
        self.zielJahr = int(ziel)

    # def herkunftjahr(self, herkunft):
    #     self.herkunftJahr = int(herkunft)
    
    def start(self):
        jahre = 0
        if self.zielJahr > self.herkunftJahr:
            jahre = self.zielJahr - self.herkunftJahr
            print(f"Sie sind {jahre} Jahre in die Zukunft gereist!")
        else:
            jahre = self.herkunftJahr - self.zielJahr
            print(f"Sie sind {jahre} Jahre in die Vergangenheit gereist!")

maschine1 = Zeitreisemaschine()
maschine1.zieljahr(2133)
# maschine1.herkunftjahr(2023)
maschine1.start()