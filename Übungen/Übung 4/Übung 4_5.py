
preis = 20
inflationsrate = 8
jahre = 10
i = 0

if inflationsrate > 8: 
    print(f"Inflationsrate in Prozent: {inflationsrate}")
    for i in range(0, jahre):
        preis = preis * 1.05
        print(f"Preis nach Jahr {i}: {preis}")
        i = i + 1
elif 0 < inflationsrate < 5:
    print(f"Inflationsrate in Prozent: {inflationsrate}")
    inflationsrate = inflationsrate / 100 + 1
    for i in range(0, jahre)