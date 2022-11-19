#####  The bitwise operators perform bit by bit operation on the values of the two operands ####
                                
                                ##### OPERATORS  #########


## - AND                            ## - &
## If both the bits at the same place in two operands are 1, then 1 is copied to the result. Otherwise, 0 is copied

## - OR                             ## - |
## The resulting bit will be 0 if both the bits are zero; otherwise, the resulting bit will be 1

## - XOR                            ## - ^
## The resulting bit will be 1 if both the bits are different; otherwise, the resulting bit will be 0

## - NOT                            ## - ~
## It calculates the negation of each bit of the operand, i.e., if the bit is 0, the resulting bit will be 1 and vice versa

## - Zero fill left shift           ## - <<
## The left operand value is moved left by the number of bits present in the right operand

## - Signed right shift             ## - >>
## The left operand is moved right by the number of bits present in the right operand.

########################################################## CODE ##########################################################################################



# for i in range(101):
#     print("Binary value of ", i, " is: ", bin(i))






















x = 6
y = 3

############# AND (&)  ###################

print('and:', bin(x & y), x & y) 


###########  OR (|)  #####################
# print(bin(5)), bin(7)
# print('or:', bin(x | y), x | y)


################  XOR (^) ###################

# print('xor:', bin(x ^ y), x ^ y)

##################  NOT (~)  ##################
## it conatains only one operant flip the value 1 become 0 and 0 becomes 1

# print('not:', bin(~x), ~x)

################## Zero fill left shift (<<) ############################
## shift the bits to left / discard

# a = 20
# print(a<<2)

################################ right shift (>>) #####################################

# a = 20
# print(a>>2)






