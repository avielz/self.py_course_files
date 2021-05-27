#Insert the temperature you would like to convert: 50F
#10C
#%%
temperature_input = input("Insert the temperature you would like to convert: ")
temperature_type = temperature_input[-1].lower()
temperature = float(temperature_input[:-1])
#print(temperature)

if temperature_type == "c":
    temp_type_conv = "F"
    temperature_converted = (temperature * 9/5) +32
elif temperature_type == "f":
    temp_type_conv = "C"
    temperature_converted = (temperature - 32) * 5/9
else :
    temp_type_conv = ""
    temperature_converted = "enter a value ending with C or F"

print(temperature_converted,temp_type_conv)
