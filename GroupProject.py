import turtle as trtl #import turtle
import random #import random
import math
stars=trtl.Turtle() #create turtle object
trtl.setup(800, 500)
#setup screen up here so we can see the stars being drawn
wn=trtl.Screen()
wn.bgcolor("midnight blue")

#setup object attributes
stars.speed(0)
stars.penup()
stars.pensize(1.8)
stars.color("white")
stars.hideturtle()

#function to draw stars by stamping with turtle. we're not using this
def draw_star():
  #pendown to start drawing
  stars.pendown()
  for i in range(5):
    #repeat 5 times: go forward, turn 144 deg. will result in a star
    stars.forward(5)
    stars.right(144)
    #penup to move
  stars.penup()
    
#loop the function so that we have multiple.
for j in range(40):
  #go to random position within the range...
  stars.goto(random.randint(-400,400),random.randint(50,250))
  #...and draw the star
  draw_star()


import turtle as trtl
road = trtl
#screen size
trtl.setup(800, 500)

#actual road
color = input("What color would you like the road to be? (gray, black, blue, green) ")
road.penup()
road.pencolor(color) #color
road.pensize(100)
road.goto(-400,-200) #start of road divider
road.pendown()
road.forward(800)

road.pencolor("black")
road.turtlesize(1)
road.pensize(6)
road.penup()
road.goto(-400,-150)
road.pendown()
#road boarder
road.forward(800)
road.penup()
road.goto(-400,-200) #start of road divider
road.pendown()
#road middle hashes
road.pencolor("yellow")
for i in range(10):
  road.forward(40)
  road.penup()
  road.forward(40)
  road.pendown()
#building 1-4
road.pencolor("black")
road.pensize(6)
road.penup()
road.goto(-340,-150)
#Draw first building
road.pendown()
road.left(90)
road.forward(250)
road.right(90)
road.forward(100)
road.right(90)
road.forward(250)
#Draw second building
road.penup()
road.goto(-240,25)
road.left(90)
road.pendown()
road.forward(75)
road.right(90)
road.forward(175)
#Draw third building
road.penup()
road.color("Black")
road.goto(-165,-25)
road.left(90)
road.pendown()
road.forward(80)
road.right(90)
road.forward(125)
road.penup()
#Draw fourth building
road.pendown()
road.left(180)
road.forward(300)
road.right(90)
road.forward(86)
road.right(90)
road.goto(0,-150)


#building 5 
road.pencolor("black")
road.penup()
road.goto(20,-150)
road.pendown()
road.left(180)
road.forward(200)
road.right(90)
road.forward(150)
road.right(90)
road.forward(200)
#building 6
road.left(90)
road.forward(20)
road.left(90)
road.forward(100)
road.right(90)
road.forward(130)
road.right(90)
road.forward(100)
#building 7
road.left(180)
road.forward(150)
road.right(70)
road.forward(100)

#moon
road.penup()
road.goto(350,150)
#Draw the gray circle for the moon
road.pendown()
road.fillcolor("gray")
road.begin_fill()
road.circle(40)
road.end_fill()

#draw first circle
road.penup()
road.goto(378,170)
road.fillcolor("DarkSlateGrey")
road.begin_fill()
road.pendown()
road.circle(4)
road.end_fill()

#draw second circle
road.penup()
road.goto(360,180)
road.fillcolor("DarkSlateGrey")
road.begin_fill()
road.pendown()
road.circle(7)
road.end_fill()

#draw third circle
road.penup()
road.goto(340,168)
road.fillcolor("DarkSlateGrey")
road.begin_fill()
road.pendown()
road.circle(3)
road.end_fill()

#draw fourth circle
road.penup()
road.goto(370,195)
road.fillcolor("DarkSlateGrey")
road.begin_fill()
road.pendown()
road.circle(3)
road.end_fill()

#draw fifth circle
road.penup()
road.goto(350,210)
road.fillcolor("DarkSlateGrey")
road.begin_fill()
road.pendown()
road.circle(5)
road.end_fill()

#draw sixth circle
road.penup()
road.goto(349,160)
road.fillcolor("DarkSlateGrey")
road.begin_fill()
road.pendown()
road.circle(5)
road.end_fill()

#draw seventh circle
road.penup()
road.goto(330,190)
road.fillcolor("DarkSlateGrey")
road.begin_fill()
road.pendown()
road.circle(5)
road.end_fill()

#setup turtle
window_painter=trtl.Turtle()
window_painter.speed(0)
window_painter.hideturtle()

#define window - length is the side length of the window.
def draw_windows(x,y,length=10):
  #set either gray or yellow window color - 50/50.
  color=random.randint(0,1)
  if color==1:
    win_color="gray"
  else:
    win_color="yellow"
    
  #setting up the drawer
  window_painter.setheading(270)#the first one becomes weird if this doens't exist
  window_painter.fillcolor(win_color)#set winodw color to the one decided up there
  window_painter.penup()#go to the location
  window_painter.goto(x,y)
  window_painter.pendown()
  window_painter.begin_fill()
  window_painter.speed(20)
  
  #draw the square with a loop
  for i in range(4):
    window_painter.left(90)
    window_painter.forward(length)
  window_painter.end_fill()#end filling
  
  #draw the crossbars
  for heading in (0,90):#first draw horizontal, then vertical
    window_painter.penup()
    window_painter.goto(x+length/2,y+length/2)#go to the center
    window_painter.pendown()
    
    #go  back & forth to draw crossbars
    window_painter.setheading(heading)
    window_painter.forward(length/2)
    window_painter.backward(length)
    

#to draw an array of windows: change value in the range functions.

# (starting position, end position, distance in between)

#drawing windows for the square building, 5th from the left
for y in range(-140,40,20):
  for x in range(30,170,20):
    draw_windows(x,y)

import turtle as trtl 
screen_h = 500
screen_w = 800
startx = 0
starty = -50
turtle_scale = 1

def move():
  car.dot(10)
  car.fd(50)

def turn_left():
  car.speed(0)
  car.lt(90)
  car.speed(2)
  
wn = trtl.Screen()
wn.setup(width=screen_w, height=screen_h)
robot_image = "spidey.gif"
wn.addshape(robot_image)

spider = trtl.Turtle(shape=robot_image)
spider.hideturtle()
spider.color("darkorchid")
spider.pencolor("darkorchid")
spider.penup()
spider.setheading(90)
spider.turtlesize(turtle_scale, turtle_scale)
spider.goto(startx, starty)
spider.speed(2)
spider.showturtle()





wn = trtl.Screen()
wn.setup(width=screen_w, height=screen_h)
car_image = "car1transparent.gif"
wn.addshape(car_image)

car = trtl.Turtle(shape=car_image)
#Position the car
for i in range(5):
  car.goto(-300,-200)
  car.goto(300,-200)
car.penup()
car.hideturtle()
car.color("darkorchid")
car.pencolor("darkorchid")
car.penup()
car.setheading(90)
car.turtlesize(turtle_scale, turtle_scale)
car.goto(startx, starty)

carspeed= int(input("How fast does the car drive?"))
car.speed(carspeed)
car.showturtle()
car.turtlesize(20,20)

for i in range(5):
  car.goto(-300,-150)
  car.goto(300,-150)

wn = trtl.Screen()
wn.mainloop()
