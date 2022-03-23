import constants
from Space_Invaders_Galatic.Services.color import Color
from Space_Invaders_Galatic.Services.point import Point

class Actor:
    #The visual parts of the game.
    def __init__(self):
        #Constructs a new Actor.
        self._text = ""
        self._font_size = 15
        self._color = Color(255, 255, 255, 255)
        self._position = Point(0, 0)
        self._velocity = Point(0, 0)

    def get_color(self):
        #Gets the actor's color as a tuple of three ints (r, g, b).
        return self._color

    def get_font_size(self):
        #Gets the actor's font size.
        return self._font_size

    def get_position(self):
        #Gets the actor's position in 2d space.
        return self._position
    
    def get_text(self):
        #Gets the actor's textual representation.
        return self._text

    def get_velocity(self):
        #Gets the actor's speed and direction.
        return self._velocity
    
    def move_next(self):
        """Moves the actor to its next position according to its velocity. Will wrap the position 
        from one side of the screen to the other when it reaches the given maximum x and y values.
        """
        x = (self._position.get_x() + self._velocity.get_x()) % constants.MAX_X
        y = (self._position.get_y() + self._velocity.get_y()) % constants.MAX_Y
        self._position = Point(x, y)

    def set_color(self, color):
        #Updates the color to the given one.
        self._color = color

    def set_position(self, position):
        #Updates the position to the given one.
        self._position = position
    
    def set_font_size(self, font_size):
        #Updates the font size to the given one.
        self._font_size = font_size
    
    def set_text(self, text):
        #Updates the text to the given value.
        self._text = text

    def set_velocity(self, velocity):
        #Updates the velocity to the given one.
        self._velocity = velocity