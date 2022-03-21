class Script:
    '''
    The responsibility of Script is to keep track of a collection of actions. It has methods for 
    adding, removing and getting them by a group name.
    '''
    def __init__(self):
        #Constructs a new Action.
        self._actions = {}

        def add_action(self, group, action):
        #Adds an action to the given group.
        if not group in self._actions.keys():
            self._actions[group] = []
        if not action in self._actions[group]:
            self._actions[group].append(action)

    def get_actions(self, group):
        #Gets the actions in the given group.
        results = []
        if group in self._actions.keys():
            results = self._actions[group].copy()
        return results
    
    def remove_action(self, group, action):
        #Removes an action from the given group.
        if group in self._actions:
            self._actions[group].remove(action)