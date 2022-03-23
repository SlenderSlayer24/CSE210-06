from game.services.color import Color

#The screen, cell size, font
COLUMNS = 40
ROWS = 20
CELL_SIZE = 15
MAX_X = 900
MAX_Y = 600
FRAME_RATE = 15
FONT_SIZE = 15
#colors red, gree, blue, alpha/transparency
CAPTION = "SPACE INVADERS GALATIC!"
WHITE = Color(255,255,255,255)
ENEMY = Color(255,0,0,255)
PLAYER = Color(0,255,0,255)
SHIP_LENGTH = 1
'''
shields should be at least somewhat transparent so the player knows
they can shoot through them and visiably see their own bullets passing 
through it.
'''
SHIELD = Color(0,0,255,155)