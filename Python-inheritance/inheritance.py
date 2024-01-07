"""
Inheritance is basically where we can define a bunch of attributes and functions and things inside of a class 
and then we can create another class and we can inherit all of those attributes. 
So I can basically have one class that has all the functionality of another class without having to physically
write out any of the same methods or attributes.
"""

from chef import Chef
from chineseChef import ChineseChef

myChef = Chef()
myChef.make_special_dish()

myChineseChef = ChineseChef()
myChineseChef.make_chicken()