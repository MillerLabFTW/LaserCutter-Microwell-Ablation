#File 
fname = "5D1.gcode"
f = open(fname,"w")

#Laser Parameters
laserPowers     = [10] #% max power
dwellTimes      = [10] #ms
x_start			= 402
y_start			= 343
z_start         = 109.4 #mm above home
iterations      = 1
onTime          = 0 #ms
offTime         = 0 #ms; time between iterations
pauseTime       = 500 #ms; time paused after movement before ablation
feedRate        = 500 #movement speed

# Rectangle size properties
rectLength      = 40 #mm; x-direction
rectWidth       = 40 #mm; y-direction
spaceSmall      = 1 #mm; space between rectangles
spaceLarge      = 1 #mm
hexLength       = 0.25 #mm

#Other
decimal         = 3 #number of decimal places for gcode
relative 		= 0 #1 for no starting x,y; 0 for using starting co-ordinates
inverse         = 0
cleanWellCheck  = 100000



#Block Parameters
blockRatio 		= 1.5 	# width to length
blockHeight 	= 0.9	# mm
blockWidth	= blockHeight/blockRatio

#Spacing Parameters
letterSpace     = 0.25 #mm
wordSpace       = 1 #mm
lineSpace       = 0.35 #mm

#Text Laser Parameters
textfeedRate	= 1000	# mm/s
textlaserPower	= 27	# %max power
textpauseTime	= 500	# ms

#Other Text Parameters
upperAlphabet   = map(chr, range(65,91))
lowerAlphabet   = map(chr, range(97,123))
numbers         = range(0,10)


def make_charDict():
    charDict = {}
    for letter in upperAlphabet:
        funcName = "charFuncs.letter" + letter
        charDict[letter] = funcName
    
    for letter in lowerAlphabet:
        upperLetter = letter.upper()
        funcName = "charFuncs.letter" + upperLetter
        charDict[letter] = funcName
    
    for number in numbers:
        funcName = "charFuncs.number" + str(number)
        charDict[str(number)] = funcName

    charDict[" "] = "charFuncs.space"
    charDict[":"] = "charFuncs.colon"
    charDict["-"] = "charFuncs.dash"
    charDict["/"] = "charFuncs.slash"
    
    return charDict
