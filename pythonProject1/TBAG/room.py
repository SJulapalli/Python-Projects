import object

class Room:
    up = "Wall"
    left = "Wall"
    right = "Wall"
    down = "Wall"
    desc = ""
    objects = []
    items = []
    enemies = []
    friendlies = []

    def __init__(self):
        pass

    def initEmpty(self, u, l, r, d):
        self.desc = "an empty room"
        if u is not None:
            self.up = u
        if l is not None:
            self.left = l
        if r is not None:
            self.right = r
        if d is not None:
            self.down = d

    def initCustom(self, description, itemList, objectList, enemyList, friendlyList, u, l, r, d):
        self.initEmpty(u, l, r, d)
        self.desc = description
        self.items = itemList
        self. objects = objectList
        self. enemies = enemyList
        self.friendlies = friendlyList

    def initStudy(self, u, l, r, d):
        self.initEmpty(u, l, r, d)
        self.desc = "a small study. There are bookshelves along the walls, and near the back lies a desk.";

        desk = object.Object()
        desk.initDesk()

        self.objects = [desk]


    def getDesc(self):
        return self.desc

    def getItems(self):
        return self.items

    def getObjects(self):
        return self.objects

    def getEnemies(self):
        return self.enemies

    def getFriendlies(self):
        return self.friendlies

    def removeItem(self, item):
        if item in self.items:
            return self.items.remove(item)

    def removeItem(self, index):
        if -1 < index < len(self.items):
            return self.items.pop(index)

    def removeEnemy(self, enemy):
        if enemy in self.enemies:
            return self.items.remove(enemy)

    def removeEnemy(self, index):
        if -1 < index < len(self.enemies):
            return self.items.pop(index)

    def setUp(self, u):
        self.up = u

    def setLeft(self, l):
        self. left = l

    def setRight(self, r):
        self.right = r

    def setDown(self, d):
        self.down = d
