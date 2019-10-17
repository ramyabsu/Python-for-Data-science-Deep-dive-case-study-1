'''
A robot moves in a plane starting from the original point (0,0).
The robot can move toward UP, DOWN, LEFT and RIGHT with a given steps. The trace of robot movement is shown as the following:
UP 5, DOWN 3, LEFT 3, RIGHT 2
The numbers after the direction are steps. Please write a program to compute the distance from current
position after a sequence of movements.
'''
import math
#Init vars
mypos = [0, 0]
moves = {"UP": [0, 1], "DOWN": [0, -1], "LEFT": [-1, 0], "RIGHT": [1, 0]}

#Set inputs
data = ["UP 5", "DOWN 3", "LEFT 3", "RIGHT 2"]

#Move robot
for i in data:
    mystr = i.split()
    mv = mystr[0]
    val = mystr[1]
    if mv in moves and val.isnumeric():
        mypos[0] += moves[mv][0]*int(val)
        mypos[1] += moves[mv][1]*int(val)

#get distance
distance = math.sqrt(mypos[0]**2 + mypos[1]**2)
print('The distance after sequence of movement is: ', round(distance, 3))