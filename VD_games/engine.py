import prompt


def run_game(description, get_question_and_answer):
    print("Welcome to the VD Games!")
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")
    print(description)

    rounds = 3

    for _ in range(rounds):
        question, correct_answer = get_question_and_answer()

        print(f"Question: {question}")
        answer = prompt.string("Your answer: ")

        if answer != correct_answer:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return

        print("Correct!")

    print(f"Congratulations, {name}!")
