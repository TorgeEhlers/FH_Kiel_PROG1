def anfangsbuchstabe():
    words = ["apple", "banana", "orange", "avocado","grape"]
    a = []
    for wort in words:
        b =[]
        for i in wort:
            b.append(i)
        if b[0] == "a":
            a.append(wort)
        else:
            pass
    
    return a

def main():
    liste = anfangsbuchstabe()
    print(f"Die Wörter {liste} beginnen mit dem Buchstaben a!")

main()
