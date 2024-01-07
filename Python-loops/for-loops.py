"""
for loop is a special type of loop in Python, which allows us to loop over ifferent collections of items. 
A lot of times we'll use for loops in Python to loop through different arrays, or we can loop over like the letters inside of a string, 
or we could just loop through like a series of numbers. 
"""

friends = ["Jim", "Karen", "Kevin"]
for index in range(5):
    if index == 0:
        print("First Iteration")
    else:
        print("Not first")