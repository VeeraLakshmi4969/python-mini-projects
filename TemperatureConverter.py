# Temperature Converter

Temperature = float(input("Please input your temperature: "))
units = input("Is your temperature in Celsius or Fahrenheit(C/F): ")

if units == "C":
    Temperature = round((9*Temperature)/5 + 32,1)
    print(f"Temperature in Fahrenheit is: {Temperature}°F")
    # To get degree symbol Alt + 0176
elif units == "F":
    Temperature = round((Temperature-32)*(5/9),1)
    print(f"Temperature in Celsius is: {Temperature}°C")
else:
    print(f"Your units {units} is invalid")