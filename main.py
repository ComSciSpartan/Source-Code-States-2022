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
**Tie Breaker**
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
of each shape and return their difference (rectangle area - rectangle2 area).
"""
def question7(length, width, length2, width2):
    pass


"""
Mid Point
Calculate the mid point between (x1,y1) and (x2,y2) then return it. Return the answer as a pair
ex: return (distance1,distance2)
"""
def question8(x1, y1, x2, y2):
    pass


"""
Scalar Volume
Use the length, width, and height to calculate the area of the rectangular prism. Then scale the 
volume by using the passed in scale factor. Return the final scaled volume.
"""
def question9(length, width, height, scale):
    pass


"""
Logic Flow
Use an if else block to determine if x1 is greater than or equal to x2. If x1 is greater than or 
equal to x2 return true, otherwise return false.
"""
def question10(x1, x2):
    pass


"""
Averages From a List
A list of numbers will be passed in. Use a for loop to calculate the average of all the numbers
in the list and return that average.
"""
def question11(data):
    pass


"""
Powers
A base and an exponent will be passed in. Raise the base to power of the exponent and return 
the computed value. 
"""
def question12(base, power):
    pass


"""
Extract a Message
**Tie Breaker**
Use a for loop to iterate over the elements in the list. The list elements will be strings that
make up a secret message. To decode the message reverse each string in the list and then
concatenate the strings together to create a phrase. Return the final string and make sure there
are no leading or trailing spaces. Ex: ['terces', 'egassem'] yields 'secret message'
"""
def question13(data):
    pass


"""
Factoring
Use a while loop to compute all the factors for the number passed in. Add all the factors to a list
and return the list. Ex: 15 yields [1,3,5,15]
"""
def question14(data):
    pass


"""
Calculate Container Sizes
Compute the size of each list and return it. Ex: [54, 74, 30] yields 3
"""
def question15(data):
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
        self.assertEqual(25, question7(4, 7, 1, 3))
        self.assertEqual(32, question7(6, 10, 7, 4))

    def testQ8(self):
        self.assertEqual((5,5), question8(0, 0, 10, 10))
        self.assertEqual((7.5,7.5), question8(5, 5, 10, 10))

    def testQ9(self):
        self.assertEqual(1000, question9(5, 5, 5, 2))

    def testQ10(self):
        self.assertEqual(True, question10(5, 0))
        self.assertEqual(False, question10(0, 5))
        self.assertEqual(True, question10(1, 1))

    def testQ11(self):
        self.assertEqual(1, question11([1,1,1,1,1,1,1,1]))
        self.assertEqual(10, question11([10,10,10,10,10,10,10]))
        self.assertEqual(3, question11([1,2,3,4,5]))

    def testQ12(self):
        self.assertEqual(256, question12(2, 8))
        self.assertEqual(1000, question12(10, 3))

    def testQ13(self):
        message1 = "Welcome to source code states 2022"
        coded1 = ['emocleW', 'ot', 'ecruos', 'edoc', 'setats', '2202']
        self.assertEqual(message1, question13(coded1))

    def testQ14(self):
        set1 = [1, 2, 3, 4, 6, 8, 12, 16, 24, 48]
        self.assertEqual(set1, question13(48))
        set2 = [1, 2, 4, 5, 10, 20, 25, 50, 100]
        self.assertEqual(set2, question13(100))

    def testQ15(self):
        container = []
        for i in range(50):
            self.assertEqual(i, question15(container))
            container.append(i)

if __name__ == '__main__':
    unittest.main()
