import time


class Object:
    name = ""
    desc = ""
    liftable = True
    dmg = 0
    health = 0

    def __init__(self):
        pass

    #  Method for initializing custom objects
    def initCustom(self, name, desc, liftable, dmg, health):
        self.name = name
        self.desc = desc
        self.liftable = liftable
        self.dmg = dmg
        self.health = health

    #  Assigns the object the parameters of a desk
    def desk(self):
        obj = Object()
        obj.name = "Mahogany Desk"
        obj.desc = "It is a small desk, suitable for one person. Upon it lies a few open books and a small candle."
        obj.liftable = True
        obj.dmg = 10
        obj.health = 40
        return obj

    #  Assigns the object the parameters of a bookshelf
    def bookShelf(self):
        obj = Object()
        obj.name = "Bookshelf"
        obj.desc = "It is a large bookshelf filled with books. You don't recognize any of the titles."
        obj.liftable = False
        obj.dmg = 100
        obj.health = 70
        return obj

    #  Handles dealing damage to an object
    def dmg(self, dmg):
        self.health -= dmg
        print(self.name + "takes " + dmg + "damage!")

    #  Handles interaction between the player and an object
    def interact(self):
        print("You walk up to the " + self.name)
        time.sleep(.75)
        print(self.desc)
        time.sleep(1.5)
