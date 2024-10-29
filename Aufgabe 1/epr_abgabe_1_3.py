__author__ = "Chris"

# creating a list with 12 months and their days.
# if its a leap year, 1 is added to the 2nd element of the list (in this case February (28 -> 29)).
def friday_13th(leap_year):
    months_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    months_days [1] += leap_year
    f_13_list = []

# loop goes through all months and days in a week. If it finds a friday 13th it adds it to the list
    for starting_week_day in range(7):
        friday_13 = 0
        week_day = starting_week_day
        for month in months_days:
            for day in range(month):
                week_day = (week_day + 1) % 7
                if week_day == 4 and day == 12:
                    friday_13 = friday_13 + 1
        f_13_list.append(friday_13)
    return f_13_list

# asking user if its a leap year or not. Has to answer with (y/n).
leap_year_calc = input("Soll die min/max Anzahl an Freitag den 13-ten in"+ 
                       " einem Schaltjahr berechnet werden? (y/n): ")

# shows you min/max friday 13th for leap year.
if (leap_year_calc == "y"):
    a = friday_13th(1)
    minimum = min(a)
    maximum = max(a)
    print(a)
    print("Es gibt minimum", minimum, "Freitag der 13-te")
    print("Es gibt maximum", maximum, "Freitag der 13-te")

# shows you min/max friday 13th for regular year.
elif (leap_year_calc == "n"):
    b = friday_13th (0)
    minimum = min(b)
    maximum = max(b)
    print(b)
    print("Es gibt minimal", minimum, "Freitag der 13-te")
    print("Es gibt maximal", maximum, "Freitag der 13-te")
else:
    print("Eingabe nicht korrekt!")

##Testcases##
#   1. If User chooses "y" as an input, expected output will show the following list:
#   [1,2,2,1,1,3,2] and will show the following texts: "Es gibt minimal 1 Freitag der 13-te"
#                                                      "Es gibt maximal 3 Freitag der 13-te"
#   2. If User chooses "k" as an input, he will get the "Eingabe nicht korrekt!" output, because
#      of the if/else condition.
#   3. If User chooses "n" as an input, expected output will show the following list:
#      [2,1,3,1,1,2,2] and will show the following texts: "Es gibt minimal 1 Freitag der 13-te"
#                                                         "Es gibt maximal 3 Freitag der 13-te"