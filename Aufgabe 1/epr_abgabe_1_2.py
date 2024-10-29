__author__ = "Chris"

# user chooses year to check if leap year or not.
# only integer else ValueError. Also 4 digit years.
leap_year = int(input("Geben Sie ihr gewünschtes Jahr ein: "))

# if year is dividable by 4 and 400 but not 100, it's a leap year.
if leap_year % 4 == 0 and (leap_year % 100 != 0 or leap_year % 400 == 0):
    print("Das Jahr", leap_year, "ist ein Schaltjahr.")
else:
    print("Das Jahr", leap_year, "ist kein Schaltjahr!")

##Testcases##
#   1. if user chooses "2000" as an input, 
#      expected output will be: "Das Jahr 2000 ist ein Schaltjahr."
#   2. if user chooses "a" as an input, an ValueError occures, because "a" not being an Integer.
#   3. if user chooses "2022" as an input,
#      expected output will be: "Das Jahr 2022 ist kein Schaltjahr!"
