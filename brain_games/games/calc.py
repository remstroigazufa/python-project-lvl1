import random
TASK_GAME = 'What is the result of the expression?'
MIN_NUMBER = 1
MAX_NUMBER = 100
STEP = 1


def decides():
    first_number = random.randrange(MIN_NUMBER, MAX_NUMBER, STEP)
    second_number = random.randrange(MIN_NUMBER, MAX_NUMBER, STEP)
    action = [' + ', ' - ', ' * ']
    operation = random.choice(action)
    expression = str(first_number) + str(operation) + str(second_number)
    if operation == '+':
        answer = first_number + second_number
    elif operation == '-':
        answer = first_number - second_number
    elif operation == '*':
        answer = first_number * second_number
    return(str(expression), str(answer))
