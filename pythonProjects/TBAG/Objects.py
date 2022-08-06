import Books


class SmallObject:
    name = ""
    dmg = 0
    health = 0
    value = 0
    searchable = False

    def cosbyPoster(self):
        self.name = "Cosby Poster"
        self.dmg = 1
        self.health = 1
        self.value = 100

    def cosbyDaikamakura(self):
        self.name = "Cosby Daikamakura"
        self.dmg = 99999999
        self.health = 99999999
        self.value = 99999999

    def srijaysDidlo(self):
        self.name = "Black Dildo with diamond knuckles and spikes"
        self.dmg = 87
        self.health = 10
        self.value = 500

    def stp(self):
        self.name = "Sauron Titty Poster"
        self.dmg = 1
        self.health = 1
        self.value = 100

class MediumObject:
    name = ""
    dmg = 0
    health = 0
    value = 0
    searchable = False

class MassiveObject:
    name = ""
    health = 0;
    searchable = True
    loot = []

    def bigMassiveBed(self):
        self.name = "Big Massive Bed"
        self.health = 500

    def theWHOLEGamingSetup(self):
        self.name = "The WHOLE Gaming Setup"
        self.health = 1000

    def shelf(self):
        self.name = "A Whole Shelf"
        self.health = 700

    def mangaShelf(self):
        self.name = "A Whole Shelf of Manga"
        self.health = 1000

    def excessSchmegma(self):
        self.name = "Excess schmegma"
        self.health = 999999999

