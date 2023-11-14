# Es wird ein Bruch aus zwei eingegebenen Zahlen erstellt

eingabe = 0
    
def bruch_zu_string (a,b):
    print(f"Die beide Zahlen als Bruch: {a}/{b}")

# Zwei Zahlen werden als Dezimalzahl angegeben

def bruch_zu_string2 (a,b):
    print(f" Die beiden Zahlen als Dezimalzahl: {a/b}")

# Eingabe des Benutzers
    
def inputUser():
    a = int(input("Geben Sie eine Zahl für den Nenner ein: "))
    b = int(input("Geben Sie eine Zahl für den Zähler ein: "))
    return(a,b)

# Ausgabefunktion

def output():
    print(bruch_zu_string(inputUser))
    print(bruch_zu_string(inputUser))

output()
    



