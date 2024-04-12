#   LIST in python:
# =================

# A built-in data type that stores set of values.
# It can store elements of different types(int, float, stirng.. etc).

# examples:-->

# marks = [67, 79, 97, 56, 89, 45, 90, 56, 67, 79, 67]        #int values

# students = ["Karan", "Arjun", "Ram", "Delhi", "Jhumritaliaya"]  #string values

# bio = ["Radhika", 25.5, "dist. Rampur"]           #float and string values




# LIST INDEXING:--->
#===============
# bio = ["Radhika", 25.5, "dist- Rampur", 92]
#         0           1       2           3         #index




# LIST SLICING:--->
#=================== 

#it is similar to list slicing.

# syntax:-->     list_name[starting_idx : ending_idx]
                      
#                       #NOTE: ending index is not included
                       

# bio = ["Radhika", 25.5, "dist. Rampur", 33]
# print(bio[1])                                  #returns 25.5


# marks = [67, 79, 97, 56, 89, 45, 90, 56, 67, 79, 67]
# slice1 = marks[3 : 7]
# print(slice1)                         #returns [56, 89, 45, 90]

# slice2 = marks[ : ]         #returns complete list
# print(slice2)           #[67, 79, 97, 56, 89, 45, 90, 56, 67, 79, 67]

# slice3 = marks[ : 8]            #1st to 7th index tak
# print(slice3)                  # [67, 79, 97, 56, 89, 45, 90, 56]


# # NEGETIVE SLICING:---->
# NUM = [ 56, 89, 45, 90, 56, 67, 79, 67]
# print(NUM[-5 : -2])                         #returns [90, 56, 67]




# LENGTH OF LIST:-->
#=====================
# marks = [67, 79, 97, 56, 89, 45, 90, 56, 67, 79, 67]
# print(len(marks))                                       #returns 11



# LIST METHODS:-->
# # =========================
marks = [67, 79, 97, 56, 89, 45, 90, 56, 67, 79, 67]

# 1.APPEND
# marks.append(76)
# print(marks)            #appends value at the end of list
                        #returns [67, 79, 97, 56, 89, 45, 90, 56, 67, 79, 67, 76]

# 2. SORT ASCENDING
# marks.sort()
# print(marks)       #sorts in ascending order
                    #[45, 56, 56, 67, 67, 67, 79, 79, 89, 90, 97]

# 3. SORT DESCENDING
# marks.sort(reverse=True)
# print(marks)                #[97, 90, 89, 79, 79, 67, 67, 67, 56, 56, 45]




# 4. REVERSE

# marks.reverse()
# print(marks)        #[67, 79, 67, 56, 90, 45, 89, 56, 97, 79, 67]




# 5. INSERT

# syntax:-->
# #             list.insert(index, element)
# marks.insert(5, "Ram")
# print(marks)                [67, 79, 97, 56, 89, 'Ram', 45, 90, 56, 67, 79, 67]




# 6. REMOVE
# syntax:-->    list.remove(element)
#         
# marks.remove(89)
# print(marks)        #[67, 79, 97, 56, 45, 90, 56, 67, 79, 67]



# 7. POP
# syntax:-->    list.pop(index)
                                #removes elements at index
# marks.pop(0)
# print(marks)    #[79, 97, 56, 89, 45, 90, 56, 67, 79, 67]


