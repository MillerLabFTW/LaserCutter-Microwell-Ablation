#File
fname = 'Aryeh4-2_30x30mm.gcode'
f=open(fname,'w')

#Laser Parameters
laserPower     = 16 #% max power
dwellTime      = 8 #ms
x_start        = 410
y_start        = 335
z_start        = 123.90 #mm above home
pauseTime      = 500 #ms; time paused after movement before ablation
feedRate       = 250 #movement speed

# Rectangle size properties
rectLength     = 30 #mm; x-direction
rectWidth      = 30 #mm; y-direction
spaceSmall     = 3 #mm; space between rectangles
hexLength      = 0.600 #mm

#Other
relative       = 0 #0 for homing before beginning.  1 if machine has already been homed
cleanTrigger	= 15 #number of rows between laser head cleanings