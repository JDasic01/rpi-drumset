import pgzrun
from preset import *

# Set Pygame Zero screen size and title
WIDTH = 800
HEIGHT = 600
TITLE = "Drum Module Demo"

def setup():
    presets = create_preset_list()
    preset_num = 0

def draw():
    '''Draw a pygame window'''
    screen.fill((192, 192, 192))
    screen.draw.text(screen_title, fontsize=40, center=(400,50), shadow=(1, 1), 
    color=(255, 255, 255), scolor="#202020")


def on_key_down(key):
    ''' for testing sounds with keyboard '''
    if keyboard.up:
        sounds.hi_hat.play()
        sounds.hi_hat.play()
    if keyboard.down:
        sounds.snare.set_volume(0.5)
        sounds.snare.play()
    if keyboard.right:
        sounds.bass.play()
    if keyboard.left:







pgzrun.go()
