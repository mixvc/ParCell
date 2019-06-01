import numpy as np

from copy import deepcopy

#Keep upto 5 places of decimal for numpy array
np.set_printoptions(formatter={'float': lambda x: "{0:0.3f}".format(x)})

def fit(x,y,v):
    z = np.polyfit(x, y, 3)

    p = np.poly1d(z)

    return p(v)

def f(Q):
    return Q

def partition(N,C,EMAs,plist):

    groups = [[] for _ in range(C)]

    print ("EMAs:*****",EMAs)

    #Consider only alive cells
    L = [i for i in range(N) if plist[i]]

    #Sort the alive cells by increasing EMAs value
    L = [x for _, x in sorted(zip(EMAs, L),reverse = True)]


    while(True):

        m = 0
        for i in range(1,len(groups)):
            if sum([EMAs[j] for j in groups[i]]) < sum([EMAs[j] for j in groups[m]]):
                m = i

        groups[m].append(L.pop(0))

        if len(L) <= 0:
            break

    return groups

def average(EMAs,P,n):

    alpha = 2.0 / float(n + 1)

    for i in range(len(EMAs)):
        if EMAs[i] == 0:
            EMAs[i] = P[i]
        else:
            EMAs[i] = alpha * P[i] + (1.0 - alpha) * EMAs[i]

    return EMAs

def fit_EMAs(L):

    A = L[0]
    for i in range(1,len(L)):

        alpha = 2.0 / float(i + 1)
        A = alpha * L[i] + (1 - alpha) * A

    return A

def average1(RECORD,N):

    EMAs = [None for _ in range(N)]
    for i in range(N):
        v = len(RECORD[i])

        if v == 0:
            EMAs[i] = 0.0
        elif v < 10:
            EMAs[i] = fit_EMAs(RECORD[i])
        else:
            EMAs[i] = fit(range(len(RECORD[i])), RECORD[i],v)


    print ("EMAs:*****",EMAs)
    return EMAs

def shuffle_positions(N,C,plist):

    A = [i for i in range(N) if plist[i]]
    #print ("A:",A)

    groups = [[] for i in range(C)]
    for i in range(len(A)):
        groups[i % C].append(A[i])

    return groups