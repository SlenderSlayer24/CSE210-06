from turtle import right
import constants
from Space_Invaders_Galatic.Scripting.action import Action
from Space_Invaders_Galatic.Services.point import Point

LEFT = Point(-constants.CELL_SIZE, 0)
RIGHT= Point(constants.CELL_SIZE, 0)
NONE = Point(0,0)

class ControlActorsAction(Action):
    """
    An input action that controls the ship.
    
    The responsibility of ControlActorsAction is to get the direction and move the ship.
    """

    def __init__(self, keyboard_service):
        #Constructs a new ControlActorsAction using the specified KeyboardService.
        self._keyboard_service = keyboard_service

    def execute(self, cast, script):
        #Executes the control actors action.
        if self._keyboard_service.is_key_down('a'):
            self._direction = LEFT
        elif self._keyboard_service.is_key_down('d'):
            self._direction = RIGHT
        else:
            self._direction = None
        
        ship = cast.get_x_actor("ship", 1)
        ship.turn_ship(self._direction)