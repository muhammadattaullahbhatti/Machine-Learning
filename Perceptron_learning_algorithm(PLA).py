"""
Created on Fri Mar 19 17:46:04 2021
@author: Muhammad Attaullah Bhatti
"""
# W = weights list
# X = Independent features list
# Y = labels/dependent variable list
# P = pridicted labels list 

#%%
import numpy as np
X = W = Y = []
j = -1
end = True
#%%
# Get inputs
n = int(input('please input number of total samples :'))
no_of_features = int(input('please enter total number of independent features :'))
W = [float(item) for item in input("Enter the weights : ").split()]
Y = [float(item) for item in input("Enter the class labels : ").split()]
for i in range(n):
    X.append([float(item) for item in input("Enter the x1 space x2 : ").split()])
a = int(input('please input value of alpha/eta :'))

#%%
# perform checks for data consistency
assert(no_of_features == len(W)),'Number of features and weights dimentions mismatched, either is more'
assert(len(Y) == n),'Number of samples and labels are mismatched, either is more'


#%%
# Algorithm for calculating weights
while end:
    P = []    
    for i in range(len(Y)):
        weight = 0        
        for f in range(no_of_features):
            weight+=W[f]*X[i][f]
        if weight >= 0:
            P.append(1)
        else:
            P.append(-1)   
    comparison = np.array(P) == np.array(Y)   
    if(comparison.all()):
        end = False
    else:
        for i in range(len(Y)):
            if P[i] != Y[i]:
                j = i
                break
        for i in range(len(W)):
                W[i] = W[i]+a*(Y[j]*X[j][i])
#%%
# printing final weights                
print('Final weights are {}'.format(W))   

#%%
# sample inputs for visualization:
# X = [[1,1],[2,-2],[-1,-1.5],[-2,-1],[-2,1],[1.5,-0.5]]
# Y = [1,-1,-1,-1,1,1]
# W = [1, 0.5]