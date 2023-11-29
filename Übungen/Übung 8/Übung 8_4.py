# Fernseher

class Senderliste:

    def __init__(self):
        self.senderliste = {}
        self.sender = 0

    def addSender(self):
        a = True
        platz = 0
        while a:
            weiter = 0 
            sender = input(f"Geben Sie ihren Sender ein: ")
            platz = int(input(f"Auf welchen Senderplatz soll dieser Sender: "))
            if platz > 30:
                print("Die Sender Nummer ist zu hoch!")
                break
            self.senderliste[platz] = sender
            weiter = int(input("Möchten Sie einen weiteren sender eingeben? (0 = Nein; 1 = Ja): "))
            if weiter == 0:
                a = False
        print("Ihre Senderliste ist fertig!")

    def senderlisteAbrufen(self):
        print(self.senderliste)
    
    def senderAbrufen(self):
        self.sender = int(input("Welchen Senderplatz wollen Sie abrufen: "))
        print(self.senderliste[self.sender])

    def senderHoch(self):
        self.sender += 1
        print(self.senderliste[self.sender])
 

s = Senderliste()
s.addSender()
s.senderlisteAbrufen()
s.senderAbrufen()
s.senderHoch()
s.addSender()
