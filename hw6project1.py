#! /usr/bin/python
# Exercise No.   1
# File Name:     hw6project1.py
# Programmer:    Hunter Madsen
# Date:          October 3 2021
#
# Problem Statement: Create two functions which will call the area and volume of a sphere, prompt the user to enter a radius, call the functions, and display the results
#
# Overall Plan:
# 1. Create two functions which returns the volume and the area of a sphere
# 2. Prompt the user to enter a radius to be used to solve for the area and volume
# 3. Call the functions
# 4. Print the results showing the users radius, volume, and area of a sphere.
#
# Importing the math library
import math

# Shpere volume function
def sphereVolume(usersRadius):
    usersVolume = (4 / 3) * (math.pi * (usersRadius * usersRadius))
    return(usersVolume)

# Sphere area function
def sphereArea(usersRadius):
    usersArea = math.pi * (usersRadius * usersRadius) * 4
    return(usersArea)

# Main function
def main():
    # Prompting the user for a radius to use
    usersRadius = float(input("Please type in the radius that you would like to use in a sphere and press enter when you are done: "))

    # Calling the functions
    usersArea = sphereArea(usersRadius)
    usersVolume = sphereVolume(usersRadius)

    # Printing the results 
    print("If a sphere had a radius of", usersRadius, "the area of that sphere would be", usersArea, "and the volume of that sphere would be", usersVolume)
main()