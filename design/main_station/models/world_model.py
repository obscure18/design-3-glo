"""
    This class is a model for visualizing the game
"""


class WorldModel:
    def __init__(self):
        self._obstacles_coordinates = [(1153, 877), (991, 396)]
        self._path_coordinates = [(96, 226), (400, 556), (490, 915), (1017, 616), (1453, 303), (1455, 834)]   # dummy test
        self._robot_coordinates = [(405, 570)]
        self._drawing_zone_coordinates = [(216, 363), (216, 771), (621, 771), (621, 363)]   # dummy test
        self._game_image = ""

        # these will be the registered functions for view updating
        self._update_functions = []

    @property
    def obstacles_coordinates(self):
        return self._obstacles_coordinates

    @obstacles_coordinates.setter
    def obstacles_coordinates(self, coordinates):
        self._obstacles_coordinates = coordinates

    @property
    def path_coordinates(self):
        return self._path_coordinates

    @path_coordinates.setter
    def path_coordinates(self, coordinates):
        self._path_coordinates = coordinates

    @property
    def robot_coordinates(self):
        return self._robot_coordinates

    @robot_coordinates.setter
    def robot_coordinates(self, coordinates):
        self._robot_coordinates = coordinates

    @property
    def drawing_zone_coordinates(self):
        return self._drawing_zone_coordinates

    @drawing_zone_coordinates.setter
    def drawing_zone_coordinates(self, coordinates):
        self._drawing_zone_coordinates = coordinates

    @property
    def game_image(self):
        return self._game_image

    @game_image.setter
    def game_image(self, image_path):
        self._game_image = image_path

    # subscribe a view method for updating
    def subscribe_update_function(self, function):
        if function not in self._update_functions:
            self._update_functions.append(function)

    # unsubscribe a view method for updating
    def unsubscribe_update_function(self, function):
        if function in self._update_functions:
            self._update_functions.remove(function)

    # update registered view methods
    def announce_update(self):
        for function in self._update_functions:
            function()