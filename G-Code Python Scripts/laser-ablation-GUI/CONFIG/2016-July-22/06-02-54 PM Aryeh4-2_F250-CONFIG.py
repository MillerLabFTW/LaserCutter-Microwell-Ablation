#File
fname = 'Aryeh4-2_F250.gcode'
f=open(fname,'w')

#Laser Parameters
laserPower     = 30 #% max power
dwellTime      = 15 #ms
x_start        = 405
y_start        = 330
z_start        = 123.90 #mm above home
pauseTime      = 500 #ms; time paused after movement before ablation
feedRate       = 100 #movement speed

# Rectangle size properties
rectLength     = 8 #mm; x-direction
rectWidth      = 8 #mm; y-direction
spaceSmall     = 3 #mm; space between rectangles
hexLength      = 0.600 #mm

#Other
relative       = 0 #0 for homing before beginning.  1 if machine has already been homed
cleanTrigger	= 15 #number of rows between laser head cleanings