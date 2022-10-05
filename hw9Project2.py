#! /usr/bin/python
# Exercise No.   2
# File Name:     hw9project2.py
# Programmer:    Hunter Madsen
# Date:          October 31 2021
#
# Problem Statement: Create a modified button class that creates circular buttons and then test the CButton class in the roller.py program.
# 
# Overall Plan:
# 1. Go through the button class and change the constructors definition and changing all the buttons to circles and change the 
# clicked function to accept a click within the radius of the circle defined
# 2. Import the necessary libraries 
# 3. Bring the code over from the roller.py program and store it in main
# 4. In main go through the button classes and convert them to the new CButton class 
# 5. Roll the dice using the circular buttons
#

# Importing all the needed libraries
from graphics import *
from CButton import *
from dieview import DieView 
from random import randrange

# CButton Class
class CButton:

    # Docstring describing the CButton Class
    """ A CButton is a labeled circle in a window. It is activated or deactivated with the activate() and deactivate() methods. 
    The clicked(p) method returns true if the button is active and p is inside it. """

    # Creating the constructor
    def __init__(self, window, center, radius, label):

        # Docstring describing the constructor
        """ Creates a circlular button, eg: qb = CButton(theWindow, centerPoint, radiusArea, 'Quit') """ 

        # Getting the center and radius of the circle
        self.xLocationCenter = center.getX()
        self.yLocationCenter = center.getY()
        self.radius = radius
        self.center = center 

        # Creating the circle
        self.circle = Circle(center, radius)
        self.circle.setFill('lightgray')
        self.circle.draw(window)
        
        # Creating the label
        self.label = Text(center, label)
        self.label.draw(window)
        self.deactivate()


    def clicked(self, p):

        # Docstring describing what happens when the user clicks 
        "Returns true if button active and p is inside"
        
        return (self.active and
                # Getting the x and y position to verify it is wihtin the radius of the circle
                (self.xLocationCenter - p.getX() ** 2 + self.yLocationCenter - p.getY() ** 2)
                <= self.radius ** 2)

    def getLabel(self):

        # Docstring describing what will happen when the 
        "Returns the label string of this button."

        return self.label.getText()

    def activate(self):

        # Doscstring desribing if the button is active
        "Sets this button to 'active'."

        self.label.setFill('black')
        self.circle.setWidth(2)
        self.active = True

    def deactivate(self):

        # Docstring describing if the button is inactive
        "Sets this button to 'inactive'."

        self.label.setFill('darkgrey')
        self.circle.setWidth(1)
        self.active = False
    
# Main Function
def main():

    # create the application window
    win = GraphWin("Dice Roller")
    win.setCoords(0, 0, 10, 10)
    win.setBackground("green2")

    # Draw the interface widgets
    die1 = DieView(win, Point(3,7), 2)
    die2 = DieView(win, Point(7,7), 2)
    rollButton = CButton(win, Point(5,4.5), 1.4, "Roll \n Dice")
    rollButton.activate()
    quitButton = CButton(win, Point(5,1), 1, "Quit")

    # Event loop
    pt = win.getMouse()
    while not quitButton.clicked(pt):
        if rollButton.clicked(pt):
            value1 = randrange(1,7)
            die1.setValue(value1)
            value2 = randrange(1,7)
            die2.setValue(value2)
            quitButton.activate()
        pt = win.getMouse()

    # close up shop
    win.close()

main()