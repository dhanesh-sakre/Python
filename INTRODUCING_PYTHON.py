# Python:-->
# print("hello world...!")

# characterstics:
#         * Case sensitive language
#         * Typed language(implicit)
#         * Simple and easy
#         * free and open source
#         * developed by Guido Van Rossum

#     character sets:
#              letters: a to z   and  A to z
#              digits : 0 to 9

            
#      special symbols : +, -, *, / etc
#         white space : blank space, tab, return, newline, formfeed
#         other characters : all ASCII and Unicode characters

#         variables :
#                 a variable is a name given to a memory location in a programming.
#                     name = "dhanesh sakre"
#                     age = 26
#                     focus = growth mindset
#         data types:
#                     1. integer (int)
#                     2. string (str)
#                     3. float (11.11)
#                     4. boolean(true/false)
#                     5. none (a = none)

#         keywords : reserved words in python
#                     and          else       in      return    assert     is   true      except
#                     false        break      class   continue    def     del   if    else     elif
#                     finally      for        form    global      as      import      lambda      nonlocal
#                     none        not         or      pass        raise   try        with     while   yeild



#         types of tokens:->

#1. Punctuators: 
#             punctuators are symbols to organize structures in programming.
#             (), {}, [], #, @,  -=, +=, *=, /=, //=  etc..



# 2. E xpression execution:

# A, B = 2, 3
# txt = "@"
# print(A*B*txt) #gives us @@@@@@



# 3. string and string can operate with "+"

# A, B = "2", 3
# Txt = "@"
# print(A + Txt) #gives us 2@
# print((A + Txt)* B) #gives us 2@2@2@


# 4. Numeric values can operate with all arithmetic operators:

# A, B = 2, 4
# C = 8
# print(A+B*C) # GIVES US 34

                                    
# 5. Arithmetic expressions with integer and float will result in float:

# A, B = 10, 5.5
# print(A*B) #gives us 55.0



#  6. Result of division operator with two integers will be float
# A, B = 5, 2
# div = A/B
# print(div) #gives us 2.5


# 7. floor gives us closest integer value which is lesser than or equals to the float value
# A, B = 7, 3
# C = 7 // 3
# print(C) #gives us 2


# 8. Modulas to get the remainder
# A, B = 7, 2
# mod = A%B
# print(mod) #gives us 1 as remainder


# 9. result of " A//B " is same as "floor(A/B)"



# COMMENTS in pthon:
#                 1. single line comment : #single line comment

#                 2. multi-line comment: """ this is
#                                         multi-line
#                                         comment
#                                                 """



# TYPES OF OPERATIONS:

# 1. Arithmetic (+, -, *, /,  //, %, **) 

#NOTE: ** means power
# A, B = 2, 4
# power = A ** B
# print(power)            #gives us 16

# 2. Relation/comparsion operators(==, !=, >=, <=, <, >)

# 3. Assignment Operators :(+=, -=, *=, /=, //=, %=, **=)

# 4. Logical Operators (not, and, or)

# 5. Membership operators: (in, not in)

# 6. Identity operators: (is, is not)

# 7. Bitwise operators ( .(period)  &(ampersand)  | (vertical bar)  ^ (conjuction) )





# SEPERATORS-->         Syntax: 
# ==============                 sep = "~"

# print(5, 6, 7, 9, "hey!", sep="~")      #returns 5~6~7~9~hey!



# end statement --->
# ==============               syntax:
# #                                     end =" "
# NOTE: by default there is a synax (/n) at the end to add new line. If we don't wnat
# to add next line and want to print item in the same line the we use ending statment:

# print("hello...!")             #returns   hello...!
# print("world")                            world

                                
# print("hello...!", end=" ")      #returns
# print("world")                            hello...! world
                                  