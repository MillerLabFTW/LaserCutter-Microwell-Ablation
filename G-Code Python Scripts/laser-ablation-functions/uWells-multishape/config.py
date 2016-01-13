#File
fname = 'C3-4 and C3-5.gcode'
f=open(fname,'w')

FOCUS = 124.1

#Laser Parameters
laserPower     = [45, 45] #% max power
dwellTime      = [60, 60] #ms
zValue		   = [8, 12] #mm below focus
x_start        = 416
y_start        = 343
pauseTime      = 500 #ms; time paused after movement before ablation
feedRate       = 500 #movement speed

# Rectangle size properties
rectLength     = 15 #mm; x-direction
rectWidth      = 15 #mm; y-direction
spaceSmall     = 3 #mm; space between rectangles
hexLength      = 1.8 #mm

#Other
#relative       = 0 #0 for homing before beginning.  1 if machine has already been homed