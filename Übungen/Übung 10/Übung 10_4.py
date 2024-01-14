# Vokale in einem Wort zählen

# Vokale in einem Wort berechnen
def anzahl_vokal(wort):
    counter = 0 
    wliste = []
    vliste = []
    vokale = "aeiouAEIOU"
    for x in vokale:
        vliste.append(x)

    for x in wort:
        wliste.append(x)

    for x in wliste:
        if x in vliste:
            counter += 1

    return counter

# Eingabe des Benutzers
def User_input():
    buchstaben = input("Geben Sie eine Liste an buchstaben ein: ")
    return buchstaben

# Hauptfunktion
def main():
    wort = User_input()
    counter = anzahl_vokal(wort)
    print(f"Das Wort {wort} hat {counter} Vokale")

main()

