#File
fname = 'Massey_cylinders1_40x40mm.gcode'
f=open(fname,'w')

#Laser Parameters
laserPower     = 25 #% max power
dwellTime      = 20 #ms
x_start        = 420
y_start        = 345
z_start        = 123.90 #mm above home
pauseTime      = 2000 #ms; time paused after movement before ablation
feedRate       = 150 #movement speed

# Rectangle size properties
rectLength     = 40 #mm; x-direction
rectWidth      = 40 #mm; y-direction
spaceSmall     = 3 #mm; space between rectangles
hexLength      = 3.000 #mm

#Other
relative       = 0 #0 for homing before beginning.  1 if machine has already been homed
cleanTrigger	= 50 #number of rows between laser head cleanings