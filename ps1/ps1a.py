#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  9 15:19:30 2020

@author: zao

total_cost  need input

portion_down_payment = 0.25

current_savings = 0

r = 0.04  annual rate

annual_salary need input

portion_saved need input

mouthly_salary

how many mounths for a down payment
"""

annual_salary = int(input('Enter your annual_salary: '))
portion_saved = float(input('Enter the persent of your salary to save as a decimal: '))
total_cost = int(input('Enter the cost of your dream home: '))

portion_down_payment = 0.25
current_savings = 0
r = 0.04
mounths = 0

while(current_savings < portion_down_payment * total_cost):
    current_savings += current_savings * r / 12
    current_savings += annual_salary / 12 * portion_saved
    mounths +=1

print('Number of mounths:', mounths)


