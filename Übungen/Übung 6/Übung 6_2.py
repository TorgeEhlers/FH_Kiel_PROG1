# Variablen
gesamt = 0
avg = 0
hmonat = 0
nmonat = 100000000000

# Leere Liste erstellen
umsatz = []


for i in range(1,13):
    monat = int(input(f" Bitte geben Sie den Umsatz für den Monat {i} ein: "))
    umsatz.append(monat)
    gesamt += monat
    if monat >= hmonat:
        hmonat = monat
    elif monat <= nmonat:
        nmonat = monat
    else:
        pass

avg = gesamt / 12

print(f"Sie haben einen gesamt Umsatz von {gesamt}€")
print(f"Höchster Umsatz des Jahres: {hmonat}€")
print(f"Niedrigser Umsatz des Jahres: {nmonat}€")
print(f"Durchschnittlicher Umsatz des Jahres: {avg}€")
