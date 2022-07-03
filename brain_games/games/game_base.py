'#!/usr/bin/env python3'
import prompt


def progress(game):
    a = 1
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name?')
    print('Hello, ', name + '!')
    print(game.QUESTION)
    while a < 4:
        q, answer = game.question()
        print('Question: ' + q)
        b = prompt.string('Your answer:')
        if a < 4 and answer == b:
            print('Correct!')
            a = a + 1
        else:
            print(b, 'is wrong answer ;(. Correct answer was ', answer, '.')
            print('Let\'s try again,', name + "!")
            break
        if a == 4:
            print('Congratulations,', name + '!')
            break
