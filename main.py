"""
Welcome to the 2022 Michigan State Source Code competition. Please make sure that you
fill out the variables before so that your grade can be recorded accurately.

Please remove the pass statement from any function that you attempt to complete.

If you have any questions please raise your hand. You are allowed to use the internet
however you see fit. Best of luck!
"""

import unittest
import math

teamName = "ENTER TEAM NAME"
teamNumber = "ENTER TEAM NUMBER"
ourNames = "ENTER YOUR NAME/NAMES IF A PAIR"

"""
Simple Function
Make the function return True.
"""
def question1():
    pass


"""
Fibonacci Numbers
Calculate the first 20 Fibonacci numbers and put them in a list. Simply adding the first 20 to a
list will result in no points. You must use a for loop in order to receive credit. 
"""
def question2():
    pass


"""
Converting Types
A list of numbers "data" will be passed in. Convert the list of strings to a list of integers and 
return it. You must perform a conversion on each list item to receive points. 
"""
def question3(data):
    pass


"""
Calculations
Two points will be passed into this function. Use the distance formula to calculate the distance
between the two points and return it. The math library is already imported for you. 
"""
def question4(x1, y1, x2, y2):
    pass


"""
Prime Numbers
A random number "data" will be passed in. Create an algorithm to check if the number is prime.
Return True if prime and False otherwise. Hard coding the inputs to return a certain value
will result in no points. Ex: if(input == 2) return True, is not allowed.
"""
def question5(data):
    pass


"""
Build a Dictionary
Create a dictionary from the passed in list "data" and return it. The dictionary key is the value's
index in the list and the dictionary value is the list element at that index. Ex the list
[red, green, blue] is passed in. The resulting dictionary would be {'0' : 'red', '1' : 'green', 
'2' : 'blue'}
"""
def question6(data):
    pass


"""
Difference in Area
Calculate the difference between the area of the rectangle and the sphere. The rectangle is 
passed in as "length" and "width" while the circle is passed in as "radius". Calculate the area
of each shape and return their difference (rectangle area - circle area).
"""
def question7(length, width, radius):
    pass


class testCases(unittest.TestCase):

    def testQ1(self):
        self.assertEqual(True, question1())

    def testQ2(self):
        expected = [0,1,1,2,3,5,8,13,21,34,55,89,144,233,377,610,987,1597,2584,4181,6765]
        self.assertEqual(expected, question2())

    def testQ3(self):
        setOne = ["0", "1", "2", "3"]
        setOneUpdated = [0, 1, 2, 3]
        setTwo = ["52", "64", "11000115", "999841"]
        setTwoUpdated = [52, 64, 11000115, 999841]
        self.assertEqual(setOneUpdated, question3(setOne))
        self.assertEqual(setTwoUpdated, question3(setTwo))

    def testQ4(self):
        self.assertEqual(1, question4(2, 1, 1, 1))
        self.assertEqual(10, question4(10, 8, 2, 2))

    def testQ5(self):
        setOne = [17, 2, 3, 5]
        setTwo = [4, 6, 8, 9]
        setThree = [11, 12, 13, 14]
        setOneUpdated = [True, True, True, True]
        setTwoUpdated = [False, False, False, False]
        setThreeUpdated = [True, False, True, False]
        for i in range(len(setOne)):
            self.assertEqual(setOneUpdated[i], question5(setOne[i]))
        for i in range(len(setTwo)):
            self.assertEqual(setTwoUpdated[i], question5(setTwo[i]))
        for i in range(len(setOne)):
            self.assertEqual(setThreeUpdated[i], question5(setThree[i]))

    def testQ6(self):
        setOne = ["item1", "item2", "item3"]
        setOneD = {'0' : 'item1', '1' : 'item2', '2' : 'item3'}
        self.assertEqual(setOneD, question6(setOne))

    def testQ7(self):
        pass


if __name__ == '__main__':
    unittest.main()
