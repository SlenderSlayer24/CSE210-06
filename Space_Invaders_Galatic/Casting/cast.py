class Casting:
    '''
    The responsibility of a cast is to keep track of a collection of actors. It has methods for 
    adding, removing and getting them by a group name.
    '''
    def __init__(self):
        # Constructs a new Actor.
        self._actors = {}
        
    def add_actor(self, group, actor):
        # Adds an actor to the given group.
        if not group in self._actors.keys():
            self._actors[group] = []
            
        if not actor in self._actors[group]:
            self._actors[group].append(actor)

    def get_actors(self, group):
        # Gets the actors in the given group.
        results = []
        if group in self._actors.keys():
            results = self._actors[group].copy()
        return results
    
    def get_all_actors(self):
        # Gets all of the actors in the cast.
        results = []
        for group in self._actors:
            results.extend(self._actors[group])
        return results

    def get_x_actor(self, group, x):
        # Gets the actor in the given position and group.
        result = None
        if group in self._actors.keys():
            # because lists start at zero, the position you want should be 1 less then what you want,
            # example: the first is one and the second is two.
            result = self._actors[group][x-1]
        return result

    def remove_actor(self, group, actor):
        # Removes an actor from the given group.
        if group in self._actors:
            self._actors[group].remove(actor)