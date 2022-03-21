from Space_Invaders_Galatic.Scripting.action import Action

class MoveActorsAction(Action): 
    def __init__(self):
        pass
    def execute(self, cast, script):
        actors = cast.get_all_actors()
        for actor in actors:
            actor.move_next()