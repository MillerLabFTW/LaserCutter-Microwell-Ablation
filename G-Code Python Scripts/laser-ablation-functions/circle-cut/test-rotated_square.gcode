;(***************uWellPlate******************)
;(*** Wednesday, November 12, 2014 @ 03:59:06 PM ***)
G90 ; absolute coordinates
;(***************End of Beginning*********************)
M3 S0
G0 X406 Y331 F2000
G0 Z124.1 F300
M3 S0
G0 X413.071 Y338.071 F1000
G4 P500
M649 S13 B0
G1 X398.929 Y338.071 F500
G1 X398.929 Y323.929 F500
G1 X413.071 Y323.929 F500
G1 X413.071 Y338.071 F500
M3 S0
M3 S0
G0 X406.0 Y331.0 F1000
G4 P500
G0 Z109.1 F300
M3 S0 

;(end of the file, shutdown routines)
M127 ; Laser Off
M701 S0 ; Laser PWM set to zero
M84 ; motors off
