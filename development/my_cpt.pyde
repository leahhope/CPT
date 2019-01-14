import random
import time
import sys

speed = 0.1
score = 0
highscore = 0
snake = (0,0,0,0)
x1=200
x2=25
y1=25
y2=25
steps = 0
sf = 500

#setup the size of the screen
def setup():
    size(500, 500)

#colour of the background 
#calling the drawings
def draw():
    background(0)
    draw_snake()
    draw_food()

#creating snake
def draw_snake():
    global x1,y1,x2,y2
    fill(50,205,50)
    rect(x1, y1, x2, y2)

#creating food
def draw_food():
    noStroke()
    fill(255,0,0)
    ellipse(25,25,20,20)
   
   class Apple:
    x = 0
    y = 0
    step = 44
    
    def _init_(self, x,y):
        self.x = x * self.step
        self.y = y * self.step
        
    def draw(self, surface, image):
        surface.blit(image,(self.x, self.y))
    
#moving the snake
def keyPressed():
    global space_pressed, up_pressed
    print(keyCode)
    if keyCode == 32:  # space keycode is 32
        space_pressed = True
    elif keyCode == 38:  # up arrow
        up_pressed = True
            
#collison
def keyPressed():
    global x1, y1, x2, y2, steps
    steps=steps+1
    rect(x1, y1, x2, y2)
    if (key==CODED):
        if (keyCode == LEFT) and x1>=1:
            x1=x1-10
            print(x1)
            rect(x1,y1,x2,y2)            
 
        elif (keyCode == RIGHT) and x1<=470:
            x1=x1+10
            print(x1)
            rect(x1,y1,x2,y2)
 
        elif (keyCode == UP) and y1>=1:
            y1=y1-10
            print(y1)
            rect(x1,y1,x2,y2)
 
        elif (keyCode == DOWN) and y1<=465:
            y1=y1+10
            print(y1)
            rect(x1,y1,x2,y2)

        else:
            fill(255,255,0)
            rect(x1,y1,x2,y2)
            text("game over",220,200)
