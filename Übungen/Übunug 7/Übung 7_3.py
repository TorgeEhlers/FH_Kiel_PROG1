# Tante-Emma-Laden

warenlager = {  'Butter': 1.90,
                'Brot': 2.30,
                'Schokolade': 1.50,
                'Apfel': 1.20}

def inputUser():
    gekauftebutter = int(input("Wie viel Butter haben Sie gekauft: "))
    gekauftesbrot = int(input("Wie viele Brote haben Sie gekauft: "))
    gekaufteschokolade = int(input("Wie viel Schokolade haben Sie gekauft: "))
    gekaufteapfel = int(input("Wie viele Äpfel haben Sie gekauft: "))
    einkauf =[gekauftebutter, gekauftesbrot, gekaufteschokolade,gekaufteapfel]
    return einkauf


def preis(liste):
    preisbutter = warenlager['Butter'] * liste[0]
    preisbrot = warenlager['Brot'] * liste[1]
    preisschokolade = warenlager['Schokolade'] * liste[2]
    preisapfel = warenlager['Apfel'] * liste[3]
    preise = [preisbutter, preisbrot, preisschokolade, preisapfel]
    return preise

def endpreis(b):
    endpreis = b[0] +  + b[1] + b[2] + b[3]
    return endpreis

def main():
    a = inputUser()
    b = preis(a)
    c = endpreis(b)
 
    print(f"Butter: {b[0]} €")
    print(f"Brot: {b[1]} €")
    print(f"Schokolade: {b[2]} €")
    print(f"Äpfel: {b[3]} €")
    print(f"Gesamt: {round(c, 2)} €")

main()
    

