#!/usr/bin/env python3

import random
from brain_games.games.module_game import check_answer, welcome_user


def gcd(num_1, num_2):
    n = 1
    right_answer = 1
    while n <= num_1 and n <= num_2:
        if num_1 % n == 0 and num_2 % n == 0:
            right_answer = n
            n += 1
        else:
            n += 1
    print('Question: {} {}'.format(num_1, num_2))
    return right_answer


def check_gsd():
    name = welcome_user()
    print('Find the greatest common divisor of given numbers.')
    n = 0
    while n < 3:
        num_1 = random.randrange(1, 100)
        num_2 = random.randrange(1, 100)
        right_answer = gcd(num_1, num_2)
        answer = int(input())
        n += check_answer(answer, right_answer, name)
        if n == 3:
            return print('Congratulations, {}!'.format(name))
