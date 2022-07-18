import random
import math
TASK_GAME = 'Find the greatest common divisor of given numbers.'
MIN_NUMBER = 1
MAX_NUMBER = 100
STEP = 1


def get_game_data():
    first_number = random.randrange(MIN_NUMBER, MAX_NUMBER, STEP)
    second_number = random.randrange(MIN_NUMBER, MAX_NUMBER, STEP)
    expression = f'{first_number} {second_number}'
    answer = math.gcd(first_number, second_number)
    return (str(expression), str(answer))
