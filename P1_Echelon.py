import numpy as np

pivot_counter = 0
inconsistense = False


   
def echln(A,i,j):
    m,n = A.shape
    for x in range(i,m):
        if A[x,j] != 0 : 
            if x >i :
                A[[x, i]] = A[[i, x]]            
            break
    else :  
        return A , 1
    A[i] = (A[i] / A[i,j] )
    A[i+1:] += -1 * ( A[i] * (A[i+1:,j:j+1]))
    for w in range(i,m):
        for z in range(j,n):
            if abs(A[w,z]) < 0.0001 :
                A[w,z] = 0
    return A , 0



def reduced_echln(A,i):
    n,m = A.shape
    
    for j in range(0,n):
        if A[i,j] != 0:
            break
    else:  
        if A[i,-1] != 0:
            global inconsistense
            inconsistense = True
        return A

    global pivot_counter        
    pivot_counter +=1

    A[i] = A[i] / A[i,j]
    A[:i] -= A[i] * A[:i,j:j+1]        
    
    return A


n=int(input("Enter the coefficient matrix size : "))
print("\n enter coefficient matrix: \n")

A=np.zeros((n,n))
for i in range(n):
   A[i] =input().split()

print("\n enter constant terms vector in a row \n")
b = np.zeros((1,n))
b[0] = input().split()
b = b.reshape((n,1))

A= np.hstack((A, b))
print(A)
print()
print("".center(40,"8"))
print("echelon step by step : ")
print()

for t in range(0,n):
    A,x = echln(A,t,t)
    k = t
    while(x == 1 and k<n):
        k+=1
        A,x = echln(A,t,k)
    print(A)
    print("====================================")

print()
print("".center(40,"8"))
print()
print("reduced_echelon step by step : ")

for i in range(n-1,-1,-1):
    A = reduced_echln(A,i)
    print(A)
    print("=====================================")

print()
print("".center(40,"8"))
print()    


if inconsistense : 
    print(" matrix is inconsistent")
elif pivot_counter < n : 
    print(" matrix has infinte answer")
else : 
     print("answer : ")
     b = A[:,-1]
     b = b.reshape((n,1))    
     print(b)
