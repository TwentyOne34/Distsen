# Distsen
Works with a HC-SR04 distance sensor and Raspbarry Pi. Turns on and off the screen.

Makes a measurement of 125 Centimeters, detects anything under the 125 Cm and it will be seen as a hit.
The hit will let the display stay or turn on for a maximum of 2 hours.

Turns screen on if someone walks trough the sensor's measurement.

Turns screen off if there are none measurement changes after 2 hours. 

To run, type in shell/terminal: screen Python2.7 Distsen.py
