#!/usr/bin/env python3

import random
import operator


question = 'What is the result of the expression?'


def test():
    num_1 = random.randrange(100)
    num_2 = random.randrange(100)
    ops = {'+': operator.add, '-': operator.sub, '*': operator.mul}
    arithmetic = ['+', '-', '*']
    calculation = random.choice(arithmetic)
    right_answer = ops[calculation](num_1, num_2)
    print('Question: {} {} {}'.format(num_1, calculation, num_2))
    return str(right_answer)
