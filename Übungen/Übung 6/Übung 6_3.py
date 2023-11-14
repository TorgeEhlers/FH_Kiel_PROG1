# Wörter rückwärts schreiben

# Leere Liste
wort = []
umkehr = []

def reverse(text):#
    reversetext = ""
    wort.append(text)
    for i in text:
        umkehr.insert(0, i)
    for elem in umkehr:
        reversetext = reversetext + elem
    return reversetext


    


print(reverse(str(input("Geben Sie ein Wort ein:"))))