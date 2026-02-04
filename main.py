import random

# A list of dictionaries to store questions and answers
question = {
    "What is the output of: print(5 * 2)?\na) 10 b) 25 c) 52\nAnswer? - ":"a",
    "What type of loop is used to repeat a block of code a fixed number of times?\na) while b) for c) loop\nAnswer? - ":"b",
    "What does 'if' do in Python?\na) Starts a function b) Checks a condition c) Declares a variable\n Answer? - ":"b",
    "Which function gets input from the user?\n a) input() b) print() c) str()\nAnswer? - ":"a",
    "What is the correct syntax to define a function?\na) function myFunc(): b) def myFunc(): c) define myFunc():\n Answer? - ":"b"
    }

options = ["a","b","c"]

# Shuffle questions to randomize order
random.choice(question)

# Initialize score counter
score = 0

# Welcome the user
print("Welcome to the Year 12 Python Quiz!\n")

# Loop through each question
for questions, answer in question.items(): #Loop to ask questions
        user_answer=input(questions).lower() #Asks user for input for the questions in the dictionary, then turns it lowercase
        while user_answer not in options: #Checks if the input for the question is in the multichoice options
            user_answer=input("The options are only a,b,c: ").lower() #Asks user again for input, and turns it lowercase
        if user_answer==answer.lower(): #Checks if the answer is correct from the dictionary
            print("Correct, that's 1 point! \n")
            score+=1 #Adds 1 point to the score
        else:
            print("Incorrect \n")

# Final Score
print(f"Quiz Completed! Your final score: {score}/5")
