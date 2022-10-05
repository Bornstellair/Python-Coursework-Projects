#! /usr/bin/python
# Exercise No.   2
# File Name:     hw8project2.py
# Programmer:    Hunter Madsen
# Date:          October 24 2021
#
# Problem Statement: Prompt the user for a file name that contains an image and then prompt the user for the name of the file to store the image in once it has changed colors. 
# Next, construct the image and get the dimensions. Now create a window in which we can view the image in. Running through nested for loops change the individual pixels on each axis of 
# the image and update it as you go to see the changes. Once the image has changed colors on all pixels, save the image. 
# 
# Overall Plan:
# 1. Prompt the user for the desired file that contains the image and then prompt the user for the desired file to store the image once the color has changed.
# 2. Construct the image and get the dimensions.
# 3. Create a window which will allow you to view the image.
# 4. Create a nested for loop which will go through each axis of the image and change the individual pixel starting from left to right and update the window.
# 5. Finally, save the image once it has fully changed colors to the desired file location the user input. 
#

# Importing the graphics library
from graphics import *

def main():
    # Informing the user what to enter
    print("This program will change the color of an image that is entered. Please enter the name of the file and the name of the new file when the color is changed.")

    # Prompting the user to enter the file name to open the image and then prompting the user to enter the file location to store the new image
    usersInputFile = input("Please enter the name of the file the image is contained in: ")
    usersOutputFile = input("Please enter the name of the file that you would like to store the image in once the color has changed: ")


    # Constructing the image 
    usersImage = Image(Point(350, 350), usersInputFile)

    # Getting the images dimensions
    usersImageWidth = usersImage.getWidth()
    usersImageHeight = usersImage.getHeight()

    # Creating a window and drawing the image into it
    window = GraphWin("hw8Project2", 700, 700)
    usersImage.draw(window)
    
    # Values to iterate through in the for loops
    imagesXAxis = 0
    imagesYAxis = 0

    # For loop which goes through both axis's of the image to change the color contents
    for imagesXAxis in range(usersImageWidth):
        for imagesYAxis in range(usersImageHeight):

            # Getting the images color values
            r, g, b = usersImage.getPixel(imagesXAxis, imagesYAxis)
            imageBrightness = int(round(0.299 * r + 0.587 * g + 0.144 * b))

            # Converting the images colors to the new brightness
            usersImage.setPixel(imagesXAxis, imagesYAxis, color_rgb(imageBrightness, imageBrightness, imageBrightness))

            # Updating the window 
            window.update()

    # Saving the image to the desired file location
    usersImage.save(usersOutputFile)



main()