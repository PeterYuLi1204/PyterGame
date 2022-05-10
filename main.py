# Introduction to Python

import time

def main():
    # A quiz application

    # Create some questions and initialize variables
    questions = [["What is the colour of the sun?: ", "yellow"],
                 ["What is 55 x 2?: ", "110"],
                 ["What is the current year?: ", "2022"]]

    score = 0

    # Ask the questions

    print("Hi, welcome to the quiz \nPlease try out some of these fun questions!\n")

    # Get the answer

    for question in questions:
        time.sleep(1)

        user_answer = input(question[0]).strip(" ,.?!").lower()

        time.sleep(1)
        print("Checking answer...")

        # See if user's answers are correct
        time.sleep(1)

        if user_answer == question[1]:
            print("That was absolutely correct!\n")
            score += 1

        else:
            print(f"That was absolutely wrong!\nThe correct answer was: {question[1]}\n")

    print(f"Your final score was {score}/{len(questions)}")


if __name__ == "__main__":
    main()
