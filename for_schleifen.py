#for-Schleife
#for-Schleifen iterieren über eine iterierbare Objekte
#Was bedeutet das? Wir kennen z.B. Listen
#[0, 1, 2, 3, 4] darüber können wir mit einer for-Schleife laufen
#dabei wird jedes Listenelement nacheinander betrachtet

meine_Liste = [0, 1, 2, 3, 4]

for eintrag in meine_Liste:
    print(eintrag)
#hierbei haben wir eine Variable angelegt, hier: eintrag
#diese wird dann verwendet um in der Liste die Anweisung auszuführen

farben = ['rot', 'gruen', 'blau']
for farbe in farben:
    print(farbe)
#das Gleiche nur in gruen


user_input_range = int(input("Range angeben: "))
for zaehler in range (0, user_input_range + 1 ):
    print(f"Der {zaehler}. Durchlauf", end=" ")
#range erzeugt eine Sequenz von Zahlen
#range(5) erzeugt 0, 1, 2, 3, 4 -> Ende wird nie erreicht, es ist immer einer weniger!
#beginnt standardmäßig bei 0!
#es können auch startwerte eingegeben werden
#range(1,5) startet bei 1 und geht bis 4 -> 1, 2, 3, 4
#außerdem können anstatt ziffern auch variablen eingesetzt werden, z.B. von einem Userinput
#user_input_range = int(input("Range angeben: "))
#for zaehler in range (0, user_input_range + 1 ):
#    print(f"Der {zaehler}. Durchlauf", end=" ")

#Schrittweite bei range
for i in range (0, 10 , 2): # 0 2 4 6 8
    print(i, end=" ")
#anstatt nur +1 auf die Variable i am Ende der Schleife zu rechnen, nimmt er nun +2
print()
#das Ganze geht auch negativ
for i in range (10, 0 , -2):
    print(i, end=" ")
#syntax für range(start, stop, step)
#zählt von start bis stop-1 in schritten step
print()
#Strings sind auch iterierbare Objekte

for buchstabe in "Hallo Welt":
    print(buchstabe)