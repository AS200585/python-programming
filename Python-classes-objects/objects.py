"""
Object is an instance of a class
"""

from classes import Student

student1 = Student("Andrew", "BCA", "4.0", False) #Object of Student
student2 = Student("Lara", "B.Sc", "3.6", True)

print(student2.honour_roll())