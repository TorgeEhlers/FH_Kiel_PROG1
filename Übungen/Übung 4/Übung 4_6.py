# Tagesrechner seit Jahresbeginn

# Variablen
eingabe = True
eingabe2 = True 
eingabe3 = True
eingabe4 = True
anzahl_tage = 0

# Eingabeüberprüfung Monate

while eingabe: 
    monat = input("In welchem Monat befinden Sie sich: ")
    try:
        monat = int(monat)
        if 0 < monat < 13:
            eingabe = False
        else:
            print("Der Monat muss zwischen 1 und 12 liegen!")
    except:
        print("Dies ist keine nummerische Zahl!")
        print("Geben Sie eine neue Zahl ein!")

# Eingabeüberprüfung Tage

while eingabe2:
    tag = input("Welcher Tag im Monat ist es: ")
    try:
        tag = int(tag)
        if monat == 2:
            while eingabe3:
                if 0 < tag < 29:
                    eingabe3 = False
                    tag = int(tag)
                else: 
                    print("Februar hat nur 28 Tage, bitte gib eine neue Zahl ein!")
                    tag = input("Welcher Tag im Monat ist es: ")
            eingabe2 = False
        elif monat == 4 or monat == 6 or monat == 9 or monat == 11:
            while eingabe4:
                if 0 < tag < 31:
                    eingabe4= False
                    tag = int(tag)
                else: 
                    print("Dieser Monat hat nur 30 Tage, bitte gib eine neue Zahl ein!")
                    tag = input("Welcher Tag im Monat ist es: ")
            eingabe2 = False
        elif 0 < tag < 32:
            eingabe2 = False
        else:
            print("Es geht nur von 1 bis 30 Tagen!")
    except:
        print("Dies ist keine nummerische Zahl!")
        print("Geben Sie eine neue Zahl ein!")

# Addierung der bereits vergangenen Monate

for i in range(1, monat):
    if i == 1 or i == 3 or i == 5 or i == 7 or i == 8 or i == 10 or i == 12:
        anzahl_tage +=31
    elif i == 2:
        anzahl_tage += 28
    else:
        anzahl_tage += 30
 
# Addierung der Tage des aktuellen Monats auf die bisher vergangenen Monate

anzahl_tage += tag 

# Ausgabe 

print(f"Es sind schon {anzahl_tage} Tage vergangen")
