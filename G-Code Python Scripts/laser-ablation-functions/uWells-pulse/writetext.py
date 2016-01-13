##### NEED TO FIX DIVISION OPERATOR!!!!!
from __future__ import division
#http://docs.python.org/release/2.2.3/whatsnew/node7.html
#The most controversial change in Python 2.2 heralds the start of an effort to fix an old design flaw that's been in Python from the beginning. Currently Python's division operator, /, behaves like C's division operator when presented with two integer arguments: it returns an integer result that's truncated down when there would be a fractional part. For example, 3/2 is 1, not 1.5, and (-1)/2 is -1, not -0.5. This means that the results of divison can vary unexpectedly depending on the type of the two operands and because Python is dynamically typed, it can be difficult to determine the possible types of the operands.

import config
import charFuncs

#Array of characters with function names
charDict	= config.make_charDict()
blockWidth      = config.blockWidth
letterSpace     = config.letterSpace

def print_letter(x_pos, y_pos, char):
	# Check if letter is valid
	if not (char in charDict):
		return 0
	
	#evaluate function from charFuncs.py module
	funcName = charDict[char]
	eval(funcName)(x_pos, y_pos)
	return 1


def print_line(x_pos, y_pos, line):
	#Split word into characters
	chars = list(line)
	
	#Print letters in order
	for char in chars:
		printCheck = print_letter(x_pos, y_pos, char)
		if not (printCheck):
			continue
		
		x_pos = charFuncs.new_letter(x_pos)
	
	return x_pos

def print_text(x_pos, y_pos, text):
	lines = text.split("\n")
	
	for line in lines:
		print_line(x_pos, y_pos, line)
		y_pos = charFuncs.new_line(y_pos)
	
	return y_pos

def text_distance(text):
        chars  = list(text)
        distance = 0

        for char in chars:
                if not (char in charDict):
                        continue
                distance += blockWidth + letterSpace

        return distance










	
	

















