#!/usr/bin/env python3

import random
from brain_games.games.game_calc import check_answer, welcome_user


def progression():
    n = 2
    a1 = random.randrange(20)
    p = [a1]
    d = random. randrange(20)
    while n <= 10:
        p.append(a1 + d * (n - 1))
        n += 1
    return p


def question(p, i):
    right_answer = p[i]
    p[i] = '..'
    print('Question: ', *p)
    return right_answer


def check_progression():
    name = welcome_user()
    print('What number is missing in the progression?')
    n = 0
    while n < 3:
        p = progression()
        i = random.randrange(9)
        right_answer = int(question(p, i))
        answer = int(input())
        n += check_answer(answer, right_answer, name)
        if n == 3:
            return print('Congratulations, {}!'.format(name))
