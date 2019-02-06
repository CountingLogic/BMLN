
from sympy import*
import numpy
import math
import itertools

################################# True Predicate Grounding goes here ############################

global Smokes
Smokes = {
        "Anna": True,
        "Bob": False,
        "Clara": True,
         }
global Cancer
Cancer = {
        "Anna": True, 
        "Bob": True,
        "Clara": True,
        }

global Freindship
Freindship = {

        "Anna,Anna": True, 
        "Anna,Bob": True,
        "Anna,Clara": True, 
        "Bob,Anna": True,
        "Bob,Clara": True, 
        "Bob,Bob": True,
        "Clara,Clara": True,
        "Clara,Bob": True,
        "Clara,Anna": True,

        } 


##################################  End Predicate Grounding #####################################


################################## Weights #####################################################
Weight = {
        "SmokingImpliesCancer": 1.5,
        "FreindshipImpliesSmoking": 0.5,

        }
################################# End Weights ######### #########################################



################################# Smoking(x) => cancer(x) #######################################


def SmokingImpliesCancer(x_):
    
    x = Symbol('x')
    y = Symbol('y')
    
    x = Smokes[x_]
    y = Cancer[x_]

    return(Implies(x,y))
################################################################################################


########################### Freindship(x,y) => (Smoking(x) <=> Smoking(y))#######################

def FreindshipImpliesSmoking(x_, y_ = "0"):
 
    if y_ == "0":
        pair = x_.split(',')
        x_ = pair[0]
        y_ = pair[1]

    x = Symbol('x')
    y = Symbol('y')
    z = Symbol('z')

        
    x = Smokes[x_]
    y = Smokes[y_]
    z = x_ +","+ y_ 
  
    if Freindship[z] == True:
        return(Implies(x,y) & Implies(y,x))
    #Should it really be True if there is no freindship
    elif Freindship[z] == False:
         return True

#################################################################################################
def FreindshipImpliesCancer(x_, y_ = "0"):
 
    if y_ == "0":
        pair = x_.split(',')
        x_ = pair[0]
        y_ = pair[1]

    x = Symbol('x')
    y = Symbol('y')
    z = Symbol('z')

        
    x = Cancer[x_]
    y = Cancer[y_]
    z = x_ +","+ y_ 
  
    if Freindship[z] == True:
        return(Implies(x,y) & Implies(y,x))
    #Should it really be True if there is no freindship
    elif Freindship[z] == False:
         return True



###################################### Weighted Potential: exp(w_i*f_i)##########################

def Weighted_Potential(Instance, Formula):
    #We need formula name for the weights dictionaries
    if Formula(Instance):
        if Formula.__name__ in list(Weight.keys()):
            return math.exp(Weight[Formula.__name__])
        else:
            return math.exp(0.5)
    else: 
         return math.exp( 0)

#################################################################################################
   

############################### Summation over weighted potential: Energy  ##################################################### Summation runs over all the given groundings ####################

def Energy_Formula(Grounding, Formula):

    Energy = 1
    for key, value in Grounding.items():
        Energy = Energy*(Weighted_Potential(key, Formula))

    return Energy

Energy_log = []
def Energy_True():  

    Energy_true = Energy_Formula(Smokes, SmokingImpliesCancer)*Energy_Formula(Freindship, FreindshipImpliesSmoking)
    Energy_log.append(Energy_true)
    return Energy_true

################################################################################################
print("True Enegy for Smoking Implies Cancer") 
print(Energy_Formula(Smokes, SmokingImpliesCancer), "\n")

print("True Enegy for Freindship Implies Smoking") 
print(Energy_Formula(Freindship, FreindshipImpliesSmoking), "\n")

print("Total true Energy")
True_Energy = Energy_True() 
print(Energy_True(), "\n")
  
x = Symbol('x')
models = satisfiable((x >> x), all_models = True)
print(list(models))
#################################### Model Counting and Partiton ###############################

def Partition():
    Partition = 0
    for i in itertools.product([True,False], repeat=15):
        i = list(i)
        global Smokes
        Smokes = {
                "Anna": i[0],
                "Bob": i[1],
                "Clara": i[2],
                 }
        global Cancer
        Cancer = {
                "Anna": i[3], 
                "Bob": i[4],
                "Clara": i[5],
                }
        global Freindship
        Freindship = {
        
                "Anna,Anna": i[14], 
                "Anna,Bob": i[6],
                "Anna,Clara": i[7], 
                "Bob,Anna": i[8],
                "Bob,Clara": i[9], 
                "Bob,Bob": i[10],
                "Clara,Clara": i[11],
                "Clara,Bob": i[12],
                "Clara,Anna": i[13],
        
                } 

        Partition = Partition + Energy_True() 
    return Partition

def Formula_Energy_all_worlds(Grounding, Formula):
    Partition = 0
    for i in itertools.product([True,False], repeat=15):
        i = list(i)
        global Smokes
        Smokes = {
                "Anna": i[0],
                "Bob": i[1],
                "Clara": i[2],
                 }
        global Cancer
        Cancer = {
                "Anna": i[3], 
                "Bob": i[4],
                "Clara": i[5],
                }
        global Freindship
        Freindship = {
        
                "Anna,Anna": i[14], 
                "Anna,Bob": i[6],
                "Anna,Clara": i[7], 
                "Bob,Anna": i[8],
                "Bob,Clara": i[9], 
                "Bob,Bob": i[10],
                "Clara,Clara": i[11],
                "Clara,Bob": i[12],
                "Clara,Anna": i[13],
        
                } 

        Partition = Partition + Energy_Formula(Grounding, Formula) 
    return Partition

FIC_Energy = Formula_Energy_all_worlds(Freindship, FreindshipImpliesCancer)


Partition_func = Partition()
print("\n One of the  least probable world is ")
print(min(Energy_log))



print("The partition function has a value ")
print(Partition_func)

print("Probability of our world being true")
print(True_Energy/Partition_func)

n_w = 0
for i in Energy_log:
    if i == True_Energy:
        n_w = n_w + 1

print("Number of worlds that have the same energy as our world")
print(n_w)
print(n_w/2**15)

print("Probability of freindship implies cancer")
print(FIC_Energy/Partition_func)
#def CancerGivenMLN:











def Partition_Function():

#    for key_smokes,value in Smokes.items():
#        x = Symbol('x')
#        for  key_cancer,value in Cancer.items():
#            y = Symbol('y')
#
#            if key_smokes == key_cancer:
#                print("Smoking(%s) => Cancer(%s)" %(key_cancer, key_cancer) )
#                models = satisfiable(Implies(x,y), all_models=True)
#                print(list(models))
    PartitionFunction = 0
    for key_freindship, values in Freindship.items():
        PartitionExponent = 0
        pair = key_freindship.split(",")
        x1 = pair[0]
        y1 = pair[1]
         
        xs = Symbol('xs')
        ys = Symbol('xs')
        xc = Symbol('ys')
        yc = Symbol('yc')
        xyf = Symbol('xyf')


######################### A or B = ~A & B + A & ~B + A & B #####################################
#################### Worl weigh  = Wb     + Wa     + Wa + Wb ###################################

        y = Symbol('y')
        z = Symbol('z')
        
        xs   = "Smokes_" + x1 
        ys   = "Smokes_" + y1
        xc   = "Cancer_"+ x1 
        yc   = "Cancer_ "+ y1 
        xyf  = "Freinds_"+ x1+"_" + y1
        if (pair[0] != pair[1]):
            print("%s => %s " %(xs, xc))
            print("%s  => %s " %(ys, yc))
            print("%s  => ( %s  <=>  %s )" % (xyf, xs, ys))     
            models = satisfiable((Implies(xs,xc)& Implies(xyf, (Implies(xs,ys)& Implies(ys,xs)))), all_models=True)
            n1 = len(list(models))
            
            PartitionFunction = exp(Weight['SmokingImpliesCancer'] + Weight['FreindshipImpliesSmoking'] )*n1 + PartitionFunction
           
            models = satisfiable((Implies(xs,xc)& ~Implies(xyf, (Implies(xs,ys)& Implies(ys,xs)))), all_models=True)

            n2 = len(list(models))

            PartitionFunction = exp(Weight['SmokingImpliesCancer'])*n2 + PartitionFunction

            models = satisfiable((~Implies(xs,xc)& Implies(xyf, (Implies(xs,ys)& Implies(ys,xs)))), all_models=True)

            n3 = len(list(models))
            PartitionExponent = exp(Weight["FreindshipImpliesSmoking"])*n3 + PartitionFunction
        


            models = satisfiable((Implies(xs,xc) | Implies(xyf, (Implies(xs,ys)& Implies(ys,xs)))), all_models=True)
            print(len(list(models)))
            

#        if pair[0] == pair[1]:
#            print("Smoking(%s) => Cancer(%s)" %(x1, y1) )
#            print("Freindship(%s,%s) => (Smokes(%s) <=> Smokes(%s))" % (x1,y1,x1,y1)) 
#           
#            models = satisfiable((Implies(x,y) & Implies(z, (Implies(x,y)& Implies(x,y)))), all_models=True)
#            print(list(models)) 
    return PartitionFunction  



#print(Partition_Function())
#print("Number of Worlds for Smoking Implies Cancer")
#print(SIC_Count, "\n")
#SIC_Partition = math.exp(SIC_Count*Weight['SmokingImpliesCancer'])
#
#def Model_Count():
#    
#    x = Symbol('x')
#    y = Symbol('y')
#    z = Symbol('z')
#    Count_SIC = 0
#    Count_FIC
#
#    for key_freindship, values in Freindship.items():
#        pair = key_freindship.split(",")
#        x = pair[0]
#        y = pair[1]
#
#        if pair[0] == pair[1]:
#            model_SIC = satisfiable(SmokingImpliesCancer(x), all_models=True)
#            Count_for_Instance  = sum(1 for i in models_SIC)
#
#
#    for key_smokes,value in Smokes.items():
#        x = key_smokes
#        satisfiable(Implies(y,x), all_models=True)
#        for key_cancer,values in Cancer.items():
#            y = key_cancer
#            for key_freindship, values in Freindship.items():
#                z = key_freindship
#                print(x)
#                print(y)
#                print(z)
#                models_FIC = satisfiable(Implies(z, (Implies(x,y) & Implies(y,x))), all_models=True)
#                #models_SIC = 
 # 
#                print(next(models_FIC))
#                Count_for_Instance  = sum(1 for i in models_FIC) 
#                Count =  Count_for_Instance + Count
#    
#    return(Count)
#
##print("Model Count")
##print(Model_Count())
#
#def Model_Count_FIC():
#    
#    xf = Symbol('x')
#    yf = Symbol('y')
#
#    for key_freindship, values in Freindship.items():
#        pair =  key_freindship.split(',')
#        print(pair)
#        xf = pair[0]
#        yf = pair[1]
#        models = satisfiable(FreindshipImpliesSmoking(xf,yf), all_models=True)
#        print(list(models))
#
#    
#    return
#
#
#print("Number of Wolrds for freindship causes smoking")
#FIC_Count = Model_Count_FIC()
##print(FIC_Count, "\n")
#FIC_Partition =  math.exp(FIC_Count*Weight['FreindshipImpliesSmoking'])
#
#print("Smoking Implies Cancer: Partition")
#print(SIC_Partition, "\n")
#
#
#print("Freindship Implies Smoking: Partition ")
#print(FIC_Partition, "\n")
#
#print("Total Partition")
#print(FIC_Partition* SIC_Partition, "\n" )
#
#print(Energy_True()/(FIC_Partition* SIC_Partition ))
