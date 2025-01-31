'''
This code was developed by Damião Gomes

git hub profile: github.com/dam1aoGomes/
'''
import pgzrun

# Pygame zero Config
WIDTH = 900
HEIGHT = 540
TITLE = 'Help the Green Alien'

# Game Config
GRAVITY = 1
INITIAL_X_POS_PLAYER = 80
INITIAL_Y_POS_PLAYER = 10
DEBUG_MODE = False

MUSIC_VOLUME = 0.35

in_menu = True
sound_enable = True

'''
This is a collision map, where there is a 1 in some vector space,
it will be rendered in x,y on the map as if it were a Rect,
this collision map has no impact on game optimization as a smaller vector is created just with the selected blocks.
'''
down_collision_mask = [
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],#1
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0],
    
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0],
    
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],#15
    
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,0,0,0,1,1,1,0,0,1,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],#30
]

right_collision_mask = [
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],#1
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0],
    
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],#15
    
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],#30
]

left_collision_mask = [
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],#1
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0],
    
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],#15
    
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],#30
]

selected_rect_collider_down = []
selected_rect_collider_right = []
selected_rect_collider_left = []

# Game Actor Class
class Player:
    def __init__(self,x_pos,y_pos):
        # Actor Class Var
        self.actor = Actor('player_0001_right')
        self.actor.x = x_pos
        self.actor.y = y_pos
        # Player Class Var
        self.h_direction = 1 # 1: right -1: left
        self.on_move = False 
        self.velocity_y = 0
        self.velocity_x = 3
        self.is_colliding_down = False
        # vertical speed (jump)
        self.v_speed = 11
        # animation time
        self.animation_time = 0.1
        # key system
        self.have_key = False
        self.win = False
        
    def move_right(self):
        self.h_direction = 1
        self.on_move = True
        self.actor.x += self.velocity_x
         
    def move_left(self):
        self.h_direction = -1
        self.on_move = True
        self.actor.x -= self.velocity_x
                
    def jump(self):
        self.is_colliding_down = False
        self.velocity_y -= self.v_speed
        if sound_enable:
            sounds.jump.set_volume(0.2)
            sounds.jump.play()
    
    def dead(self):
        if sound_enable:
            if self.have_key:
                sounds.hurt_with_key.play()
            else:
                sounds.hurt.play()

        self.actor.x = INITIAL_X_POS_PLAYER
        self.actor.y = INITIAL_Y_POS_PLAYER
        self.have_key = False
        self.win = False
        
    def animation(self):
        if self.on_move:
            if self.h_direction == 1:
                if self.actor.image == 'player_0001_right':
                    self.actor.image = 'player_0002_right'
                else:
                    self.actor.image = 'player_0001_right'
            
            if self.h_direction == -1:
                if self.actor.image != 'player_0002_left':
                    self.actor.image = 'player_0002_left'
                else:
                    self.actor.image = 'player_0001_left'
                    
        else:
            if self.h_direction == 1:
                if self.actor.image != 'player_0002_right_idle':
                    self.actor.image = 'player_0002_right_idle'
                else:
                    self.actor.image = 'player_0001_right_idle'
            
            if self.h_direction == -1:
                if self.actor.image != 'player_0002_left_idle':
                    self.actor.image = 'player_0002_left_idle'
                else:
                    self.actor.image = 'player_0001_left_idle'
                    
        clock.schedule_unique(self.animation,self.animation_time) 
    
class EnemyRedAlien:
    def __init__(self,x_pos,y_pos,x_max,x_min):
        self.actor = Actor('enemy_0001_run_red_alien_right')
        self.actor.x = x_pos
        self.actor.y = y_pos
        self.max_x = x_max
        self.min_x = x_min
        self.direction = 'right'
        self.velocity_x = 0.5
        self.animation_time = 0.2
        # Alien sprite is a 24 x 24 px
        self.sprite_width = 24
        self.sprite_height = 24
        # Box collider
        self.width_box_collider = 10
        self.height_box_collider = 10
        self.rect_collider = Rect((self.actor.x - self.sprite_width / 2,self.actor.y - self.sprite_height / 2),(self.width_box_collider,self.height_box_collider))
        
    def update(self):
        self.rect_collider = Rect(((self.actor.x - self.sprite_width / 2) + 6,(self.actor.y - self.sprite_height / 2) + 6),(self.width_box_collider,self.height_box_collider))
    
    def moviment(self):
        if self.direction == 'right':
            if self.actor.x < self.max_x:
                self.actor.x += self.velocity_x
            else:
                self.direction = 'left'
                
        if self.direction == 'left':
            if self.actor.x > self.min_x:
                self.actor.x -= self.velocity_x
            else:
                self.direction = 'right'      
    
    def animate(self):
        if self.direction == 'right':
            if self.actor.image != 'enemy_0002_run_red_alien_right':
                self.actor.image = 'enemy_0002_run_red_alien_right'
            else:
                self.actor.image = 'enemy_0001_run_red_alien_right'
        
        if self.direction == 'left':
            if self.actor.image != 'enemy_0002_run_red_alien_left':
                self.actor.image = 'enemy_0002_run_red_alien_left'
            else:
                self.actor.image = 'enemy_0001_run_red_alien_left'
                
        clock.schedule_unique(self.animate,self.animation_time)

class EnemyYellowAlien:
    def __init__(self,x_pos,y_pos,x_max,x_min):
        self.actor = Actor('enemy_alien_yellow_0001_right')
        self.actor.x = x_pos
        self.actor.y = y_pos
        self.max_x = x_max
        self.min_x = x_min
        self.direction = 'right'
        self.velocity_x = 1
        self.animation_time = 0.2
        # Alien sprite is a 24 x 24 px
        self.sprite_width = 24
        self.sprite_height = 24
        # Box collider
        self.width_box_collider = 10
        self.height_box_collider = 10
        self.rect_collider = Rect((self.actor.x - self.sprite_width / 2,self.actor.y - self.sprite_height / 2),(self.width_box_collider,self.height_box_collider))
        
    def update(self):
        self.rect_collider = Rect(((self.actor.x - self.sprite_width / 2) + 6,(self.actor.y - self.sprite_height / 2) + 6),(self.width_box_collider,self.height_box_collider))
    
    def moviment(self):
        if self.direction == 'right':
            if self.actor.x < self.max_x:
                self.actor.x += self.velocity_x
            else:
                self.direction = 'left'
                
        if self.direction == 'left':
            if self.actor.x > self.min_x:
                self.actor.x -= self.velocity_x
            else:
                self.direction = 'right'      
    
    def animate(self):
        if self.direction == 'right':
            if self.actor.image != 'enemy_alien_yellow_0002_right':
                self.actor.image = 'enemy_alien_yellow_0002_right'
            else:
                self.actor.image = 'enemy_alien_yellow_0001_right'
        
        if self.direction == 'left':
            if self.actor.image != 'enemy_alien_yellow_0002_left':
                self.actor.image = 'enemy_alien_yellow_0002_left'
            else:
                self.actor.image = 'enemy_alien_yellow_0001_left'
                
        clock.schedule_unique(self.animate,self.animation_time)

class EnemyBox:
    def __init__(self,x_pos,y_pos,time_change_type):
        self.actor = Actor('box_peaceful')
        self.actor.x = x_pos
        self.actor.y = y_pos
        self.time_change_type = time_change_type
        self.type = 'peaceful'
        # Box Sprite is a 24x24 p
        self.sprite_width = 24
        self.sprite_height = 24
        # Box Collider
        self.width_box_collider = 10
        self.height_box_collider = 10
        self.rect_collider = Rect((self.actor.x - self.sprite_width / 2 + 7,self.actor.y - self.sprite_height / 2 + 7),(self.width_box_collider,self.height_box_collider))
        
    def change_type(self):
        if self.type == 'peaceful':
            self.type = 'dangerous'
            self.actor.image = 'box_dangerous'
        else:
            self.type = 'peaceful'
            self.actor.image = 'box_peaceful'
        
        clock.schedule_unique(self.change_type,self.time_change_type)

class Key:
    def __init__(self,x_pos,y_pos):
        self.actor = Actor('key')
        self.actor.x = x_pos
        self.actor.y = y_pos

class Door:
    def __init__(self):
        self.rect = Rect((810,375),(18,18))
            
class Spike:
    def __init__(self,x_pos,y_pos):
        self.rect = Rect((x_pos,y_pos),(18,18))
        
# Instance Actors
player = Player(INITIAL_X_POS_PLAYER,INITIAL_Y_POS_PLAYER)
red_alien_01 = EnemyRedAlien(230,225,310,230)
yellow_alien_01 = EnemyYellowAlien(460,405,560,460)
box_01 = EnemyBox(547,154,5)
box_02 = EnemyBox(640,154,2.5)
box_03 = EnemyBox(675,407,1)
key = Key(850,60)
door = Door()

spikes = [
    Spike(378,306),    
    Spike(702,216),
    Spike(738,216),
    Spike(774,216),
    Spike(810,216),
    Spike(846,216),
    Spike(882,216),
    Spike(756,180),
    Spike(828,180)
]

# Menu Var
start_game_rect = Rect((27,95),(242,40))
sound_game_rect = Rect((27,176),(507,40))
exit_rect = Rect((27,246),(87,40))

# On Key Down
def on_key_down(key,mod,unicode):
    if keys.W == key and player.is_colliding_down:
        player.jump()

# On Mouse Down
def on_mouse_down(pos):
    global in_menu, sound_enable
    
    if in_menu:
        if start_game_rect.collidepoint(pos):
            in_menu = False
            start_game()
                    
        if sound_game_rect.collidepoint(pos):
            if sound_enable:
                sound_enable = False
                music.pause()
            else:
                sound_enable = True
                music.unpause()
        
        if exit_rect.collidepoint(pos):
            exit()

# Start Game Def
def start_game():
    red_alien_01.animate()
    yellow_alien_01.animate()
    box_01.change_type()
    box_02.change_type()
    box_03.change_type()
    player.animation()   
            
# On Start Game Def 
def setup():
    for idx_h, h in enumerate(down_collision_mask):
        for idx_w, w in enumerate(h):
            if w == 1:
                x = idx_w * 18
                y = idx_h * 18
                selected_rect_collider_down.append(Rect((x,y,16,2)))

    for idx_h, h in enumerate(right_collision_mask):
        for idx_w, w in enumerate(h):
            if w == 1:
                x = idx_w * 18
                y = idx_h * 18
                selected_rect_collider_right.append(Rect((x-3,y,18,18)))
    
    for idx_h, h in enumerate(left_collision_mask):
        for idx_w, w in enumerate(h):
            if w == 1:
                x = idx_w * 18
                y = idx_h * 18
                selected_rect_collider_left.append(Rect((x+3,y,18,18)))
                        
    # Music and Sounds
    music.play('soundtrack')
    music.set_volume(MUSIC_VOLUME)

# Draw Def
def draw():
    screen.clear()
    screen.fill('skyblue')
    
    if not in_menu:
        screen.blit('map',(0,0))
    
    if DEBUG_MODE:
        # Drawing down mask collider
        for rect in selected_rect_collider_down:
            color_red = 255,0,0
            screen.draw.rect(rect,color_red)
        
        # Drawing right mask collider
        for rect in selected_rect_collider_right:
            color_blue = 0,0,255
            screen.draw.rect(rect,color_blue)

        # Drawing left mask collider
        for rect in selected_rect_collider_left:
            color_green = 0,255,0
            screen.draw.rect(rect,color_green)
        
        # Debug Enemy Rect Collider
            color = 0,100,0
            screen.draw.rect(red_alien_01.rect_collider,color)
            screen.draw.rect(box_01.rect_collider,color)
            screen.draw.rect(door.rect,color)

        # Debug Spike Rect Collider
        for spike in spikes:
            screen.draw.rect(spike.rect,color)
    
    if in_menu:
        color_white = 255,255,255
        
        screen.draw.rect(start_game_rect,color_white)
        screen.draw.rect(sound_game_rect,color_white)
        screen.draw.rect(exit_rect,color_white)
        
        screen.draw.text('Start Game',(30,100),fontname='8_bit')
        screen.draw.text('Enable or Disable Sound ',(30,180),fontname='8_bit')
        screen.draw.text('Exit',(30,250),fontname='8_bit')
        
        screen.draw.text('Help the Green Alien get the key \nand get him to the door safely',(30,310),fontname='8_bit',fontsize=16)
    
        screen.draw.text('Controls\n\nJump W\nRight  D\nLeft  A',(30,400),fontname='8_bit',fontsize=16)
        
        screen.draw.text('Developed by Damiao Gomes',(30,500),fontname='8_bit',fontsize=10)
        
    else:
        # Drawing Actors
        red_alien_01.actor.draw()
        yellow_alien_01.actor.draw()
        box_01.actor.draw()
        box_02.actor.draw()
        box_03.actor.draw()
        
        if player.have_key == False:
            key.actor.draw()
            
        player.actor.draw()
        
        # Player Win Text
        if player.win:
            screen.draw.text('You Win',(785,350))

# Update Def      
def update():
    if in_menu:
        pass
    else:
        # Collider list
        right_collider_list = player.actor.collidelist(selected_rect_collider_right)
        left_collider_list = player.actor.collidelist(selected_rect_collider_left)
        
        # Gravity System
        player.actor.y += player.velocity_y
        player.velocity_y += GRAVITY

        # Collision Down Check Player
        for rect in selected_rect_collider_down:
                if player.actor.colliderect(rect):
                    player.is_colliding_down = True
                    player.velocity_y = 0
                    if not player.actor.y > rect.y:
                        player.actor.bottom = rect.y
                    ## bug check
                    elif player.actor.collidelist(selected_rect_collider_down) > -1:
                        player.actor.bottom = selected_rect_collider_down[player.actor.collidelist(selected_rect_collider_down)].y

        # Right Moviment Player
        if keyboard[keys.D]:
            if right_collider_list == -1:
                player.move_right()
                
        # Left Moviment Player
        if keyboard[keys.A]:
            if left_collider_list == -1:
                player.move_left()
                
        # Idle
        if not keyboard[keys.A] and not keyboard[keys.D]:
            player.on_move = False 
            
        # Player fell off the map
        if player.actor.top >= HEIGHT:
            player.dead()
            
        # Enemy Moviment
        red_alien_01.update()
        red_alien_01.moviment()
        
        yellow_alien_01.update()
        yellow_alien_01.moviment()
        
        # Player Collide Enemys
        if player.actor.colliderect(red_alien_01.rect_collider):
            player.dead()

        if player.actor.colliderect(yellow_alien_01.rect_collider):
            player.dead()

        if player.actor.colliderect(box_01.rect_collider):
            if box_01.type == 'dangerous':
                player.dead()
        
        if player.actor.colliderect(box_02.rect_collider):
            if box_02.type == 'dangerous':
                player.dead()
        
        if player.actor.colliderect(box_03.rect_collider):
            if box_03.type == 'dangerous':
                player.dead()
        
        # Player Collide Spikes
        for spike in spikes:
            if player.actor.colliderect(spike.rect):
                player.dead()
        
        # Player Collide Key
        if player.actor.colliderect(key.actor):
            if not player.have_key and sound_enable:
                sounds.get_key.play()
                
            player.have_key = True
        
        # Player Collide Door
        if player.actor.colliderect(door.rect):
            if player.have_key:
                if not player.win and sound_enable:
                    sounds.player_win.play()        

                player.win = True

setup()
pgzrun.go()