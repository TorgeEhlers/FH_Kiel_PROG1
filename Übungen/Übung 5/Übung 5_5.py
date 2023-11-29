# Verbesserter BMI Rechner

# Eingabe der Größe

def userInputGroesse():
    a = int(input("Geben Sie ihre Größe in cm an: "))
    return a

# Eingabe des Gewichts

def userInputGewicht():
    b = float(input("Geben Sie ihr Gewicht in kg ein: "))
    return b

# Berechnug des BMIs

def bmi_rechner(groesse, gewicht):
    bmi = gewicht / ((groesse/100) ** 2)
    return bmi

# Auswertung des BMIs

def bmi_auswertung(bmi):
    if bmi < 18.5:
        print("Sie haben Untergewicht!")
    elif 18.5 < bmi < 24.9:
        print("Sie haben Normalgewicht!")
    elif 25 < bmi < 29.9:
        print("Sie haben Übergewicht!")
    elif 30  < bmi < 34.9:
        print("Sie haben Adipositas Grad 1!")
    elif 35 < bmi < 39.9:
        print("Sie haben Adipositas Grad 2!")
    elif bmi > 40:
        print("Sie haben Adipositas Grad 3!")

# Hauptfunktion
def main():
    groesse = userInputGroesse()
    gewicht = userInputGewicht()
    bmi = bmi_rechner(groesse, gewicht)
    auswertung = bmi_auswertung(bmi)

# Ausführung der Hauptfunktion

main() 
