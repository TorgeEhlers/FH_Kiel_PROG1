# User Input
a = input("Geben Sie eine ganzzahlige Zahl ein: ")
fakutltaet = 1

zahl = int(a)
# Schleife dür die Fakultät
while zahl > 0:
    fakutltaet = fakutltaet * zahl
    zahl -= 1

print(f"Die Fakultät der Zahl {a} ist {fakutltaet}!")