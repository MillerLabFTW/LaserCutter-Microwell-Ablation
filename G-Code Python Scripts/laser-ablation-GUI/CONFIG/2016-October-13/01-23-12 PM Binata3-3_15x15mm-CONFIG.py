#File
fname = 'Binata3-3_15x15mm.gcode'
f=open(fname,'w')

#Laser Parameters
laserPower     = 40 #% max power
dwellTime      = 35 #ms
x_start        = 414
y_start        = 335
z_start        = 118.10 #mm above home
pauseTime      = 2000 #ms; time paused after movement before ablation
feedRate       = 150 #movement speed

# Rectangle size properties
rectLength     = 15 #mm; x-direction
rectWidth      = 15 #mm; y-direction
spaceSmall     = 3 #mm; space between rectangles
hexLength      = 0.900 #mm

#Other
relative       = 0 #0 for homing before beginning.  1 if machine has already been homed
cleanTrigger	= 50 #number of rows between laser head cleanings