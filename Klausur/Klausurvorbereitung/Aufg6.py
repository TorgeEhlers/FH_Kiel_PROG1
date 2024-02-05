# Liste definieren
words = ["apple","banana","orange","avocado","grape"]


for wort in words:
    a = []
    for buchstabe in wort:
        a.append(buchstabe)
    if a[0] == "a":
        print(wort)
    else:
        pass