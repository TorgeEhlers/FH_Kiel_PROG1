class ZeitreiseMaschine:
    def __init__(self):
        self.zieljahr = 0
        self.herkunftJahr = 2024
    
    def eingeben_zieljahr(self):
        jahr = input("Geben Sie das Ziel Jahr ihrere Reise an!")
        self.zieljahr = int(jahr)

    def start(self):
        distanz = self.zieljahr - self.herkunftJahr
        if distanz > 0:
            print(f"Sie sind {distanz} Jahre in die Zukunft gereist")
        else:
            distanz = distanz * (-1)
            print(f"Sie sind {distanz} Jahre in die Vergangenheit gereist!")

a = ZeitreiseMaschine()
a.eingeben_zieljahr()
a.start()