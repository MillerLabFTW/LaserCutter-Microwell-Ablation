from time import strftime, localtime

# Simple function to get current time and format as string
def now():
	# now = strftime("%I:%M:%S %p", gmtime())
	now = strftime("%A, %B %d, %Y @ %I:%M:%S %p", localtime())
	return now

# Write the heading for the G-Code file
def header(f):
	f.writelines(";(***************uWellPlate******************)\n")
	f.writelines(";(*** " + str(now()) + " ***)\n")
	f.writelines("""G91 ; relative coordinates
;(***************End of Beginning*********************)
""")

def closefile(f):
	f.writelines("""
;(end of the file, shutdown routines)
M3 S0 ; Laser PWM set to zero
""")
	f.close()


