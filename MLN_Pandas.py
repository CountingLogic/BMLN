import pandas as pd
import numpy as np 
import itertools
import operator as op
import time

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
    df.loc[df["SIC_"+ person]==True,["SIC_"+ person]] = 1.5
    df.loc[df["SIC_"+ person]==False,["SIC_"+ person]] = 0


for Freindship in Freinds:

    df["FIS_"+ Freindship[1:3]] = IMPLIES(df[Freindship],(IMPLIES(df["S"+Freindship[1:2]], df["S"+ Freindship[2:3]]) & IMPLIES(df["S"+Freindship[2:3]], df["S"+ Freindship[1:2]])))

    df.loc[df["FIS_"+ Freindship[1:3]]==True,["FIS_"+ Freindship[1:3]]] = 1.4
    df.loc[df["FIS_"+ Freindship[1:3]]==False,["FIS_"+ Freindship[1:3]]] = 0

#df.loc[df["FIS_BC"]==True,["FIS_BC"]] = 100


#Initiating a column for probability to zero 
df['FIS_P']=0

for Freindship in Freinds:

    df['FIS_P'] = df["FIS_" + Freindship[1:3]] + df['FIS_P']

df['FIS_P'] = np.exp(df['FIS_P'])

df['SIC_P'] = 0


for person in Persons:
    df['SIC_P'] = df["SIC_" + person] + df['SIC_P']

df['SIC_P'] = np.exp(df['SIC_P'].astype(float))

df['Potential'] = df['FIS_P'] * df['SIC_P']

#Power of pandas : THis step is much faster then looping 
Z = df['Potential'].sum()

df['P']  =  df['Potential']/Z 

#print(df)

#print(df['P'].sum())

#print(df['P'].min())

#Again loop is not running on cells but columns, the cells are operated on in a vectorised manner 
for Freindship in Freinds:

    df["FIC_"+ Freindship[1:3]] = IMPLIES(df[Freindship],(IMPLIES(df["C"+Freindship[1:2]], df["C"+ Freindship[2:3]]) & IMPLIES(df["C"+Freindship[2:3]], df["C"+ Freindship[1:2]])))
    df.loc[df["FIC_"+ Freindship[1:3]]==True,["FIC_"+ Freindship[1:3]]] = 1
    df.loc[df["FIC_"+ Freindship[1:3]]==False,["FIC_"+ Freindship[1:3]]] = 0

df['FIC_P'] = df['P']*df['FIC_AC']*df['FIC_AB']*df['FIC_BC']
#df['FIC_AB_BC_P'] = df['P']*df['FIC_AB']*df['FIC_BC']
#df['FIC_AB_P'] = df['P']*df['FIC_AB']
 
t1 = time.clock()

total = t1 - t0
#print(df.head())
print(total)

#print(df['FIC_AB_P'].sum())

#print(df['FIC_AC'])
