

def anzahl_vokale():
    # Variablen und Listen definieren
    vokale = "aeiouAEIOU"
    wort = "Hallo"
    vokalelist = []
    woerterlist = []
    counter = 0

    # Liste mit allen Vokalen erstellen
    for buchstabe in vokale:
        vokalelist.append(buchstabe)
    
    #Liste mit jedem einzelnen Buchstaben des Wortes
    for buchstabe in wort:
        woerterlist.append(buchstabe)
    
    # Überprüfen ob der Buchstabe aus der Wörterliste in der Vokallsite vorhanden ist
    for buchstabe in woerterlist:
        if buchstabe in vokalelist:
            counter += 1

    print(f"Das Wort {vokale} enthält {counter} Vokale!")

    
anzahl_vokale()