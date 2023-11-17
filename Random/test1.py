zahl = 1
x = 0

try:
    int(zahl)
    it_is = True
except:
    it_is = False


if it_is == True:
    x += 1
else:
    print("Hallo")

print(x)
