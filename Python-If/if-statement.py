"""
if statements are special structures in Python, where we can actually help our programs to make decisions. 
So by using an if statement, we can execute certain code when certain conditions are true. 
And we can execute other code when other conditions are true.
if statements allow our programs to respond to the input that they're given. 
So depending on the data that we're using in the program, our programs will be able to respond.
"""

isMale = True
isTall = False
if isMale and isTall:
    print("You are male and tall .")
elif isMale and not(isTall):
    print("You are male and short.")
elif isTall and not(isMale):  ##elif = else-if
    print("You are not male and tall.")
else:
    print("You are neither male nor tall.")