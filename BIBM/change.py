import numpy as np

from generate import *
from copy import deepcopy
from constantz import *



def changeBirth(plist,T,birthArray,idList,maxID,moleculeA,bM,envr,N):

    global con,con_template,no_mole

    envr_store = [0.0 for i in range(len(envr))]
    isIt = False

    curr = os.getcwd()
    os.chdir('Output')
    fw = open("LineageTree.txt", "a+")
    os.chdir(curr)

    for i in range(len(plist)):
        if plist[i] and T >= birthArray[i] and not isIt:
            #print (T,"ENTER")
            for j in range(len(plist)):
                if not plist[j]:

                    plist[j] = True
                    idList[j] = maxID
                    maxID += 1
                    fw.write('[Dividing cell, Divided cell, Dying cell, Total cell, Time] = [' + str(idList[i])+ ' ' + str(idList[j]))
                    fw.close()

                    orig = [k for k in moleculeA[i]]
                    for l in range(len(envr)):
                        envr_store[l] = moleculeA[i][envr[l]]

                    s = np.array(np.random.binomial(1001, 0.5, no_mole))
                    s = np.array([float(m)/1001.0 for m in s])
                    moleculeA[i] = np.multiply(np.array(orig), np.array(s))
                    moleculeA[i] = moleculeA[i].astype(int)
                    moleculeA[j] = np.array(orig) - np.array(moleculeA[i])


                    for l in range(len(envr)):
                        moleculeA[i][envr[l]] = envr_store[l]
                        moleculeA[j][envr[l]] = envr_store[l]

                    birthArray[i] = generateTime(bM) + T
                    birthArray[j] = generateTime(bM) + T

                    isIt = True

                    break

    return birthArray,idList,maxID,moleculeA,plist,isIt




def checkDeath(idList,plist,T, N):

    curr = os.getcwd()
    os.chdir('Output')
    fw = open("LineageTree.txt", "a+")
    os.chdir(curr)

    i = random.choice([i for i in range(len(plist)) if plist[i] == True])

    fw.write(' ' + str(idList[i]) + ' ' + str(N/2) + ' ' + str(T) + ']\n')
    fw.close()
    idList[i] = -1
    plist[i] = False

    return idList,plist

