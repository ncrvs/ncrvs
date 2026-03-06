import random
import prompt


def main():
    print("Welcome to the VD Games!")
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")
    print("What is the result of the expression?")

    rounds = 3

    for _ in range(rounds):
        a = random.randint(1, 50)
        b = random.randint(1, 50)
        op = random.choice(["+", "-", "*"])

        print(f"Question: {a} {op} {b}")

        answer = int(prompt.string("Your answer: "))

        if op == "+":
            correct = a + b
        elif op == "-":
            correct = a - b
        else:
            correct = a * b

        if answer != correct:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct}'.")
            print(f"Let's try again, {name}!")
            return

        print("Correct!")

    print(f"Congratulations, {name}!")
