

class Auto:

    def __init__(self, name):
        self._kmstand = 0           # _ bedeutet, dass man außerhalb die Variable nicht verändern darf 
        self.naechste_wartung = 500
        self.name = name
    
    def fahren(self, gefahrene_km):
        self._kmstand += gefahrene_km
        print(f"Fahre {gefahrene_km}km mit dem Auto")
        self.pruefeWartung()

    def pruefeWartung(self):
        if self._kmstand >= self.naechste_wartung:
            print("Achtung bitte Wartung durchführen!")

    def macheInspektion(self):
        print("Überprüfe und mache alles.")
        self.naechste_wartung = self._kmstand + 500
        print(f"Nächster Termin bei {self.naechste_wartung}km")

    def zeigeKmStand(self):
        print(f"Der km Stand von {self.name} ist {self._kmstand} km")

    def __repr__(self):
        return f"Auto('{self.name}')"

bmw = Auto("BMW Z3")
bmw.zeigeKmStand()
bmw.fahren(400)
bmw.fahren(130)
bmw.macheInspektion()
bmw.fahren(50)
bmw.fahren(191288)
bmw.zeigeKmStand()
print(bmw)
bmw.kmstand = 121987
bmw.zeigeKmStand()

# vw = Auto("VW Golf")
# vw.zeigeKmStand()
# vw.fahren(499)
# vw.fahren(120)
# vw.macheInspektion()
# vw.fahren(20)
# vw.zeigeKmStand()
# print(vw)


