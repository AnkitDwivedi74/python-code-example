#############################  Logical Operators ##################

#               OPERATORS     
#               
#               and (Returns True if both statements are true) 
#               or (Returns True if one of the statements is true)
#               not (Reverse the result, returns False if the result is true)       


############################################################### CODE ##################################################################################

#### and #####

x = 5
print(x > 3 and x < 10)
# returns True because 5 is greater than 3 AND 5 is less than 10

##### or ####

x = 5
print(x > 3 or x < 4)
# returns True because one of the conditions are true (5 is greater than 3, but 5 is not less than 4)

######## not #######

x = 5
print(not(x > 3 and x < 10))
# returns False because not is used to reverse the result