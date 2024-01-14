
class Kaffeemaschine:
    def __init__(self):
        self.kaffeesorten = {
            "Crema": 0, 
            "Cappuccino": 0,
            "Kakao": 0,
            "Espresso": 0,
            "Americano": 0,
            "Latte Macchiato": 0, 
            "Flat White": 0,
        }

    def zubereiten(self, auswahl):
        if auswahl in self.kaffeesorten:
            self.kaffeesorten[auswahl] = self.kaffeesorten[auswahl] + 1
            print(f"{auswahl} wird zubereitet")
        else:
            print("Diese Kaffeesorte gibt es nicht!")


    def auswahl_key(self, liste):
        return liste[1]

    def display(self):
        liste = self.kaffeesorten.items()
        sortierte_liste = sorted(liste,key = self.auswahl_key, reverse = True)
        print("Künstliche Intelligenz !")
        print("Die beliebtesten Kaffeesorten sind: ")
        for sorte in sortierte_liste[:4]:
            print(sorte[0])
    
    def __repr__ (self):
        info = ""
        for sorte in self.kaffeesorten:
            info += f"{sorte+':':18s}:\t{self.kaffeesorten[sorte]}"
        return info

class KaffeemaschineMitMilchaufschäumer(Kaffeemaschine):
    def milchaufschäumen(self):
        print("Schäume Milch auf!")

        


jura1 = KaffeemaschineMitMilchaufschäumer()
jura1.zubereiten("Americano")
jura1.zubereiten("Americano")
jura1.zubereiten("Americano")
jura1.zubereiten("Americano")
jura1.zubereiten("Espresso")
jura1.zubereiten("Espresso")
jura1.zubereiten("Americano")
jura1.zubereiten("Latte Macchiato")
jura1.zubereiten("Latte Macchiato")
jura1.zubereiten("Latte Macchiato")
jura1.zubereiten("Kakao")
jura1.zubereiten("Kakao")
jura1.zubereiten("Kakao")
jura1.zubereiten("Kakao")
jura1.display()
jura1.milchaufschäumen()
