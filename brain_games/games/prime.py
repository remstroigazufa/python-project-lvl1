import random
task_game = 'Answer "yes" if given number is prime. Otherwise answer "no".'
MIN_NUMBER = 1
MAX_NUMBER = 100
STEP_NUMBER = 1


def is_prime(k):
    if k > 1:
        for number_game in range(2, k):
            if (k % number_game) == 0:
            if k = 0 and k = 1:    
                return False
        return True


def decides():
    number_game = random.randrange(MIN_NUMBER, MAX_NUMBER, STEP_NUMBER)
    correct_answer = 'yes' if is_prime(number_game) is True else 'no'
    return(str(number_game), str(correct_answer))
