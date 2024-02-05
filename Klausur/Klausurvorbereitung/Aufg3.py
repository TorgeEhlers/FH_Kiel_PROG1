# Eingabe des Alters überprüfen

x = True

while x == True:
    alter = input("Geben Sie ihr Alter ein: ")
    try:
        a = int(alter)
        print("Die Eingabe war korrekt!")
        x = False
    except:
        print("Diese Eingabe ist nicht korrekt!")
        print("Es muss eine ganzzahlige Zahl sein!")
        print("Probieren Sie es erneut")
