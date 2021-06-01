#!/usr/bin/env python

import prompt


def test_welcome_user():
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name + '!')
