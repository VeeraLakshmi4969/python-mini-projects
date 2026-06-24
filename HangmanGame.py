# Hangman game python program
# when we use "\" back slash so we have to escape sequence so we use\\
    
    
import random
# from wordslistForHangman import words
# OR


items  = ["apple","banana","coconut","kiwi","goa","pineapple","orange"]
hangman_art = {
    0:("   ",
       "   ",
       "   "),
    1:(" o ",
       "   ",
       "   "),
    2:(" o ",
       " | ",
       "   "),
    3:(" o ",
       "/| ",
       "   "),
    4:(" o ",
       "/|\\ ",
       "   "),
    5:(" o ",
       "/|\\",
       "/ "),
    6:(" o ",
       "/|\\",
       "/ \\"),
    }


def display_man(wrong_guesses):
    for line in hangman_art[wrong_guesses]:
        print(line)
        
def display_hint(hint):
    print(" ".join(hint))
    
def display_answer(answer):
    print(" ".join(answer))

def main():
    answer = random.choice(items)
    hint = ["_"] * len(answer)
    print(hint)
    wrong_guesses = 0
    guessed_letters = set()
    # in python we cannot create empty set by using (). we must use set()
    is_running = True
    
    while is_running:
        display_man(wrong_guesses)
        display_hint(hint)
        guess =  input("Enter a letter : ").lower()
        
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input")
            continue
        
        elif guess in guessed_letters:
            print("You have already guessed this letter")
            continue
        # 1. Sets use .add()
        # 2. Lists use .append()
        guessed_letters.add(guess)
        
        if guess in answer:
            for i in range(len(answer)):
                if answer[i] == guess:
                    hint[i] = guess
        else:
            wrong_guesses +=1
            
        if '_' not in hint:
            display_man(wrong_guesses)
            display_answer(answer)
            print("You Win!")
            is_running = False
        elif wrong_guesses >= len(hangman_art)-1:
            display_man(wrong_guesses)
            display_answer(answer)
            print("You Lose!")
            is_running = False
                    
if __name__=='__main__':
    main()
    
