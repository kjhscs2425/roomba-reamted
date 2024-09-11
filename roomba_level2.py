# -----------------------------------------------------------------------------
# Roomba in Python
# This file implements an algorithm for a roomba cleaning a room.
#
# Author: Nick <------ REPLACE THIS WITH YOUR NAME!
# -----------------------------------------------------------------------------
 
from turtle import right, left, forward, backward, speed
import room

# Make the turtle go faster
speed(7)

# Draw the Level 2 version of the room
window = room.draw_room(level = 2)


###
# Start your code here

square=40

height=15
width=20

forward((height-1)*square)
for i in range(15):
    for e in range(2):
            
                vertical_arm_lenght = (height - i-e)*square
                horizontal_arm_lenght = (width - i-e) * square
    left(90)
    forward(horizontal_arm_lenght)
    left(90)
    forward(vertical_arm_lenght)
    
    
    
    
 
 
# End your code here
###
 
window.exitonclick()