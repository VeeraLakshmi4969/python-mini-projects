# Menu of Restaurant
print("Program Started")
print("-------------------------MENU-----------------------")
menu = { 
    "Veg Dum Biryani": 190, 
    "Egg Biryani (2 Eggs)": 200, 
    "Chicken Dum Biryani (Regular)": 240, 
    "Chicken Dum Biryani (Jumbo)": 340, 
    "Mutton Dum Biryani": 320, 
    "Chicken Fry Biryani": 260, 
    "Chicken Boneless Biryani": 280, 
    "Special Chicken Lollypop Biryani": 290, 
    "Mixed Non-Veg Biryani": 350 
}

cart = []
total = 0

for key,value in menu.items():
    print(f"{key:35} : {value} Rs.")

print("----------------------------------------------------")

while True:
    order =  input(f"Enter your order(Q to quit)         : ").strip().title()
    if order == "Q":
        break
    # title capitalize first letter of every word
    # capitalize only very first letter
    elif menu.get(order)  is not None:
        cart.append(order.title())
    else:
        print("Item not found.  Enter item correctly!")

print("----------------------------------------------------")

print("You have ordered                      :")
for food in cart:
    print(food,end=", ")
    total += menu.get(food)

print(f"\nYour total bill is : {total:.2f} Rs.")