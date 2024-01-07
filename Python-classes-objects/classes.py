"""
Classes and objects are extremely useful in Python programming and they can help you to make your programs more organized and more powerful.
A lot of times when we're writing programs, we're going to have to work with different types of data. 
There's essentially like a few basic types of data we can do with usually things like strings, plain text, numbers, and Boolean values.
But, the problem is that not all information and data  can be represented using strings, numbers, or Booleans.
So what we can do with classes and objects is we can essentially create our own data types. 
So, we can create our own data type from anything we want in Python. For example, we can create a phone data type and it could represent a phone
in order to store all the information we would want to know about our phone inside of that data type.
So with a class, you can essentially define your own data type.
"""
"""a class function is essentially a function that we can use inside of a class and it can either modify the objects of that class 
or it can give us specific information about those objects. """

class Student:
    def __init__(self, name, major, gpa, on_probation): #def __init__() to state class contents
       self.name = name
       self.major = major
       self.gpa = gpa
       self.on_probation = on_probation

    def honour_roll(self):
        if self.gpa >= 3.5:
           return True
        else:
           return False
