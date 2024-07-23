# oops (object oriented programming)
# =====
# to map with realworld scenerios, we started using objects in code.


# class:
# =======
# class is like a blueprint from which objects are created.

# (1)CLASS VARIABLE --> is shared  by all instance of a class
# (2) INSTANCE VARIABLE --> unique to each instances
# (3) METHOD ---> function that we define inside a class

# syntax-->   
# class ClassName:          #Name of the class should be started with Capital letter.
#     statement1
#     .
#     .
#     .
#     .
#     statementN

# let's see...


#this is not a good way to write this code.. let's see the better way

# class Student:
#     def __init__(self, first, last, marks):
#         self.first = first
#         self.last = last
#         self.marks = marks
#         self.email = first + "." + last + "@abc.com"

#     def fullName(self):
#         return f"{self.first} {self.last}"


# stud1 = Student("john", "sharma", 90)
# stud2 = Student("ravi", "patel", 93)

# print(stud1.first)      #john
# print(stud2.email)      #ravi.patel@abc.com

# print(f"{stud1.first} {stud1.last}")        #john sharma


# print(stud1.fullName())   #john sharma                       

# print(stud2.fullName())     #ravi patel





