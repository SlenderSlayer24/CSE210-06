#*trumpet noises* The main file
import constants

from game.casting.cast import Casting
from game.casting.ship import Ship
from game.scripting.script import Script
from game.scripting.control_actors_action import ControlActorsAction
from game.scripting.move_action import MoveActorsAction
from game.scripting.draw_actors import Draw_Actors
from game.directing.director import Director
from game.services.Keyboard import KeyboardService
from game.services.Display import VideoService
from game.services.color import Color
from game.services.point import Point


def main():
    
    # create the cast
    Cast = Casting()
    Cast.add_actor("ship", Ship())
   
    # start the game
    keyboard_service = KeyboardService()
    video_service = VideoService()

    script = Script()
    script.add_action("input", ControlActorsAction(keyboard_service))
    script.add_action("update", MoveActorsAction())
    script.add_action("output", Draw_Actors(video_service))
    
    director = Director(video_service)
    director.start_game(Cast, script)


if __name__ == "__main__":
    main()