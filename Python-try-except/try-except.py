"""
A lot of times when we're running Python programs, we encounter different errors. 
So different situations could come up and your program might throw an error or it might throw an exception.
And a lot of times when these situations happen, it will completely stop your program from running. 
So instead of our program just breaking and stop executing, we can actually handle those errors and do things when they occur.
In order to handle these errors, we can use something called a try except block. 
A try except block will basically allow our program to try out a piece of code.If everything goes well, then we're great.
"""

try:
    value = 10/0
    number = int(input("Enter a number :"))
    print(number)
except ZeroDivisionError:
    print("Divided by Zero")
except ValueError:
    print("Invalid")