
class Student:
    def __init__(self,name,matrikelnummer):
        self.name = name
        self.matrikelnummer = matrikelnummer
        self.noten =[]
        self.insgesamt = 0
        self.durchschnitt = 0

    def note_hinzufuegen(self):
        boo = True
        while boo == True: 
            note = float(input("Geben Sie ihre Note in Prozent ein: "))
            self.noten.append(note)
            c = int(input("Wollen Sie noch eine Note hinzufügen (Ja = 1, Nein = 0): "))
            if c == 1:
                boo = True
            elif c == 0:
                boo = False
        print(f"Ihre Notenliste ist fertig: {self.noten}")

    def schlechtesten_streichen(self):
        a = 100
        b = 100
        for i in self.noten:
            if i < a:
                a = i
            else:
                pass

        if len(self.noten) > 3:
            for i in self.noten:
                if i == a:
                    pass
                elif i < b:
                    b = i
                else: 
                    pass 
            self.noten.remove(b)        
        self.noten.remove(a) 

    def durchschnit_berechnen(self):
        for i in self.noten:
            self.insgesamt = self.insgesamt + i
        self.laenge = len(self.noten)
        self.durchschnitt = self.insgesamt / self.laenge

    def ausgabe(self):
        print(f"Student: {self.name}, Matrikelnummer: {self.matrikelnummer}")
        print(f"Alle Noten: {self.noten}")
        print(f"Sie haben einen Notendurchschnitt von: {round(self.durchschnitt, 2)}%")


student1 = Student("Torge", "943090")
student1.note_hinzufuegen()
student1.schlechtesten_streichen()
student1.durchschnit_berechnen()
student1.ausgabe()