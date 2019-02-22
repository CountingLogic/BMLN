import numpy as np
import pandas as pd
from itertools import product
from inspect import  signature

def AND(x,y):
    return np.multiply(x,y)

def OR(x,y):
    z = x+y
    z[z > 1] = 1
    return z
    
def NOT(x):
    x = x + np.ones(len(x), dtype = np.int32)
    x[x == 2] = 0
    return x

a = np.array([0, 0, 1, 1])
b = np.array([0,1,0,1])
print(a)
print(b)
print(NOT(AND(a, NOT(b))))




def truth_table(f):
    values = []
    for x in product([False, True],repeat= len(sig.parameters)):
        values = [list(x) + [f(*x)]]+values
        df = pd.DataFrame(values, columns = (func_args + [f.__name__]))
        print(type(df[f.__name__]))
    return df


#print(truth_table(OR))








