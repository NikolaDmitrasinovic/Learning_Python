# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 20:50:22 2024

@author: nikol
"""

#expenses = [10.50, 8, 5, 15, 20, 5, 3]
expenses = []
num_expenses = int(input('Enter # of expenses:'))
for i in range(num_expenses):
    expenses.append(float(input('Enter an expense:')))

total = sum(expenses)

#for x in expenses:
 #   sum += x
    
print('You spent $', total, sep = '')
