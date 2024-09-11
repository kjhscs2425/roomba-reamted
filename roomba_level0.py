# -----------------------------------------------------------------------------
# Roomba in Python
# This file implements an algorithm for a roomba cleaning a room.
#
# Author: Nick <------ REPLACE THIS WITH YOUR NAME!
# -----------------------------------------------------------------------------
 
from turtle import right, left, forward, backward
import room

# Draw the Level 0 version of the room
window = room.draw_room(level = 0)

###
# Start your code here
for i in range (3):
    forward(160)
    left(90)
for i in range (2):
    forward(120)
    left(90)
for i in range (2):
    forward(80)
    left(90)
for i in range (2):
    forward(40)
    left(90)




# End your code here
###
 
window.exitonclick()