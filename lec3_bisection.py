#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  9 09:43:00 2020

@author: zao
"""

cube = float(input('Please input cube number: '))

epsilon = float(input('Please input epsilon: '))

high = cube
low = 0
guess = (high + low)/2
num_guess = 0

while(abs(guess ** 3 - cube) >= epsilon):
    if (guess ** 3 > cube):
        high = guess
    else:
        low = guess
    guess = (high + low) / 2
    num_guess += 1

print('guess', num_guess, 'times')
print(guess, 'is close to cube root of', cube)
