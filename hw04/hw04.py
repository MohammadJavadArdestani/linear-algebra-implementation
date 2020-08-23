import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

# reading data from .csv file and store the World column in depended_variable vector
col_list = ["World"]
df = pd.read_csv("total_cases.csv", usecols=col_list , skipfooter=7)
depended_variable = df.values

# creating matrix A = [n^2  n  1] and n is number of days that we got from .csv file  
matrix_A=np.zeros((len(df),3))

for i in range(1,len(df)+1):
    matrix_A[i-1] = [(i**2) , i ,1]

matrix_AT = np.transpose(matrix_A)


matrix_ATA = matrix_AT.dot(matrix_A)
print("matrix_A^TA is :")
print(matrix_ATA)
print("\n" + "".center(30,"*")+"\n")

matrix_ATb = matrix_AT.dot(depended_variable)
print("matrix_A^Tb is :")
print(matrix_ATb)
print("\n" + "".center(30,"*")+"\n")

x = np.linalg.solve(matrix_ATA, matrix_ATb)
print("the result of A^TA x = A^Tb is : ")
print(x)
# print(x.astype(int))
print("\n" + "".center(30,"*")+"\n")

# add calculation result to a list for using in plot
cal_list=[]
for i in range(1,len(df)):
   cal_list.append(((x[0,0]*i**2 ) + (x[1,0])*(+i) + x[2,0]))


   
plt.plot(cal_list, label='calculated polynomial')
plt.scatter(range(1,len(df)+1),depended_variable, label='actual values', color='r')
plt.legend(loc = 'best')
plt.show()
plt.savefig('my_figure.png')


# calculate last 7 day for checking ou accuracy 
print("the calculation for last 7 day : ")
for i in range(1,9):
       print(int((x[0,0]*((i+len(df))**2 ) + ((x[1,0])*(len(df)+i)) + x[2,0])))