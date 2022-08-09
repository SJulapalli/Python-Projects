import room
import item
import time
import object


class Player:
    name = ""
    currentRoom = room.Room()
    inventory = []
    health = 0
    heldItem = item.Item()
    heldItem.oldSword()

    def move(self, direction):
        if direction == 1:  # Move left
            if str(self.currentRoom.left) == "Wall":
                print("You cannot move in that direction")
            else:
                self.currentRoom = self.currentRoom.left
                print("You enter " + str(self.currentRoom.desc))
        elif direction == 2:  # Move Up
            if self.currentRoom.up == "Wall":
                print("You cannot move in that direction")
            else:
                self.currentRoom = self.currentRoom.up
                print("You enter " + str(self.currentRoom.desc))
        elif direction == 3:  # Move Right
            if self.currentRoom.right == "Wall":
                print("You cannot move in that direction")
            else:
                self.currentRoom = self.currentRoom.right
                print("You enter " + str(self.currentRoom.desc))
        else:  # Move Down
            if self.currentRoom.down == "Wall":
                print("You cannot move in that direction")
            else:
                self.currentRoom = self.currentRoom.down
                print("You enter " + str(self.currentRoom.desc))
        time.sleep(1.5)

    def __init__(self):
        pass

    def damage(self, dmg):
        self.health -= dmg
        print(self.name + "takes " + dmg + "damage!")

    def initPlayer(self, name, currentRoom, inventory, health, helditemindex):
        self.name = name
        self.currentRoom = currentRoom
        self.inventory = inventory
        self.health = health
        if -1 < helditemindex < len(self.inventory):
            self.heldItem = inventory[helditemindex]

    def attack(self, target):
        target.damage(self.heldItem.dmg)

    # Returns a string containing a list of the player's items and heldItem
    def getInv(self):
        print("---------------------------------------------------------------------------------------------------")
        out = "        Inventory\n["
        for invItem in self.inventory:
            out += invItem.name + ", "

        return out + "]\nHeld Item: " + self.heldItem.name

    # Interacts with a given target. If the target is an object/item, it will have an additional custom interaction
    def interact(self, target):
        target.interact()
        if isinstance(target, object.Object):
            self.interactObject(target)
        elif isinstance(target, item.Item):
            self.interactItem(target)


    def interactObject(self, target):
        if target.liftable:
            pIn = input("It looks light enough for you to lift, would you like to pick it up? (Y/N): ")
            if pIn.upper() == "Y" or pIn.upper() == "YES":
                if isinstance(self.heldItem, object.Object):
                    print("You set down the " + self.heldItem.name + " and pick up the " + target.name)
                    self.currentRoom.objects.append(object.Object(self.heldItem))
                    self.heldItem = target
                    self.currentRoom.objects.remove(object.Object(target))
                else:
                    print("You put away the " + self.heldItem.name + " and pick up the " + target.name)
                    self.inventory.append(self.heldItem)
                self.heldItem = target
                self.currentRoom.objects.remove(target)
        else:
            print("It looks too heavy for you to lift")

    def interactItem(self, target):
        print("You pick up the " + target.name)
        if target.equippable:
            pIn = input("Would you like to equip it (Y/N)? ")
            if pIn.upper() == "Y" or pIn.upper() == "YES":
                self.inventory.append(self.heldItem)
                self.heldItem = target
            else:
                self.inventory.append(target)
        self.currentRoom.items.remove(target)

