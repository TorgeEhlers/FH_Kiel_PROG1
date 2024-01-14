
class Rectangle:
    def __init__(self, leange, breite):
        self.flaecheninhalt = 0
        self.laenge = int(leange)
        self.breite = int(breite)

    def berechnen(self):
        self.flaecheninhalt = self.laenge * self.breite
        print(f"Der Flächeninhalt beträgt {self.flaecheninhalt} Flächeneinheiten!")
    

rechteck1 = Rectangle(5,6)
rechteck1.berechnen()