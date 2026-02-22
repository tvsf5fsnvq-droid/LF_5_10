# Bislang haben wir immer Code geschrieben und dieser wird maximal einmal ausgeführt
# Schleifen wiederholen einen bestimmten Codeblock nach bestimmten Kriterien
# Es gibt zwei Arten von Schleifen: while und for

# while - solange

while True:
    # klassische Endlosschleife
    # while überprüft die Bedingung, die dahintersteht auf Wahrheit (True)
    # solange die Bedingung wahr (True) ist, wird der Codeblock, der darunter eingerückt ist, ausgeführt
    # Immer und immer und immer und immer wieder
    text = input("Eingabe: ")
    print("Du hast geschrieben:", text)


# Um Schleifen abzubrechen, kann der Befehl break verwendet werden

    while True:

    # wie auch bei if-elif-else haben wir hier mit Einrückungen zu arbeiten
        text = input("Eingabe (drücke q zum Beenden): ")

    # Eingerückter Code gilt für den jeweiligen Befehl oben
        if text == 'q':

            break

        #als eine weitere Verschachtelung muss der Code dann zweimal eingerückt werden, damit er zum if zählt
        print("Du hast geschrieben:", text)

print("Der Code geht weiter....")



zaehler = 0
while zaehler < 5:
    print(f"Der {zaehler}. Durchlauf")
    zaehler += 1 # -> zaehler = zaehler +1, ein sogeanntes Inkrement
                 #zaehler++ in anderen Programmiersprachen
print(f"{zaehler} ist nicht mehr < 5")