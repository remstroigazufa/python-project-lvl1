'#!/usr/bin/env python3'
import prompt
import random


def main():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name?')
    print('Hello, ', name + '!')
    print('What number is missing in the progression?')
    a = 1
    while a < 4:
        i = random.randrange(1, 10, 1)
        y = random.randrange(5, 10, 1)
        x = random.randrange(1, 10, 1)
        g = list(range(i, x * y, x))
        p = ' '
        r = random.randrange(0, len(g), 1)
        for n in g:
            if g[r] == n:
                p += ' ' + '..'
            else:
                p += ' ' + str(n)
        print('Question:', p)
        b = prompt.integer('Your answer:')
        if a < 4 and g[r] == b:
            print('Correct!')
            a = a + 1
        else:
            print(b, 'is wrong answer ;(. Correct answer was ', g[r], '.')
            print('Let\'s try again, ', name + "!")
            break
        if a == 4:
            print('Congratulations, ', name + '!')
            break

if __name__ == '__main__':
    main()

