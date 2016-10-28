#File
fname = 'test.gcode'
f=open(fname,'w')

#Laser Parameters
laserPower     = 10 #% max power
dwellTime      = 10 #ms
x_start        = 1
y_start        = 1
z_start        = 115.2 #mm above home
pauseTime      = 500 #ms; time paused after movement before ablation
feedRate       = 210 #movement speed

# Rectangle size properties
rectLength     = 100 #mm; x-direction
rectWidth      = 100 #mm; y-direction
spaceSmall     = 3 #mm; space between rectangles
hexLength      = 10.000 #mm

#Other
relative       = 0 #0 for homing before beginning.  1 if machine has already been homed