# Schreiben Sie ein Programm, welches alle geraden Zahlen von 0 bis 20 ausgibt.
# Geben Sie mithilfe von Schleifen folgende Figur aus Sternen auf dem Bildschirm aus.
# Hinweis: Pro Schreibvorgang darf immer nur ein Stern geschrieben werden.

# * * * * * * *   7
#   * * * * *     5
#     * * *      3
#       *       1

# Schreiben Sie ein Programm, in das der Benutzer eine ganze Zahl eingibt und das
# im Anschluss die Fakultät dieser Zahl berechnet und ausgibt. Verwenden Sie keine
# Rekursion zur Lösung der Aufgabe.(Hinweis: 0!=1)

print("_", "Varitante 1", "_" * 40)

# Variante 1 um jeder zweite Zahl auf zu listen.
for i in range(0, 21, 2):
    print(i)
print("_", "Varitante 2", "_" * 40)

#Variante 2 um jeder zweite Zahl auf zu listen.
for i in range (0, 21):
    if i % 2 ==0:
        print(i)

print("_", "Pyramide", "_" * 40)


def zeichne_pyramide():
    max_sterne = 7
    # Wir definieren die Anzahl der Sterne pro Zeile
    anzahl_sterne_pro_zeile = (7, 5, 3, 1)

    for sterne_aktuell in anzahl_sterne_pro_zeile:
        # Wir rücken pro "fehlendem" Stern zwei Leerzeichen ein,
        # da ein Stern inklusive Leerzeichen ('* ') zwei Zeichen breit ist.
        anzahl_leerraum = max_sterne - sterne_aktuell

        # Teil A: Einrücken (Leerraum am Zeilenanfang)
        print(' ' * anzahl_leerraum, end="")

        # Teil B: Sterne schreiben
        for i in range(sterne_aktuell):
            if i < sterne_aktuell - 1:
                print('* ', end="")  # Stern mit folgendem Leerzeichen
            else:
                print('*', end="")  # Letzter Stern ohne folgendes Leerzeichen

        # Teil C: Zeilenumbruch
        print()


zeichne_pyramide()
print("_" * 41)

def fakultät(n):
    if n < 0:
        return "Fakultät ist für negative Zahlen nicht definiert"
    elif n == 0:
        return 1
    else:
        ergebnis = 1
        for i in range(1, n + 1):
            ergebnis *= i
        return ergebnis


# Benutzereingabe
try:
    zahl = int(input("Geben Sie eine nicht-negative ganze Zahl ein: "))

    # Berechnung und Ausgabe der Fakultät
    ergebnis_fakultät = fakultät(zahl)
    print(f"Die Fakultät von {zahl} ist {ergebnis_fakultät}")

except ValueError:
    print("Ungültige Eingabe. Bitte geben Sie eine ganze Zahl ein.")
print("_" * 40)
