# iterativ

def potenz(basis, exponent):
    wert = 1
    a = True
    while a == True:
        wert = wert * basis
        exponent -= 1
        if exponent == 0:
            a = False
    return int(wert)

def main():
    basis = int(input("Geben Sie den Wert der Basis ein: "))
    exponent = int(input("Geben Sie den Wert des Exponenten ein: "))
    print(f"Das Potenz lautet:", potenz(basis, exponent))

main()

# rekursiv

def potenz2(basis2,exponent2):
    if exponent2 == 0:
        return 1
    return basis2 * potenz2(basis2, exponent2 - 1)

def main2():
    basis2 = int(input("Geben Sie den Wert der Basis ein: "))
    exponent2 = int(input("Geben Sie den Wert des Exponenten ein: "))
    print(f"Das Potenz lautet:", potenz2(basis2, exponent2))



main2()

