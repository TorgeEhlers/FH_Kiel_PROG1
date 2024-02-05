
class Privatauto:
    def __init__(self):
        self.kmstand = 0

    def fahren(self, km):
        self.kmstand += km
        print(f"Dein Auto ist {self.kmstand} Kilometer gefahren!")

class Arbeitsauto(Privatauto):
    def kosten(self):
        teuer = self.kmstand * 30
        print(f"Die Kosten dafür betragen {teuer}€")

meinAuto = Privatauto()
meinAuto2 = Arbeitsauto()
meinAuto2.fahren(50)
meinAuto2.kosten()
meinAuto.fahren(30)


