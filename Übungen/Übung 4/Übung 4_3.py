buchwert = int(input("Wie hoch ist ihr Buchwert: "))
monat = int(input("Über wie viele Monate wollen Sie abschreiben: "))
abschreibesatz = buchwert / monat

for monat in range(1, monat+1):
    buchwert = buchwert - abschreibesatz
    print(f"Monat {monat:2d}: {buchwert:10.2f} Euro")
