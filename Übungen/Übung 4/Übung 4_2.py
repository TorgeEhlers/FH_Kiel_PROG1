x = int(input("Wie viele Sterne soll das Quadrat lang werden: "))
y = int(input("Wie viele Sterne soll das Quadrat hoch sein: "))

for _ in range(y):
    for _ in range(x):
        print(end="* ")
    print(" \n")
    
