#File
fname = 'reid1_P100-3.gcode'
f=open(fname,'w')

#Laser Parameters
laserPower     = 16 #% max power
dwellTime      = 12 #ms
x_start        = 402.5
y_start        = 306
z_start        = 122.30 #mm above home
pauseTime      = 500 #ms; time paused after movement before ablation
feedRate       = 500 #movement speed

# Rectangle size properties
rectLength     = 4 #mm; x-direction
rectWidth      = 4 #mm; y-direction
spaceSmall     = 3 #mm; space between rectangles
hexLength      = 0.750 #mm

#Other
relative       = 0 #0 for homing before beginning.  1 if machine has already been homed
cleanTrigger	= 100 #number of rows between laser head cleanings