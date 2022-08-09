class NPC:
    dialogueTree = None
    items = list
    health = 0
    heldItem = None

    def damage(self, dmg):
        self.health -= dmg
        print(self.name + "takes " + dmg + "damage!")

    def interact(self):
        print("Hello!")