#! /usr/bin/python
# Exercise No.   2
# File Name:     hw6project2.py
# Programmer:    Hunter Madsen
# Date:          October 3 2021
#
# Problem Statement: Create a function which can go through a list of numbers and add all the numbers together to give you a sum
#
# Overall Plan:
# 1. Create the Sum List funtion which uses a for loop to iterate through all the numbers in the list and add them together returning the sum
# 2. Hard code in the list of numbers
# 3. Print the results which display the (hard coded) list, and then call the Sum List function to iterate through the numbers list returning the sum
#

# Sum List function
def sumList(numsList):
    # Initializing to 0
    numbersSum = 0

    # For loop which goes through the numbers in the list and adds it to the total
    for numberFromList in numsList:
        numbersSum += numberFromList

    # Returning the sum of the numbers
    return(numbersSum)

# Main function
def main():
    # Hard coding in the numbers list 
    listOfNumbers = [28, 10, 3, 19, 67, 45, 20]

    # Printing the information for the user to see what the list is and the total of all the numbers in the list
    print("The list of random numbers is:", listOfNumbers, ", and the total of all the numbers added together is:", sumList(listOfNumbers))
main()