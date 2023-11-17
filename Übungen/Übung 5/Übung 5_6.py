# Primzahlen Überprüfung 

# Eingabe des Benutzers 

def userInput():
    a = int(input("Geben Sie ihre Zahl ein: "))
    return a 

# Überprüfung, der Teiler

def ueberpruefen(zahl):
    x = 0
    for i in range(1, zahl+1):
        b = int(zahl//i)
        if zahl == b * i:
            x += 1 
        else:
            pass
        i += 1 
    return x 

# Überprüfung, ob Primzahl

def primzahl(anzahl):
    if anzahl >= 3:
        print("Deine Zahl ist keine Primzahl!")
        print(f"Die Zahl hat {anzahl} Teiler")
    else:
        print("Deine Zahl ist eine Primzahl")

# Hauptfunktion 

def main():
    zahl = userInput()
    anzahl = ueberpruefen(zahl)
    primzahl(anzahl)

# Ausführung der Hauptfunktion

main()


    



