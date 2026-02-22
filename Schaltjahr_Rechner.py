# Schreiben Sie ein Programm, welches nach der Eingabe einer Jahreszahl ausgibt, ob es sich um ein Schaltjahr handelt oder
# nicht. Ein Jahr ist ein Schaltjahr, wenn die Jahreszahl durch 4 und nicht durch 100 teilbar ist. Ausnahme:
# Ein Jahr ist ein Schaltjahr, wenn es durch 4 und durch 100 teilbar und  durch 400 teilbar ist.

# Dictionary erstellen.
Schaltjahr = {}

from datetime import date

# Datum am Tag der Erstellung, des Programmes.
x = date(2025, 10, 28)
print(x)

print("-" * 40)

#Nutzereingabe einer Jahreszahl
BLAU = '\033[94m'      # Hellblau für Menü
GRUEN = '\033[92m'     # Grün für "Schaltjahr!"
ROT = '\033[91m'       # Rot für "Kein Schaltjahr!"
ENDE = '\033[0m'       # Setzt die Farbe zurück auf Standard
def schaltjahr_pruefen():

    while True:
        try:
            uyear_str = input("\nBitte geben Sie eine Jahreszahl (oder 'x' für Menu) ein: ")
            if uyear_str.lower() =='x':
                return

            uyear = int(uyear_str)

            if uyear % 400 == 0:
                print(f"{GRUEN}Es ist {uyear} ein Schaltjahr!{ENDE}")

            elif uyear % 100 == 0:
                print(f"{ROT}Es ist kein Schaltjahr!{ENDE}")

            elif uyear % 4 == 0:
                print(f"{GRUEN}Es ist ein Schaltjahr!{ENDE}")

            else:
                print(f"{ROT}Es ist kein Schaltjahr!{ENDE}")
        except ValueError:
            print(f"{ROT}Ungültige Eingabe. Bitte geben Sie eine ganze Jahreszahl oder 'x' ein.{ENDE}")
            
            
# Zeigt das Hauptmenu an und startet den Programmablauf
def haupt_menu():


    print("Willkommen beim Schaltjahr-Prüfer!")

    while True:
        print(f"\n{BLAU}--- Hauptmenu ---{ENDE}")
        print(f"1:{BLAU} Jahreszahl prüfen{ENDE}")
        print(f"2:{BLAU} Programm beenden{ENDE}")
        print(f"{BLAU}----------------{ENDE}")

        wahl = input("Ihre Wahl (1 oder 2): ")

        if wahl == '1':
            schaltjahr_pruefen()
        elif wahl == '2':
            print("Auf Wiedersehen!")
            break
        else:
            print("Ungültige Wahl. Bitte geben Sie '1' oder '2' ein.")


if __name__ == "__main__":
    haupt_menu()
