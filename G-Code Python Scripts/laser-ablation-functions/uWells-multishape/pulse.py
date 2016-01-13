import config
import writefile


## Parameters

#File
f = config.f

FOCUS			= config.FOCUS

#Laser Parameters
laserPower 		= config.laserPower
dwellTime     	= config.dwellTime
zValue			= [FOCUS-z for z in config.zValue]
x_start			= config.x_start
y_start			= config.y_start

pauseTime 		= config.pauseTime
feedRate        = config.feedRate
FOCUS			= config.FOCUS

# Rectangle size properties
rectLength 	= config.rectLength
rectWidth   = config.rectWidth
spaceSmall 	= config.spaceSmall
hex_pack	= config.hexLength

# Other Parameters
#relative   	= config.relative

def check_Conditions(laser, dwell, z):
	if len(laser) != len(dwell): return 0
	if len(laser) != len(z): return 0
	return len(laser)
	
def hex_pattern(hex_pack):
	global x_dist
	x_dist = float("{:.3f}".format(hex_pack))
	global y_dist
	y_dist = float("{:.3f}".format(hex_pack * (3**0.5) / 2))
	y_dist = x_dist
	return
	
def formatFloat(fl):
	fl = float(fl)
	fl = float("{:.3f}".format(fl))
	return fl

def gcode_move(x_move, y_move):
	x_move = formatFloat(x_move)
	y_move = formatFloat(y_move)
	f.writelines("G0 X" + str(x_move) + " Y" + str(y_move) + " F1000\n")
	f.writelines("G4 P" + str(pauseTime) + "\n")

def gcode_rectangle(dwellTime, laserPower, conditions):
	x_total = 0
	y_total = 0
	flag = -1
	pulseDist = formatFloat(1 / (conditions * x_dist))
	while y_total < rectWidth:
		f.writelines("G1 X" + str(-1*rectLength) + " S" + str(laserPower) + " L" + str(dwellTime*1000) + " P" + str(pulseDist) + " F" + str(feedRate) + " B1\n") 
		#f.writelines("M3 S0\n")
		x_total -= rectLength
		
		x_overhang = flag * x_dist/2
		gcode_move(rectLength + x_overhang, -1*y_dist)
		x_total += rectLength + x_overhang
		
		y_total += y_dist
		flag *= -1
		
		
	totals = [x_total, y_total]
	return totals
	

def writeGCODE():
	
	conditions 	= check_Conditions(laserPower, dwellTime, zValue)
	if conditions == 0: quit()
	
	#Hexagonal packing distances
	hex_pattern(hex_pack)
	
	## Write GCODE file
	writefile.header(f)
	
	f.writelines("M3 S0\n") ## Laser Off
	f.writelines("G28\n") ## Home axes
	
	for i in range(0,conditions):
		f.writelines("G90\n")
		f.writelines("M3 S0\n") ## Laser Off
		f.writelines("G0 X" + str(x_start-x_dist*i) + " Y" + str(y_start) + " F2000\n") # Move to x and y-axis start
		f.writelines("G0 Z" + str(zValue[i]) + " F300\n") ##Move to z-axis position
		f.writelines("G91\n")
	
		## Print Squares
		x_grid = 0
		y_grid = 0
		
		x_move = 0
		y_move = 0
	
		gcode_move(x_move, y_move)
	
		totals = gcode_rectangle(dwellTime[i], laserPower[i], conditions)
		x_move = totals[0] - rectLength - spaceSmall 
		y_move = totals[1]
	
		x_grid += rectLength + spaceSmall
		
		gcode_move(x_move + x_grid, y_move - rectWidth - spaceSmall)
		x_grid = 0
		y_grid += rectWidth + spaceSmall
	
	writefile.closefile(f)

def main():
	writeGCODE()

if __name__ == '__main__': main()
	
	
	
	




