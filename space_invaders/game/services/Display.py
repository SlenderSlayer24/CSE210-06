import pyray
import constants

class VideoService:
    #displays the game state
    def __init__(self, debug = False):
        #displays in specified debug mode.
        self._debug = debug

    def close_window(self):
        pyray.close_window()

    def clear_buffer(self):
        #clears out the game and makes it drawable again.
        pyray.begin_drawing()
        pyray.clear_background(pyray.BLACK)
        if self._debug == True:
            self._draw_grid()
    
    def draw_actor(self, actor, centered=False):
        #draw the actors
        text = actor.get_text()
        x = actor.get_position().get_x()
        y = actor.get_position().get_y()
        font_size = actor.get_font_size()
        color = actor.get_color().to_tuple()

        if centered:
            width = pyray.measure_text(text, font_size)
            offset = int(width / 2)
            x -= offset
            
        pyray.draw_text(text, x, y, font_size, color)
        
    def draw_actors(self, actors, centered=False):
        #write out the text for the screen
        for actor in actors:
            self.draw_actor(actor, centered)
    
    def flush_buffer(self):
        #buffers the drawing and ends the drawing phase.
        pyray.end_drawing()

    def is_window_open(self):
        #checks if the window is close by the user.
        return not pyray.window_should_close()

    def open_window(self):
        #creates new window for the game
        pyray.init_window(constants.MAX_X, constants.MAX_Y, constants.CAPTION)
        pyray.set_target_fps(constants.FRAME_RATE)

    def _draw_grid(self):
        #Draws a grid on the screen.
        for y in range(0, constants.MAX_Y, constants.CELL_SIZE):
            pyray.draw_line(0, y, constants.MAX_X, y, pyray.GRAY)
            
        for x in range(0, constants.MAX_X, constants.CELL_SIZE):
            pyray.draw_line(x, 0, x, constants.MAX_Y, pyray.GRAY)
    
    def _get_x_offset(self, text, font_size):
        width = pyray.measure_text(text, font_size)
        return int(width / 2)