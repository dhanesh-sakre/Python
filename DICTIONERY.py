# dictionary
# =============

# ** are used to store data value in "key: value" pair.

# ** properties:  unordered, mutable(changable), don't allow duplicate value. 


# dict1 = {
#     "name": "dhanesh",
#     "hobby": "cooking",
#     "marks": [67, 87, 97]    #dictioneries can contain lists, dictionery,tuple
# }

# info = {
#     "key": "value",
#     "name": "Ram",
#     "age": "34",
#     "marks": "9.8",
#     "tuple": (33, 30, 89, 84, 67),
#     "list": ["ram", "shayam", "radha"],
#     "yes": True
# }

# # print(info)

# info["name"] = "dhanesh"  #assigns new value to the key and name is changed.
# print(info)

# NOTE: we cannot use list and dictionery as keys.




# null sictionery
# =================
# null = {}
#                             #adding values to null dictionery
# null["name"] = "raju"     
# null["job"] = "coder"
# null["age"] = 45

# print(null)         #returns {'name': 'raju', 'job': 'coder', 'age': 45}




# NESTED DICTIONERY:
# ======================(dictionery within dictionery)

# student = {
#     "name": "Dhanesh",
#     "score":{
#         "math": 98,        #this is nested dictionery
#         "science": 89,
#         "social": 78,
#         "history": 89,
#         "physics": 98
#     },
#     "surname": "sakre"
# }

# print(student)



# dictionery methods:
# =====================

# dict.keys() #returns all main keys

# dict.value()    #returns all values

# dict.items() #returns all pairs (key: value) as tuple

# dict.get("key")  #returns key according to value

# dict.update(new_dict)       #insert specific items to the dictionery


# student.update({"city": "mumbai"})   #added new dictionery

# print(student)      returns {'name': 'Dhanesh', 'score': {'math': 98, 'science': 89, 'social': 78, 
#                                                           'history': 89, 'physics': 98}, 'surname': 'sakre', 'city': 'mumbai'}