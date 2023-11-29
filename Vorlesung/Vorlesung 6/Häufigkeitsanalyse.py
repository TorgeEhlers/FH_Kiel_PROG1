
zahlen ="6319462934935198358418943759194387589139566531985984390156797431"

zaehlliste = [0,0,0,0,0,0,0,0,0,0]

for zahl in zahlen:
    index = int(zahl)
    zaehlliste[index] += 1

for index, zahl in enumerate(zaehlliste):
    print(f"Die Zahl {index} kommt {zahl}x vor")


print(zaehlliste)