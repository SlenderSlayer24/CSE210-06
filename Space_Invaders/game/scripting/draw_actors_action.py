from game.scripting.action import Action


class DrawActorsAction(Action):
    """
    An output action that draws all the actors.
    
    The responsibility of DrawActorsAction is to draw all the actors.

    Attributes:
        _video_service (VideoService): An instance of VideoService.
    """

    def __init__(self, video_service):
        """Constructs a new DrawActorsAction using the specified VideoService.
        
        Args:
            video_service (VideoService): An instance of VideoService.
        """
        self._video_service = video_service

    def execute(self, cast, script):
        """Executes the draw actors action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        ship = cast.get_first_actor("ship")
        segment = ship.get_segments()
        bullet = cast.get_first_actor('bullet')
        bullets = bullet.get_bullets()
        alienLine1 = cast.get_first_actor("alienLine1")
        aliensLine1 = alienLine1.get_aliens()
        messages = cast.get_actors("messages")

        self._video_service.clear_buffer()
        self._video_service.draw_actors(segment)
        self._video_service.draw_actors(aliensLine1)
        self._video_service.draw_actors(bullet)
        self._video_service.draw_actors(messages, True)
        self._video_service.flush_buffer()