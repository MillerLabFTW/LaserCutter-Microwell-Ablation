;(***************uWellPlate******************)
;(*** Tuesday, June 30, 2015 @ 05:27:36 PM ***)
G91 ; absolute coordinates
;(***************End of Beginning*********************)
M3 S0
G28
G0 X417 Y333 F2000
G0 Z122.6 F300
G0 X0.0 Y0.0 F1000
G4 P500
G1 X-5 S10.0 L4000 P1.0 F500 B1
G0 X4.5 Y-0.866 F1000
G4 P500
G1 X-5 S10.0 L4000 P1.0 F500 B1
G0 X5.5 Y-0.866 F1000
G4 P500
G1 X-5 S10.0 L4000 P1.0 F500 B1
G0 X4.5 Y-0.866 F1000
G4 P500
G1 X-5 S10.0 L4000 P1.0 F500 B1
G0 X5.5 Y-0.866 F1000
G4 P500
G1 X-5 S10.0 L4000 P1.0 F500 B1
G0 X4.5 Y-0.866 F1000
G4 P500
G1 X-5 S10.0 L4000 P1.0 F500 B1
G0 X5.5 Y-0.866 F1000
G4 P500
G0 X0.0 Y-2.804 F1000
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
G0 X417.0 Y301.0000000000006 F1000
G4 P500
G91
;; Done Cleaning


;(end of the file, shutdown routines)
M3 S0 ; Laser PWM set to zero