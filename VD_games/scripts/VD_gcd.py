import random
import prompt
import math


def main():
    print("Welcome to the VD Games!")
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")
    print("Find the greatest common divisor of given numbers.")

    rounds = 3

    for _ in range(rounds):
        a = random.randint(1, 100)
        b = random.randint(1, 100)

        print(f"Question: {a} {b}")

        answer = int(prompt.string("Your answer: "))

        correct = math.gcd(a, b)

        if answer != correct:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct}'.")
            print(f"Let's try again, {name}!")
            return

        print("Correct!")

    print(f"Congratulations, {name}!")
