#*trumpet noises* The main file
import constants

from Space_Invaders_Galatic.Casting.cast import Casting
from Space_Invaders_Galatic.Casting.Ship import Ship
from Space_Invaders_Galatic.Scripting.script import Script
from Space_Invaders_Galatic.Scripting.control_actors_action import ControlActorsAction
from Space_Invaders_Galatic.Scripting.move_action import MoveActorsAction
from Space_Invaders_Galatic.Scripting.draw_actors import Draw_Actors
from Space_Invaders_Galatic.Directing.director import Director
from Space_Invaders_Galatic.Services.Keyboard import KeyboardService
from Space_Invaders_Galatic.Services.Display import VideoService
from Space_Invaders_Galatic.Services.color import Color
from Space_Invaders_Galatic.Services.point import Point


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