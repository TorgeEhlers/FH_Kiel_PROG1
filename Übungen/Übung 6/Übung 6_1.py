produktpreise = [100, 150, 200, 250, 300, 500, 20, 30, 80, 12, 8, 23, 45]


avg = 0
for i, zahl in enumerate(produktpreise):
    avg += zahl

Durchschnitt = avg / (i + 1)

print(f"Der Durchschnitt beträgt: {Durchschnitt}")