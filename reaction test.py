from sense_hat import SenseHat
import time
import random







sense = SenseHat()
sense.clear()

blue = (0,0,255)
clear = (0,0,0)

x = 3
y = 4

sense.set_pixel(x,y,blue)


while True:
    for x in range(1):
    print(random.randint(1,6))
    time.sleep(2.4)
 
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
        sense.clear()
        sense.set_pixel(x,y,blue)