import constants
import random
from Space_Invaders_Galatic.Casting.actor import Actor
from Space_Invaders_Galatic.Services.point import Point

class Ship(Actor):
    # The Space ship and the hero.
    # Creates the Ship and Shoots bullets.
    def __init__(self):
        super().__init__()
        self._ship = []
        self._construct_ship()

    def _construct_ship(self):
        x = 100
        y = 100

        
        for i in range(constants.SHIP_LENGTH):
            position = Point(x - i * constants.CELL_SIZE, y)
            velocity = Point(1 * constants.CELL_SIZE, 0)
            text = "0" if i == 0 else "#"
            color = constants.WHITE if i == 0 else constants.PLAYER

        ship = Actor()
        ship.set_position(position)
        ship.set_velocity(velocity)
        ship.set_text(text)
        ship.set_color(color)
        self._ship.append(ship)

        # update velocities
        for i in range(len(self._ship) - 1, 0, -1):
            trailing = self._ship[i]
            previous = self._ship[i - 1]
            velocity = previous.get_velocity()
            trailing.set_velocity(velocity)

    def get_ship(self):
        return self._ship

    def turn_ship(self, velocity):
        self._ship[0].set_velocity(velocity)

    def move_next(self):
        # move the ship
        for ship in self._ship:
            ship.move_next()