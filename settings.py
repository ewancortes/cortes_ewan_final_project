# This File was Created By Ewan Cortes

# Import SysFont and init from pygame
from pygame.font import SysFont
from pygame import init
init()
###################################################

# Set up the Window Settings
XWIN, YWIN = 800,600 #                Sets up the resolution of the screen
HALF_XWIN,HALF_YWIN = XWIN/2,YWIN/2 # Sets up where the center of the screen is
DISPLAY = (XWIN,YWIN)
FLAGS = 0 #                           Sets up the screen to be fullscreen and resizeable 
FPS = 60 #                            Sets up the render frame rate

# Set up the Colors
BLACK = (0,0,0)
WHITE = (255,255,255)
GRAY = (100,100,100)
YELLOW = (255,211,67)
LIGHT_GREEN = (131,252,107)
ANDROID_GREEN = (164,198,57)
FOREST_GREEN = (87,189,68)

# Set up the Player settings
PLAYER_SIZE = (25,35)
PLAYER_COLOR = BLACK
PLAYER_MAX_SPEED = 30
PLAYER_JUMPFORCE = 5
PLAYER_BONUS_JUMPFORCE = 70
GRAVITY = .90

# Set up the Platform settings
PLATFORM_COLOR = FOREST_GREEN
PLATFORM_COLOR_LIGHT = WHITE
PLATFORM_COLOR_MOVING = ANDROID_GREEN
PLATFORM_SIZE = (100,10)
PLATFORM_DISTANCE_GAP = (50,210)
MAX_PLATFORM_NUMBER = 12
BONUS_SPAWN_CHANCE = 20
BREAKABLE_PLATFORM_CHANCE = 10
MOVING_PLATFORM_CHANCE = 10

# Set up the Fonts
LARGE_FONT = SysFont("",128)
SMALL_FONT = SysFont("arial",24)

