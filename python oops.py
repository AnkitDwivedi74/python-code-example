######################################    PYTHON OOPS    ###############################################

############ CLASS   ###################################################################################

# class MyClass:
#   x = 5
# print(MyClass)


##############################################
# class MyClass:
#   x = 5
# print(MyClass.x)

########################   OBJECT   ####################################################################

# class MyClass:
#   x = 5
# p1 = MyClass()
# print(p1.x)

########################################################################################################

################################   SELF  #############################################################
#it is clearly seen that self and obj is referring to the same object​

#it is clearly seen that self and obj is referring to the same object

# class check:
# 	def __init__(self):
# 		print("Address of self = ",id(self))
# obj = check()
# print("Address of class object = ",id(obj))


#################        __init__ method    #################
# A Sample class with init method
# class Person:

# 	# init method or constructor
# 	def __init__(self, name):
# 		self.name = name
# 	# Sample Method
# 	def say_hi(self):
# 		print('Hello, my name is', self.name)
# p = Person('Nikhil')
# p.say_hi()

############################################################################################################################
############### Inheritance ################


# class baseClass:
#     print("Ankit")
# class derivedClass(baseClass):
#     pass
    

#####################  
# class Person:
#   def __init__(self, fname, lname):
#     self.firstname = fname
#     self.lastname = lname

#   def printname(self):
#     print(self.firstname, self.lastname)

# class Student(Person):
#   pass

# x = Student("Mike", "Olsen")
# x.printname()

##################################################

####################   Polymorphism ####################
# class Bird:

# 	def intro(self):
# 		print("There are many types of birds.")

# 	def flight(self):
# 		print("Most of the birds can fly but some cannot.")

# class sparrow(Bird):

# 	def flight(self):
# 		print("Sparrows can fly.")

# class ostrich(Bird):

# 	def flight(self):
# 		print("Ostriches cannot fly.")

# obj_bird = Bird()
# obj_spr = sparrow()
# obj_ost = ostrich()

# obj_bird.intro()
# obj_bird.flight()

# obj_spr.intro()
# obj_spr.flight()

# obj_ost.intro()
# obj_ost.flight()


###################################   Encapsulation #####################

# Python program to
# demonstrate private members

# Creating a Base class
# class Base:
# 	def __init__(self):
# 		self.a = "Hello"
# 		self.c = "Ankit"

# # Creating a derived class
# class Derived(Base):
# 	def __init__(self):

# 		# Calling constructor of
# 		# Base class
# 		Base.__init__(self)
# 		print("Calling private member of base class: ")
# 		print(self.c)

# # Driver code
# obj1 = Base()
# print(obj1.a)
# print(obj1.c)

# Uncommenting print(obj1.c) will
# raise an AttributeError

# Uncommenting obj2 = Derived() will
# also raise an AtrributeError as
# private member of base class
# is called inside derived class


###########################   DATA ABSTRACTION        ###################################
from abc import ABC, abstractmethod   
class Car(ABC):   
    def mileage(self):   
        pass  
  
class Tesla(Car):   
    def mileage(self):   
        print("The mileage is 30kmph")   
class Suzuki(Car):   
    def mileage(self):   
        print("The mileage is 25kmph ")   
class Duster(Car):   
     def mileage(self):   
          print("The mileage is 24kmph ")   
  
class Renault(Car):   
    def mileage(self):   
            print("The mileage is 27kmph ")   
          
# Driver code   
t= Tesla ()   
t.mileage()   
r = Renault()   
r.mileage()    
s = Suzuki()   
s.mileage()   
d = Duster()   
d.mileage()

############################  Child class ###################

# class Person:
#   def __init__(self, fname, lname):
#     self.firstname = fname
#     self.lastname = lname

#   def printname(self):
#     print(self.firstname, self.lastname)

# class Student(Person):
#   pass

# x = Student("Mike", "Olsen")
# x.printname()

#############################################################################################################################
# # A Sample class with init method
# class Person:
# 	# init method or constructor
# 	def __init__(self, name):
# 		self.name = name
# 	# Sample Method
# 	def say_hi(self):
# 		print('Hello, my name is', self.name)
# # Creating different objects
# p1 = Person('Nikhil')
# p2 = Person('Abhinav')
# p3 = Person('Anshul')
# p1.say_hi()
# p2.say_hi()
# p3.say_hi()


#######################################################################################################################
# class Parrot:

#     # class attribute
#     species = "bird"

#     # instance attribute
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

# # instantiate the Parrot class
# blu = Parrot("Blu", 10)
# woo = Parrot("Woo", 15)

# # access the class attributes
# print("Blu is a {}".format(blu.__class__.species))
# print("Woo is also a {}".format(woo.__class__.species))

# # access the instance attributes
# print("{} is {} years old".format( blu.name, blu.age))
# print("{} is {} years old".format( woo.name, woo.age))