import Room
import Objects

class Player:
    name = ""
    inventory = []
    location = ""
    wealth = 100
    held_item = ""
    health = 100
    FistAtkMult = 1;
    RangeAtkMult = 1;

    def die(self):
        print("You died")
        return True

    def init(self, location, name):
        self.name = name
        self.location = location

    def changeWealth(self, amount):
        wealth = self.wealth + amount
        return wealth

    def move(self, direction):
        if direction == 1:
            self.location = self.location.left_room
        elif direction == 2:
            self.location = self.location.front_room
        elif direction == 3:
            self.location = self.location.right_room
        elif direction == 4:
            self.location = self.location.previous_room

    def showInventory(self):
        count = 1
        print("\nItems:")
        for x in self.inventory:
            print(str(count) + ". " + x.name)
            count = count + 1

    def collect(self, item):
        if isinstance(item, Objects.SmallObject):
            self.location.objects.remove(item)
            self.inventory.append(item)
        elif isinstance(item, Objects.MediumObject):
            self.location.objects.remove(item)
            self.inventory.append(item)
            if self.held_item != "":
                held_item = item
                print("You pick up the " + item.name)
            else:
                print("You pick up the " + item.name + ", putting the "
                      + self.held_item.name + " away")
                held_item = item
        else:
            print("You cannot pickup this object")

    def drop(self, item):
        print("You drop " + item.name)
        self.location.objects.append(item)
        self.inventory.remove(self.inventory.index(item))
        if self.held_item == item:
            self.held_item == ""

    def atk(self, target):
        if self.held_item == "":
            target.health = target.health - 5
            print(self.name + " punches " + target.name + " for 5 dmg!")
        else:
            target.health = target.health - self.held_item.dmg
            print(
                self.name + " deals " + str(self.held_item.dmg) + " dmg to " + target.name + " with his " + self.held_item.name + "!")
        if target.health < 1:
            print("You kill " + target.name + "!")

