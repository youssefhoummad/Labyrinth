class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __repr__(self):
        return "<Position({},{})>".format(self.x, self.y)

    def __add__(self, other):
        return Position(self.x+other.x, self.y+other.y)


class Item:
    def __init__(self, pos, img, tag):
        self.position = pos
        self.image = img
        self.tag = tag

    def __repr__(self):
        return "<Item: {} at {}>".format(self.tag, self.position)


class Character:
    def __init__(self, pos, img, tag):
        self.position = pos
        self.image = img
        self.tag = tag

    def move(self, dx, dy):
        self.position += Position(dx, dy)

    def __repr__(self):
        return "<Character: {} at {}>".format(self.tag, self.position)
