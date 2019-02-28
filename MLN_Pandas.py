import pandas as pd
import numpy as np 
import itertools
import operator as op
import jedi
import time 
jedi.preload_module('pandas','numpy', 'itertools', 'operator')

t0 = time.clock()
IMPLIES = lambda x,y : ~(op.and_(x,~y))



Persons = ['A', 'B', 'C']
Smokes = ["S"+ x for x in Persons]
Cancer  = ["C"+ x for x in Persons]
Freinds = ["F" + "".join(a) for a in itertools.combinations(Persons, 2)]
Groundings  = Smokes + Cancer + Freinds

df = pd.DataFrame(list(itertools.product([False, True], repeat = len(Groundings))), columns=Groundings)


#Running loop over persons to define columns, not time consuming only trivial naming
for person in Persons :
    df["SIC_"+ person] = IMPLIES(df["S"+person],df["C"+ person])
    #df.loc[df["SIC_"+ person]==True,["SIC_"+ person]] = 1.5
    #df.loc[df["SIC_"+ person]==False,["SIC_"+ person]] = 0


for Freindship in Freinds:

    df["FIS_"+ Freindship[1:3]] = IMPLIES(df[Freindship],(IMPLIES(df["S"+Freindship[1:2]], df["S"+ Freindship[2:3]]) & IMPLIES(df["S"+Freindship[2:3]], df["S"+ Freindship[1:2]])))

    #df.loc[df["FIS_"+ Freindship[1:3]]==True,["FIS_"+ Freindship[1:3]]] = 1
    #df.loc[df["FIS_"+ Freindship[1:3]]==False,["FIS_"+ Freindship[1:3]]] = 0
#print(df.head())
#df.loc[df["FIS_BC"]==True,["FIS_BC"]] = 100

MLN_FORMULAS = df.loc[:, df.columns.str.startswith(('FIS','SIC'))]
n1 = len(df.columns[pd.Series(df.columns).str.startswith('SIC')])
n2 = len(df.columns[pd.Series(df.columns).str.startswith('FIS')])
weights = np.array([1.5, 1.4])
w_matrix =np.repeat(weights,[n1,n2])
w_matrix = pd.DataFrame(w_matrix)
#print(w_matrix)



#print(MLN_FORMULAS.head())
#print(MLN_FORMULAS.shape)
P = np.exp(np.matmul(MLN_FORMULAS, w_matrix))
P = np.stack(P,axis = 1 )
#print(type(P[0]))
P = P[0]
#print(len(P))
#MLN_FORMULAS['Probability'] = P
df['Potential'] = P
df['Probability'] = P/df['Potential'].sum()
#print(df.head())


for Freindship in Freinds:

    df["FIC_"+ Freindship[1:3]] = IMPLIES(df[Freindship],(IMPLIES(df["C"+Freindship[1:2]], df["C"+ Freindship[2:3]]) & IMPLIES(df["C"+Freindship[2:3]], df["C"+ Freindship[1:2]])))
    #df.loc[df["FIC_"+ Freindship[1:3]]==True,["FIC_"+ Freindship[1:3]]] = 1
    #df.loc[df["FIC_"+ Freindship[1:3]]==False,["FIC_"+ Freindship[1:3]]] = 0

df['FIC_P'] = df['Probability']*df['FIC_AC']*df['FIC_AB']*df['FIC_BC']

#print(df.head())
#df['FIC_AB_BC_P'] = df['P']*df['FIC_AB']*df['FIC_BC']
#df['FIC_AB_P'] = df['P']*df['FIC_AB']
 


#print(df['FIC_AB_P'].sum())


#print(df.filter(regex=r'^SIC\.', axis=1))

t1 = time.clock()

total = t1 - t0
print(total)
