import game_utils as util

class Apple:

    def __init__(self, location):
        # get from some rand func
        self._location = util.get_random_apple_data()

    def get_location(self):
        return self._location