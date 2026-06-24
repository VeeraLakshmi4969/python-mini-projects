# python Slot Machine

import random 

def spin_row():
    symbols = ['🍒','🍉','🍋','🔔','⭐']
    
    # results = []
    # for symbol in range(3):
    #     results.append(random.choice(symbols))
    # return results

# OR

    return [random.choice(symbols) for symbol in range(3)]

def print_row(row):
    print("-----------")
    print(" | ".join(row))
    # join method is iterable method
    print("-----------")
def get_payout(row,bet):
    if row[0]==row[1]==row[2]:
        if row[0]=="🍒":
            return bet*2
        elif row[0]=="🍉":
            return bet*3
        elif row[0]=="🍋":
            return bet*5
        elif row[0]=="🔔":
            return bet*10
        elif row[0]=="⭐":
            return bet*10
    else:
        return 0
def main():
    balance = 1000
    print("----------------------")
    print("Welcome to Python Slot")
    print("Symbols: 🍒🍉🍋🔔⭐")
    # to get emojis hold your window and ;(🪟+";")
    print("----------------------")
    while balance>0:
        print(f"Current balance is {balance} Rs.")
        bet = input("Please enter your bet amount: ")
        if not bet.isdigit():
            print("This is Invalid bet amount")
            continue
        
        bet = int(bet)
        if bet <= 0:
            print("Bet must be greater than zero")
            continue
        
        if bet>balance:
            print("Insufficient Balance")
            continue
        
        balance -= bet 
        
        row = spin_row()
        print("Spinning---\n")
        print_row(row)
        
        payout = get_payout(row,bet)
        if payout>0:
            print(f"You have won {payout}")
            balance += payout
            
        else:
            print("Sorry. You have lost.")
            
        again = input("Do you want to play again (y/n) : ").lower()
        if again != "y":
            break
        
    print("------GAME OVER------")
    print(f"Now your balance is {balance}.")
if __name__ =="__main__":
    main()