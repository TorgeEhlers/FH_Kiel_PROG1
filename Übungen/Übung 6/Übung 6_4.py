# Satz Analyse

satz = []

def userInput():
    a = str(input("Geben Sie ein Satz ein: "))
    return a

def satz_analyse(text):
    satz = text.split(" ")
    print(f"Der Satz hat {len(satz)} Wörter")

def buchstaben_analyse():
    

def main():
    text = userInput()
    satz_analyse(text)
