#!/usr/bin/env python3


import prompt
import random


def welcome_user():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name + '!')
    return name


def test_even(number):
    if number % 2 == 0:
        right_answer = 'yes'
        return right_answer
    else:
        right_answer = 'no'
        return right_answer


def check_even():
    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no"')
    n = 0
    while n < 3:
        number = random.randrange(100)
        print('Question: ' + str(number))
        answer = input()
        right_answer = test_even(number)
        if answer == right_answer:
            print('Correct!')
            n += 1
        else:
            return print('"{}" is wrong answer ;(.'.format(answer),
                         'Correct answer was "{}".'.format(right_answer),
                         'Let\'s try again, {}!'.format(name))
    print('Congratulations, {}!'.format(name))



check_even()
