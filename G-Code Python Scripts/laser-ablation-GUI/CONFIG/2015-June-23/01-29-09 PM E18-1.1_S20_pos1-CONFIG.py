#File
fname = 'E18-1.1_S20_pos1.gcode'
f=open(fname,'w')

#Laser Parameters
laserPower     = 20 #% max power
dwellTime      = 4 #ms
x_start        = 405
y_start        = 333
z_start        = 122.60 #mm above home
pauseTime      = 500 #ms; time paused after movement before ablation
feedRate       = 500 #movement speed

# Rectangle size properties
rectLength     = 5 #mm; x-direction
rectWidth      = 5 #mm; y-direction
spaceSmall     = 3 #mm; space between rectangles
hexLength      = 0.600 #mm

#Other
relative       = 0 #0 for homing before beginning.  1 if machine has already been homed