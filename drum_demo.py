import pgzrun
import os
screen_title = "Drum Module Demo"
# Set Pygame Zero screen size and title
WIDTH = 800
HEIGHT = 600
TITLE = screen_title
# class Preset:

class Preset:
    def create_preset_folder(self, preset_name, preset_sounds):
         '''Take the name of the folder and an array with presets, create the folder as the subfolder f "sounds"'''
      pass
      def choose_preset(name):#
     '''Find path to the preset with selected name'''
         path = ...
         return path

def draw():
    screen.fill((192, 192, 192))
    screen.draw.text(screen_title, fontsize=40, center=(400,50), shadow=(1, 1), 
    color=(255, 255, 255), scolor="#202020")

def on_key_down(key):
    # play(path_from_choose_preset)
    if keyboard.up:
        sounds.hi_hat.play()
        sounds.hi_hat.play()
    if keyboard.down:
        sounds.snare.set_volume(0.5)
        sounds.snare.play()
    if keyboard.right:
        sounds.bass.play()
pgzrun.go()
