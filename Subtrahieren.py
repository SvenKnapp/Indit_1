strZahl1 = input("Eingabe 1.Zahl: ")
floatZahl1 = float(strZahl1)
strZahl2 = input("Eingabe 2.Zahl ")
floatZahl2 = float(strZahl2)

#Subtrahierung kleine Zahl von großer

if floatZahl1 > floatZahl2:
    floatDifferenz = floatZahl1 - floatZahl2
    floatNegDifferenz = floatZahl2 - floatZahl1
    print("Differenz: ", floatDifferenz)
    print("Differenz: ", floatNegDifferenz)
elif floatZahl2 > floatZahl1:
    floatDifferenz = floatZahl2 - floatZahl1
    floatNegDifferenz = floatZahl1 - floatZahl2
    print("Differenz: ", floatDifferenz)
    print("Differenz: ", floatNegDifferenz)
else:
    print("Differenz ist Null") 
