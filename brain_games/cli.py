#!/usr/bin/env python3

import prompt


def welcome_user():
    print('Welcome to the Brain games!')
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name + '!')
    return name
