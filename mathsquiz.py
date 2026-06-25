import random


def displayMenu():
    print("\nDIFFICULTY LEVEL")
    print("1. Easy")
    print("2. Moderate")
    print("3. Advanced")

    while True:
        choice = input("Choose a difficulty level (1-3): ")
        if choice in ["1", "2", "3"]:
            return int(choice)
        print("Invalid choice. Please try again.")


def randomInt(level):
    if level == 1:  # Easy
        return random.randint(0, 9)
    elif level == 2:  # Moderate
        return random.randint(10, 99)
    else:  # Advanced
        return random.randint(1000, 9999)


def decideOperation():
    return random.choice(["+", "-"])


def displayProblem(num1, num2, operation):
    return int(input(f"{num1} {operation} {num2} = "))


def isCorrect(userAnswer, correctAnswer):
    if userAnswer == correctAnswer:
        print("Correct!")
        return True
    else:
        print("Incorrect.")
        return False


def displayResults(score):
    print("\nQUIZ RESULTS")
    print(f"Final Score: {score}/100")

    if score >= 90:
        grade = "A+"
    elif score >= 80:
        grade = "A"
    elif score >= 70:
        grade = "B"
    elif score >= 60:
        grade = "C"
    elif score >= 50:
        grade = "D"
    else:
        grade = "F"

    print(f"Rank: {grade}")


def playQuiz():
    level = displayMenu()
    score = 0

    for question in range(1, 11):
        num1 = randomInt(level)
        num2 = randomInt(level)
        operation = decideOperation()

        if operation == "+":
            correctAnswer = num1 + num2
        else:
            correctAnswer = num1 - num2

        print(f"\nQuestion {question}")

        answer = displayProblem(num1, num2, operation)

        if isCorrect(answer, correctAnswer):
            score += 10
        else:
            print("Try again.")
            answer = displayProblem(num1, num2, operation)

            if isCorrect(answer, correctAnswer):
                score += 5
            else:
                print(f"The correct answer was {correctAnswer}.")

    displayResults(score)


def main():
    while True:
        playQuiz()

        again = input("\nWould you like to play again? (Y/N): ").upper()

        if again != "Y":
            print("Thank you for playing!")
            break


main()