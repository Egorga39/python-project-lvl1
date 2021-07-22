#!/usr/bin/env python3

import random

question = 'Find the greatest common divisor of given numbers.'


def test():
    num_1 = random.randrange(1, 100)
    num_2 = random.randrange(1, 100)
    n = 1
    right_answer = 1
    while n <= num_1 and n <= num_2:
        if num_1 % n == 0 and num_2 % n == 0:
            right_answer = n
            n += 1
        else:
            n += 1
    print('Question: {} {}'.format(num_1, num_2))
    return str(right_answer)
