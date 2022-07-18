'#!/usr/bin/env python3'
import prompt
ROUND_COUNT = 3


def run_game(game):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(game.TASK_GAME)
    for round in range(0, ROUND_COUNT):
        question_game, answer = game.get_game_data()
        print(f'Question: {question_game}')
        b = prompt.string('Your answer: ')
        if answer == b:
            print('Correct!')
        else:
            print(f'{b}, is wrong answer ;(. Correct answer was , {answer}.')
            print(f'Let\'s try again, {name}!')
            break
        if round == (ROUND_COUNT - 1):
            print(f'Congratulations, {name}!')
            break
