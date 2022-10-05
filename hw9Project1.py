#! /usr/bin/python
# Exercise No.   1
# File Name:     hw9project1.py
# Programmer:    Hunter Madsen
# Date:          October 31 2021
#
# Problem Statement: Create a button class which allows for the use of rectangular buttons, next using Text take the input of a mother and father in inches, 
# once the user has entered the Text let them verify they have entered it by pressing the buttons and gray them out indicating they are done, then moving on to two more buttons 
# allow for the user to click either male or female and gray out the button once it has been clicked, then run through a loop to get the calculations for the height,
# then using more Text display all the information gathered, finally give the user a button to close the window when they are done
# 
# Overall Plan:
# 1. Create a button class which will display rectangular buttons
# 2. Create a window after importing the graphics library
# 3. Prompt the user to enter data in Text entrys and using the button class verify once the user has finished by graying out
# 4. Convert the values entered in the entry to ints (this part isn't working for me though and I can't figure it out for the life of me haha)
# 5. Once the user has clicked either the male or female button run through a nested loop to get the correct calculations for the specified gender
# 6. Finally, display all the informatino gathered via Text and then give the user a final button to click when they are finsihed to close the window
#

# Importing the graphics library
from graphics import *

# I know I could have imported the button class but I created this from the book to fully grasp the concept while tackling this problem
# Button Class
class Button:

    # Docstring describing the button class
    """A button is a labeled rectangle in a window. It is activated or deactivated with the activate() and deactivate() methods. 
    The clicked(p) method returns true if the button is active and p is inside it. """

    def __init__(self, window, center, width, height, label):

        # Docstring describing the constructor
        """ Creates a rectangular button, eg: qb = Button(myWin, centerPoint, width, height, 'Quit') """ 

        widthValue, heightValue = width / 2.0, height / 2.0
        xValue, yValue = center.getX(), center.getY()
        self.xMax, self.xMin = xValue + widthValue, xValue - widthValue
        self.yMax, self.yMin = yValue + heightValue, yValue - heightValue
        p1 = Point(self.xMin, self.yMin)
        p2 = Point(self.xMax, self.yMax)
        self.rectangle = Rectangle(p1,p2)
        self.rectangle.setFill('lightgray')
        self.rectangle.draw(window)
        self.label = Text(center, label)
        self.label.draw(window)
        self.deactivate()

    def clicked(self, p):

        # Docstring describing what happens when the user clicks 
        "Returns true if button active and p is inside"

        return (self.active and
                self.xMin <= p.getX() <= self.xMax and
                self.yMin <= p.getY() <= self.yMax)

    def getLabel(self):

        # Docstring describing how the label will return
        "Returns the label string of this button."

        return self.label.getText()

    def activate(self):

        # Doscstring desribing if the button is active
        "Sets this button to active."

        self.label.setFill('black')
        self.rectangle.setWidth(2)
        self.active = True

    def deactivate(self):

        # Docstring describing if the button is inactive
        "Sets this button to inactive."

        self.label.setFill('darkgrey')
        self.rectangle.setWidth(1)
        self.active = False

# Main Function
def main():

    # Creating a GUI window
    window = GraphWin("Homework 9 Project 1", 700, 700)

    # Initializing the height for the mother and the father
    usersMothersHeight = 0
    usersFathersHeight = 0


    # Prompting the user to enter the needed data and then to having the user click the necessary buttons to indicate they are done
    mothersHeightButton = Button(window, Point(350, 100), 400, 40, "Click here when you have entered the Mothers Height")
    Text(Point(320, 50), "Please enter the Mothers height in inches here: ").draw(window)
    usersMothersHeight = Entry(Point(510, 50), 5)
    usersMothersHeight.setText(0)
    usersMothersHeight.draw(window)
    fathersHeightButton = Button(window, Point(350, 250), 400, 40, "Click here when you have entered the Fathers Height")
    Text(Point(320, 200), "Please enter the Fathers height in inches here: ").draw(window)
    usersFathersHeight = Entry(Point(510, 200), 5)
    usersFathersHeight.setText(0)
    usersFathersHeight.draw(window)
    usersChildMaleGender = Button(window, Point(200, 400), 300, 40, "Click here if the childs gender is male")
    usersChildFemaleGender = Button(window, Point(500, 400), 300, 40, "Click here if the childs gender is female")

    # Activating the buttons
    mothersHeightButton.activate()
    fathersHeightButton.activate()
    usersChildFemaleGender.activate()
    usersChildMaleGender.activate()

    # Getting the users mouse clicks
    usersClickPoint = window.getMouse()

    # Getting the string values the user entered
    usersFathersHeight = usersFathersHeight.setText(usersFathersHeight.getText())
    usersMothersHeight = usersMothersHeight.setText(usersMothersHeight.getText())

    # Converting the string values to ints to account for 'NoneType' in calculations
    usersFathersHeightInt = int(0 if usersFathersHeight is None else usersFathersHeight)
    usersMothersHeightInt = int(0 if usersMothersHeight is None else usersMothersHeight)

    # While statement to deactivate the mothers button once it has been clicked
    while mothersHeightButton.clicked(usersClickPoint):

        # Deactivating the button once the user has clicked it
        mothersHeightButton.deactivate()

    # Getting the users second mouse point
    usersClickPointTwo = window.getMouse()

    # While statement to deactivate the fathers button once it has been clicked
    while fathersHeightButton.clicked(usersClickPointTwo):

        # Deactivating the button once the user has clicked it
        fathersHeightButton.deactivate()

    # Getting the users third mouse point
    usersClickPointThree = window.getMouse()
    
    # While statement to verify which of the two buttons was clicked to get the calculations for each specific gender
    while usersChildMaleGender.clicked(usersClickPointThree) or usersChildFemaleGender.clicked(usersClickPointThree):

        # If else statement to determine the gender of the child
        if usersChildMaleGender.clicked(usersClickPointThree):
            # Male calculations
            maleChildsHeight = ((usersMothersHeightInt * 13/12) + usersFathersHeightInt) / 2
            childsHeightFeet = maleChildsHeight / 12
            childsHeightInches = maleChildsHeight % 12 

            # Deactivating the button after the calculations 
            usersChildMaleGender.deactivate()

        elif usersChildFemaleGender.clicked(usersClickPointThree):
            # Female calculations
            femaleChildsHeight = ((usersFathersHeightInt * 12/13) + usersMothersHeightInt) / 2
            childsHeightFeet = femaleChildsHeight / 12
            childsHeightInches = femaleChildsHeight % 12

            # Deactivating the button after the calculations
            usersChildFemaleGender.deactivate()
        else:
            return

    # String value to store in the text box to display the information
    informationStringOne = "Based on the heights entered for the parents the child would be about this many feet tall: "
    informationStringTwo = "Based on the heights entered for the parents the child \n would be about this many inches tall added on top of their total feet: "

    # Text information to display the results
    Text(Point(320, 500), informationStringOne).draw(window)
    Text(Point(350, 550), informationStringTwo).draw(window)
    Text(Point(650, 500), round(childsHeightFeet)).draw(window)
    Text(Point(650, 560), round(childsHeightInches)).draw(window)

    # Getting another mouse click from the user so the window doesn't close
    usersClickPointFour = window.getMouse()

    # Prompting the user to close the window with a button when they are done
    closeButton = Button(window, Point(350, 600), 300, 40, "Click here to exit the window")

    # If statement to close only when the user clicks on it
    if closeButton.clicked(usersClickPointFour):

        # Deactivating the button once it has been clicked
        closeButton.deactivate()

        # Closing the window once the user has clicked the close button
        window.close()
    else:
        return

main()