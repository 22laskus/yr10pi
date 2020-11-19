from sense_hat import SenseHat
import time
import random

sense = SenseHat()
sense.clear()

blue = (0,0,255)
red = (255,0,0)
clear = (0,0,0)

x = 3
y = 4

sense.set_pixel(x,y,blue)


while True:
    wall = random.randint(1,5)
    if wall == 1:
        y=0
    elif wall == 2:
        y=7
    elif wall == 3:
        x=0
    elif wall == 4:
        x=7
    sense.clear()
    sense.set_pixel(x,y,red)
    start_time = time.time()
       
    for event in sense.stick.get_events():
        # check if joystick is pressed
        if event.action == 'pressed':
            
            # check which direction has been pressed
            if event.direction == 'up':
                if y==0:
                    y=0
                else:
                    y=y-1
            elif event.direction == 'down':
                if y==7:
                    y=7
                else:
                    y=y+1
            elif event.direction == 'left':
                if x==0:
                    x=0
                else:
                    x=x-1
            elif event.direction == 'right':
                if x==7:
                    x=7
                else:
                    x=x+1
            elif event.direction == 'middle':
                sense.set_pixel(4,4,blue)
        elif event.action == 'released':
            sense.set_pixel(2,2,clear)
            
    print(f"{x},{y}")
    end_time = time.time()
    time.sleep(1.4)
    time_lapsed = end_time - start_time
    print(time_lapsed)
    sense.clear()
    sense.set_pixel(x,y,blue)
    time.sleep(1.4)
