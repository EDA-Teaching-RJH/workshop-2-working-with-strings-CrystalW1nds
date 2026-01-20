import random

def main():
    age = int(input("Please enter your age: "))

    if age >= 18:
        print("You are an adult.")
    else:
        print("You are a child.")

    guessGame()
    gradeCalculator()

def guessGame():
    secret_number = random.randint(1, 10)
    guess = int(input("Guess a number between 1 and 10: "))

    if guess == secret_number:
        print("Congratulations! You guessed the correct number.")
    elif guess > secret_number:
        print("Too high. The secret number was", secret_number)
    else:
        print("Too low. The secret number was", secret_number)

def gradeCalculator():
    score = int(input("Enter your score (0-100): "))
    
    if score >= 90 and score <= 100:
        grade = 'A'
    elif score >= 80 and score < 90:
        grade = 'B'
    elif score >= 70 and score < 80:
        grade = 'C'
    elif score >= 60 and score < 70:
        grade = 'D'
    elif score < 60:
        grade = 'F'
    else :
        print("Invalid score. Try again.")
    

    print(f"Your grade is: {grade}")
    if grade == 'F':
        print("You failed.")
    elif grade == 'D':
        print("You just about passed.")
    elif grade == 'C':
        print("You did alright.")
    elif grade == 'B':
        print("Well done!")
    else:
        print("Very well done!")



main()