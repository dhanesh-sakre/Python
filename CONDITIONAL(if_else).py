# conditional statement:
# ======================== syntax---> (if,elif, else)

# if(condition):
#     statement1

# elif(condition):
#     statement2

# else:
#     statementN

# --------------------------------------------

#     example:(1)
#     =========

# age = int(input("type your age here: "))

# if (age >= 18):
#     print("eligible for vote")
# elif(age < 18):
#     print("not eligble")
# else:
#     print("invalid voter")


    # example: (2)
    # ============= traffic signal


# light = input("signal colour: ")
# if (light == "red"):
#     print("please stop")
# elif( light == "green"):
#     print("you can go")
# elif( light == "yellow"):
#     print("please look around")
# else:
#     print("light is broken")




# SINGAL LINE IF or TERNARY OPERATOR:--->
# ======================================

# case(1):
# <var> = <var1> if <condition> else <val2>

# food = input("your favourite food: ")
# eat = "yes" if food == "cake" else "no"
# print(eat)


# case(2):
# ========

# <statement1> if <condition> else <statement2>

# food = input("food:")
# print("sweet") if food == "cake" or food == "jalebi" else print("not sweet")



# case(3):
# # =========
# <variable> = (FalseValue, TrueValue) [<condition>]

# example(1):--->
# age = int(input("age: "))
# vote = ("yes", "no") [age<18]
# print(vote)


# sal = float(input("your salary is :"))
# tax = sal*(0.1, 0.2) [sal > 50000]      #if salary is less than 50k, tax 10%
# print(tax)                                #if salary is more than 50k, tax 20%

# example:(3)----> 
# age = int(input("entre your age here: "))
# if (age>=18):
#     vote= "yes"
# else:
#     vote= "no"
# print(vote)
