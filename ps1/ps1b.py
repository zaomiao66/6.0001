#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  9 16:24:23 2020

@author: zao
"""


annual_salary = int(input('Enter your annual_salary: '))
portion_saved = float(input('Enter the persent of your salary to save as a decimal: '))
total_cost = int(input('Enter the cost of your dream home: '))
semi_annual_raise = float(input('Enter the semi-annual raise, as a decimal: '))

portion_down_payment = 0.25
current_savings = 0
r = 0.04
mounths = 0

while(current_savings < portion_down_payment * total_cost):
    current_savings += current_savings * r / 12
    current_savings += annual_salary / 12 * portion_saved
    mounths +=1
    if (mounths % 6 == 0):
        annual_salary += annual_salary * semi_annual_raise

print('Number of mounths:', mounths)