#Insert the temperature you would like to convert: 50F
#10C
#>>> Enter a date: 01/01/2000
#Saturday
#>>> Enter a date: 27/11/2051
#Monday
#print(calendar.weekday(2016, 5, 15))
#%%

import calendar
list(calendar.day_name)
['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
date_input = input("Enter a date (dd/mm/yyyy): ")
year = int(date_input[6:10])
month = int(date_input[3:5])
day = int(date_input[0:2])
weekday = calendar.weekday(year, month, day)

print(calendar.day_name[weekday])

#if temperature_type == "c":
#    temp_type_conv = "F"
#    temperature_converted = (temperature * 9/5) +32
#elif temperature_type == "f":
#    temp_type_conv = "C"
#    temperature_converted = (temperature - 32) * 5/9
#else :
#    temp_type_conv = ""
#    temperature_converted = "enter a value ending with C or F"

##print(temperature_converted,temp_type_conv)
