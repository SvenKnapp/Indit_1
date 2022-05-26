#Schreiben Sie ein Programm, das auf 2 möglichen Versionen, die in der Liste angeführten Personen begrüßt.
#z.B."Hallo Peter"
#
#Version 1: forSchleife im Hauptprogramm, Ausgabe der Begrüßung in einem Unterprogramm
#
#Version2: forSchleife und Ausgabe der BEgrüßung in einem Unterprogramm

namen = ["Mateo", "Hannah", "Juna", "Mila", "Thiago"]

def begruessung(name):
    print("Hola ", name)
    print("Estoy feliz de verte!")
    print("Diviertete con el programa!")
    
def begruessung2(namensliste):
    for ein_name in namensliste:
        print("Hola ", name)
        print("Estoy feliz de verte!")
        print("Diviertete con el programa!")
        
print("Version 1")
for name in namen:
    begruessung(name)

print("Version 2")
begruessung2(namen) 