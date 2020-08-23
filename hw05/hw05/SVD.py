import matplotlib.pyplot as plt
import numpy as np

def estimator(m,n,k,U,S,V):
    # estA = np.zeros((m,n)) 
    numZ = np.count_nonzero(S==0)
    sv_num= min((len(S)-numZ),k)
    S = np.diag(S[0:sv_num])
    return np.matmul(np.matmul(U[:,:sv_num],S[:,:sv_num]),V[:sv_num,:])


    # for i in range(min((len(S)-numZ),k)):
    #     d = (U[:,i].reshape(m,1)).dot(V[i,:].reshape(1,n))
    #     estA +=(S[i]*d)   
    # return estA




img = plt.imread('1.PPM')
plt.imshow(img)
plt.show()



r = img[:,:,0]
g = img[:,:,1]
b = img[:,:,2]

m,n = r.shape
print(m,n)


Ur, Sr, Vr = np.linalg.svd(r)
Ug, Sg, Vg = np.linalg.svd(g)
Ub, Sb, Vb = np.linalg.svd(b)

k = int(input("please enter your k for estimating : "))

estR = estimator(m,n,k,Ur,Sr,Vr)
estG = estimator(m,n,k,Ug,Sg,Vg)
estB = estimator(m,n,k,Ub,Sb,Vb)


newimg = np.zeros((m,n,3))
newimg[:,:,0] = estR/256
newimg[:,:,1] = estG/256
newimg[:,:,2] = estB/256


plt.imshow(newimg)
plt.show()

