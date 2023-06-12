import game_utils as util

# for orientation
HORIZ = 0
VERT = 1

class Wall:
    def __init__(self):
        x, y , self.direction = util.get_random_wall_data()
        self.location = x, y

        if self.direction == "Left" or self.direction == "Right":
            self.orientation = HORIZ
            self.location_list = [(x-1, y), (x, y), (x+1, y)]
        elif self.direction == "Up" or self.direction == "Down":
            self.orientation = VERT
            self.location_list = [(x, y - 1), (x, y), (x, y + 1)]

    def move_wall(self) -> None:
        x, y = self.location_list[1]

        if self.direction == "Left":
            self.location_list = [(x - 2, y), (x - 1, y), (x, y)]
        elif self.direction == "Right":
            self.location_list = [(x, y), (x + 1, y), (x + 2, y)]
        elif self.direction == "Down":
            self.location_list = [(x, y - 2), (x, y - 1), (x, y)]
        elif self.direction == "Up":
            self.location_list = [(x, y), (x, y + 1), (x, y + 2)]

    # def wall_disappear(self) -> True:
    #     self.

    def get_location(self) -> tuple:
        return self.location

    def get_direction(self) -> str:
        return self.direction

the_wall = Wall()
print(the_wall.location_list)
