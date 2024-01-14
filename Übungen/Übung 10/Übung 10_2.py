# Fakultät von eingegebener Zahl berechnen 

def fakultieren(zahl):
    fakultaet = 1
    while zahl > 0:
        fakultaet = fakultaet * zahl
        zahl -= 1
    print(fakultaet)

def User_input():
    eingabe = True
    while eingabe:
        zahl = input("Geben Sie eine Zahl ein, die sie fakultieren wollen: ") 
        try: 
            zahl = int(zahl)
            if zahl > 0:
                eingabe = False
        except: 
            print("Die Ausgabe ist nicht korrekt, sie muss ganzzahlig und größer als null sein!")

    return zahl

def main():
    x = User_input()
    fakultieren(x)

main()


