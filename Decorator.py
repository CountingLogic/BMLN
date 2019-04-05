
# Functions can be as variable 

def greet(name):
    return "hello   "+name

greet_someone = greet

print(greet_someone("John"))

#Functions can be defined inside other functions

def greet(name):
    def get_message():
        return "Hello  "

    result = get_message()+name
    return result

print(greet("John"))


def greet(name):
    return "Hello"+name


