# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 08:40:11 2024

@author: nikol
"""

age = int(input("How old are you?\n"))
decades = age//10
years = age % 10

print("Your are " + str(decades) + " decades and " + str(years) + " years old")
