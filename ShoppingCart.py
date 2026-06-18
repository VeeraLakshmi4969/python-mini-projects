# Shopping cart 

items = []
prices = []
total = 0

while True:
    item = input("Enter a item that you want to buy (q to  quit): ")
    if item.lower() == "q":
        break
    # this lower function convert items into lower case. so that if user gives "Q" to quit this will work 
    else:
        price = float(input(f"Enter price of {item}: Rs."))
        items.append(item)
        prices.append(price)

print("-------------YOUR CART-------------")

for x in items:
    print(x,end=" ")
    #  This will print horizortally
#  print(x) this prints in new line(vertical)
print()

for price in prices:
    total += price

print(f"Your total bill is: {total} Rs.")