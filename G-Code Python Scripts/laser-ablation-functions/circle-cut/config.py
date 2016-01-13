import math

#File 
fname = "P150.gcode"
f = open(fname,"w")

#Polygon Parameters
nSides      = 1000   # Number of sides to polygon
radius      = 66.5   # Radius of polygon
theta		= 0

#Laser Parameters
feedRate    = 500   # mm/s
laserPower  = 20    # percent max power
pauseTime   = 500   # ms
x_start 	= 378  #418-radius-0.5  # mm
y_start		= 296  #340-radius-0.5	# mm
z_start     = 124.1 - 25  # mm

## Focus = 124.1 

#Other
decimal     = 3     # number of decimal places in gcode

