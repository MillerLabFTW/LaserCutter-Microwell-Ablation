#File
fname = 'Nick-test-5-31-16.gcode'
f=open(fname,'w')

#Laser Parameters
laserPower     = 15 #% max power
dwellTime      = 10 #ms
x_start        = 414
y_start        = 340
z_start        = 120.10 #mm above home
pauseTime      = 500 #ms; time paused after movement before ablation
feedRate       = 100 #movement speed

# Rectangle size properties
rectLength     = 25 #mm; x-direction
rectWidth      = 25 #mm; y-direction
spaceSmall     = 3 #mm; space between rectangles
hexLength      = 0.800 #mm

#Other
relative       = 0 #0 for homing before beginning.  1 if machine has already been homed
cleanTrigger	= 15 #number of rows between laser head cleanings