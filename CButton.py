#! /usr/bin/python
# Exercise No.   2
# File Name:     CButton.py
# Programmer:    Hunter Madsen
# Date:          October 31 2021
#

# Importing the graphics library
from graphics import *

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
        "Sets this button to active."

        self.label.setFill('black')
        self.circle.setWidth(2)
        self.active = True

    def deactivate(self):

        # Docstring describing if the button is inactive
        "Sets this button to inactive."

        self.label.setFill('darkgrey')
        self.circle.setWidth(1)
        self.active = False
        