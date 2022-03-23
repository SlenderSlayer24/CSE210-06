from Space_Invaders_Galatic.Scripting.action import Action

class Draw_Actors(Action):
    #An output action that draws all the actors.
    def __init__(self, video_service):
        #Constructs a new DrawActorsAction using the specified VideoService.
        self._video_service = video_service

    def execute(self, cast, script):
        #Executes the draw actors action.
        ship = cast.get_first_actor("ship")
        self._video_service.clear_buffer()
        self._video_service.draw_actor(ship)
        self._video_service.flush_buffer()