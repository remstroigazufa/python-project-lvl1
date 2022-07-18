import random
TASK_GAME = 'What is the result of the expression?'
MIN_NUMBER = 1
MAX_NUMBER = 100
STEP = 1


def get_game_data():
    first_number = random.randrange(MIN_NUMBER, MAX_NUMBER, STEP)
    second_number = random.randrange(MIN_NUMBER, MAX_NUMBER, STEP)
    action = ['+', '-', '*']
    operation = random.choice(action)
    expression = f'{first_number} {operation} {second_number}'
    if operation == '+':
        answer = first_number + second_number
    elif operation == '-':
        answer = first_number - second_number
    elif operation == '*':
        answer = first_number * second_number
    return (str(expression), str(answer))
