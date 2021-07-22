#!/usr/bin/env python3

import random


question = 'Answer "yes" if the number is even, otherwise answer "no"'


def test():
    num_1 = random.randrange(100)
    print('Question: ' + str(num_1))
    if num_1 % 2 == 0:
        right_answer = 'yes'
        return right_answer
    else:
        right_answer = 'no'
        return right_answer
