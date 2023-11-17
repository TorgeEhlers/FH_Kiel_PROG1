# Eingabe
groesse_cm = input("Bitte Größe in cm eingeben:")
groesse_cm = int(groesse_cm)

gewicht_kg = input("Bitte Gewicht in kg eingeben:")
gewicht_kg = float(gewicht_kg)
print(f"Du bist {groesse_cm}cm groß und {gewicht_kg}kg schwer.")

# Verarbeitung
bmi = gewicht_kg / ((groesse_cm/100) **2)

#Ausgabe
print("bmi =", bmi )