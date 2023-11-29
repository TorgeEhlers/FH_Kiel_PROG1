# Mein elektronisches Sparschwein

class Sparschwein:

    def __init__(self):
        self.geld = 0

    def einzahlen(self):
        ebetrag = float(input("Wie viel geld wollen Sie einzahlen (in Euro): "))
        self.geld += ebetrag
        print(f"{ebetrag}€ wurden erfolgreich eingezahlt!")

    def abheben(self):
        abetrag = float(input("Wie viel Geld wollen Sie abheben( in Euro):"))
        self.geld -= abetrag
        print(f"{abetrag}€ wurden erfolgreich abgehiben!")

    def zeige_geldbestand(self):
        print(f"Sie haben {self.geld}€ in ihrem Sparschwein!")

rs = Sparschwein()
rs.einzahlen()
rs.einzahlen()
rs.zeige_geldbestand()
rs.abheben()
rs.zeige_geldbestand()