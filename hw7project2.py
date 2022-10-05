#! /usr/bin/python
# Exercise No.   2
# File Name:     hw7project2.py
# Programmer:    Hunter Madsen
# Date:          October 10 2021
#
# Problem Statement: Take the input of a mother and father in inches, take the input of the gender of the child, next using the given formulas 
# estimate the height of the child and output their height in feet and inches.
#
# Overall Plan:
# 1. Prompt the user to enter the height of the mother and father 
# 2. Prompt the user to enter the gender of the child to determine the height
# 3. Next, use an else if statement to narrow down the calculations to output the right results of the height of the child using the gender the user picked
# 4. Finally, print screen showing all the outputted information for the user to see the estimated height of the child
#

def main():
    # Informing the user on what to enter
    print("This program can estimate the height of a child using the height of the mother and father.")

    # Prompting the user to enter the height of the mother
    mothersHeight = int(input("Please enter the height of the mother of the child in inches and press enter: "))

    # Prompting the user to enter the height of the father
    fathersHeight = int(input("Please enter the height of the father of the child in inches and press enter: "))

    # Prompting the user to enter the childs gender
    childsGender = int(input("Please enter the gender of the child (If the child is male, enter 1. If the child is female, enter 2.): "))

    # If else statement to determine the gender of the child
    if childsGender == 1:
        # Male calculations
        maleChildsHeight = ((mothersHeight * 13/12) + fathersHeight) / 2
        childsHeightFeet = maleChildsHeight / 12
        childsHeightInches = maleChildsHeight % 12 
    elif childsGender == 2:
        # Female calculations
        femaleChildsHeight = ((fathersHeight * 12/13) + mothersHeight) / 2
        childsHeightFeet = femaleChildsHeight / 12
        childsHeightInches = femaleChildsHeight % 12
    else:
        print("Error, you did not enter the childs gender correctly. Please try again.")
        return 

    # Printing the results
    print("If a child had a father who was", fathersHeight, "inches tall and a mother who was", mothersHeight, "inches tall")
    print("the child of these partents would be approximatelty", round(childsHeightFeet), "feet", round(childsHeightInches), "inches tall.")
main()