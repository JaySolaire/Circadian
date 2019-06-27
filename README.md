#Circadian
Colors.py is a python program that can be used to control the Colors of an LED Light Strip connected to a Raspberry pi
It has the option to set the color to any one of the preprogrammed color choices simply by clicking on the box (or touching it with a Pi touch screen), or adjust the color by 10 RGB units at a time, or set it to automatically adjust the color based on the time of day. This would start out red at 8am, move to orange, yellow, then green/white during the day, blue in the evening, purple at 11pm and turn off at midnight. The transitions are smooth, and slow for the hour-based method but faster if the user wants to switch it to a specific color.
Requirements:
Python 3.4
Pigpiod
Pygame (for user interface)

A tutorial for the wire setup can be found at dordnung.de/raspberrypi-ledstrip/
