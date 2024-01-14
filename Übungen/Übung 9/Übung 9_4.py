# Hotel

class Room:
    def __init__(self, nummer):
        self.rooms = {}
        self.rooms[nummer] = True



class Hotel:
    def isAvailable(self, nummer):
        if self.rooms[nummer] == True:
            print("Das Zimmer ist noch frei!")
        elif self.rooms[nummer] == False:
            print("Das Zimmer ist schon belegt!")
        else:
            print("Dieses Zimmer gibt es nicht")




rooms = []
rooms.append(Room(100))
rooms.append(Room(101))
rooms.append(Room(102))
print(rooms)


