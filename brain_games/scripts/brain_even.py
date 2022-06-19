'#!/usr/bin/env python3'
import prompt
import random


def main():
    print('Welcome to the Brain Games!')
    main_three()


def main_three():
    name = prompt.string('May I have your name? ')
    print('Hello,', name + '!')
    print('Answer "yes" if the number is even, otherwise answer "no"')
    a = 1
    while a < 4:
        i = random.randrange(1, 100, 1)
        print('Question:', i)
        b = input('Your answer:')
        cor = 'yes' if i % 2 == 0 else 'no'
        if cor == b:
            print('Correct!')
            a = a + 1
        else:
            print(f'\'{b}\' is wrong answer ;(. Correct answer was\'{cor}\'')
            print(f'Let\'s try again, {name}!')
            break
        if a == 4:
            print('Congratulations,', name + '!')
            break


if __name__ == '__main__':
    main()
