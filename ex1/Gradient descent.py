import sys
import matplotlib
import numpy as np
import pandas as pd
import os
import matplotlib.pyplot as plt

#Two  lines to make our compiler able to draw:
# get the current model path
full_path = os.path.realpath(__file__)
file_path = os.path.dirname(full_path)
# the data file lcated in the model directory
fpath= file_path +"\ex1data1.txt" 

data = np.genfromtxt(fpath,delimiter = ',',dtype='float64')
x=data[:,0]
y=data[:,1]

m = len(x) # number of training examples

z= np.ones((m,1))
aXrr=(x) # Add a column of ones to x
aXrr=np.array(aXrr).reshape(m,1)
aXrr=np.hstack((aXrr,z))
aXrr=np.array(aXrr).reshape(m,2)
theta = np.zeros(2) # initialize fitting parameters
out=np.empty(m)
iterations = 10000
alpha = 0.01

J_history = np.zeros(iterations);

theta=[-1, 2]        
theta=np.array(theta).reshape(2,1)  

def computeCost(x, y, theta):

    theta= np.array(theta).reshape(2,1)
    x=np.array(x).reshape(m,2)
    h=np.dot(x,theta)
        
    h=np.array(out).reshape(m,1)
    sError =pow((h - y), 2)
    
    J = sum(sError) / (2 * m)
    return	J


def gradientDescent(x, y, theta, alpha, num_iters):
   
    z=np.dot(x,theta)
   
    y=np.array(y).reshape(m,1)
    z=np.array(z).reshape(m,1)
    xt=np.transpose(x)
    zz=z - y
    xtzz=np.array(np.dot(xt,zz))
    
   
    for iter in range(iterations):
        
        h=np.dot(x,theta)
        loss=h-y
        
        gradient = np.dot(xt, loss) / m
        theta = theta - alpha * gradient
        J_history[iter]=computeCost(x,y,theta)
        print(J_history[iter])
       
gradientDescent(aXrr, y, theta, alpha, iterations)        

