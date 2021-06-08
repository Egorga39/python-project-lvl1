#!/usr/bin/env python3


import random

from brain_games.games.game_calc import check_answer, welcome_user


def test_even(number):
    print('Question: ' + str(number))
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
        right_answer = test_even(number)
        answer = input()
        n += check_answer(answer, right_answer, name)
        if n == 3:
            return print('Congratulations, {}!'.format(name))
