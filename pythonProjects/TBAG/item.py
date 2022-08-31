import time


class Item:
    name = ""
    desc = ""
    equippable = True
    dmg = 0
    type = ""  # Types: Weapon (w), Healing (h)

    def __init__(self):
        pass

    # Method for initializing custom items
    def initCustom(self, name, desc, equippable, dmg, type):
        item = Item()
        item.name = name
        item.desc = desc
        item.equippable = equippable
        item.dmg = dmg
        item.type = type
        return item

    #  Handles interaction between the player and an object
    def interact(self):
        print("You walk up to the " + self.name)
        time.sleep(.75)
        print(self.desc)
        time.sleep(1.5)

    def fists(self):
        item = Item()
        item.name = "Fists"
        item.desc = "Your good ol' bruisers. They've never let you down."
        item.equippable = True
        item.dmg = 5
        item.type = "w"
        return item

    def oldSword(self):
        item = Item()
        item.name = "Old Sword"
        item.desc = "A rusty sword. It must've been down here for a long time."
        item.equippable = True
        item.dmg = 10
        item.type = "w"
        return item
