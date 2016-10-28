#File
fname = 'Test1-3-3_10x10mm.gcode'
f=open(fname,'w')

#Laser Parameters
laserPower     = 20 #% max power
dwellTime      = 20 #ms
x_start        = 410
y_start        = 320
z_start        = 120.85 #mm above home
pauseTime      = 500 #ms; time paused after movement before ablation
feedRate       = 200 #movement speed

# Rectangle size properties
rectLength     = 10 #mm; x-direction
rectWidth      = 10 #mm; y-direction
spaceSmall     = 3 #mm; space between rectangles
hexLength      = 0.700 #mm

#Other
relative       = 0 #0 for homing before beginning.  1 if machine has already been homed
cleanTrigger	= 15 #number of rows between laser head cleanings