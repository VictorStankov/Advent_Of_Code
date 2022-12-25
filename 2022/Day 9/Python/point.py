class Point:
    x = 0
    y = 0

    def __repr__(self):
        return f'X: {self.x}, Y: {self.y}'

    def move_x(self, spaces: int):
        self.x += spaces

    def move_y(self, spaces: int):
        self.y += spaces

    def __sub__(self, other):
        return self.x - other.x, self.y - other.y

    def vals(self):
        return self.x, self.y
