# Warteschlange im Amt

class Warteschlange:

    def __init__(self):
        self.warteschlange = []

    def ankommen(self):
        name = input("Geben Sie ihren Namen ein: ")
        self.warteschlange.append(name)
        print(self.warteschlange)
    
    def ausgabe(self):
        print(self.warteschlange)

    def verlassen(self):
        wert = self.warteschlange.pop(0)
        print(wert)
 

w = Warteschlange()
w.ausgabe()
w.ankommen()
w.ankommen()
w.ankommen()
w.ausgabe()
w.verlassen()
w.verlassen()
w.verlassen()

