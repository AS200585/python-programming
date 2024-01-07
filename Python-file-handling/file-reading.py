"""
A lot of times in Python, you're going to want to read from files that are outside of your Python file.
So you might want to read information from like a text file or a CSV file or like an HTML file. 
We can actually use something called the Python read command. 
It will allow you to read a file that is stored outside of your Python file. 
So we can use these files to get information or you can parse through different files and do different things.
"""

employee_file = open("File-reading.txt", "r") #"r" for read, "w" for write, "a" for append, "r+" for read 'n' write
for employee in employee_file.readlines():
    print(employee)
##print(employee_file.writable())   .readable() and .writable()
#print(employee_file.readline()) .readline() to read one line
employee_file.close()