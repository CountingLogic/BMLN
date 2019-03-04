import sympy
import itertools
from sympy import  *
from sympy.parsing.sympy_parser import parse_expr




# Input the number of students (num_students). 
# One is added because we start counting from 1. But python starts counting from 0

num = int(input("Number of people on campus :"))+1

variables = ['a{}'.format(i) for i in range(1, num)]

#variables = symbols(variables)
#print(variables)

############# 
###ATOMIC ###
##FORMULAS###
#############

#professor(x)
#student(x)
#course(x)
#teaches(x,y)
#attends(x,y)



#Predicates with arity equal to ONE: Professor, Course and Student 
for var in variables:
    professor =  ['professor_{}'.format(i) for i in variables]
    course =  ['course_{}'.format(i) for i in variables]
    student  =  ['student_{}'.format(i) for i in variables]

professor = symbols(professor)
course =  symbols(course)
student = symbols(student)
 
 

#print(parse_expr(professor[0]))





for var in variables:
    constraint_1 =  ['professor_{} & course_{} & student_{}'.format(i,i,i) for i in variables]
    #constraint_2 =  ['professor_{} >> (~ course_{})'.format(i,i[1]) for i in itertools.product(variables, repeat = 2)]
    constraint_2 =  ['professor_{} >> (~ course_{})'.format(i,i) for i in variables]
    constraint_2 =  ['professor_{} >> (~ course_{})'.format(i,i) for i in variables]
    constraint_2 =  ['professor_{} >> (~ course_{})'.format(i,i) for i in variables]






print(constraint_1[1])

print(parse_expr(constraint_1[1]))

 

#Predicates with arity equal to TWO : Teaches, Attends

#cross_product = itertools.product(variables, repeat = 2)
#
#teaches = ['Teaches({}) >> (Professor({}) &  '.format(i[0]) for i in cross_product]
#
#cross_product = itertools.product(variables, repeat = 2)
#
#attends =['Attends({})'.format(i) for i in cross_product]
#
#print(teaches)
#print(attends)
# 
 


    

x = symbols('x')
y = symbols('y')
z = symbols('z')

f = Function('f')
print(sympy.__version__)


class disjuncition(Function):
    @classmethod 
    def eval(cls, x):

        with evaluate(False):
            expr = False
            for i  in range(0, len(x)):
                expr = (x[i]|expr)
            
            print(expr)

            return expr

class conjunction(Function):
    @classmethod 
    def eval(cls, x):

        with evaluate(True):
            expr = True
            for i  in range(0, len(x)):
                expr = (x[i] & expr)
            
            print(expr)

            return expr



expr = conjunction(constraint_1)

with evaluate(False):
    models = satisfiable(expr, all_models = True)

for model in models:
    print(model)
