import random


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def generate_question():
    number = random.randint(1, 100)
    correct = "yes" if is_prime(number) else "no"
    return str(number), correct


def get_game():
    description = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    return description, generate_question
