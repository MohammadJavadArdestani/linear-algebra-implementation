
import numpy as np


def echln(A,i,j,pivot_rows,pivot_cols):
    m,n = A.shape
    for x in range(i,m):
        if A[x,j] != 0 : 
            if x >i :
                A[[x, i]] = A[[i, x]]            
            break
    else :  
        return A , 1
    pivot_rows.append(i)
    pivot_cols.append(j)
  
    A[i] = (A[i] / A[i,j] )
    A[i+1:] += -1 * ( A[i] * (A[i+1:,j:j+1]))
    for w in range(i,m):
        for z in range(j,n):
            if abs(A[w,z]) < 0.0001 :
                A[w,z] = 0
    return A , 0



def reduced_echln(A,i):
    m,n = A.shape
    
    for j in range(0,n):
        if A[i,j] != 0:
            break
    else:  
        return A

    A[i] = A[i] / A[i,j]
    A[:i] -= A[i] * A[:i,j:j+1]        
    
    return A




m,n=map(int,input("Enter the number of rows and columns  : ").strip().split())
print()

matrix=np.zeros((m,n))
for i in range(m):
   matrix[i] =input().split(" ")


b = np.zeros((1,m))
b = b.reshape((m,1))

matrix= np.hstack((matrix, b))


pivot_rows = []
pivot_cols  = []
pivot_positions = []
print(matrix)
print()

A = np.copy(matrix)


for t in range(0,m):
    A,x = echln(A,t,t,pivot_rows,pivot_cols)
    k = t
    while(x == 1 and k<n):
        k+=1
        A,x = echln(A,t,k,pivot_rows,pivot_cols)



print("")
print("echelon  : ")
print(A)
print()

non_pivot_cols = list(set(range(0,n)) - set(pivot_cols))

rowcounter = 1;
mlis = []
print("base of row space :")
for r in pivot_rows :
    row  = A[r][:-1]
    row = row.reshape((n,1))
    mlis.append(row)
    print("r{} :".format(rowcounter))
    print()
    print(row)
    print()
    rowcounter +=1




print("".center(20,'*'))

print("we show elements of a vector in one row  for better Appearance \n ")
print("base of column space : \n")
pcol_counter = 1;
blist = []
for c in pivot_cols :
    col = matrix[:,c]
    # col = col.reshape((m,1))
    bb = "b" + str(pcol_counter)
    blist.append(bb)
    print("b{} = {}".format(pcol_counter,col))
    pcol_counter +=1


for i in range(m-1,-1,-1):
    A = reduced_echln(A,i)



mult = {}
for col in non_pivot_cols :
    mult[col] = []
for i in pivot_rows:
    for j in non_pivot_cols:
        mult[j].append(A[i,j])

print("\n\nnon poivot columns :\n")

for x in non_pivot_cols :
    mlist = list(zip(mult[x],blist))
    print("{} = {} ".format(matrix[:,x] , mlist[:]) )
    

print("\n \n")