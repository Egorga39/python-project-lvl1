#!/usr/bin/env python3

import random
import operator
import prompt


def welcome_user():
    print('Welcome to the Brain games!')
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name + '!')
    return name


def check_answer(answer, right_answer, name):
    if answer == right_answer:
        print('Correct!')
        return 1
    else:
        print("'{}' is wrong answer ;(.".format(answer),
              "Correct answer was '{}'.\n".format(right_answer),
              "Let's try again, {}!".format(name))
        return 5