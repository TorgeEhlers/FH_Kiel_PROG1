# Text der Bibel lesen, Wörter zählen und als CSV ausgeben

import os

# Variable initialisieren

woerterCounter = 0
woerterDict = {}

# Zuweisen ders VErzeichnisses der geöffneten Datei
aktuelles_verzeichnis = os.path.dirname(__file__)
print("Das aktuelle Verzeichnis lautet:", aktuelles_verzeichnis)

# Dateiname für das Einlesen zusammenführen
dateiname = os.path.join(aktuelles_verzeichnis, "bibel.txt")
print("Der Dateipfad der Bibel.txt lautet: ", dateiname)

# Datei öffnen 
datei = open(dateiname, "r")

for zeile in datei:
    # Definition aller Zeichen, die entfernt werden sollen
    ueberspringe = [".",",",";",":","(",")","#","-","§","!","\n","1","2","3","4","5","6","7","8","9","0"]
    # Schleife zum prüfen jedes Chars in jeder Zeile 
    for character in ueberspringe:
        zeile = zeile.replace(character, "")
   # Maßnahme zur Verienheitlichung der Zeichenkette
    zeile = zeile.lower() # Alle Buchstaben werden klein gemacht
    zeile = zeile.strip() # Leerzeichen am Anfang und Ende entfernen
    # überführen der Zeichenkette in eine Liste
    woerter = zeile.split(" ")
    woerterCounter += len(woerter)
    #  Durch die Liste woerter iterieren   
    for wort in woerter:
        if wort in woerterDict:
            woerterDict[wort] += 1
        else:
            # Prüfen ob das Wort nicht leer oder größer als drei Zeichen ist
            if wort != "" and len(wort) > 3:    
                woerterDict[wort] = 1

# Datei wieder schließen
datei.close()

print(woerterDict)