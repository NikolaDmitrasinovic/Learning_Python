# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 21:20:27 2024

@author: nikol
"""

# Get details of loan
money_owed = float(input('How much money do you owe, in dolalrs\n'))
apr = float(input('What is the annual percantage rate of the laon?\n'))
payment = float(input('How much will you pay off each mont in dollars?\n'))
months = int(input('Now many months do you want to see the results for?\n'))

monthly_rate = apr/100/12

for i in range(months):
#calc intrest
 interest_paid = money_owed*monthly_rate
#add interest
 money_owed = money_owed + interest_paid
 
 if(money_owed - payment < 0):
     print('The last payment is', money_owed)
     print("You paid off the loan in", i+1, 'months')
     break

#make payment
 money_owed = money_owed - payment

 print("Paid", payment, "of which", interest_paid, "was interest", end=" ")
 print("How I owe", money_owed)
