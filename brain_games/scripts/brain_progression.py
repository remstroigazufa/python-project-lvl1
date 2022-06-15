'#!/usr/bin/env python3'
import prompt
import random


def main():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, ', name, '!')
    print('What number is missing in the progression?')
    a = 1
    while a < 4:
        i = random.randrange(1, 9, 1)
        y = random.randrange(70, 100, 1)
        x = random.randrange(1, 5, 1)
        u = random.randrange(1, 9, 1)
        r = list(range(i, y, x))
        g = r[0:9]
        q = g[u]
        g[u] = '..'
        r = ' '
        for k in range(len(g)):
            r += f'{g[k]} '
        print('Question: ', r)
        b = prompt.integer('Your answer: ')
        if a < 4 and q == b:
            print('Correct!')
            a = a + 1
        else:
            print(b, 'is wrong answer ;(. Correct answer was', q)
            print('Let\'s try again, ', name, "!")
            break
        if a == 4:
            print('Congratulations, ', name, '!')
            break


if __name__ == '__main__':
    main()
