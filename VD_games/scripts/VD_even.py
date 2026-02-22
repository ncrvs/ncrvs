import random

import prompt


def main() -> int:
    print("Welcome to the VD-games!")
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")
    print('Answer "yes" if the number is even, otherwise answer "no".')

    rounds_to_win = 3

    for _ in range(rounds_to_win):
        number = random.randint(1, 100)
        print(f"Question: {number}")

        answer = prompt.string("Your answer: ").strip().lower()

        correct = "yes" if number % 2 == 0 else "no"

        if answer != correct:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct}'.")
            print(f"Let's try again, {name}!")
            return 0

        print("Correct!")

    print(f"Congratulations, {name}!")
    return 0
