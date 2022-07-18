import random
TASK_GAME = 'What number is missing in the progression?'
MIN_NUMBER_START = 1
MIN_NUMBER_STOP = 6
MIN_NUMBER_STEP = 2
MAX_NUMBER_START = 5
MAX_NUMBER_STOP = 15
STEP = 1
MIN_NUMBER_LIST = 0


def get_game_data():
    start_int = random.randrange(MIN_NUMBER_START, MAX_NUMBER_START, STEP)
    stop_int = random.randrange(MIN_NUMBER_STOP, MAX_NUMBER_STOP, STEP)
    step_int = random.randrange(MIN_NUMBER_STEP, MAX_NUMBER_START, STEP)
    list_game = list(range(start_int, step_int * stop_int, step_int))
    empty_string = ' '
    list_empty = random.randrange(MIN_NUMBER_LIST, len(list_game), STEP)
    for n in list_game:
        if list_game[list_empty] == n:
            empty_string += '..' + ' '
        else:
            empty_string += str(n) + ' '
    empty_string_strip = empty_string.strip()
    return (str(empty_string_strip), str(list_game[list_empty]))
