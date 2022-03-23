class Point:
    '''
    The responsibility of Point is to hold and provide information about itself. Point has a few 
    convenience methods for adding, scaling, and comparing them.
    '''
    def __init__(self, x, y):
        #creates a new point
        self._x = x
        self._y = y
    
    def add(self, other):
        #add two points together
        x = self._x + other.get_x()
        y = self._y + other.get_y()
        return Point(x, y)

    def equals(self, other):
        #checks if points are the same
        return self._x == other.get_x() and self._y == other.get_y()

    def get_x(self):
        #get the x of a point
        return self._x
    
    def get_y(self):
        #get the y of a point
        return self._y

    def reverse(self):
        #reverse a point
        new_x = self._x * -1
        new_y = self._y * -1
        return Point(new_x, new_y)

    def scale(self, factor):
        #scale a point
        return Point(self._x * factor, self._y * factor)