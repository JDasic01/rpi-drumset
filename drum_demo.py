import pgzrun

screen_title = "Drum Module Demo"
# Set Pygame Zero screen size and title
WIDTH = 800
HEIGHT = 600
TITLE = screen_title
# class Preset:


def draw():
    screen.fill((192, 192, 192))
    screen.draw.text(screen_title, fontsize=40, center=(400,50), shadow=(1, 1), 
    color=(255, 255, 255), scolor="#202020")

def on_key_down(key):
    if keyboard.up:
        sounds.hi_hat.play()
    if keyboard.down:
        sounds.snare.play()
    if keyboard.right:
        sounds.bass.play()
pgzrun.go()