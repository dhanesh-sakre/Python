# strins:
#===========
#         string is a data type that is stores a sequence of characters.



# BASICS POERATAIONS ON PYTHON:
#===============================

# # 1. CONCATENATION:
# con = "Dhanesh" +" " + "Sakre"
# print(con)          #returns us:    Dhanesh Sakre

# 2. print lenghth of a String 

# location = "India"
# length = len(location)
# print(length)       # output is:  5



# INDEXING:
# ==============

#             in the string characters are indexed(in a sequence).
# # in simple words they are assigned an identity.
# stirngg = "alpha+bita"
#       # 0123456789 

# str1 = "progress"

# first = str1[0]
# print(first)    #gives us "p" which is at the 0th index
# second = str1[1]
# print(second)   #gives us "r" which is at the 1st index



# SLICING:
# ==========
#         accessing parts of a string.

# syntax =>     string[starting_index : ending_index]

#NOTE: ending index is not included.


# str2 = "strength"
# let = str2[0 : 5]     
# print(let)              #returns us "stren"


#NOTE
# let = str2[0 : 5] 
#                   is same as 
# let = str2[ : 5]
                    #or
# let = str2[0th_index : 5]              


#NOTE
# let = str2[4 : ]
                    # is same as  
# let = str2[4 : 8]
                    # or
# let = str2[4 : len(str2)] 




# NEGETIVE_SLICING =>
# ===================

# "STRONG" => S   T  R   O   N   G
          #  -6  -5 -4  -3  -2  -1 (negetive indexing)

# ste = "STRONG"

# print(ste[-5 : -1])   #returns us "TRON"

# print(ste[-6 : ])       #returns us "STORNG" 
#            # this is same as 
#  print(ste[-6 :len(ste)])


# STRING_FUNCTIONS :
# ===================
str = "i am a sharp coder"

# 1. endswith         -------> #returns boolean value(true/false)
# print(str.endswith("er"))    #true
# print(str.endswith("et"))     #false


# 2.  capitalize     ------> #print(str.capitalize())
# print(str.capitalize())         #capitalized first letter of the sentence
                                # I am a sharp coder


# 3.replace    ------->    str.roplace(old, new)
# print(str.replace("am", "is"))      #i is a sharp coder


#4. find      ------->  # print(str.find("substirng"))
# print(str.find("am"))    #returns 1st index of 1st occurance of the word

# 5. count      ------->   #print(str.count(substirng))
# print(str.count("am"))    #counts the occurance of the substring

# 6. centre    ------> # print(str.center(spaces)) 
# print(str.center(50))      #50 is the vlaue of spaces 
                            #it centres the string

                            

