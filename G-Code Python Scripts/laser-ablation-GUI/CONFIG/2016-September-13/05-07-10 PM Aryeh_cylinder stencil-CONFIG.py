#File
fname = 'Aryeh_cylinder stencil.gcode'
f=open(fname,'w')

#Laser Parameters
laserPower     = 16 #% max power
dwellTime      = 8 #ms
x_start        = 405
y_start        = 330
z_start        = 123.90 #mm above home
pauseTime      = 500 #ms; time paused after movement before ablation
feedRate       = 250 #movement speed

# Rectangle size properties
rectLength     = 45 #mm; x-direction
rectWidth      = 45 #mm; y-direction
spaceSmall     = 3 #mm; space between rectangles
hexLength      = 3.000 #mm

#Other
relative       = 0 #0 for homing before beginning.  1 if machine has already been homed
cleanTrigger	= 20 #number of rows between laser head cleanings