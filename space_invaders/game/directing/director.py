class Director:
    #The Director of the game.
    def __init__(self, video_service):
        #Constructs a new Director using the specified video service.
        self._video_service = video_service

    def start_game(self, cast, script):
        #Starts the game using the given cast and script. Runs the main game loop.
        self._video_service.open_window()
        while self._video_service.is_window_open():
            self._execute_actions("input", cast, script)
            self._execute_actions("update", cast, script)
            self._execute_actions("output", cast, script)
        self._video_service.close_window()

    def _execute_actions(self, group, cast, script):
        #Calls execute for each action in the given group.
        actions = script.get_actions(group)    
        for action in actions:
            action.execute(cast, script)