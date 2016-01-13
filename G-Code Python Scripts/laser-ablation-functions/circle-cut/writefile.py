import time
from time import gmtime, strftime, localtime
import datetime
import config

f = config.f

def now():
	# now = strftime("%I:%M:%S %p", gmtime())
	now = strftime("%A, %B %d, %Y @ %I:%M:%S %p", localtime())
	return now

def openGcode():
	f.writelines(";(***************uWellPlate******************)\n")
	f.writelines(";(*** " + str(now()) + " ***)\n")
	f.writelines("""G90 ; absolute coordinates
;(***************End of Beginning*********************)
""")

def closeGcode():
	f.writelines("M3 S0 \n")
	f.writelines("""
;(end of the file, shutdown routines)
M127 ; Laser Off
M701 S0 ; Laser PWM set to zero
M84 ; motors off
""")
	f.close
