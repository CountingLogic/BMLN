import pandas as pd
import numpy as np
import itertools
import operator as op
from pyDatalog import pyDatalog
from sympy import symbols



pyDatalog.create_terms('x,y,z')
B = [True, False]

print((( x._in(B) & (y._in(B) & z._in(B) )) | ( ~x._in(B) & (~y._in(B)  & ~z._in(B) )) |  ( ~x._in(B) & (y._in(B)  & z._in(B) ))))



print((X._in(allvalues)) & (Y._in(allvalues)))

x,y,z = symbols('x,y,z')
EXPR = (( x & (y & z )) | ( ~x & (~y  & ~z )) |  ( ~x & (y  & z )))     
Groundings = EXPR.atoms()
print(Groundings)

df = pd.DataFrame(list(itertools.product([True, False], repeat = len(Groundings))), columns=Groundings)

substitutions = df.to_dict(orient = 'records')

print(substitutions)

for i in substitutions:
    print(i)
    #print(substitutions[i])
    print(EXPR.subs(i))

