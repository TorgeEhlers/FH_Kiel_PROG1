class Rectangle:
    def __init__(self,x,y):
        self.breite = x
        self.laenge = y

    def rechnen(self):
        A = self.breite * self.laenge
        print(f"Das Rechteck mit der Länge {self.laenge} und der Breite {self.breite} hat ein Flächeninhalt von {A}")

a = Rectangle(3,3)
a.rechnen()