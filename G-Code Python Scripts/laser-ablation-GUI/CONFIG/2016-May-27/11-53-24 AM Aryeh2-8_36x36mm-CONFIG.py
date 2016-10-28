#File
fname = 'Aryeh2-8_36x36mm.gcode'
f=open(fname,'w')

#Laser Parameters
laserPower     = 9 #% max power
dwellTime      = 4 #ms
x_start        = 414
y_start        = 340
z_start        = 123.40 #mm above home
pauseTime      = 500 #ms; time paused after movement before ablation
feedRate       = 500 #movement speed

# Rectangle size properties
rectLength     = 36 #mm; x-direction
rectWidth      = 36 #mm; y-direction
spaceSmall     = 3 #mm; space between rectangles
hexLength      = 0.300 #mm

#Other
relative       = 0 #0 for homing before beginning.  1 if machine has already been homed
cleanTrigger	= 15 #number of rows between laser head cleanings