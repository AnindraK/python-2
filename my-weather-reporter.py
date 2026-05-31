city = input("Write you city name:")
temp = float(input("Write your temp here in C:"))
if temp > 35:
    print("Warning: It is very hot today!")

if temp > 25:
        print("It is a great day to go outside!")
else:
        print("Grab a jacket before u go out!")

if temp > 35:
       print("Warning: it is schorching hot!")
elif temp >25:
       print("Weather: warm and sunny!")
elif temp > 15:
       print("weather: cool and brezzy!")
else:
       print("Weather: Cold- STAY WARM!")

import datetime
import calendar

now = datetime.datetime.now()
print("City:", city)
print("Time now:", now)
print(calendar.calendar(now.year))
    