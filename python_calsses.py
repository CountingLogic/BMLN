# https://docs.python.org/3/tutorial/classes.html
# Classes : Python documentation 
# Pyhton Objects have individuality, and multiple names (in different scopes) can be bound to the same object 


###################### Mutable vs Immuatable #####################
# In python strings are immutable 
try:
    message = "strings immutable"
    message[8] = ' '
    print(message)

except:
    print(message)

# In python tupples are immutable and lists are mutable
try:
    my_tupple = (5,4,5)
    my_tupple[0] =  1

except:
    print(my_tupple[0] == 1)

#If you want to write most efficient code, you should be the knowing difference between mutable and immutable in python. Concatenating string in loops wastes lots of memory , because strings are immutable, concatenating two strings together actually creates a third string which is the combination of the previous two. If you are iterating a lot and building a large string, you will waste a lot of memory creating and throwing away objects. Use list compression join technique.
#
#Python handles mutable and immutable objects differently. Immutable are quicker to access than mutable objects. Also, immutable objects are fundamentally expensive to "change", because doing so involves creating a copy. Changing mutable objects is cheap.
##################################################################

###################### Namspaves in Python #######################
# Namespace is a mapping from names to objects. Namespaces are about global and local declaration of variables
# They key thing is that varibales defined in different scopes are independent of each other
# A function func defined in class_1 and func defined in class_2 are independent and can be asseced as class_1.func

####################### Scope and NameSpace  #########################
#A special quirk of Python is that – if no global statement is in effect – assignments to names always go into the innermost scope. Assignments do not copy data — they just bind names to objects. The same is true for deletions: the statement del x removes the binding of x from the namespace referenced by the local scope. In fact, all operations that introduce new names use the local scope: in particular, import statements and function definitions bind the module or function name in the local scope.

#The global statement can be used to indicate that particular variables live in the global scope and should be rebound there; the nonlocal statement indicates that particular variables live in an enclosing scope and should be rebound there.

def scope_test():
    def do_local():
        spam = "local spam"

    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"

    def do_global():
        global spam
        spam = "global spam"

    spam = "test spam"
    do_local()
    print("After local assignment:", spam)
    do_nonlocal()
    print("After nonlocal assignment:", spam)
    do_global()
    print("After global assignment:", spam)

scope_test()
print("In global scope:", spam)



##################################### CLASS DEFINITION AND SYNTAX ###########################

'''A class defines its own scope'''

class MyClass:
    """ A simple example class"""

    i = 12345

    def f(self):
        return 'hello world'

#Creating an object. This will create an empty object 


class MyClass_1:
    """ A simple example class"""

    i = 12345
#Self
    def __init__(self):
        self.data = []

    def f(self):
        return 'hello world'
#self helps us create instance based variables 

x = MyClass_1()

# Data attributes need not be defined they can just spring into existence

x.counter = 1
while x.counter < 12:
    x.counter = x.counter * 2
print(x.counter)
del x.counter


# A method is a function that belongs to a certain object 

print(x.f())

#self is the instance of the object 
# Note that class variables must nor be immutable 

class Dog_wrong:

    tricks = []             # mistaken use of a class variable

    def __init__(self, name):
        self.name = name

    def add_trick(self, trick):
        self.tricks.append(trick)







class Dog_right:
    kind = [1,2,3]
    def __init__(self, name):
        self.name = name
        self.tricks = []    # creates a new empty list for each dog

    def add_trick(self, trick):
        self.tricks.append(trick)

#Data attribute override class attribute when overloaded
#Capitalise method names
#Prefix attribtes with a unique string 
d = Dog_right('Fido')
print(d.name)
print(d.kind)

b = Dog_right('Dodo')
print(b.kind)

d.kind = [1,2,2]
print(b.kind)
print(d.kind)

def reverse(data):
    for index in range(len(data)-1, -1, -1):
        print(index)
        yield data[index]

for char in reverse('golf'):
    print(char)
