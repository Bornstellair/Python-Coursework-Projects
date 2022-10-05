#! /usr/bin/python
# Exercise No.   1
# File Name:     hw7project1.py
# Programmer:    Hunter Madsen
# Date:          October 10 2021
#
# Problem Statement: Prompt the user to enter a grade percentage, next using else if statements filter through and print the users letter grade based on the percent.
#
# Overall Plan:
# 1. Prompt the user to enter a grade percentage
# 2. Create an if else statement to filter through the percentage to determine the letter grade
# 3. Print the letter grade
#

def main():
    # Prompting the user to enter their percentage grade to see their letter grade
    usersGradePercent = float(input("Please enter the current grade percentage (from a range of 0-100%) to be converted to a letter grade: "))

    # If else statement to determine what letter grade equates to the percentage that the user entered
    if usersGradePercent <= 100 and usersGradePercent >= 90:
        print("You currently have an A based on that percentage.")
    elif usersGradePercent < 90 and usersGradePercent >= 80:
        print("You currently have a B based on that percentage.")
    elif usersGradePercent < 80 and usersGradePercent >= 70:
        print("You currently have a C based on that percentage.")
    elif usersGradePercent < 70 and usersGradePercent >= 60:
        print("You currently have a D based on that percentage.")
    elif usersGradePercent < 60:
        print("You currently have an F based on that percentage.")
    else:
        print("Error entering grade percentage.")
        return
main()