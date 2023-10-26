# Ein Viereck aus Sternen ausgeben, bei dem man Länge und Höhe selber bestimmen kann

# Einagbe der Werte

x = int(input("Wie viele Sterne soll das Viereck lang werden: "))
y = int(input("Wie viele Sterne soll das Viereck hoch sein: "))

# Schleifen zum zeichnen der Sterne

for _ in range(y):
    for _ in range(x):
        print(end="* ")
    print(" \n")
    
