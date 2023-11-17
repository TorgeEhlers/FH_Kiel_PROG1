# Berechnung des optimalen Pulses


# Eingabe des Benutzers

def userInput():
    a = int(input("Alter: "))
    return a

# Berechnung des optmalen Pulses 

def optimaler_puls(b):
    puls = 165 - 0.75 * b
    return puls

# Zusammnführung der Funktionen

def main():
    alter = userInput()
    opuls = optimaler_puls(alter)
    print(f"optimaler Puls: {opuls}")

# Ausführung der Hauptfunktion

main()