from game.scripting.action import Action

class MoveActorsAction(Action):
    #moving all actors at the same time.
    def __init__(self):
        pass

    def execute(self, cast, script):
        actors = cast.get_all_actors()
        for actor in actors:
            actor.move_next()