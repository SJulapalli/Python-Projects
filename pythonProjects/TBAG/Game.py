import Room
import Objects
import Player
import NPC
import Enemy
import Books

r1 = Room.NicksRoom()
r2 = Room.VedasRoom()
r3 = Room.SrijaysRoom()
r1.front_room = r2
r2.front_room = r3
r2.previous_room = r1
r3.previous_room = r2
p = Player.Player()
p.init(r1, "Jorge")
dead = False
while dead == False:
    print("What would you like to do?")
    print("1. Attack " + p.location.people[0].name)
    print("2. Speak with " + p.location.people[0].name)
    print("3. Inspect room")
    print("4. Pickup item")
    print("5. Show inventory")
    print("6. Change rooms")
    pIn = input()
    if pIn == "1":
        p.atk(p.location.people[0])
        p.location.people[0].atk(p.location.people[0], p)
    elif pIn == "2":
       p.location.people[0].talk(p.location.people[0])
    elif pIn == "3":
        print(p.location.description)
        print("The room contains:")
        for x in p.location.objects:
            print("A " + x.name)
        print("As well, " + p.location.people[0].name + " is in the room")
    elif pIn == "4":
        pIn = input("Which item would you like to collect? ")
        p.collect(p.location.objects[p, int(pIn)])
    elif pIn == "5":
        p.showInventory()
    elif pIn == "6":
        p.move(int(input("Which room would you like to enter? ")))

    dead = input("Are you dead? ")
    if dead == "yes":
        dead = p.die()
    else: dead = False

