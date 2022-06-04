'#!/usr/bin/env python3'
import prompt
import random


def main():
    print('Welcome to the Brain Games!')
#    welcome_user()
#    main_two()
    main_three()


#def welcome_user():
#   name = prompt.string('May I have your name? ')
#    print('Hello, ', name,'!')
#    return name

#def main_two():
#    print('Answer "yes" if the number is even, otherwise answer "no"')


def main_three():
    name = prompt.string('May I have your name? ')
    print('Hello, ', name,'!')
    print('Answer "yes" if the number is even, otherwise answer "no"') 
    a = 1
    while a < 4:
        i = random.randrange(1, 100, 1)
        print('Question: ',i)
        b = input('Your answer: ' )
        if i % 2 == 0 and b == 'yes':
            print('Correct!')
            a = a + 1 
        elif i % 2 != 0 and b == 'no':
            print('Correct!')
            a = a + 1
        else:
            print('"yes" is wrong answer ;(. Correct answer was "no".\nLet\'s try again, ', name,"!")
            break
        if a == 4:
            print('Congratulations, ',name,'!')
            break
if __name__ == '__main__':
    main()
