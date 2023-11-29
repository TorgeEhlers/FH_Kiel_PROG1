# Währungsrechner

waehrungen = {"USD": 1.11, "EUR": 1, "GBP": 0.85, "CHF": 1.06}


def userInput():
    a = float(input("Geben Sie ihren Geldbetrag ein: "))
    b = input("Geben Sie ihre Währung ein (z.B. USD, EUR, GBP, CHF): ")
    c = input("Bitte geben Sie die Quellwährung ein (z.B. USD, EUR, GBP, CHF): ")
    liste =[]
    liste.append(a, b, c)
    return liste


print(userInput())







