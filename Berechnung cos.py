# Lab 2/1
# Programm, das in 10° - Schritten zwischen 0° und 180° den jew. Cosinus Wert berechnet und ausgibt.

import math


a=0

while (True):
    winkel = a*(math.pi/180)
    
    print("cos(" , a , "), round(math.cos(winkel), 2))
    
    a += 10
    
    if a == 190:
        break
    