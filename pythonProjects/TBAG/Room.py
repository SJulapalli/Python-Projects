import Enemy
import NPC
import Objects


class Room:
    name = ""
    description = ""
    enemies = []
    objects = []
    people = []
    dimensions = ""
    left_room = ""
    right_room = ""
    front_room = ""
    previous_room = ""

    def listObjects(self):
        print("The room contains:")
        count = 1
        for x in self.objects:
            print(str(count) + ". " + x.name)
            count = count + 1

class NicksRoom(Room):

    def __init__(self):
        temp = Objects.SmallObject()
        temp.cosbyPoster()
        self.objects.append(temp)
        temp = Objects.SmallObject()
        temp.cosbyDaikamakura()
        self.objects.append(temp)
        self.description = "The room is filled with Cosby paraphernalia and nothing else"
        self.people.append(NPC.Nick)

class VedasRoom(Room):

    def __init__(self):
        temp = Objects.MassiveObject()
        temp.bigMassiveBed()
        self.objects.append(temp)
        temp = Objects.MassiveObject()
        temp.theWHOLEGamingSetup()
        self.objects.append(temp)
        temp = Objects.MassiveObject()
        temp.shelf()
        self.objects.append(temp)
        temp = Objects.MassiveObject()
        temp.mangaShelf()
        self.objects.append(temp)
        self.people.append(NPC.Veda())
        self.description = "The room looks like an African Jungle"


class SrijaysRoom(Room):

    def __init__(self):
        self.description = "The room amounts to little more than a small cardboard box"
        temp = Objects.SmallObject()
        temp.srijaysDidlo()
        self.objects.append(temp)
        temp = Objects.SmallObject()
        temp.stp()
        self.objects.append(temp)
        temp = Objects.MassiveObject()
        temp.excessSchmegma()
        self.objects.append(temp)
        self.people.append(NPC.Srijay())