class Color:
    #color starts and ends here. Creating the color value that we use in other files
    def __init__(self, red, green, blue, alpha = 255):
        self._red = red
        self._green = green
        self._blue = blue 
        self._alpha = alpha

    #now it's a tuple
    def to_tuple(self):
        return (self._red, self._green, self._blue, self._alpha)