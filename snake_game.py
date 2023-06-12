from typing import Optional
import class_board
import game_utils
from game_display import GameDisplay

class SnakeGame:

    def __init__(self) -> None:
        self.__x = 5
        self.__y = 5
        self.__key_clicked = None
        self.board = class_board.Board()


    def read_key(self, key_clicked: Optional[str])-> None:
        self.__key_clicked = key_clicked

    def update_objects(self)-> None:
        self.board.snake.snake_move()
        if (self.__key_clicked == 'Left') and (self.__x > 0):
            self.__x -= 1
        elif (self.__key_clicked == 'Right') and (self.__x < 40):
            self.__x += 1
        elif (self.__key_clicked == 'Up') and (self.__y > 0):
            self.__y += 1
        elif (self.__key_clicked == 'Down') and (self.__y < game_utils.HEIGHT):
            self.__y -= 1
        elif (self.__key_clicked == None):
            self.__y += 1


    def draw_board(self, gd: GameDisplay) -> None:
        for i in range(len(self.board.snake.list_location)):
            x = self.board.snake.list_location[i][0]
            y = self.board.snake.list_location[i][1]
            gd.draw_cell(x, y, "black")
        walls = self.board.walls
        for wall in walls:
            for i in range(len(wall.location_list)):
                gd.draw_cell(wall.location_list[i][0], wall.location_list[i][1], "blue")



    def end_round(self) -> None:
        pass

    def is_over(self) -> bool:
        return False