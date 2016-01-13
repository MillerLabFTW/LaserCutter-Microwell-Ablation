##### OVERVIEW #####
# Program to cut n-sided polygons in PDMS with the laser cutter


##### NEED TO FIX DIVISION OPERATOR!!!!!
from __future__ import division
#http://docs.python.org/release/2.2.3/whatsnew/node7.html
#The most controversial change in Python 2.2 heralds the start of an effort to fix an old design flaw that's been in Python from the beginning. Currently Python's division operator, /, behaves like C's division operator when presented with two integer arguments: it returns an integer result that's truncated down when there would be a fractional part. For example, 3/2 is 1, not 1.5, and (-1)/2 is -1, not -0.5. This means that the results of divison can vary unexpectedly depending on the type of the two operands and because Python is dynamically typed, it can be difficult to determine the possible types of the operands.
import math
import config
import writefile


#Polygon Parameters
nSides          = config.nSides         # Number of sides to polygon
theta			= config.theta			# angle to rotate ngon in radians
nAngle          = 2*math.pi / nSides    # Angle for each side of polygon
radius          = config.radius         # Radius of polygon


#Laser Parameters
feedRate		= config.feedRate       # mm/s
laserPower		= config.laserPower     # out of 255
pauseTime       = config.pauseTime      # ms
x_start			= config.x_start
y_start  		= config.y_start
z_start         = config.z_start

#Other
decimal         = config.decimal        # decimal places for gcode
f               = config.f              # file pipe
r_hex           = radius*2 + 0.5          # hexagonal packing length


def fl(number, decimal):
    flStr = "%0." + str(decimal) + "f"
    return float(flStr % number)

def move_position(x_pos, y_pos):
    x_pos = fl(x_pos, decimal)
    y_pos = fl(y_pos, decimal)
    f.writelines("M3 S0\n")
    f.writelines("G0 X" + str(x_pos) + " Y" + str(y_pos) + " F1000\n")
    f.writelines("G4 P" + str(pauseTime) + "\n")

def draw_line(x_line, y_line):
    x_line = fl(x_line, decimal)
    y_line = fl(y_line, decimal)
    f.writelines("G1 X" + str(x_line) + " Y" + str(y_line) + " F" + str(feedRate) + "\n")

def hex_pattern(r_hex):
	x_dist = "%0.3f" % (r_hex)
	y_dist = "%0.3f" % (r_hex * (3**0.5) / 2)
	distances = [float(x_dist), float(y_dist)]
	return distances

def draw_circle(x_center, y_center):
    ## Move to first position ##
    x = x_center + radius * math.cos(theta)
    y = y_center + radius * math.sin(theta)
    move_position(x,y)


    ## Turn on Laser ##
    f.writelines("M649 S" + str(laserPower) + " B0\n")

    ## Iterate through other points, drawing lines ##
    for i in range(1,nSides+1):
        x = x_center + radius * math.cos(i*nAngle+theta)
        y = y_center + radius * math.sin(i*nAngle+theta)
        draw_line(x,y)

    ## Turn off Laser ##
    f.writelines("M3 S0\n")
    move_position(x_center, y_center)

def new_center(x_move, y_move):
    f.writelines("M3 S0\n")
    f.writelines("G91\n")
    f.writelines("G0 X" + str(x_move) + " Y" + str(y_move) + "\n")
    f.writelines("G92 X0 Y0 Z0\n")
    f.writelines("G90\n")


# Hexagonal distances
distances = hex_pattern(r_hex)
x_hex = distances[0]
y_hex = distances[1]

## Initialize gcode file ##
writefile.openGcode()

# Home z-axis
f.writelines("M3 S0\n")
#f.writelines("G28\n")
f.writelines("G0 X" + str(x_start) + " Y" + str(y_start) + " F2000\n")
f.writelines("G0 Z" + str(z_start) + " F300\n")

# Draw circles 
draw_circle(x_start,y_start)

#draw_circle(x_start-2*radius-0.5, y_start)

# draw_circle(x_start-4*radius-0.5, y_start)

# draw_circle(x_start-6*radius-0.5, y_start)

# draw_circle(x_start,y_start-2*radius-0.5)

# draw_circle(x_start-2*radius-0.5, y_start-2*radius-0.5)

# draw_circle(x_start-4*radius-0.5, y_start-2*radius-0.5)

# draw_circle(x_start-6*radius-0.5, y_start-2*radius-0.5)

# draw_circle(x_start - r_hex, y_start - r_hex)

# draw_circle(x_start, y_start - r_hex)

## Close Gcode file ##
f.writelines("G0 Z" + str(z_start - 15) + " F300\n")
writefile.closeGcode()















