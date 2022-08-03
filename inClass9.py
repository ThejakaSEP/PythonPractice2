from datetime import datetime
from datetime import date, timedelta

# 1. Use the datetime module to write a program that gets the current date and prints the day of
# the week

# print(datetime.datetime.now().strftime("%b"))
# print(datetime.datetime.now())

# 2. Write a program that takes a birthday of user as input and prints the user’s age and the number of
# days, hours, minutes and seconds until their next birthday

birthday=input("What is your next B'day Date? (in DD/MM/YYYY) ")
date_time_obj = datetime.strptime(birthday, '%d/%m/%Y')
month = date_time_obj.month
day = date_time_obj.day

today=datetime.now()
currentDay = today.now().day
currentMonth = today.now().month
currentYear = today.now().year

# Finding Age
age = today.year - date_time_obj.year -((today.month, today.day) <
         (date_time_obj.month, date_time_obj.day))

print("Age : ",age)


#Finding time till next birthday
if month > currentMonth and day > currentDay:
    nextBirthdayStr = f"{day}/{month}/{currentYear}"
    nextBirthday = datetime.strptime(nextBirthdayStr,'%d/%m/%Y')

else:
    nextBirthdayStr = f"{day}/{month}/{currentYear+1}"
    nextBirthday = datetime.strptime(nextBirthdayStr, '%d/%m/%Y')


timeTillNextBirthday = nextBirthday - today
print("Time till next Birthday : ",timeTillNextBirthday)


#3. Write a program that takes birthday of a person and calculates the total number
# of seconds they have been living in epoch time

# birthday=input("What is your next B'day Date? (in DD/MM/YYYY) ")
# date_time_obj = datetime.strptime(birthday, '%d/%m/%Y')

# 4. Write a Python program to print the date for yesterday, today, and tomorrow

def printDates():
    today = datetime.now().date()
    yesterday = today-timedelta(1)
    tomorrow = today+timedelta(1)
    print(today," ",yesterday," ",tomorrow)


printDates()