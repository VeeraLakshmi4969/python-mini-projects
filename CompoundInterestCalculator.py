# Python compound interest calculator

principle = 0
rate = 0
time = 0

while principle <= 0:
    principle = float(input("Enter the principle amount: "))
    if principle <= 0:
        print("Principle  can not be less than or zero.")


# OR (if we want to include zero)
# while True:
# principle = float(input("Enter the principle amount: "))
# if principle < 0:
#     print("Principle  can not be less than zero.")
# else:
#     break


while rate <= 0:
    rate = float(input("Enter the interest rate (in percentage): "))
    if rate <= 0:
        print("rate can not be less than or equal to zero.")

while time <= 0:
    time = float(input("Enter the time period (in years): "))
    if time <= 0:
        print("time can not be less than or equal to zero.")

total = principle *pow((1+ rate/100),time)
print(f"Your Balance is: {total:.2f}")