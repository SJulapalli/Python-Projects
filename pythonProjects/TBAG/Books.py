import Objects
import Player


class Book:
    title = ""
    health = 10
    dmg = 1

class DB(Book):
    title = "Dragon Ball"

    def read(self, player):
        player.FistAtkMult = 10
        player.RangeAtkMult = 10