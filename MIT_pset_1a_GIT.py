#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 15 20:56:21 2020

@author: skorniakova
"""

#User inputs:
annual_salary = float(input("What is your starting annual salary?"))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = float(input("Enter the cost of your dream home:"))


#downpayment for dream home is .25
portion_down_payment = total_cost * 0.25


current_savings = 0
months = 0

while current_savings < portion_down_payment:
    
        #r = annual return = 0.04
    monthly_return = current_savings * 0.04/12
    current_savings += monthly_return
    
    
        #portion from annual salary saved monthly
    salary_saved_monthly = annual_salary/12 * portion_saved
    current_savings += salary_saved_monthly
    
    months +=1
  


        #how many months

print("Number of months: " + str(months))