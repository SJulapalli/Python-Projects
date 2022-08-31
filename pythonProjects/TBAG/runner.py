import room
import player
import time

# Main Menu, Navigation, Dialogue, Combat, Inventory
States = {"MM", "N", "D", "C", "I"}
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
    two.study(None, one, None, None)
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


def combatHandler():
    global state, end, user
    enemies = user
    while user.health > 0 or len(user.currentRoom.enemies) > 0:
        print("")


def movementHandler():
    global state, end, user

    state = user.move(int(input("""---------------------------------------------------------------------------------------------------
            Directions
    (1) Left
    (2) Up
    (3) Right
    (4) Down
    Which direction would you like to move? """)))


def interactionHandler():
    global state, end, user
    print("---------------------------------------------------------------------------------------------------")
    print("The room contains the following\nObjects: ")
    if len(user.currentRoom.objects) == 0:      # Objects in the room
        print("   None")
        time.sleep(.25)
    else:
        for obj in user.currentRoom.objects:
            print("   - " + obj.name)
            time.sleep(.25)

    print("Items: ")
    if len(user.currentRoom.items) == 0:        # Items in the room
        print("   None")
        time.sleep(.25)
    else:
        for item in user.currentRoom.items:
            print("   - " + item.name)
            time.sleep(.25)

    print("People: ")
    if len(user.currentRoom.friendlies) == 0:   # Friendly NPCs in the room
        print("   None")
        time.sleep(.25)
    else:
        for NPC in user.currentRoom.friendlies:
            print("   - " + NPC.name)
            time.sleep(.25)

    exit = False
    while not exit:
        pIn = input("What would you like to interact with? Type 'exit' if you'd like to go back ")

        if pIn.upper() == "EXIT":
            exit = True
        else:
            temp = None
            for object in user.currentRoom.objects:
                if object.name == pIn:
                    temp = object

            if temp is None:
                for item in user.currentRoom.items:
                    if item.name == pIn:
                        temp = item

            if temp is None:
                for NPC in user.currentRoom.friendlies:
                    if NPC.name == pIn:
                        temp = NPC

            if temp is None:
                print("There is nothing in the room with that name")
                time.sleep(1)
            else:
                exit = True
                user.interact(temp)


def inventoryHandler():
    global state, end, user
    user.getInv()
    pIn = input("Enter the name of the item you want to interact with or 'exit' to go back: ")
    if pIn == "exit":
        state = "N"


def navigationHandler():
    global state, end, user
    print("""---------------------------------------------------------------------------------------------------
        Actions
(1) Move
(2) Interact
(3) Open Inventory
(4) Exit""")
    pIn = int(input("What would you like to do? "))
    if pIn == 1:  # Move
        movementHandler()
    elif pIn == 2:  # Interact
        interactionHandler()
    elif pIn == 3:  # Inventory
        state = "I"
    else:  # Exit
        end = exitRunner()


def main():
    global end, state, firstRoom, user

    firstRoom = initmap()
    user = initplayer("Suhas", firstRoom, [], 100, 0)

    while not end:
        if state == "N":            # Navigation
            navigationHandler()
        elif state == "D":  # Dialogue
            print("Dialogue")
        elif state == "C":  # Combat
            print("Combat")
        elif state == "I":  # Inventory
            inventoryHandler()
        else:               # End
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
