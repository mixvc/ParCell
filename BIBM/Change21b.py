import numpy as np
import os

from generate import *
from copy import deepcopy
from constantz import *

def changeBirth1(plist,T,birthArray,idList,maxID,moleculeA,bM,envr, no_cell):

    global con,con_template,no_mole

    envr_store = [0.0 for i in range(len(envr))]
    isIt = False
    try:
        for i in range(len(plist)):
            if plist[i] and input1:
                for j in range(len(plist)):
                    if not plist[j]:

                        plist[j] = True
                        idList[j] = maxID
                        maxID += 1

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

                        deathArray[i] = generateTime(dM) + T
                        deathArray[j] = generateTime(dM) + T

                        no_cell = no_cell + 1
                        isIt = True

                        break


    except:
        curr = os.getcwd()
        os.chdir('Output')
        fw = open("logfile.pcl", "a+")
        os.chdir(curr)
        fw.write("Error in defining the cellular birth block, Please use proper notation and equation.\n")
        fw.close()

        for i in range(len(plist)):
            if plist[i] and input1:
                for j in range(len(plist)):
                    if not plist[j]:

                        plist[j] = True
                        idList[j] = maxID
                        maxID += 1

                        orig = [k for k in moleculeA[i]]
                        for l in range(len(envr)):
                            envr_store[l] = moleculeA[i][envr[l]]
                        s = np.array(np.random.binomial(1001, 0.5, no_mole))
                        s = np.array([float(m) / 1001.0 for m in s])
                        moleculeA[i] = np.multiply(np.array(orig), np.array(s))
                        moleculeA[i] = moleculeA[i].astype(int)
                        moleculeA[j] = np.array(orig) - np.array(moleculeA[i])

                        for l in range(len(envr)):
                            moleculeA[i][envr[l]] = envr_store[l]
                            moleculeA[j][envr[l]] = envr_store[l]

                        birthArray[i] = generateTime(bM) + T
                        birthArray[j] = generateTime(bM) + T

                        break

    return birthArray, idList, maxID, moleculeA, plist, no_cell, isIt



