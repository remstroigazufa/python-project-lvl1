import random
import math
TASK_GAME = 'Find the greatest common divisor of given numbers.'
MIN_NUMBER = 1
MAX_NUMBER = 100
STEP_NUMBER = 1


def decides():
    first_number = random.randrange(MIN_NUMBER, MAX_NUMBER, STEP_NUMBER)
    second_number = random.randrange(MIN_NUMBER, MAX_NUMBER, STEP_NUMBER)
    expression = str(first_number) + ' ' + str(second_number)
    answer = math.gcd(first_number, second_number)
    return(str(expression), str(answer))
