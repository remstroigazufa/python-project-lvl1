'#!/usr/bin/env python3'
import prompt
import random


def is_prime(k):
    if k > 1:
        for i in range(2, k):
            if (k % i) == 0:
                return False
        return True


def main():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello,', name + '!')
    print('Answer "yes" if given number is prime. Otherwise answer "no"')
    a = 1
    while a < 4:
        i = random.randrange(2, 100, 1)
        print('Question:', i)
        b = prompt.string('Your answer:')
        correct_a = 'yes' if is_prime(i) is True else 'no'
        if correct_a == b:
            print('Correct!')
            a = a + 1
        else:
            print(b, 'is wrong answer ;(. Correct answer was', correct_a, '.')
            print('Let\'s try again,', name + "!")
            break
        if a == 4:
            print('Congratulations,', name + '!')
            break


if __name__ == '__main__':
    main()
