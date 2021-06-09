#!/usr/bin/env python3


import random

from brain_games.games.game_calc import check_answer, welcome_user


def test_prime(number):
    print('Question: ' + str(number))
    d = 2
    while d * d <= number and number % d != 0:
        d += 1
    if d * d > number:
        right_answer = 'yes'
        return right_answer
    else:
        right_answer = 'no'
        return right_answer


def check_prime():
    name = welcome_user()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    n = 0
    while n < 3:
        number = random.randrange(100)
        right_answer = test_prime(number)
        answer = input()
        n += check_answer(answer, right_answer, name)
        if n == 3:
            return print('Congratulations, {}!'.format(name))
