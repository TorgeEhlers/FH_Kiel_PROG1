
eingabe = True

while eingabe:
    alter = input("Geben Sie ihr Alter ein: ")
    try: 
        alter = int(alter)
        if alter > 0:
            eingabe = False
        else:
            print("Die Zahl ist nicht korrekt, geben Sie bitte erneut ein! (Die Zahl muss ganzzahlig sein!)")
    except:
        print("Die Zahl ist nicht korrekt, geben Sie bitte erneut ein! (Die Zahl muss ganzzahlig sein!)")

print(f"Die Eingabe ist korrekt, du bist {alter} Jahre alt!")
