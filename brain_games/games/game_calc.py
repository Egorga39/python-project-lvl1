#!/usr/bin/env python3

import random
import operator
from brain_games.games.module_game import welcome_user, check_answer


def calc(num_1, num_2):
    ops = {'+': operator.add, '-': operator.sub, '*': operator.mul}
    arithmetic = ['+', '-', '*']
    calculation = random.choice(arithmetic)
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
        right_answer = int(calc(num_1, num_2))
        answer = int(input())
        n += check_answer(answer, right_answer, name)
        if n == 3:
            return print('Congratulations, {}!'.format(name))
