import random
QUESTION = 'Answer "yes" if the number is even,'\
    ' otherwise answer "no".'
MIN_NUMBER = 1
MAX_NUMBER = 100
STEP_NUMBER = 1


def question():
    number_game = random.randrange(
        MIN_NUMBER, MAX_NUMBER, STEP_NUMBER)
    correct_answer = \
        'yes' if number_game % 2 == 0 else 'no'
    return (str(number_game), correct_answer)
