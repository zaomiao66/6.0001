#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  9 18:07:46 2020

@author: zao
"""

starting_salary = int(input('Enter your annual_salary: '))

total_cost = 1000000
semi_annual_raise = 0.07

portion_down_payment = 0.25
current_savings = 0
r = 0.04

low = 0
high = 10000
steps = 0
found = False


while (low < high):
    current_savings = 0
    annual_salary = starting_salary
    mounths = 0
    portion_saved = int((low + high) / 2)
    steps += 1
    while(mounths < 36):
        current_savings += current_savings * r / 12
        current_savings += annual_salary / 12 * portion_saved/10000
        mounths +=1
        if (mounths % 6 == 0):
            annual_salary += annual_salary * semi_annual_raise
    if (abs(current_savings - total_cost * portion_down_payment) < 100):
        found = True
        break
    
        
    if (current_savings > total_cost * portion_down_payment + 100):
        high = portion_saved
    elif (current_savings < total_cost * portion_down_payment - 100):
        low = portion_saved + 1
    
if found:
    print('Best savings rate:', portion_saved/10000)
    print('Steps in bisection search:', steps)
else:
    print('Is is not possible to pay the down payment in three years')