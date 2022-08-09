class Item:
    name = ""
    equippable = True
    dmg = 0
    type = ""  # Types: Weapon (w), Healing (h)

    def __init__(self):
        pass

    # Method for initializing custom items
    def initCustom(self, name, equippable, dmg, type):
        self.__init__()
        self.name = name
        self.equippable = equippable
        self.dmg = dmg
        self.type = type

    def oldSword(self):
        self.__init__()
        self.name = "Old Sword"
        self.equippable = True
        self.dmg = 10
        self.type = "w"
