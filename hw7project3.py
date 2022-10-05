#! /usr/bin/python
# Exercise No.   3
# File Name:     hw7project3.py
# Programmer:    Hunter Madsen
# Date:          October 10 2021
#
# Problem Statement: Prompt the user to enter the speed limit and a cars clocked speed, next create an if else statement to determine
# whether the cars speed was illegal or not, then if the speed was illegal nest another if else statement to determine the fine, finally print the fine
#
# Overall Plan:
# 1. Prompt the user to enter the speed limit and the cars clocked speed
# 2. Create an if else statement to narrow down if the speed was illegal or not
# 3. If the speed was illegal, nest another if else statement to help determine the fine based on the speed to add additional fees
# 4. Print if the speed was legal or print if the speed was illegal and the ticket they will recieve
#

def main():
    # Prompting the user to enter the speed limit and the cars clocked speed
    speedLimit = int(input("Please enter the speed limit for the area: "))
    carsClockedSpeed = int(input("Please enter what speed the car was clocked with: "))

    # Speeding ticket variable to be used
    speedingTicket = 50

    # if else statement to determine if the clocked speed was faster than the speed limit
    if carsClockedSpeed <= speedLimit:
        print("Legal. Looks like you are a safe driver!")
    else:
        print("Illegal. Looks like you weren't a safe driver!")
    
        speedOverLimit = carsClockedSpeed - speedLimit

        # Nesting another if else statement to determine the fine 
        if carsClockedSpeed < 90:
            additionalFee = speedOverLimit * 5
        else:
            print("Wow, you were going pretty fast.")
            additionalFee = speedOverLimit * 5 + 200
        
        # Print screen to show the user the fine for speeding
        print("You will be getting a ticket for $", speedingTicket + additionalFee)
main()