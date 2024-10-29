__author__ = "Chris"

import webbrowser
from datetime import datetime
import itertools
import random

def decimal_to_binary(dec) :
    """ 
    This function converts decimal numbers to binary code.
    Numbers have to be greater than 0 and may not be negative.
    Parameters:
        dec (has to be an integer): This is the number to be converted.
    Returns:
        bin (is a string): This is the converted binary code.
    """

    # Wandelt Dezimalzahl in Binärzahl um
    bin = ""
    while int(dec / 2) != 0:
        bin += str(dec % 2)
        dec = int(dec / 2)
        print(bin[:: - 1])
    return "1" + bin[:: - 1]


def exam_countdown(zeit): # Exam Countdown
    """
    This funtion show you, how many Days/Hours/Minutes are left until the Exam.
    Parameters:
        zeit (compares some time with the time of the incoming exam)
    Returns:
        None
    """
  
  
    # Den String in eine Liste von Ints zerteilen in dem Format 
    # [Jahr, Monat, Tag, Stunden, Minuten]
    epi = "2023/02/16 10:00"
    epi_list = epi.split("/") 
    epi_list = stringSplit(epi_list," ")
    epi_list = stringSplit(epi_list,":")
    epi = [int(i) for i in epi_list]
    zeit_list = zeit.split("/")
    zeit_list = stringSplit(zeit_list," ")
    zeit_list = stringSplit(zeit_list,":")
    zeit = [int(i) for i in zeit_list]
    months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    time = list(zip(zeit, epi)) # Tupel-Liste [(Input Jahr, EPI Jahr), 
                                # (Input Monat, EPI Monat), ...]
    minutes = 0
    minutes += time[4][1] - time[4][0] # Minuten Differenz berechnen
    minutes += 60 * (time[3][1] - time[3][0]) # Stunden Differenz berechnen
    # Monats Differenz berechnen
    if (time[1][1] < time[1][0]): # Der Fall wenn Klausur Termin vor dem 
                                  # eingegeben Monat stattfindet
        minutes -= 60 * 24 * (time[2][0])
        minutes -= 60 * 24 * (months[time[1][1]-1] - time[2][1])
        for i in range(time[1][1], time[1][0] - 1):
            minutes -= 60 * 24 * months[i]
    elif (time[1][1] > time[1][0]): # Wenn Klausur nach dem eingegeben 
                                    # Monat stattfindet
        minutes += 60 * 24 * (months[time[1][0] - 1] - time[2][0])
        minutes += 60 * 24 * (time[2][1])
        for i in range(time[1][0], time[1][1] - 1):
            print(i)
            minutes += 60 * 24 * months[i]
    else: # Wenn es derselbe Monat ist
        minutes += 60 * 24 * (time[2][1] - time[2][0])
    minutes += 60 * 24 * 365 * (time[0][1] - time[0][0]) # berechnet die 
                                                         # Jahresdifferenz
    for i in range(time[0][0], time[0][1]): # Schaltjahre miteinberechnen
        if i % 4 == 0:
            minutes += 60 * 24
    if time[0][1] % 4 == 0 and time[1][1] > 2: # Wenn die Klausur in einem 
                                               # Schaltjahr geschrieben wird 
                                               # und der Monat 
                                               # nach Februar kommt
        minutes += 60 * 24 

    # Minuten in Stunden und Tage Überführen
    hours = int(minutes / 60)
    minutes = minutes % 60
    days = int(hours / 24)
    hours = hours % 24

    print(f"EPI: {epi} \nNOW: {zeit}")
    print(f"{days} Tage, {hours} Stunden, {minutes} Minuten")

# Splittet alle Elemente einer Stringliste mit dem character


def stringSplit(txt_list, character): 


    for i, elem in enumerate(txt_list):
        txt_list[i] = str(elem).split(character) 
    return list(itertools.chain(*txt_list))

now = datetime.now()
dt_string = now.strftime("%Y/%m/%d %H:%M")
dt = "2023/11/21 10:00"


def open_course_page(what_course_page): # Kursseiten
    """
    This function opens your requested course page in the browser.
    Parameter:
        what_course_page (opens up course page depending what string you
        put in)
    Returns:
        True (if valid input) or False (if invalid input)
    """


    if what_course_page == "1":
        webbrowser.open_new("https://moodle.studiumdigitale.uni-frankfurt.de" + 
                            "/moodle/course/view.php?id=3292") # EPR
        return True
    elif what_course_page == "2":
        webbrowser.open_new("https://www.uni-frankfurt.de/125334408/" + 
                            "Lineare_Algebra_und_Diskrete_Mathematik_für_" + 
                            "die_Informatik__WS22_23?") # LinADI
        return True
    elif what_course_page == "3":
        webbrowser.open_new("https://ae.cs.uni-frankfurt.de/dismod22") # Dismod
        return True
    elif what_course_page == "4":
        webbrowser.open_new("https://moodle.studiumdigitale.uni-frankfurt.de" + 
                            "/moodle/course/view.php?id=3294") # GPR
        return True
    elif what_course_page == "5":
        webbrowser.open_new("https://moodle.studiumdigitale.uni-frankfurt.de" + 
                            "/moodle/course/view.php?id=3338") # STO
        return True
    else:
        print("Eingabe nicht korrekt!")
        return False


def password_gen(length): # Pw-Generator
    """
    This function will generate a random password with A-z and 1-9.
    Parameter:
        length (length of your random generated password)
    Returns:
        (random password as string)
    """


    # generiert zufälliges password 
    pw = ""
    for i in range(length):
        available_char_num = random.randint(0, 60)
        if available_char_num >= 0 and available_char_num <= 8:
            pw += str(available_char_num + 1)
        elif available_char_num >= 9 and available_char_num <= 34:
            pw += chr(available_char_num + 97 - 9)
        else:
            pw += chr(available_char_num + 65 - 35)
    return pw

if __name__ == "__main__":
    ###TESTCASES###
    print(decimal_to_binary(2000)) # 1111010000
    print(decimal_to_binary(a)) # ValueError
    print(decimal_to_binary(1)) # 1
    now = datetime.now()
    dt_string = now.strftime("%Y/%m/%d %H:%M")
    dt = "2023/11/21 10:00"
    exam_countdown(dt_string) # Zeigt die Differenz zwischen des Exams
                              # und deiner jetzigen Zeit
    exam_countdown("2023/03/12 16:23") # Zeigt minuszeit an, da Klausur in der
                                       # Vergangenheit liegt
    exam_countdown("2020/02/28 18:23") # Das Schaltjahr wird berücksichtigt
    print(open_course_page("1")) # Öffnet EPR Kursseite, True
    print(open_course_page("n")) # Eingabe nicht korrekt!, False
    print(open_course_page("6")) # Eingabe nicht korrekt!, False (nur 1-5)
    print(password_gen(20)) # Generiert ein zufälliges 20 Zeichen 
                            # langes Passwort
    print(password_gen(a)) # ValueError
    print(password_gen(999999999999999999999999999999999999999999999999))
                                 # Dauert zu lange, bis das passwort angezeigt
                                 # wird