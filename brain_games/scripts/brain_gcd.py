'#!/usr/bin/env python3'
import prompt
import random
import math


def main():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello,', name + '!')
    print('Find the greatest common divisor of given numbers.')
    a = 1
    while a < 4:
        i = random.randrange(1, 100, 1)
        y = random.randrange(1, 100, 1)
        print('Question:', i, y)
        b = prompt.integer('Your answer:')
        g = math.gcd(i, y)
        if a < 4 and g == b:
            print('Correct!')
            a = a + 1
        else:
            print(b, 'is wrong answer ;(. Correct answer was', g, '.')
            print('Let\'s try again,', name + "!")
            break
        if a == 4:
            print('Congratulations,', name + '!')
            break


if __name__ == '__main__':
    main()
