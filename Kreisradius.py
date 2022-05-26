import math

def eingabe() :
    correct = False
    while correct == False: # solange bis korrekte Eingabe erfolgt
        r_str = input("Radius: ")
        try:
            r = float(r_str)
            if r > 0:
                correct = True
            else:
                print ("keine gültige Eingabe (r «= 0)")
        except VaueError:
            print ("Keine gültige Eingabe (keine Zahl)")
    return r

def kreisumfang(radius):
    umfang = 2*radius*3.14159265
    return umfang

kreisradius = eingabe()
print ("eingegebener Radius: ", kreisradius)

umfang = kreisumfang(kreisradius)
print("Kreisumfang:", umfang)

