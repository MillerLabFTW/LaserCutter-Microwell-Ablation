##### NEED TO FIX DIVISION OPERATOR!!!!!
from __future__ import division
#http://docs.python.org/release/2.2.3/whatsnew/node7.html
#The most controversial change in Python 2.2 heralds the start of an effort to fix an old design flaw that's been in Python from the beginning. Currently Python's division operator, /, behaves like C's division operator when presented with two integer arguments: it returns an integer result that's truncated down when there would be a fractional part. For example, 3/2 is 1, not 1.5, and (-1)/2 is -1, not -0.5. This means that the results of divison can vary unexpectedly depending on the type of the two operands and because Python is dynamically typed, it can be difficult to determine the possible types of the operands.

import config

#File
f = config.f

#Block Parameters
blockHeight 	= config.blockHeight
blockWidth	= config.blockWidth

#Space Parameters
letterSpace	= config.letterSpace
wordSpace	= config.wordSpace
lineSpace	= config.lineSpace

#Laser Parameters
feedRate	= config.textfeedRate
laserPower	= config.textlaserPower
pauseTime	= config.textpauseTime

#Other
decimal 	= config.decimal


#Functions

def fl(number, decimal):
	flStr = "%0." + str(decimal) + "f"
	return float(flStr % number)

def move_position(x_pos, y_pos):
	x_pos = fl(x_pos, decimal)
	y_pos = fl(y_pos, decimal)
	f.writelines("G0 X" + str(x_pos) + " Y" + str(y_pos) + "\n")

def draw_line(x_line, y_line):
	x_line = fl(x_line, decimal)
	y_line = fl(y_line, decimal)
	f.writelines("M128 S" + str(laserPower) + " \n")
	f.writelines("G1 X" + str(x_line) + " Y" + str(y_line) + " F" + str(feedRate) + "\n")

def stop_laser():
	f.writelines("M128 S0\n")

def new_letter(x_curr):
	x_new = x_curr + blockWidth + letterSpace
	return x_new

def new_word(x_curr):
	x_new = x_curr + blockWidth + wordSpace
	return x_new

def new_line(y_curr):
	y_new = y_curr + blockHeight + lineSpace
	return y_new

#Number Definitions
def number1(x_start, y_start):
	#Move to first position
	x_letter = x_start + 1/6*blockWidth
	y_letter = y_start + blockHeight
	move_position(x_letter, y_letter)
	
	#Draw line to second position
	x_letter = x_start + 5/6*blockWidth
	y_letter = y_start + blockHeight
	draw_line(x_letter, y_letter)
	
	#Stop laser and move to third position
	stop_laser()
	x_letter = x_start + 1/2*blockWidth
	y_letter = y_start + blockHeight
	move_position(x_letter, y_letter)

	#Draw line to fourth position
	x_letter = x_start + 1/2*blockWidth
	y_letter = y_start
	draw_line(x_letter, y_letter)

	#Draw line to fifth position
	x_letter = x_start + 1/3*blockWidth
	y_letter = y_start + 1/8*blockHeight
	draw_line(x_letter, y_letter)

	#End Letter
	stop_laser()

def number2(x_start, y_start):
	#Move to first position
	x_letter = x_start
	y_letter = y_start
	move_position(x_letter, y_letter)
	
	#Draw line to second position
	x_letter = x_start + blockWidth
	y_letter = y_start
	draw_line(x_letter, y_letter)
	
	#Draw line to third position
	x_letter = x_start + blockWidth
	y_letter = y_start + 1/3*blockHeight
	draw_line(x_letter, y_letter)

	#Draw line to fourth position
	x_letter = x_start
	y_letter = y_start + blockHeight
	draw_line(x_letter, y_letter)

	#Draw line to fifth position
	x_letter = x_start + blockWidth
	y_letter = y_start + blockHeight
	draw_line(x_letter, y_letter)

	#End Letter
	stop_laser()

def number3(x_start, y_start):
	#Move to first position
	x_letter = x_start
	y_letter = y_start
	move_position(x_letter, y_letter)
	
	#Draw line to second position
	x_letter = x_start + blockWidth
	y_letter = y_start + 1/4*blockHeight
	draw_line(x_letter, y_letter)
	
	#Draw line to third position
	x_letter = x_start + 1/3*blockWidth
	y_letter = y_start + 1/2*blockHeight
	draw_line(x_letter, y_letter)

	#Draw line to fourth position
	x_letter = x_start + blockWidth
	y_letter = y_start + 3/4*blockHeight
	draw_line(x_letter, y_letter)

	#Draw line to fifth position
	x_letter = x_start
	y_letter = y_start + blockHeight
	draw_line(x_letter, y_letter)

	#End Letter
	stop_laser()

def number4(x_start, y_start):
	#Move to first position
	x_letter = x_start + 5/6*blockWidth
	y_letter = y_start + blockHeight
	move_position(x_letter, y_letter)
	
	#Draw line to second position
	x_letter = x_start + 5/6*blockWidth
	y_letter = y_start
	draw_line(x_letter, y_letter)
	
	#Draw line to third position
	x_letter = x_start
	y_letter = y_start + 1/2*blockHeight
	draw_line(x_letter, y_letter)

	#Draw line to fourth position
	x_letter = x_start + blockWidth
	y_letter = y_start + 1/2*blockHeight
	draw_line(x_letter, y_letter)

	#End Letter
	stop_laser()

def number5(x_start, y_start):
	#Move to first position
	x_letter = x_start + blockWidth
	y_letter = y_start
	move_position(x_letter, y_letter)
	
	#Draw line to second position
	x_letter = x_start
	y_letter = y_start
	draw_line(x_letter, y_letter)
	
	#Draw line to third position
	x_letter = x_start
	y_letter = y_start + 1/3*blockHeight
	draw_line(x_letter, y_letter)
	
	#Draw line to fourth position
	x_letter = x_start + blockWidth
	y_letter = y_start + 3/4*blockHeight
	draw_line(x_letter, y_letter)

	#Draw line to fifth position
	x_letter = x_start
	y_letter = y_start + blockHeight
	draw_line(x_letter, y_letter)

	#End Letter
	stop_laser()
	
def number6(x_start, y_start):
	#Move to first position
	x_letter = x_start + blockWidth
	y_letter = y_start
	move_position(x_letter, y_letter)
	
	#Draw line to second position
	x_letter = x_start
	y_letter = y_start
	draw_line(x_letter, y_letter)
	
	#Draw line to third position
	x_letter = x_start
	y_letter = y_start + blockHeight
	draw_line(x_letter, y_letter)
	
	#Draw line to fourth position
	x_letter = x_start + blockWidth
	y_letter = y_start + blockHeight
	draw_line(x_letter, y_letter)

	#Draw line to fifth position
	x_letter = x_start + blockWidth
	y_letter = y_start + 1/2*blockHeight
	draw_line(x_letter, y_letter)
	
	#Draw line to sixth position
	x_letter = x_start
	y_letter = y_start + 1/2*blockHeight
	draw_line(x_letter, y_letter)

	#End Letter
	stop_laser()
	
def number7(x_start, y_start):
	#Move to first position
	x_letter = x_start
	y_letter = y_start
	move_position(x_letter, y_letter)
	
	#Draw line to second position
	x_letter = x_start + blockWidth
	y_letter = y_start
	draw_line(x_letter, y_letter)
	
	#Draw line to third position
	x_letter = x_start + 1/3*blockWidth
	y_letter = y_start + blockHeight
	draw_line(x_letter, y_letter)
	
	#Stop laser and move to fourth position
	stop_laser()
	x_letter = x_start + 1/6*blockWidth
	y_letter = y_start + 1/2*blockHeight
	move_position(x_letter, y_letter)

	#Draw line to fifth position
	x_letter = x_start + 5/6*blockWidth
	y_letter = y_start + 1/2*blockHeight
	draw_line(x_letter, y_letter)

	#End Letter
	stop_laser()	
	
def number8(x_start, y_start):
	#Move to first position
	x_letter = x_start + 1/2*blockWidth
	y_letter = y_start
	move_position(x_letter, y_letter)
	
	#Draw line to second position
	x_letter = x_start + blockWidth
	y_letter = y_start + 1/4*blockHeight
	draw_line(x_letter, y_letter)
	
	#Draw line to third position
	x_letter = x_start
	y_letter = y_start + 3/4*blockHeight
	draw_line(x_letter, y_letter)
	
	#Draw line to fourth position
	x_letter = x_start + 1/2*blockWidth
	y_letter = y_start + blockHeight
	draw_line(x_letter, y_letter)

	#Draw line to fifth position
	x_letter = x_start + blockWidth
	y_letter = y_start + 3/4*blockHeight
	draw_line(x_letter, y_letter)

	#Draw line to sixth position
	x_letter = x_start
	y_letter = y_start + 1/4*blockHeight
	draw_line(x_letter, y_letter)

	#Draw line to seventh position
	x_letter = x_start + 1/2*blockWidth
	y_letter = y_start
	draw_line(x_letter, y_letter)

	#End Letter
	stop_laser()
	
def number9(x_start, y_start):
	#Move to first position
	x_letter = x_start + blockWidth
	y_letter = y_start + blockHeight
	move_position(x_letter, y_letter)
	
	#Draw line to second position
	x_letter = x_start + blockWidth
	y_letter = y_start
	draw_line(x_letter, y_letter)
	
	#Draw line to third position
	x_letter = x_start
	y_letter = y_start
	draw_line(x_letter, y_letter)
	
	#Draw line to fourth position
	x_letter = x_start
	y_letter = y_start + 1/3*blockHeight
	draw_line(x_letter, y_letter)

	#Draw line to fifth position
	x_letter = x_start + blockWidth
	y_letter = y_start + 1/3*blockHeight
	draw_line(x_letter, y_letter)
	
	#End Letter
	stop_laser()
	
def number0(x_start, y_start):
	#Move to first position
	x_letter = x_start
	y_letter = y_start + blockHeight
	move_position(x_letter, y_letter)
	
	#Draw line to second position
	x_letter = x_start
	y_letter = y_start
	draw_line(x_letter, y_letter)
	
	#Draw line to third position
	x_letter = x_start + blockWidth
	y_letter = y_start
	draw_line(x_letter, y_letter)
	
	#Draw line to fourth position
	x_letter = x_start + blockWidth
	y_letter = y_start + blockHeight
	draw_line(x_letter, y_letter)

	#Draw line to fifth position
	x_letter = x_start
	y_letter = y_start + blockHeight
	draw_line(x_letter, y_letter)

	#Draw line to sixth position
	x_letter = x_start + blockWidth
	y_letter = y_start
	draw_line(x_letter, y_letter)
	
	#End Letter
	stop_laser()




#Symbol Definitions
def space(x_pos, y_pos):
	return 1

def colon(x_start, y_start):
	#Move to first position
	x_letter = x_start + 1/2*blockWidth
	y_letter = y_start + 5/18*blockHeight
	move_position(x_letter, y_letter)
	
	#draw small line
	x_letter = x_start + 1/2*blockWidth
	y_letter = y_start + 7/18*blockHeight
	draw_line(x_letter, y_letter)
	
	# Move to second position
	stop_laser()
	x_letter = x_start + 1/2*blockWidth
	y_letter = y_start + 11/18*blockHeight
	move_position(x_letter, y_letter)
	
	#draw small line
	x_letter = x_start + 1/2*blockWidth
	y_letter = y_start + 13/18*blockHeight
	draw_line(x_letter, y_letter)
	
	#Stop laser
	stop_laser()
	
def dash(x_start, y_start):
	#Move to first position
	x_letter = x_start + 1/8*blockWidth
	y_letter = y_start + 1/2*blockHeight
	move_position(x_letter, y_letter)
	
	#draw small line
	x_letter = x_start + 7/8*blockWidth
	y_letter = y_start + 1/2*blockHeight
	draw_line(x_letter, y_letter)
	
	#Stop Laser
	stop_laser()

def slash(x_start, y_start):
        #Move to first position
	x_letter = x_start
	y_letter = y_start + blockHeight
	move_position(x_letter, y_letter)
	
	#draw small line
	x_letter = x_start + blockWidth
	y_letter = y_start
	draw_line(x_letter, y_letter)
	
	#Stop Laser
	stop_laser()


#Letter Definitions
def letterA(x_start, y_start):
	#Move to first position
	x_letter = x_start
	y_letter = y_start + blockHeight
	move_position(x_letter, y_letter)
	
	#Draw line to second position
	x_letter = x_start + blockWidth/2
	y_letter = y_start
	draw_line(x_letter, y_letter)
	
	#Draw line to third position
	x_letter = x_start + blockWidth
	y_letter = y_start + blockHeight
	draw_line(x_letter, y_letter)
	
	#Stop Laser and move to fourth position
	stop_laser()
	slope = -blockHeight/(blockWidth/2)
	x_letter = x_start + blockWidth/4
	y_letter = y_start + blockWidth/4*slope + blockHeight
	move_position(x_letter, y_letter)
	
	#Draw line to fifth position
	slope = blockHeight/(blockWidth/2)
	x_letter = x_start + 3/4*blockWidth
	draw_line(x_letter, y_letter)
	
	#End Letter
	stop_laser()

def letterB(x_start, y_start):
	#Move to first position
	x_letter = x_start
	y_letter = y_start
	move_position(x_letter, y_letter)
	
	#Draw line to second position
	x_letter = x_start + 2/3*blockWidth
	y_letter = y_start + 1/4*blockHeight
	draw_line(x_letter, y_letter)
	
	#Draw line to third position
	x_letter = x_start
	y_letter = y_start + blockHeight/2
	draw_line(x_letter, y_letter)
	
	#Draw line to fourth position
	x_letter = x_start + 3/4*blockWidth
	y_letter = y_start + 3/4*blockHeight
	draw_line(x_letter, y_letter)
	
	#Draw line to fifth position
	x_letter = x_start
	y_letter = y_start + blockHeight
	draw_line(x_letter, y_letter)
	
	#Draw line to Sixth position
	x_letter = x_start
	y_letter = y_start
	draw_line(x_letter, y_letter)
	
	#End Letter
	stop_laser()

def letterC(x_start, y_start):
	#Move to first position
	x_letter = x_start + blockWidth
	y_letter = y_start
	move_position(x_letter, y_letter)
	
	#Draw line to second position
	x_letter = x_start + 1/4*blockWidth
	y_letter = y_start
	draw_line(x_letter, y_letter)
	
	#Draw line to third position
	x_letter = x_start
	y_letter = y_start + 1/4*blockHeight
	draw_line(x_letter, y_letter)
	
	#Draw line to fourth position
	x_letter = x_start
	y_letter = y_start + 3/4*blockHeight
	draw_line(x_letter, y_letter)

	#Draw line to fifth position
	x_letter = x_start + 1/4*blockWidth
	y_letter = y_start + blockHeight
	draw_line(x_letter, y_letter)

	#Draw line to sixth position
	x_letter = x_start + blockWidth
	y_letter = y_start + blockHeight
	draw_line(x_letter, y_letter)

	#End Letter
	stop_laser()
	
def letterD(x_start, y_start):
	#Move to first position
	x_letter = x_start
	y_letter = y_start
	move_position(x_letter, y_letter)
	
	#Draw line to second position
	x_letter = x_start + blockWidth
	y_letter = y_start + blockHeight
	draw_line(x_letter, y_letter)
	
	#Draw line to third position
	x_letter = x_start
	y_letter = y_start + blockHeight
	draw_line(x_letter, y_letter)
	
	#Draw line to fourth position
	x_letter = x_start
	y_letter = y_start
	draw_line(x_letter, y_letter)
	
	#End Letter
	stop_laser()
	
def letterE(x_start, y_start):
	#Move to first position
	x_letter = x_start + blockWidth
	y_letter = y_start
	move_position(x_letter, y_letter)
	
	#Draw line to second position
	x_letter = x_start
	y_letter = y_start
	draw_line(x_letter, y_letter)
	
	#Draw line to third position
	x_letter = x_start
	y_letter = y_start + blockHeight
	draw_line(x_letter, y_letter)

	#Draw line to fourth position
	x_letter = x_start + blockWidth
	y_letter = y_start + blockHeight
	draw_line(x_letter, y_letter)
	
	#Stop laser and move to fifth position
	stop_laser()
	x_letter = x_start
	y_letter = y_start + 1/2*blockHeight
	move_position(x_letter, y_letter)
	
	#Draw line to fifth position
	x_letter = x_start + 2/3*blockWidth
	y_letter = y_start + 1/2*blockHeight
	draw_line(x_letter, y_letter)
	
	#End Letter
	stop_laser()

def letterF(x_start, y_start):
	#Move to first position
	x_letter = x_start + blockWidth
	y_letter = y_start
	move_position(x_letter, y_letter)
	
	#Draw line to second position
	x_letter = x_start
	y_letter = y_start
	draw_line(x_letter, y_letter)
	
	#Draw line to third position
	x_letter = x_start
	y_letter = y_start + blockHeight
	draw_line(x_letter, y_letter)
	
	#Stop laser and move to fourth position
	stop_laser()
	x_letter = x_start
	y_letter = y_start + 1/2*blockHeight
	move_position(x_letter, y_letter)
	
	#Draw line to fifth position
	x_letter = x_start + 1/2*blockWidth
	y_letter = y_start + 1/2*blockHeight
	draw_line(x_letter, y_letter)
	
	#End Letter
	stop_laser()

def letterG(x_start, y_start):
	#Move to first position
	x_letter = x_start + blockWidth
	y_letter = y_start
	move_position(x_letter, y_letter)
	
	#Draw line to second position
	x_letter = x_start + 1/4*blockWidth
	y_letter = y_start
	draw_line(x_letter, y_letter)
	
	#Draw line to third position
	x_letter = x_start
	y_letter = y_start + 1/4*blockHeight
	draw_line(x_letter, y_letter)
	
	#Draw line to fourth position
	x_letter = x_start
	y_letter = y_start + 3/4*blockHeight
	draw_line(x_letter, y_letter)

	#Draw line to fifth position
	x_letter = x_start + 1/4*blockWidth
	y_letter = y_start + blockHeight
	draw_line(x_letter, y_letter)

	#Draw line to sixth position
	x_letter = x_start + blockWidth
	y_letter = y_start + blockHeight
	draw_line(x_letter, y_letter)

	#Draw line to seventh position
	x_letter = x_start + blockWidth
	y_letter = y_start + 1/2*blockHeight
	draw_line(x_letter, y_letter)
	
	#Draw line to eighth position
	x_letter = x_start + 1/2*blockWidth
	y_letter = y_start + 1/2*blockHeight
	draw_line(x_letter, y_letter)

	#End Letter
	stop_laser()

def letterH(x_start, y_start):
	#Move to first position
	x_letter = x_start
	y_letter = y_start
	move_position(x_letter, y_letter)
	
	#Draw line to second position
	x_letter = x_start
	y_letter = y_start + blockHeight
	draw_line(x_letter, y_letter)
	
	#Stop laser and move to third position
	stop_laser()
	x_letter = x_start + blockWidth
	y_letter = y_start + blockHeight
	move_position(x_letter, y_letter)
	
	#Draw line to fourth position
	x_letter = x_start + blockWidth
	y_letter = y_start
	draw_line(x_letter, y_letter)
	
	#Stop laser and move to fifth position
	stop_laser()
	x_letter = x_start + blockWidth
	y_letter = y_start + 1/2*blockHeight
	move_position(x_letter, y_letter)
	
	#Draw line to sixth position
	x_letter = x_start
	y_letter = y_start + 1/2*blockHeight
	draw_line(x_letter, y_letter)
	
	#End Letter
	stop_laser()

def letterI(x_start, y_start):
	#Move to first position
	x_letter = x_start + 1/6*blockWidth
	y_letter = y_start
	move_position(x_letter, y_letter)
	
	#Draw line to second position
	x_letter = x_start + 5/6*blockWidth
	y_letter = y_start
	draw_line(x_letter, y_letter)
	
	#Stop laser and move to third position
	stop_laser()
	x_letter = x_start + 1/2*blockWidth
	y_letter = y_start
	move_position(x_letter, y_letter)
	
	#Draw line to fourth position
	x_letter = x_start + 1/2*blockWidth
	y_letter = y_start + blockHeight
	draw_line(x_letter, y_letter)
	
	#Stop laser and move to fifth position
	stop_laser()
	x_letter = x_start + 1/6*blockWidth
	y_letter = y_start + blockHeight
	move_position(x_letter, y_letter)
	
	#Draw line to sixth position
	x_letter = x_start + 5/6*blockWidth
	y_letter = y_start + blockHeight
	draw_line(x_letter, y_letter)
	
	#End Letter
	stop_laser()
	
def letterJ(x_start, y_start):
	#Move to first position
	x_letter = x_start + 1/6*blockWidth
	y_letter = y_start
	move_position(x_letter, y_letter)
	
	#Draw line to second position
	x_letter = x_start + 5/6*blockWidth
	y_letter = y_start
	draw_line(x_letter, y_letter)
	
	#Stop laser and move to third position
	stop_laser()
	x_letter = x_start + 1/2*blockWidth
	y_letter = y_start
	move_position(x_letter, y_letter)
	
	#Draw line to fourth position
	x_letter = x_start + 1/2*blockWidth
	y_letter = y_start + blockHeight
	draw_line(x_letter, y_letter)
	
	#Draw line to fifth position
	x_letter = x_start
	y_letter = y_start + blockHeight
	draw_line(x_letter, y_letter)
	
	#Draw line to sixth position
	x_letter = x_start
	y_letter = y_start + 2/3*blockHeight
	draw_line(x_letter, y_letter)

	#End Letter
	stop_laser()
	
def letterK(x_start, y_start):
	#Move to first position
	x_letter = x_start
	y_letter = y_start
	move_position(x_letter, y_letter)
	
	#Draw line to second position
	x_letter = x_start
	y_letter = y_start + blockHeight
	draw_line(x_letter, y_letter)
	
	#Stop laser and move to third position
	stop_laser()
	x_letter = x_start + blockWidth
	y_letter = y_start + blockHeight
	move_position(x_letter, y_letter)
	
	#Draw line to fourth position
	x_letter = x_start
	y_letter = y_start + 1/2*blockHeight
	draw_line(x_letter, y_letter)
	
	#Draw line to fifth position
	x_letter = x_start + blockWidth
	y_letter = y_start
	draw_line(x_letter, y_letter)
	
	#End Letter
	stop_laser()

def letterL(x_start, y_start):
	#Move to first position
	x_letter = x_start
	y_letter = y_start
	move_position(x_letter, y_letter)
	
	#Draw line to second position
	x_letter = x_start
	y_letter = y_start + blockHeight
	draw_line(x_letter, y_letter)
	
	#Draw line to third position
	x_letter = x_start + blockWidth
	y_letter = y_start + blockHeight
	draw_line(x_letter, y_letter)
	
	#End Letter
	stop_laser()
	
def letterM(x_start, y_start):
	#Move to first position
	x_letter = x_start
	y_letter = y_start + blockHeight
	move_position(x_letter, y_letter)
	
	#Draw line to second position
	x_letter = x_start
	y_letter = y_start
	draw_line(x_letter, y_letter)
	
	#Draw line to third position
	x_letter = x_start + 1/2*blockWidth
	y_letter = y_start + 1/3*blockHeight
	draw_line(x_letter, y_letter)
	
	#Draw line to fourth position
	x_letter = x_start + blockWidth
	y_letter = y_start
	draw_line(x_letter, y_letter)
	
	#Draw line to fifth position
	x_letter = x_start + blockWidth
	y_letter = y_start + blockHeight
	draw_line(x_letter, y_letter)
	
	#End Letter
	stop_laser()
	
def letterN(x_start, y_start):
	#Move to first position
	x_letter = x_start
	y_letter = y_start + blockHeight
	move_position(x_letter, y_letter)
	
	#Draw line to second position
	x_letter = x_start
	y_letter = y_start
	draw_line(x_letter, y_letter)
	
	#Draw line to third position
	x_letter = x_start + 3/4*blockWidth
	y_letter = y_start + blockHeight
	draw_line(x_letter, y_letter)
	
	#Draw line to fourth position
	x_letter = x_start + 3/4*blockWidth
	y_letter = y_start
	draw_line(x_letter, y_letter)
	
	#End Letter
	stop_laser()
	
def letterO(x_start, y_start):
	#Move to first position
	x_letter = x_start + 1/6*blockWidth
	y_letter = y_start
	move_position(x_letter, y_letter)
	
	#Draw line to second position
	x_letter = x_start + 5/6*blockWidth
	y_letter = y_start
	draw_line(x_letter, y_letter)
	
	#Draw line to third position
	x_letter = x_start + blockWidth
	y_letter = y_start + 1/8*blockHeight
	draw_line(x_letter, y_letter)
	
	#Draw line to fourth position
	x_letter = x_start + blockWidth
	y_letter = y_start + 7/8*blockHeight
	draw_line(x_letter, y_letter)
	
	#Draw line to fifth position
	x_letter = x_start + 5/6*blockWidth
	y_letter = y_start + blockHeight
	draw_line(x_letter, y_letter)
	
	#Draw line to sixth position
	x_letter = x_start + 1/6*blockWidth
	y_letter = y_start + blockHeight
	draw_line(x_letter, y_letter)
	
	#Draw line to seventh position
	x_letter = x_start
	y_letter = y_start + 7/8*blockHeight
	draw_line(x_letter, y_letter)
	
	#Draw line to eighth position
	x_letter = x_start
	y_letter = y_start + 1/8*blockHeight
	draw_line(x_letter, y_letter)

	#Draw line to ninth position
	x_letter = x_start + 1/6*blockWidth
	y_letter = y_start
	draw_line(x_letter, y_letter)

	#End Letter
	stop_laser()
	
def letterP(x_start, y_start):
	#Move to first position
	x_letter = x_start
	y_letter = y_start + blockHeight
	move_position(x_letter, y_letter)
	
	#Draw line to second position
	x_letter = x_start
	y_letter = y_start
	draw_line(x_letter, y_letter)
	
	#Draw line to third position
	x_letter = x_start + blockWidth
	y_letter = y_start + 1/4*blockHeight
	draw_line(x_letter, y_letter)
	
	#Draw line to fourth position
	x_letter = x_start
	y_letter = y_start + 1/2*blockHeight
	draw_line(x_letter, y_letter)

	#End Letter
	stop_laser()
	
def letterQ(x_start, y_start):
	#Move to first position
	x_letter = x_start + 1/6*blockWidth
	y_letter = y_start
	move_position(x_letter, y_letter)
	
	#Draw line to second position
	x_letter = x_start + 5/6*blockWidth
	y_letter = y_start
	draw_line(x_letter, y_letter)
	
	#Draw line to third position
	x_letter = x_start + blockWidth
	y_letter = y_start + 1/8*blockHeight
	draw_line(x_letter, y_letter)
	
	#Draw line to fourth position
	x_letter = x_start + blockWidth
	y_letter = y_start + 7/8*blockHeight
	draw_line(x_letter, y_letter)
	
	#Draw line to fifth position
	x_letter = x_start + 5/6*blockWidth
	y_letter = y_start + blockHeight
	draw_line(x_letter, y_letter)
	
	#Draw line to sixth position
	x_letter = x_start + 1/6*blockWidth
	y_letter = y_start + blockHeight
	draw_line(x_letter, y_letter)
	
	#Draw line to seventh position
	x_letter = x_start
	y_letter = y_start + 7/8*blockHeight
	draw_line(x_letter, y_letter)
	
	#Draw line to eighth position
	x_letter = x_start
	y_letter = y_start + 1/8*blockHeight
	draw_line(x_letter, y_letter)

	#Draw line to ninth position
	x_letter = x_start + 1/6*blockWidth
	y_letter = y_start
	draw_line(x_letter, y_letter)
	
	#Stop laser and move to tenth position
	stop_laser()
	x_letter = x_start + 1/2*blockWidth
	y_letter = y_start + 1/2*blockHeight
	move_position(x_letter, y_letter)
	
	#Draw line to eleventh position
	x_letter = x_start + blockWidth
	y_letter = y_start + blockHeight
	draw_line(x_letter, y_letter)

	#End Letter
	stop_laser()
	
def letterR(x_start, y_start):
	#Move to first position
	x_letter = x_start
	y_letter = y_start + blockHeight
	move_position(x_letter, y_letter)
	
	#Draw line to second position
	x_letter = x_start
	y_letter = y_start
	draw_line(x_letter, y_letter)
	
	#Draw line to third position
	x_letter = x_start + blockWidth
	y_letter = y_start + 1/4*blockHeight
	draw_line(x_letter, y_letter)
	
	#Draw line to fourth position
	x_letter = x_start
	y_letter = y_start + 1/2*blockHeight
	draw_line(x_letter, y_letter)
	
	#Draw line to fifth position
	x_letter = x_start + blockWidth
	y_letter = y_start + blockHeight
	draw_line(x_letter, y_letter)

	#End Letter
	stop_laser()
	
def letterS(x_start, y_start):
	#Move to first position
	x_letter = x_start + blockWidth
	y_letter = y_start
	move_position(x_letter, y_letter)
	
	#Draw line to second position
	x_letter = x_start
	y_letter = y_start + 1/4*blockHeight
	draw_line(x_letter, y_letter)
	
	#Draw line to third position
	x_letter = x_start + blockWidth
	y_letter = y_start + 3/4*blockHeight
	draw_line(x_letter, y_letter)
	
	#Draw line to fourth position
	x_letter = x_start
	y_letter = y_start + blockHeight
	draw_line(x_letter, y_letter)

	#End Letter
	stop_laser()
	
def letterT(x_start, y_start):
	#Move to first position
	x_letter = x_start
	y_letter = y_start
	move_position(x_letter, y_letter)
	
	#Draw line to second position
	x_letter = x_start + blockWidth
	y_letter = y_start
	draw_line(x_letter, y_letter)
	
	#Stop laser and move to third position
	stop_laser()
	x_letter = x_start + 1/2*blockWidth
	y_letter = y_start
	move_position(x_letter, y_letter)
	
	#Draw line to fourth position
	x_letter = x_start + 1/2*blockWidth
	y_letter = y_start + blockHeight
	draw_line(x_letter, y_letter)

	#End Letter
	stop_laser()

def letterU(x_start, y_start):
	#Move to first position
	x_letter = x_start
	y_letter = y_start
	move_position(x_letter, y_letter)
	
	#Draw line to second position
	x_letter = x_start
	y_letter = y_start + 5/6*blockHeight
	draw_line(x_letter, y_letter)
	
	#Draw line to third position
	x_letter = x_start + 1/6*blockWidth
	y_letter = y_start + blockHeight
	draw_line(x_letter, y_letter)
	
	#Draw line to fourth position
	x_letter = x_start + 5/6*blockWidth
	y_letter = y_start + blockHeight
	draw_line(x_letter, y_letter)

	#Draw line to fifth position
	x_letter = x_start + blockWidth
	y_letter = y_start + 5/6*blockHeight
	draw_line(x_letter, y_letter)

	#Draw line to sixth position
	x_letter = x_start + blockWidth
	y_letter = y_start
	draw_line(x_letter, y_letter)
	
	#End Letter
	stop_laser()

def letterV(x_start, y_start):
	#Move to first position
	x_letter = x_start
	y_letter = y_start
	move_position(x_letter, y_letter)
	
	#Draw line to second position
	x_letter = x_start + 1/2*blockWidth
	y_letter = y_start + blockHeight
	draw_line(x_letter, y_letter)
	
	#Draw line to third position
	x_letter = x_start + blockWidth
	y_letter = y_start
	draw_line(x_letter, y_letter)
	
	#End Letter
	stop_laser()

def letterW(x_start, y_start):
	#Move to first position
	x_letter = x_start
	y_letter = y_start
	move_position(x_letter, y_letter)
	
	#Draw line to second position
	x_letter = x_start + 1/4*blockWidth
	y_letter = y_start + blockHeight
	draw_line(x_letter, y_letter)
	
	#Draw line to third position
	x_letter = x_start + 1/2*blockWidth
	y_letter = y_start + 3/4*blockHeight
	draw_line(x_letter, y_letter)

	#Draw line to fourth position
	x_letter = x_start + 3/4*blockWidth
	y_letter = y_start + blockHeight
	draw_line(x_letter, y_letter)

	#Draw line to fifth position
	x_letter = x_start + blockWidth
	y_letter = y_start
	draw_line(x_letter, y_letter)

	#End Letter
	stop_laser()

def letterX(x_start, y_start):
	#Move to first position
	x_letter = x_start
	y_letter = y_start
	move_position(x_letter, y_letter)
	
	#Draw line to second position
	x_letter = x_start + blockWidth
	y_letter = y_start + blockHeight
	draw_line(x_letter, y_letter)
	
	#Stop laser and move to third position
	stop_laser()
	x_letter = x_start
	y_letter = y_start + blockHeight
	move_position(x_letter, y_letter)

	#Draw line to fourth position
	x_letter = x_start + blockWidth
	y_letter = y_start
	draw_line(x_letter, y_letter)

	#End Letter
	stop_laser()

def letterY(x_start, y_start):
	#Move to first position
	x_letter = x_start
	y_letter = y_start
	move_position(x_letter, y_letter)
	
	#Draw line to second position
	x_letter = x_start + 1/2*blockWidth
	y_letter = y_start + 1/2*blockHeight
	draw_line(x_letter, y_letter)
	
	#Stop laser and move to third position
	stop_laser()
	x_letter = x_start
	y_letter = y_start + blockHeight
	move_position(x_letter, y_letter)

	#Draw line to fourth position
	x_letter = x_start + blockWidth
	y_letter = y_start
	draw_line(x_letter, y_letter)

	#End Letter
	stop_laser()

def letterZ(x_start, y_start):
	#Move to first position
	x_letter = x_start
	y_letter = y_start
	move_position(x_letter, y_letter)
	
	#Draw line to second position
	x_letter = x_start + blockWidth
	y_letter = y_start
	draw_line(x_letter, y_letter)
	
	#Draw line to third position
	x_letter = x_start
	y_letter = y_start + blockHeight
	draw_line(x_letter, y_letter)

	#Draw line to fourth position
	x_letter = x_start + blockWidth
	y_letter = y_start + blockHeight
	draw_line(x_letter, y_letter)

	#Stop laser and move to fifth position
	stop_laser()
	x_letter = x_start + 1/6*blockWidth
	y_letter = y_start + 1/2*blockHeight
	move_position(x_letter, y_letter)

	#Draw line to six position
	x_letter = x_start + 5/6*blockWidth
	y_letter = y_start + 1/2*blockHeight
	draw_line(x_letter, y_letter)

	#End Letter
	stop_laser()
