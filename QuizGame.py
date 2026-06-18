# Python quiz game

questions = ("1. Which symbol is used to write a single-line comment in Python?",
             "2. Which keyword is used to create a function in Python?",
             "3. What is the output of the following code snippet? print(3 * 2)",
             "4. Which of the following data types is used to store text data in Python?",
             "5. How do you start an if statement in Python?")
options = (("a) //","b) #","c)","d) /* */"),
           ("a) func","b) define","c) def","d) function"),
           ("a) 32",'b) "32"',"c) 6","d) 3 * 2"),
           ("a) int","b) float","c) str","d) list"),
           ("a) if x > 5:","b) if (x > 5)","c) if x > 5 then","d) if {x > 5}"))
# "b) "32"" this shows error so we have to use print('b) "32"')      print("""b) "32" """)   print("b) \"32\"")

question_num = 0
answers = ("b","c","c","c","a")
guesses = []
# we append guesses so we use append
score =0

for question in questions:
    print("------------------------------------------")
    print(question)
    for option in options[question_num]:
        print(option)
    guess = input("Enter your answer(a, b, c, d): ").lower()
    guesses.append(guess)
    if guess== answers[question_num]:
        print("Your answer is correct!")
        score += 1
    else:
        print("Incorrect answer!")
        print(f"{answers[question_num]} is correct answer.")
    question_num += 1


print("------------------------------------------")
print("                RESULTS                   ")
print("------------------------------------------")


print("answers: ",end=" ")
for answer in answers:
    print(answer, end=" ")
print()

print("guesses: ",end= " ")
for guess in guesses:
    print(guess, end=" ")
print()



print(f"Your score is: {score}")

percent = int((score / len(questions))*100)
print(f"Your percentage is {percent}%")