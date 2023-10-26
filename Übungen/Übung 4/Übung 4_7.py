# Auslesung von natürlichen Zahlen

# Variablen
zahl2 = 0
eingabe = True

# Eingabe und Auswertung, ob die Zahl größer oder kleiner ist
while eingabe:
    zahl1 = input("Geben Sie eine Zahl ein: ")
    try:
        zahl1 = int(zahl1)
        if zahl1 > zahl2:
            zahl2 = zahl1
    except:
        eingabe = False

# Ausgabe der größten Zahl

print(f"Dies war keine Zahl, die höchste Zahl war: {zahl2}")
