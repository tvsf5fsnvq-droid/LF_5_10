## Praktische Beispiel - Nutzereingabe mit timeout

# wir wollen vom Nutzer eine Eingabe fordern, wenn er zu lange braucht soll das Programm sich beenden
# Zeit für den Computer wird in unixzeit angebeben
# er zählt vom 1. Januar 1970 00:00:00 Uhr die Sekunden -> ganzzahliger Wert

import time
#mit import werden weitere Bibliotheken eingebunden, die über die normalen Funktionen von
#Python gehen. Diese sind aber so speziell, dass extra gesagt werden muss, dass sie mitverwendet werden
#sollen. Einige sind im Lieferumfang von Python enthalten, andere müssen gesondert installiert werden


#timeout von 10 sekunden
timeout = 10

#Zeitpunkt der letzten Eingabe, am Anfang start des Programms
letzte_aktion = time.time()
# time.time aus dem import time (weiter oben) gibt den aktuellen Zeitpunkt wieder

while True:
    eingabe = input("Bitte etwas eingeben: ")
    vergangene_Zeit = time.time() - letzte_aktion
    #Zeit seit Start des Programms oder der letzten Eingabe des Users
    letzte_aktion = time.time()
    #Zücksetzten der Zeit, damit der Unterschied zum Timeout erneut bestimmt werden kann

    if vergangene_Zeit > timeout:
        print("Zeitüberschreitung!")
        break

    if eingabe == 'X':
        break
    print("Eingabe war:", eingabe)