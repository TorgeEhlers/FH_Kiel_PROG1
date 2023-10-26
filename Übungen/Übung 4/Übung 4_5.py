
# Berechnung der Auswirkung der Inflationsrate auf ein Produkt nach n-Jahren
# Eingabe der Werte

preis = float(input("Wie hoch ist ihr Ausgangspreis: "))
inflationsrate = float(input("Wie hoch ist die Inflationsrate in Prozent: "))
jahre = int(input("Über wie viele Jahre soll die Inflationsrate ausgegeben werden: "))
i = 0

# Berechnung wenn Inflationsrate über 5% liegt

if inflationsrate >= 5: 
    print(f"Inflationsrate in Prozent: {inflationsrate}")
    for i in range(0, jahre):
        preis = preis * 1.05
        print(f"Preis nach Jahr {i}: {round(preis, 2)}")

# Berechnung, wenn Inflationsrate unter 5%

elif 0 < inflationsrate < 5:
    print(f"Inflationsrate in Prozent: {round(inflationsrate, 2)}")
    inflationsrate = inflationsrate / 100 + 1
    for i in range(0, jahre):
        preis = preis * inflationsrate
        print(f"Preis nach Jahr {i}: {round(preis, 2)}")

