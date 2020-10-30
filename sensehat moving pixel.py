from sense_hat import SenseHat

sense = SenseHat()
sense.clear()

blue = (0,0,255)
clear = (0,0,0)

sense.set_pixel(2,2,blue)

while True:
    for event in sense.stick.get_events():
        # check if joystick is pressed
        if event.action == 'pressed':
            
            # check which direction has been pressed
            if event.direction == 'up':
                sense.set_pixel(2,1,blue)
            elif event.direction == 'down':
                sense.set_pixel(2,3,blue)
            elif event.direction == 'left':
                sense.set_pixel(1,2,blue)
            elif event.direction == 'right':
                sense.set_pixel(3,2,blue)
            elif event.direction == 'middle':
                sense.set_pixel(2,2,blue)
        elif event.action == 'released':
                sense.set_pixel(2,2,clear)