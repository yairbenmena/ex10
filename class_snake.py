class Snake:

    def __init__(self, cordds:tuple):
        self.__x = cordds[0]
        self.__y = cordds[1]
        self.direction = 'Up'
        self.list_location = [(self.__x, self.__y), (self.__x, self.__y-1), (self.__x, self.__y-2)]

    def __str__(self):
        return str(self.list_location)

    ''' this method will create the movement of the snake. it will get the direction of the snake, and will put 
    the first tuple of the snake in the location.'''

    def snake_move(self):
        head_x = self.list_location[0][0]
        head_y = self.list_location[0][1]
        if self.direction == 'Up':
            self.list_location.insert(0, (head_x, head_y+1))
        self.list_location.pop(-1)

    def snake_grow(self):
        pass
    def snake_cut(self):
        pass
        ''' one of the qualities of the snake is his direction. this method changing it '''
    def change_direction(self):
        pass

the_snake = Snake((10,15))
print(the_snake)
print(the_snake.list_location)