# LOGICAL OPERTORS :
# ===================
                        # NOT,  AND,  OR

# 1.  NOT ---> returns opposite value
#   -------
# [not True = False]

# print(not False)        --> returns True
# print(not True)           --> returns False


# 2. AND ---> returns value on the basis of conditions:
#         True and True = True
#         True and False = False
#         False and False = False
#         False and True = False

# 3. OR ---> returns value on according to the case:
#         True or True = True
#         True or False = True
#         False or False = False
#         False or True =  True



# EXAMPLES:
# =========
# a = 67
# b = 89
# c = 90
# print("and operator :", (a < b) and (a < c))     #returns True
# print("and operator :", (a < b) and (a > c))     #returns False
# print("and operator :", (a > b) and (a < c))     #returns False
# print("and operator :", (a > b) and (a > c))     #returns False

# print("and operator :", (a < b) or (a < c))      #returns True
# print("and operator :", (a < b) or (a > c))      #returns True
# print("and operator :", (a > b) or (a > c))      #returns False
