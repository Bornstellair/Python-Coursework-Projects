#! /usr/bin/python
# Exercise No.   3
# File Name:     hw6project3.py
# Programmer:    Hunter Madsen
# Date:          October 3 2021
#
# Problem Statement: Create a function which will contains the lyrics for "The Ants Go Marching", next create two lists that contain the action and number for the ants in the function,
# then create a loop which will iterate through all ten verses in the function and print them, finally call the function in main
#
# Overall Plan:
# 1. Create The Ants Go Marching Lyrics function
# 2. In the function, create two different lists that contains the number of ants and the actions that they will perform in the verse
# 3. In the function, create a for loop to iterate through the verses ten times and print them
# 4. In main, call theAntsGoMarchingLyrics function to display all the verses
#

# The Ants Go Marching Lyrics function
def theAntsGoMarchingLyrics():
    # Creating two lists that contain all the words for all the verses 
    theAntsAction = ['suck his thumb', 'tie his shoe', 'climb a tree', 'close the door', 'take a dive', 'pick up sticks', 'pray to heaven', 'shut the gate', 'check the time', 'say "The End"']
    theAntsNumber = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten']

    # Creating a for loop which will go through all 10 verses
    for i in range(10):
        print("The ants go marching", str(theAntsNumber[i]), "by", str(theAntsNumber[i]), ", hurrah! hurrah!")
        print("The ants go marching", str(theAntsNumber[i]), "by", str(theAntsNumber[i]), ", hurrah! hurrah!")
        print("The ants go marching", str(theAntsNumber[i]), "by", str(theAntsNumber[i]))
        print("The little one stops to", str(theAntsAction[i]))
        print("And they all go marching down. . .")
        print("Into the ground. . .")
        print("To get out. . .")
        print("Of the rain.")
        print("Boom! Boom! Boom!" + '\n')

# Main Function
def main():
    # Calling The Ants Go Marching Lyrics function
    theAntsGoMarchingLyrics()
main()
