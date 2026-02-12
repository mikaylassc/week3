"""
Mikayla Settles-Chambers
CMSC 111
Spring 2026
Assignment 3 Week 3 (Stop at 7)
"""
'''
#This program loops through numbers 1 to 100.
#It stops when it finds the first number divisible by 7.
'''
for number in range(1, 101):
    print(number)
    
    # Check if the number is divisible by 7
    if number % 7 == 0:
        break  # Stops the loop immediately