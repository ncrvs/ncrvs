import random


def generate_progression():
    start = random.randint(1, 20)
    step = random.randint(1, 10)
    length = 10

    progression = [start + i * step for i in range(length)]

    hidden_index = random.randint(0, length - 1)
    correct = progression[hidden_index]

    progression[hidden_index] = ".."

    return " ".join(map(str, progression)), str(correct)


def get_game():
    description = "What number is missing in the progression?"
    return description, generate_progression
