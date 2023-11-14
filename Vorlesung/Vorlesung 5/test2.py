
text = "Die Vorlesung ist echt langweilig"

liste = text.split(" ")
for wort in liste:
    print(f"Wort {wort} hat {len(wort)} Zeichen")

for index in range(len(liste)):
    print(liste[index])