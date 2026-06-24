# Banking Program

def check_balance():
    #  Accesses the global balance variable safely for reading
    print(f"Your bank balance is {balance} Rs.")
def deposit():
     # Needed to modify the global balance variable
    global balance
    amount = int(input("Enter the amount that you want to deposit : "))
    if amount <= 0:
        print("This is not valid amount.")
    else:
        balance +=amount
        print(f"{amount} Rs. deposited successfully!")

def withdraw():
     # Needed to modify the global balance variable
    global balance
    amount = int(input("Enter the amount that you want to withdraw : "))
    if amount<=0:
        print("Amount must be greater than zero.")
    elif amount <= balance:
        balance -=amount
        print(f"{amount} Rs. withdrawn successfully!")
    else:
        print("Insufficient Balance")
        
def main():
    is_running =True
    balance = 0

    while is_running:
        print("THESE ARE OUR BANK SERVICES")
        print("1.Check Bank Balance")
        print("2.Deposit")
        print("3.Withdraw")
        print("4.Exit")
        
        choice = input("Enter your choice between 1 to 4 : ")
        if choice == "1":
            check_balance()
        elif choice=="2":
            deposit()
            # in another method we can use 
            # blance += deposit
        elif choice=="3":
            withdraw()
        elif choice=="4":
            is_running=False
            print("Thank you. Have a nice day.")
        else:
            print("This is not valid choice.")

if __name__=="__main__":
    main()