# -----------------------------------------------------------------------------
# Roomba in Python
# This file implements an algorithm for a roomba cleaning a room.
#
# Author: Dr. EB <------ REPLACE THIS WITH YOUR NAME!
# -----------------------------------------------------------------------------
 
from turtle import right, left, forward, backward, speed
import room

# Make the turtle go faster
speed(7)

# Draw the Level 3 version of the room
window = room.draw_room(level = 3, radius=5)

###
# Start your code here
forward(40)
right(90)
forward(120)
left(90)
forward(40)
right(90)
forward(40)
left(90)
forward(120)
right(90)
forward(40)
backward(40)
left(90)
forward(120)
left(90)
forward(40)
right(90)
forward(40)
left(90)
forward(120)
right(90)
forward(40)
backward(40)
left(90)
forward(120)
left(90)
forward(40)
right(90)
forward(40)
left(90)
forward(120)
right(90)
forward(40)
backward(40)
left(90)
forward(120)
left(90)
forward(40)
right(90)
forward(40)
left(90)
forward(80)
backward(80)
left(90)
#forward(40)

square = 40

for i in range(7):
    arm_length = (7-i)*square
    print (arm_length)
    for e in range(2):
        forward(arm_length)
        right(90)
        

#for e in range(4):
    #forward(240)
    #right(90)
#for i in range (4):
    #forward(200)
    #right(90)
#for i in range (4):
    #forward(160)
    #right(90)
#for i in range(4):
    #forward(120)
    #right(90)
#for i in range (4):
    #forward(80)
    #right(90)
#for i in range(4):
    #forward(40)
    #right(90)
    
 
 
# End your code here
###
 
window.exitonclick()