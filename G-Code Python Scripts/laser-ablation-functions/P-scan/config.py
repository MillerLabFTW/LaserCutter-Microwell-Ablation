#File
fname = '2015-01-31_P-scanC.gcode'
f=open(fname,'w')

FOCUS = 124.1

#Laser Parameters
laserPowers     = [25, 35, 45] #% max power
dwellTimes      = [50, 60, 70] #ms
zValues			= [8, 10, 12]
x_start        	= 416
y_start        	= 343
pauseTime      	= 500 #ms; time paused after movement before ablation
feedRate       	= 500 #movement speed

# Rectangle size properties
length 			= 10
spaceSmall     	= 1.8 #mm; space between rectangles
spaceLarge		= 2.5
hexLength      	= 1.6 #mm


#Other
relative       	= 1 #1 for no starting x,y; 0 for using starting co-ordinates

## Orientation
#Note: Enter a combination of 1, 2, and 3
# Positions one and two will be prominently visible from the side.  Position Three will be
# manifest in multiple strips of PDMS
#1 = Laser power
#2 = Dwell Time
#3 = z Values
orientation = "213"