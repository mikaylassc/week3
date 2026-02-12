"""
Mikayla Settles-Chambers
CMSC 111
Spring 2026
Assignment 3 Week 4
"""
'''
#This program prints numbers from 1 to 50.
#The continue statement skips numbers divisible by 5.
'''
for number in range(1, 51):

    # Check if number is divisible by 5
    if number % 5 == 0:
        continue  # Skips this number and moves to next loop iteration

    print(number)