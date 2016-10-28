#File
fname = 'aryeh2-test1.gcode'
f=open(fname,'w')

#Laser Parameters
laserPower     = 9 #% max power
dwellTime      = 4 #ms
x_start        = 414
y_start        = 335
z_start        = 123.40 #mm above home
pauseTime      = 500 #ms; time paused after movement before ablation
feedRate       = 500 #movement speed

# Rectangle size properties
rectLength     = 10 #mm; x-direction
rectWidth      = 10 #mm; y-direction
spaceSmall     = 3 #mm; space between rectangles
hexLength      = 0.300 #mm

#Other
relative       = 0 #0 for homing before beginning.  1 if machine has already been homed
cleanTrigger	= 20 #number of rows between laser head cleanings