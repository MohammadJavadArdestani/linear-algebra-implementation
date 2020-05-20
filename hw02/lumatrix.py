import numpy as np


def factor(A,l,i,j):
    n,m = A.shape
    for x in range(i,n):
            if A[x,j] != 0 :
                break
    else :
        return A

    if x >i :
        A[[x, i]] = A[[i, x]]

    l[i:,j:j+1] = A[i:,j:j+1]/A[i,j]
    A[i+1:] -=( A[i]/A[i,j] * A[i+1:,j:j+1])
    return A,l


def forsubs(l,b):
    n,m= l.shape
    l = np.hstack((l, b))
        
    for i in range(0,n-1):
        j=i
        l[i+1:,-1] -= l[i+1,j] * l[i,-1]
        


    y = l[:,-1]
    y =  y.reshape((n,1))
        
    return y

def backsubs(u,y):
    n,m= u.shape
    u= np.hstack((u, y))
        
    for i in range(n-1,-1,-1):
        j=i
        print(i)
        u[i,-1] /=u[i,j] 
        if i != 0:
            u[:i,-1] -= (u[:i,j] * u[i,-1])
    x = u[:,-1]
    x = x.reshape((n,1))
        
    return x



    
n=int(input("Enter the matrix size : "))
print()

A=np.zeros((n,n))
l = np.zeros((n,n))

for i in range(n):
   A[i] =input().split(" ")



for t in range(0,n):
     A,l = factor(A,l,t,t)
print(" matrix U : ")     
print(A)
print()
print("".center(20,"*"))

print()
print(" matrix L : ")     
print(l)
print()
print("".center(20,"*"))
print()

reverseA = np.zeros((n,n))
e = np.zeros((n,1))
for i in range(0,n):
    e[i] = 1
    y = forsubs(l,e)
    reverseA[:,i:i+1]= backsubs(A,y)
    e[i]=0

print("".center(20,"*"))
print("reverse matrix is  : ")
print(reverseA)
