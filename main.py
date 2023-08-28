print("Moin, wir werden jetzt ganz einfach gemeinsam berechnen wie viele Kalorienen du brauchsts ")
geschlecht = input("Welches Biologisches Geschlecht hast du? [M oder W]")
größe = int(input("Wie Groß bist du? (in CM)"))
gewicht = int(input("Wie viel wiegst du? (in KG)"))
alter = int(input("Wie alt bist dU?"))
textbewegung = "So jetzt stellt sich noch die Frage wie du dich am Laufen hälst:\n" \
               "1. Sedentär (kaum bis gar keine Bewegung)\n" \
               "2. Leicht aktiv (leichte Bewegung/Sport 1-3 Tage pro Woche)\n" \
               "3. Moderat aktiv (Sport 3-5 Tage pro Woche)\n" \
               "4. Sehr aktiv (intensiver Sport 6-7 Tage pro Woche)\n" \
               "5. Super aktiv (schweres Training, physische Arbeit oder Training mehrmals täglich)\n"
print(textbewegung)

Bewegungen = int(input(" Wie viel Spoort machst du? 1, 2, 3, 4, 5"))

optionen = {
    1: 1.2,
    2: 1.375,
    3: 1.55,
    4: 1.725,
    5: 1.9
}

if geschlecht == "M":
    RMBMR = 88.362 + (13.397 * gewicht) + (4.799 * größe) - (5.677 * alter)
    MBMR = RMBMR * optionen
    print(f"Du solltest {MBMR} Kalorien am Tag zu dir nehmen.")

elif geschlecht == "W":
    RWBMR = 447.593 + (9.247 * gewicht) + (3.098 * größe) - (4.330 * alter)
    WMBR = RWBMR * optionen
    print(f"Du solltest {WMBR} Kalorien am Tag zu dir nehmen.")

else:
    print("Ungültige Eingabe.")