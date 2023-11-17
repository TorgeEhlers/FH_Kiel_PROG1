# Berechnung des Anhalteweges eines Autos 


# User gibt Geschwindigkeit des Fahrezeuges ein

def userInput():
    geschwindigkeit = float(input("Geben Sie ihre Geschwindigkeit in KmH an: "))
    return geschwindigkeit

# Anhalteweg wird aus Geschwindigkeit, Reaktionsweg und Bremswegberechnet 

def berechne_anhalteweg(geschwindigkeit):
    rweg = (geschwindigkeit / 10) * 3
    bweg = (geschwindigkeit / 10)*(geschwindigkeit / 10)
    aweg = rweg + bweg
    return aweg

# Hauptfunktion, die alle Komponenten zusammenfügt

def main():
    kmh = userInput()
    anhalteweg = berechne_anhalteweg(kmh)
    print(f"Der Anhalteweg bei {kmh} km/h beträgt {anhalteweg} Meter.")

# Ausführung der Hauptfunktion

main()