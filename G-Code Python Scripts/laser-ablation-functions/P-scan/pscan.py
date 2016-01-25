##### Code Explanation ######
# Script creates a simple M x N array of squares where:
# M corresponds to a specified array of laser power settings (laserPowers)
# N corresponds to a specified array of dwell time settings (dwellTimes)
# 
# Modify parameters via uWell-config.py file

##### NEED TO FIX DIVISION OPERATOR!!!!!
from __future__ import division
#http://docs.python.org/release/2.2.3/whatsnew/node7.html
#The most controversial change in Python 2.2 heralds the start of an effort to fix an old design flaw that's been in Python from the beginning. Currently Python's division operator, /, behaves like C's division operator when presented with two integer arguments: it returns an integer result that's truncated down when there would be a fractional part. For example, 3/2 is 1, not 1.5, and (-1)/2 is -1, not -0.5. This means that the results of divison can vary unexpectedly depending on the type of the two operands and because Python is dynamically typed, it can be difficult to determine the possible types of the operands.

import config
import writefile

## Parameters

FOCUS = config.FOCUS

#File
f = config.f

#Laser Parameters
laserPowers 	= config.laserPowers
dwellTimes      = config.dwellTimes
zValues 		= [FOCUS-z for z in config.zValues]
x_start			= config.x_start
y_start			= config.y_start
pauseTime 		= config.pauseTime
feedRate        = config.feedRate



# Rectangle size properties
length 		= config.length
spaceSmall 	= config.spaceSmall
spaceLarge 	= config.spaceLarge
hexLength	= config.hexLength

# Other Parameters
relative   	= config.relative

# Orientation
orientation = config.orientation
params = {'1':laserPowers, '2':dwellTimes, '3':zValues}

def xy_move(x_move, y_move):
	f.writelines("M3 S0\n")
	f.writelines("G0 X" + str(x_move) + " Y" + str(y_move) + " F500\n")
	f.writelines("G4 P" + str(pauseTime) + "\n")
	
def z_move(z):
	f.writelines("G90\n")
	f.writelines("G0 Z" + str(z) + " F300\n")
	f.writelines("G4 P250\n")
	f.writelines("G91\n")

def gcode_line(kvargs):
	laserPower 	= str(kvargs['1'])
	dwellTime 	= str(kvargs['2'] * 1000)
	z			= str(kvargs['3'])
	x 			= str(-1*length)
	ppm			= str(1.0/hexLength)
	speed		= str(feedRate)
	
	z_move(z)
	
	line = "G1 B1 X{0} F{1} S{2} L{3} P{4}\n".format(x, speed, laserPower, dwellTime, ppm) 
	f.writelines(line)
	
	xy_move(length, -1*spaceSmall)
	

	
## Write GCODE file
writefile.header()

f.writelines("M3 S0\n") ## Laser Off

if relative == 1: 
	f.writelines("G28\n") ## Home axes.
else: 
	f.writelines("G90\n") 
f.writelines("G0 X" + str(x_start) + " Y" + str(y_start) + " F2000\n") # Move to x and y-axis start
f.writelines("G91\n")


## Print Parameter Scan
values1 = params[orientation[0]]
values2 = params[orientation[1]]
values3 = params[orientation[2]]

x_dist = -1*(length+spaceLarge)
y_dist = len(values2)*len(values3)*spaceSmall + len(values2)*(spaceLarge-spaceSmall)

for i in range(0,len(values1)):
	value1 = values1[i]
	
	for j in range(0,len(values2)):
		value2 = values2[j]
		
		for k in range(0,len(values3)):
			value3 = values3[k]
			
			kvargs = {orientation[0]:value1, orientation[1]:value2, orientation[2]:value3}
			gcode_line(kvargs)
		
		xy_move(0, spaceSmall - spaceLarge)
	
	xy_move(x_dist, y_dist) 

# Close file
writefile.closefile()
	
	
	
	
	




