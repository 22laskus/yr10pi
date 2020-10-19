from sense_hat import SenseHat
from time import sleep

sense = SenseHat()

red=(255,0,0)
yellow=(255,255,0)
green=(0,255,0)
cyan=(0,255,255)
blue=(0,0,255)
magenta=(255,0,255)
black=(0,0,0)
white=(255,255,255)


sense.show_letter("q", red)
sleep(.5)
sense.show_letter("w", yellow)
sleep(.5)
sense.show_letter("e", green)
sleep(.5)
sense.show_letter("r", cyan)
sleep(.5)
sense.show_letter("t", blue)
sleep(.5)
sense.show_letter("y", magenta)
sleep(.5)
sense.show_letter(".", white)
