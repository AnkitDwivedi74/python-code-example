## if else 
####################################################  CODE  ####################################################
###### if #####

# a = 33
# b = 200
# if b > a:
#   print("b is greater than a")
  
#####     Elif
##   The elif keyword is pythons way of saying "if the previous conditions were not true, then try this condition

# a = 33
# b = 33
# if b > a:
#   print("b is greater than a")
# elif a == b:
#   print("a and b are equal")

## Else
### The else keyword catches anything which isn't caught by the preceding conditions

# a = 200
# b = 33
# if b > a:
#   print("b is greater than a")
# elif a == b:
#   print("a and b are equal")
# else:
#   print("a is greater than b")

############

# a = 200
# b = 33
# if b > a:
#   print("b is greater than a")
# else:
#   print("b is not greater than a")

### Short Hand If
#  If you have only one statement to execute, you can put it on the same line as the if statement

# a = 200
# b = 33
# if a > b: print("a is greater than b")

## Short Hand If ... Else
# If you have only one statement to execute, one for if, and one for else, you can put it all on the same line

# a = 2
# b = 330
# print("A") if a > b else print("B")




################## and #############

# a = 200
# b = 33
# c = 500
# if a > b and c > a:
#   print("Both conditions are True")
  
####################### or ###################

# a = 200
# b = 33
# c = 500
# if a > b or a > c:
#   print("At least one of the conditions is True")
        
################################################  Nested If..else.. ##########################################################
# You can have if statements inside if statements, this is called nested if statements 
# We can have a if...elif...else statement inside another if...elif...else statement. This is called nesting in computer programming

# x = 41
# if x > 10:
#   print("Above ten,")
#   if x > 20:
#     print("and also above 20!")
#   else:
#     print("but not above 20.")

####################################

# num = float(input("Enter a number: "))
# if num >= 0:
#     if num == 0:
#         print("Zero")
#     else:
#         print("Positive number")
# else:
#     print("Negative number")