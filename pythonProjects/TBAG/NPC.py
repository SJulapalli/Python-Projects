import Room


class NPC:
    name = ""
    inventory = []
    location = ""
    wealth = 0
    held_item = ""
    health = 100

    def atk(self, target):
        if self.held_item == "":
            target.health = target.health - 5
            print(self.name + " punches " + target.name + " for 5 dmg!")
        else:
            target.health = target.health - self.held_item.dmg
            print(self.name + " deals " + self.held_item.dmg + " dmg to " + target.name + " with his " + self.held_item.name + "!")
        if target.health < 1:
            print(self.name + " kills " + target.name + "!")


class Veda(NPC):

    name = "Veda"

    def talk(self):
        print("Veda: Piss off I'm reading manga")


class Nick(NPC):

    name = "Nick"

    def talk(self):
        print("Nick: Cosby is love, Cosby is life. How can I help you?")


class Srijay(NPC):

    name = "Srijay"

    def talk(self):
        print("Srijay: Fuck off")