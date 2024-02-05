
class Auto:
    def __init__(self):
        self.kmstand = 0

    def fahren(self,km):
        self.kmstand += km


bmw = Auto()
bmw.fahren(50)
print(bmw)
