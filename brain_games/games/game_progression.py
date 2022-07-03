import random
QUESTION = 'What number is missing in the progression?'
MIN_NUMBER_ONE = 1
MIN_NUMBER_TWO = 6
MIN_NUMBER_THREE = 2
MAX_NUMBER_ONE = 5
MAX_NUMBER_TWO = 10
STEP_NUMBER = 1
MIN_NUMBER_ZERO = 0


def question():
    start_int = random.randrange(MIN_NUMBER_ONE, MAX_NUMBER_ONE, STEP_NUMBER)
    stop_int = random.randrange(MIN_NUMBER_TWO, MAX_NUMBER_TWO, STEP_NUMBER)
    step_int = random.randrange(MIN_NUMBER_THREE, MAX_NUMBER_ONE, STEP_NUMBER)
    list_game = list(range(start_int, step_int * stop_int, step_int))
    empty_string = ' '
    list_empty = random.randrange(MIN_NUMBER_ZERO, len(list_game), STEP_NUMBER)
    for n in list_game:
        if list_game[list_empty] == n:
            empty_string += '..' + ' '
        else:
            empty_string += str(n) + ' '
    return (str(empty_string), str(list_game[list_empty]))
