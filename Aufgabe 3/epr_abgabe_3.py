__author__ = "Chris"

import eprtools
from datetime import datetime

# Abfrage, welches Programm ausgeführt werden soll
what_programm = input("Welches Programm willst du ausführen?\n" + 
                    "(1) Binär-Rechner\n(2)" + " Exam-Countdown\n" + 
                    "(3) Kursseiten öffnen\n(4) Password-Generator\n")

# zugriff auf die funktionen vom importierten Modul
while True:
    if what_programm == "1":
        decimal = int(input("Welche Dezimalzahl willst du in Binär" + 
                            " umwandeln?: "))
        print(eprtools.decimal_to_binary(decimal))
        break
    elif what_programm == "2":
        date = datetime.now()
        dt_string = date.strftime("%Y/%m/%d %H:%M")
        eprtools.exam_countdown(dt_string)
        break
    elif what_programm == "3":
        wcp = input("Welche Kursseite willst du öffnen?\n(1) EPR\n(2)" + 
                " LinADI\n(3) Dismod\n(4) GPR\n(5) STO\n")
        print(eprtools.open_course_page(wcp))
        break
    elif what_programm == "4":
        length = int(input("Wie lang soll dein Password sein?: "))
        print(eprtools.password_gen(length))
        break
    else:
        print("Eingabe ungültig.")
        what_programm = input("Welches Programm willst du ausführen?\n" +
                            "(1) Binär-Rechner\n(2)" + " Exam-Countdown\n" +
                            "(3) Kursseiten öffnen\n(4) Password-Generator\n")