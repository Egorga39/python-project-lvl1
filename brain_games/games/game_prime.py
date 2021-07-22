#!/usr/bin/env python3

import random


question = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def test():
    number = random.randrange(100)
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
