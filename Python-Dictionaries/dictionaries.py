"""
A dictionary is a special structure in Python which allows us to store information in what are called key value pairs. 
So essentially different key value pairs and then when we want to access a specific piece of information inside of the
dictionary we can just refer to it by its key. 
"""

monthConversions = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
}

print(monthConversions.get("Lex", "Invalid key")) ##passing default value to an unmappable key
##print(monthConversions["Feb"])