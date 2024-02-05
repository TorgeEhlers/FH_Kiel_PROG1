
x = True
while x == True:
    z = input("Geben Sie eine Zahl ein: ")
    try:
        zahl = int(z)
        print("Die Eingabe war erfolgreich!")
        x = False
    except:
        print("Die Eingabe war falsch!")
        print("Probieren Sie erneut!")
