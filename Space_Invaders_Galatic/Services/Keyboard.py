import pyray
from point import Point


class KeyboardService:
    '''
    The responsibility of a KeyboardService is to 
    indicate whether or not a key is up or down.
    '''

    def __init__(self):
        #the contorls on the keyboard
        self._keys = {}
        self._keys['w'] = pyray.KEY_W
        self._keys['a'] = pyray.KEY_A
        self._keys['s'] = pyray.KEY_S
        self._keys['d'] = pyray.KEY_D

    def is_key_up(self, key):
        #Checks if the given key is currently up.
        pyray_key = self._keys[key.lower()]
        return pyray.is_key_up(pyray_key)

    def is_key_down(self, key):
        #Checks if the given key is currently down.
        pyray_key = self._keys[key.lower()]
        return pyray.is_key_down(pyray_key)