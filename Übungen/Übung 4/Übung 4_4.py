# Dieses Programm berechnet, wie lange es dauert eine bestimmte Höhe an Schulden zurückzuzahlen.
schulden = float(input("Wie hoch sind Ihre Schulden: "))
rückzahlung = float(input("Wie viel wollen sie pro Monat zurück zahlen: "))
zinsen = float(input("Wie viel Prozent an Zinsen bekommen Sie: "))
monat = 0
zinsen = zinsen / 100 + 1


while schulden > 0:
    schulden = schulden - rückzahlung
    schulden = schulden * 1.01
    monat += 1
    if schulden < 0:
        print(f"Monat {monat}: 0")
        break
    else:
        print(f"Monat {monat}: {schulden:10.2f}")
    
print(f"Das Unternehmen benötigt {monat} Monate, um schuldenfrei zu sein.")



