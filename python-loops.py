##################  PYTHON LOOPS  #################################

############     WHILE
############     FOR
############     NESTED LOOPS

#######################      WHILE       ############################

i = 1
while i < 6:
  print(i)
  i += 1
  
#############################  While break 

i = 1
while i < 6:
  print(i)
  if (i == 3):
    break
  i += 1


############################## continue while

i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)

# Note that number 3 is missing in the result


##############################   else while

i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")





