#File
fname = '3.1.2_S20_1.gcode'
f=open(fname,'w')

#Laser Parameters
laserPower     = 20 #% max power
dwellTime      = 20 #ms
x_start        = 414
y_start        = 340
z_start        = 122.10 #mm above home
pauseTime      = 500 #ms; time paused after movement before ablation
feedRate       = 500 #movement speed

# Rectangle size properties
rectLength     = 10 #mm; x-direction
rectWidth      = 10 #mm; y-direction
spaceSmall     = 3 #mm; space between rectangles
hexLength      = 1.000 #mm

#Other
relative       = 0 #0 for homing before beginning.  1 if machine has already been homed
cleanTrigger	= 15 #number of rows between laser head cleanings