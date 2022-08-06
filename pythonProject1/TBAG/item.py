class Item:
    name = ""
    equippable = True
    dmg = 0

    def __init__(self):
        pass

    def init(self, name, equippable, dmg):
        self.__init__()
        self.name = name
        self.equippable = equippable
        self.dmg = dmg
