import room
import player
import time

# Main Menu, Navigation, Dialogue, Combat
States = {"MM", "N", "D", "C"}
state = "MM"
end = False
firstRoom = None
user = None


def initmap():
    one = room.Room()
    two = room.Room()
    three = room.Room()
    four = room.Room()
    five = room.Room()

    one.initEmpty(None, None, None, None)
    two.initStudy(None, one, None, None)
    three.initCustom("Room Three", None, None, None, None, None, None, one, None)
    four.initCustom("Room Four", None, None, None, None, None, None, None, one)
    five.initCustom("Room Five", None, None, None, None, None, one, None, None)

    one.setRight(five)
    one.setUp(four)
    one.setLeft(three)
    one.setDown(two)

    return one


def initplayer(name, currentRoom, inventory, health, index):
    p = player.Player()
    p.initPlayer(name, currentRoom, inventory, health, index)
    return p


def mainMenu():
    print("Welcome to TBAG!")

    pIn = input("Start game? (Y/N) ").upper()

    if pIn == "Y" or pIn == "YES":
        return False
    elif pIn == "N" or pIn == "NO":
        return True
    else:
        print("Please enter a valid input\n")


def exitRunner():
    pIn = input("Are you sure you want to exit? (Y/N) ").upper()
    if pIn == "Y" or pIn == "YES":
        return True
    else:
        return False


def main():
    global end, state, firstRoom, user

    firstRoom = initmap()
    user = initplayer("Suhas", firstRoom, [], 100, 0)

    while not end:
        if state == "N":
            print("""---------------------------------------------------------------------------------------------------
        Actions
(1) Move
(2) Interact
(3) Open Inventory
(4) Exit""")
            pIn = int(input("What would you like to do? "))
            if pIn == 1:
                user.move(int(input("""
(1) Left
(2) Up
(3) Right
(4) Down
Which direction would you like to move? """)))
            elif pIn == 2:
                print("The room contains: ")
                for object in user.currentRoom.objects:
                    print(object.name + ", ")
                    time.sleep(.5)

                pIn = input("What would you like to interact with? ")

                temp = None
                for object in user.currentRoom.objects:
                    if object.name == pIn:
                        temp = object

                if temp is None:
                    print("There is no object with that name in the room.")
                else:
                    user.interact(temp)

            elif pIn == 3:
                print(user.getInv())
            else:
                end = exitRunner()
        elif state == "D":
            print("Dialogue")
        elif state == "C":
            print("Combat")
        else:
            end = mainMenu()

            if not end:
                state = "N"

                print("You step through the door into the dungeon...")
                time.sleep(1.15)
                print("As you look back, the wall closes behind you...")
                time.sleep(1.15)
                print("You see before you " + str(user.currentRoom.desc) + ".")
                time.sleep(1)


main()
