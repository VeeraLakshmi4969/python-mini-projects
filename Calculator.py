# Python Calculator

operator = input("Please enter an operator you want(+ - / * %) : ")
num1 = float(input("Enter your first number: "))
num2 = float(input("Enter your second number: "))

if operator == "+":
    print(round(num1 + num2,2))
elif operator == "-":
    print(round(num1 - num2,2))
elif operator == "*":
    print(round(num1 * num2,2))
elif operator == "/":
    print(round(num1 / num2,2))
elif operator == "%":
    print(round(num1 % num2,2))
else:
    print("Please run again and enter a valid operator ")