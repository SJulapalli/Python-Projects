import time


class Object:
    name = ""
    desc = ""
    liftable = True
    dmg = 0
    health = 0

    def __init__(self):
        pass

    def initCustom(self, name, desc, liftable, dmg, health):
        self.name = name
        self.desc = desc
        self.liftable = liftable
        self.dmg = dmg
        self.health = health

    def initDesk(self):
        self.name = "Mahogany Desk"
        self.desc = "It is a small desk, suitable for one person. Upon it lies a few open books and a small candle."
        self.liftable = True
        self.dmg = 10
        self.health = 40

    def dmg(self, dmg):
        self.health -= dmg
        print(self.name + "takes " + dmg + "damage!")

    def interact(self):
        print("You walk up to the " + self.name)
        time.sleep(1)
        print(self.desc)
        time.sleep(3)
