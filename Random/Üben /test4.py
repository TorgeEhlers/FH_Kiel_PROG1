
# Flächeinhalt eines Rechtecks berechnen
def rechteck(x,y):
    A = x * y
    return A

def dreieck(g,h):
    B = 0.5 * g * h
    return B 

def zusammenrechnen(a,b):
    inhalt = a + b
    return inhalt

def main():
    a = rechteck(1,2)
    b = dreieck(2,2)
    print(f"Beide Formen haben einen Flächeninhalt von insgesamt{zusammenrechnen(a,b)} FE")


main()
