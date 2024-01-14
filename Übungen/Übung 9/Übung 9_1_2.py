# Einschreibeliste für Vorlesungen

class Vorlesung:
    def __init__(self):
        self.titel = "Platzhalter"
        self.studierende = []
    
    def schreibeEin(self, name):
        self.studierende.append(name)
    
    def schreibeAus(self, name):
        self.studierende.remove(name)
    
    def getAnzahlStudierende(self):
        i = 0
        for anzahl in self.studierende:
            i += 1
        print(f"Es sind {i} Studenten eingeschrieben!")

    def getStudierende(self):
        self.studierende.sort()
        print(self.studierende)


class VorlesungOnline(Vorlesung):
    def setLink(self,link):
        self.zoomlink = link
    
    def getLink(self):
        print(f"Der Zomm-Link ist: {self.zoomlink}")



a = VorlesungOnline()
a.schreibeEin("Torge")
a.schreibeEin("Ove")
a.schreibeEin("Tilo")
a.schreibeAus("Tilo")
a.schreibeEin("Meeno")
a.getAnzahlStudierende()
a.getStudierende()
a.setLink("Platzhalter")
a.getLink()

