#! /usr/bin/python
# Exercise No.   1
# File Name:     hw8project1.py
# Programmer:    Hunter Madsen
# Date:          October 24 2021
#
# Problem Statement: Prompt the user to enter a value of a number in a fibonacci sequence and output the nth value the user entered
# 
# Overall Plan:
# 1. Prompt the user to enter the nth value of a positive number
# 2. Create several variables to be plugged into an if else statement 
# 3. Create an if else statement which goes through the various scenarios up to the second fibonacci value
# 4. In the else statement run through a for loop from the range of the second fibonacci value to the nth value the user entered transitioning between the various variables to output the desired value
#

def main():
    # Getting the nth value from the user
    usersNValue = int(input("Please enter the nth value of a positive number to calculate the fibonacci value of the desired number: "))

    # Creating variables to be used in the if else statement
    zeroFibonacciValue = 0
    firstFibonacciValue = 1
    secondFibonacciValue = 1
    a = 1
    b = 1
    temp = 0

    # If else statement to go throught the possible scenarios to give only positive values
    if usersNValue == 0:
        print("The fibonacci value is: ", zeroFibonacciValue)
    elif usersNValue == 1:
        print("The fibonacci value is: ", firstFibonacciValue)
    elif usersNValue == 2:
        print("The fibonacci value is: ", secondFibonacciValue)
    elif usersNValue < 0:
        print("Sorry, the value you entered is a negative number and won't work for this. Please try again.")
    else: 
        # Now that we've got the positive values, and we have larger values than 1, we can go through a for loop and add the previous values to each other up to the nth value
        for i in range(2, usersNValue):
            temp = a + b
            a = b
            b = temp

        # Printing the fibonacci value of the users nth value
        print("The fibonacci value is: ", b)

main()