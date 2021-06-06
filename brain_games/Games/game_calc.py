#!/usr/bin/env python3

import random
import operator
import prompt


def welcome_user():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name + '!')
    return name


def calc(num_1, num_2):
    ops = {'+': operator.add, '-': operator.sub, '*': operator.mul}
    arithmetic = ['+', '-', '*']
    calculation  = random.choice(arithmetic)
    right_answer = ops[calculation](num_1, num_2)
    print('Question: {} {} {}'.format(num_1, calculation, num_2))
    return right_answer


def check_calc():
    name = welcome_user()
    print('What is the result of the expression?')
    n = 0
    while n < 3:
        num_1 = random.randrange(100)
        num_2 = random.randrange(100)
        right_answer = calc(num_1, num_2)
        answer = input()
        if int(answer) == int(right_answer):
            print('Correct!')
            n += 1
        else:
            return print('"{}" is wrong answer ;(.'.format(answer),
                         'Correct answer was "{}".'.format(right_answer),
                         'Let\'s try again, {}!'.format(name))
    print('Congratulations, {}!'.format(name))


check_calc()

