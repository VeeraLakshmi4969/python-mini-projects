# WEIGHT CONVERTER

weight = float(input("Enter your weight: "))
units = input("Is this weight in kilograms or pounds? (K or L): ")
if units == "K":
    weight = weight * 2.205
    units = "Lbs."
    print(f"Your weight is {weight} {units}")
elif units == "K":
    weight = weight / 2.205
    units = "Lbs."
    print(f"Your weight is {weight} {units}")
else:
    print(f"{units} is valid number")

