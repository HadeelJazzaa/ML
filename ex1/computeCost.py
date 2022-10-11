#Three lines to make our compiler able to draw:
import sys
import matplotlib
import numpy as np
import pandas as pd
import os

#Two  lines to make our compiler able to draw:
# get the current model path
full_path = os.path.realpath(__file__)
file_path = os.path.dirname(full_path)
# the data file lcated in the model directory
fpath= file_path +"\ex1data1.txt" 
#fpath="/../ex1data1.txt"
#df = pandas.read_csv('test.csv', usecols = [0, 2:7], skiprows=5)
#print(df)
data = np.genfromtxt(fpath,delimiter = ',',dtype='float64')
x=data[:,0]
y=data[:,1]

m = len(x) # number of training examples
y=np.array(y).reshape(m,1)
z= np.ones((m,1))
aXrr=(x) # Add a column of ones to x
aXrr=np.array(aXrr).reshape(m,1)
aXrr=np.hstack((aXrr,z))
#print(aXrr)
theta = np.zeros(2) # initialize fitting parameters
out=np.empty(m)
iterations = 1500
alpha = 0.01

def computeCost(X, y, theta):
#Matrix Multiplication between two matrices A and B is valid only if the number of columns in matrix A is equal to the number of rows in matrix B.

    theta= np.array(theta).reshape(1,2)
    #h =  np.multiply (X , theta)
    z=np.dot(X,theta) 
    
    
    for i in range (m):
        ss=h[i]
        out[i]= sum(ss)
    
    h=np.array(out).reshape(m,1)
    sError =pow((h - y), 2)
    
    J = sum(sError) / (2 * m)
    #J = 1/(2*m) * sum((X*theta -y).^2)
    
    return	J
print(computeCost(aXrr, y, [-1, 2]))
