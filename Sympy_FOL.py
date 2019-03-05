import sympy
import numpy
import pandas as pd
import itertools
from sympy import  *
from sympy.parsing.sympy_parser import parse_expr




# Input the number of students (num_students). 
# One is added because we start counting from 1. But python starts counting from 0

num = int(input("Number of people on campus :"))+1

variables = ['a{}'.format(i) for i in range(1, num)]

############################################################
#### START : USER DEFINED  PREDICATES AND CONSTRAINTS  #####
############################################################

#Predicates with arity equal to ONE: Professor, Course and Student 

unary_predicates = ['professor', 'course' , 'student']

for predicate in unary_predicates:
        unary_atomic_formulas   =  [str(predicate)+'_{}'.format(i) for i in variables]
        

#Predicates with arity equat to TWO : 

binary_predicates = ['teaches', 'attends', 'freindship']

for predicate in binary_predicates:
        binary_atomic_formulas   =  [str(predicate)+'_{}'.format(i) for i in variables]



#Constraints in conjunction 

constraint = '(professor_{} | course_{} | student_{}) & (professor_{} >> ~course_{}) &  (professor_{} >> ~student_{}) &  (student_{} >> ~ course_{}) & (teaches_{}_{} >> (professor_{} & student_{})) & (attends_{}_{} >> (student_{} & course_{}))'


################################################################
####     START : GROUNDING THE PREDICATES AND CONSTRAINTS   ####                                
################################################################

##############################################################################
# NOTE : THE PROCESS OF GROUNDING TAKES PLACE IN TWO STAGES               ####
# 1. GENERATE A STRING FOR THE FORMULA TO BE GROUNDED                     ####
# 2. DEFINE THE STRING AS A SYMBOL IN ORDER TO PARSE COMPLEX FORMULAS     ####
##############################################################################




# GENERATE GROUNDED  UNARY PREDICATE STRINGS
for predicate in unary_predicates:
        pred_list   =  [str(predicate)+'_{}'.format(i) for i in variables]

# GENERATE GROUNDED BINARY PREDICATE STRINGS
for predicate in binary_predicates:
        pred_list_1   =  [str(predicate)+'_{}_{}'.format(i[0],i[1]) for i in itertools.product(variables, repeat = 2)]
        pred_list = pred_list + pred_list_1


# CONVERT THE GROUNDED ATOMIC FORMULAS TO SYMPY SYMBOLS
atomic_formulas = symbols(pred_list)


# GENERATE GROUNDED CONSTRAINTS AS STRINGS

for var in variables:
    
    constraints =  [constraint.format(i[0],i[0],i[0],i[0],i[0],i[0],i[0],i[0],i[0],i[0],i[1],i[0],i[1],i[0],i[1],i[0],i[1]) for i in itertools.product(variables, repeat = 2)]



####################################################################
####### DEFINING QUATIFIERS : FOR EVERY <==>  CONJUNCTION  #########
#######                    THERE EXISTS <==>  DISJUNCTION  #########
####################################################################
 

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

        with evaluate(False):
            expr = True
            for i  in range(0, len(x)):
                expr = (expr & (x[i]))

            return expr


###################################################################

expr = conjunction(constraints)
print(expr)
with evaluate(True):
    models = satisfiable(expr, all_models = True)

truth_table = list(models)

truth_table = pd.DataFrame(truth_table)

print(truth_table)
