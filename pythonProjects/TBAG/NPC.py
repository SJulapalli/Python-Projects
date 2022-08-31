class NPC:
    dialogueTree = None
    items = list
    health = 0
    heldItem = None

    def damage(self, dmg):
        self.health -= dmg
        print(self.name + "takes " + dmg + "damage!")


class Enemy(NPC):
    dmg = 0

    def atk(self, target):
        target.damage(self.dmg)

class Friendly(NPC):
    def interact(self):
        return str("Hello")
