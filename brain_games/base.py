'#!/usr/bin/env python3'
import prompt


def unites(game):
    a = 1
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name?')
    print('Hello, ', name + '!')
    print(game.task_game)
    while a < 4:
        question_game, answer = game.decides()
        print('Question: ' + question_game)
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
