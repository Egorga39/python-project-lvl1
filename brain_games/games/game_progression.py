#!/usr/bin/env python3

import random


question = 'What number is missing in the progression?'


def progression():
    n = 2
    a1 = random.randrange(20)
    p = [a1]
    d = random. randrange(20)
    while n <= 10:
        p.append(a1 + d * (n - 1))
        n += 1
    return p


def test():
    i = random.randrange(9)
    p = progression()
    right_answer = p[i]
    p[i] = '..'
    print('Question:', *p)
    return str(right_answer)
