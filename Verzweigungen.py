# Verzweigungen in Python
# if - elif - else

erste_Zahl = 12
if erste_Zahl > 10: #Abgleich mit einem boolschen Wert (true / false), nur bei true gehts in die Einrückung
    # Wenn die Zahl größer als 10 ist, wird diese Zeile ausgeführt
    # 12 > 10 ist wahr, also wird auf der Konsole u.A. "Anweisungsblock 1" ausgegeben
    print("Anweisungsblock 1")
    #Es können beliebig viele Zeilen in dem eingerückten Bereich stehen
    print("Anweisungsblock 1.2")
#Dieser Bereich ist nicht mehr eingerückt und zählt damit nicht mehr zur if-Bedingung
#Das heißt, diese Zeile wird IMMER ausgeführt, unabhängig von der Zahl oben
print("Anweisungsblock 2")

if erste_Zahl > 100:
    # Wenn die Zahl größer als 100 ist, wird diese Zeile ausgeführt
    # 12 > 100 ist falsch, also wird auf der Konsole nichts ausgegeben
    print("Anweisungsblock 3")
#Dieser Bereich ist nicht mehr eingerückt und zählt damit nicht mehr zur if-Bedingung
#Das heißt, diese Zeile wird IMMER ausgeführt, unabhängig von der Zahl oben
print("Anweisungsblock 4")


#Mehrere Bedingungen hintereinander
alter = int(input("Gib dein Alter ein: "))
#input ist immer string, wenn nicht anders deklariert
if alter >= 18:
    print("Du bist volljährig.")
elif alter >=16:
    #elif ist kurz für else if, eine Folgebedingung
    #Dieser Bereich wird nur ausgeführt, wenn wir oben im if ein false haben
    #Wenn wir ein true haben, wird dieser Bereich übersprungen
    #Wird genau gleich behandelt wie ein if, braucht aber vorher ein if
    print("Du bist fast volljährig, Landtagswahlen sind ok.")
else:
    #Wenn kein vorheriges if oder elif wahr ist, wird dieser Codeblock ausgeführt
    print("Du bist minderjährig")
#if-elif-else wäre ein zusammenhängender if loop
#mehrere if loops untereinander sind jeweils separate loops
#es müssen nicht immer nach jedem if ein elif oder ein else kommen


#Schreibe ein Programm, das eine Zahl liest und ausgibt, ob sie positiv, negativ oder null ist.

user_input = float(input("Gib eine Zahl ein: "))
if user_input > 0 :
    print("Die Zahl ist positiv")
elif user_input < 0:
    print("Die Zahl ist negativ")
else:
    print("Die Zahl ist 0.")

#and - und
#hier gilt:
#True and True ist True
#True and False ist False
#False and True ist False
#False and False ist False
#and = alle aussagen müssen Wahr sein

#or - oder
#hier gilt:
#True or True ist True
#True or False ist True
#False or True ist True
#False or False ist False
#or = eine aussage muss Wahr sein

#not - nicht
#hier gilt:
#not True zu False
#not False zu True
#not = das gegenteil der Aussage wird geprüft


#Pattern matching in Python
#effizientere if bedingungen
#Syntax: match / case

#Abgleich mit vorgefertigten Ergebnissen

wochentag = input("Gib den aktuellen Wochentag ein: ")
#Es gibt eine kleine feste Menge an erwarteten Ergebnissen
#Nun abgleichen der Eingabe mit den Ergebnissen

match wochentag:
    #Welche Variable wollen wir abgleichen -> wochentag
    case "Montag":
        print("Es ist der erste Tag der Woche.")
    case "Dienstag":
        print("Es ist der zweite Tag der Woche.")
    case "Mittwoch":
        print("it is wednesday my dudes.")
    case "Donnerstag":
        print("Es ist der vierte Tag der Woche.")
    case "Freitag":
        print("WOCHENENDE!!!! SAUFEN!!!!")
    case "Samstag":
        print("Es ist der erste Tag des Wochendes.")
    case "Sonntag":
        print("Oh ne, morgen ist wieder Montag... *Sad piano music*")
    case _: #sozusagen das else bei match/case, tritt ein, wenn keiner weiter oben eintritt
        print("Rechtschreibung überprüfen!!!")
#wie auch bei if-elif-else ist die Anzahl der Anweisungen pro case unbegrenzt