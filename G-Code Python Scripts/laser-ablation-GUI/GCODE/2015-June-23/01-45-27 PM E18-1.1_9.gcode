;(***************uWellPlate******************)
;(*** Tuesday, June 23, 2015 @ 01:45:27 PM ***)
G91 ; absolute coordinates
;(***************End of Beginning*********************)
M3 S0
G90
M3 S0
G0 X393 Y313 F2000
G0 Z122.6 F300
G91
G0 X0.0 Y0.0 F1000
G4 P500
G1 X-5 S20.0 L4000 P1.333 F500 B1
G0 X4.625 Y-0.65 F1000
G4 P500
G1 X-5 S20.0 L4000 P1.333 F500 B1
G0 X5.375 Y-0.65 F1000
G4 P500
G1 X-5 S20.0 L4000 P1.333 F500 B1
G0 X4.625 Y-0.65 F1000
G4 P500
G1 X-5 S20.0 L4000 P1.333 F500 B1
G0 X5.375 Y-0.65 F1000
G4 P500
G1 X-5 S20.0 L4000 P1.333 F500 B1
G0 X4.625 Y-0.65 F1000
G4 P500
G1 X-5 S20.0 L4000 P1.333 F500 B1
G0 X5.375 Y-0.65 F1000
G4 P500
G1 X-5 S20.0 L4000 P1.333 F500 B1
G0 X4.625 Y-0.65 F1000
G4 P500
G1 X-5 S20.0 L4000 P1.333 F500 B1
G0 X5.375 Y-0.65 F1000
G4 P500
G0 X0.0 Y-2.8 F1000
G4 P500

;; Cleaning

M3 S0
G90
G0 X232 Y335 F1000
G4 P250
G0 Y255 F1000
G4 P250
G0 Y335 F1000
G4 P250
G0 X417.0 Y261.00000000000153 F1000
G4 P500
G91
;; Done Cleaning


;(end of the file, shutdown routines)
M3 S0 ; Laser PWM set to zero
