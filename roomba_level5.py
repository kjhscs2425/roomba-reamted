# -----------------------------------------------------------------------------
# Roomba in Python
# This file implements an algorithm for a roomba cleaning a room.
#
# Author: Dr. EB <------ REPLACE THIS WITH YOUR NAME!
# -----------------------------------------------------------------------------
 
from turtle import right, left, forward, backward, speed
import room

# THIS PARAMETER CAN CHANGE!!!
# Make sure your code works for n_alcoves = 0, 1, 2, 3, and 4
# (You are allowed to use this parameter in your code)
n_alcoves = 3

speed(10) 
# Draw the Level 5 version of the room
window = room.draw_room(level = 5, n_alcoves = n_alcoves)

###
# Start your code here
 
forward(40*14)
left(180)
forward(40)
left(90)
forward(120)

backward(240)
right(90)
forward(40)
right(90)
forward(40)
for i in range(3):
    backward(320)
    left(90)
    forward(40)
    right(90)
    forward(320)
    left(90)
    forward(40)
    right(90)
backward(320)
forward(280)
left(90)
forward(40)
right(90)
backward(240)
right(90)
forward(40)
right(90)
forward(40)
left(90)
forward(120)
right(90)
forward(40*5)
backward(40)
left(90)
forward(40)
left(90)
forward(40)
right(90)
forward(40)
backward(40)
right(90)
forward(40)
right(90)
forward(80)
right(90)
forward(40)
left(90)
forward(40)
backward(40)
right(90)
forward(40)
right(90)
forward(80)
backward(40)
left(90)

forward(480)


left(90)
forward(40)
right(90)
forward(40)
left(90)
forward(40)
backward(40)

right(90)
forward(40)
right(90)
forward(40)
left(90)
forward(40)
backward(40)


right(90)
forward(40)
right(90)
forward(40)
left(90)
forward(40)
backward(80)
forward(40)
right(90)
forward(40)
right(90)
forward(40)
left(90)
forward(240)
right(90)

#new stuff alert
speed(4)
forward(240)
right(90)
forward(40)
left(90)
forward(40)
right(90)
forward(40)
backward(40)
left(90)
forward(40)
left(90)
forward(40)
right(90)
forward(40)
backward(40)
left(90)
forward(40)
left(90)
forward(40)
right(90)
forward(40)
backward(40)
left(90)
forward(40)



 
 
# End your code here
###
 
window.exitonclick()