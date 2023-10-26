# Ein ausgewähltes Wort n-mal ausgeben

# Eingabe der Werte
wort = str(input("Geben Sie ein Wort ein:"))
n = int(input("Wie häufig soll das Wort angezeigt werden:"))

# Schleife zum ausgeben
while n > 0:
    print(wort)
    n = n - 1