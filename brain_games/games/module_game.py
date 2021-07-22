#!/usr/bin/env python3

import prompt


def welcome_user():
    print('Welcome to the Brain games!')
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name + '!')
    return name


def game(question, test):
    name = welcome_user()
    print(question)
    n = 0
    while n < 3:
        right_answer = test()
        answer = input()
        if answer == right_answer:
            n += 1
            print('Correct!')
        else:
            return print("'{}' is wrong answer ;(.".format(answer),
                         "Correct answer was '{}'.\n".format(right_answer),
                         "Let's try again, {}!".format(name))
    return print('Congratulations, {}!'.format(name))
