import time
from time import gmtime, strftime, localtime
import datetime
import config

f = config.f

def now():
	# now = strftime("%I:%M:%S %p", gmtime())
	now = strftime("%A, %B %d, %Y @ %I:%M:%S %p", localtime())
	return now

def header():
	f.writelines(";(***************uWellPlate******************)\n")
	f.writelines(";(*** " + str(now()) + " ***)\n")
	f.writelines("""G91 ; absolute coordinates
;(***************End of Beginning*********************)
""")

def closefile():
	f.writelines("""
;(end of the file, shutdown routines)
M3 S0 ; Laser PWM set to zero
""")
	f.close
