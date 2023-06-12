import game_display
from game_display import GameDisplay
import game_utils
import class_snake
import snake_game
from class_wall import Wall




class Board:
    def __init__(self, width:int=game_display.WIDTH, height:int=game_display.HEIGHT):
        self.snake = class_snake.Snake((width//2, height//2))
        self.walls = []
        self.apples = []
        self.counter = 0
        pass

    def update_board(self, walls_max):
        cur_rounds = self.counter
        if cur_rounds % 2 == 0 and cur_rounds != 0:
            for wall in self.walls:
                wall.move_wall()
        if len(self.walls) < walls_max and cur_rounds % 10 == 0:
            self.get_new_wall()
        self.snake.snake_move()

    def get_new_wall(self):
        if self.free_space_wall:
            self.walls.append(Wall())


    def cell_contains(self):
        ''' getting cell corddinations
        returning value of cell ("A" (apple), "S" (snake), "W" (wall)'''
        pass

    def is_free_cell(self):
        ''' getting:cell name
         returning: True if free, False else'''

    def free_space_wall(self):
        return True


