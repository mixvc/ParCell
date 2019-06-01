import random,pickle
import sys
sys.path.append("/usr/local/lib/python3.5/dist-packages/numpy/")
import numpy as np
import time, os
#import matplotlib.pyplot as plt

from copy import deepcopy
from constantz import *
from default_environment import *
from load import *
from Gillespie import *
from Gillespie22 import *
from change import *
from multiprocessing import Pool
from input2_parcell import *
from default_environment22 import *
from Change211d import  *
if cellular_birth_exist:
    from Change22b import *
if cellular_death_exist:
    from Change22d import *
if break_exist:
    from break_condition22 import *


np.set_printoptions(precision=30)

def write_log(moleculeA,plist,idList):

    aliveID = [i for i in range(len(idList)) if plist[i]]

    #Write file to pickle
    subMoleculeA = np.array([moleculeA[aliveID[i]] for i in range(len(aliveID))])
    aliveID = [idList[i] for i in aliveID]

    for i in range(len(aliveID) - 1):
        for j in range(i + 1, len(aliveID)):
            if aliveID[i] > aliveID[j]:
                temp = aliveID[i]
                aliveID[i] = aliveID[j]
                aliveID[j] = temp

                temp = subMoleculeA[i].copy()
                subMoleculeA[i] = subMoleculeA[j].copy()
                subMoleculeA[j] = temp.copy()

    return subMoleculeA,aliveID

def write_to_pickle(subMoleculeA,aliveID):
    history.append(subMoleculeA)
    ID_history.append(aliveID)

    curr = os.getcwd()
    os.chdir('Output')
    pickle.dump(history, open('history.p', 'wb'))
    pickle.dump(ID_history, open('ID_history.p', 'wb'))
    os.chdir(curr)


def f(L):


    Q = L[0]
    mA = L[1]
    t = L[2]

    results = []

    for q in Q:
        I = gillespie1(t,mA[Q.index(q)],q,q)
        results.append(I)

    return results


initT = time.time()
writeInitial = True

'''
curr = os.getcwd()
os.chdir('Output')
if os.path.exists('logfile.txt'):
    os.remove('logfile.txt')

if os.path.exists('LineageTree.txt'):
    os.remove('LineageTree.txt')

os.chdir(curr)
'''

p = Pool(processes=C)
P = [0.0 for _ in range(N)]

global moleculeA,plist,birthArray,deathArray,idList,maxID, envr, bM, no_cell, S_Dict

t = 1
t0 = time.time()

lastWrite = 0.0
#isIt = False
while True:
    #print "*****", no_cell
    if writeInitial:
        subMoleculeA, aliveID = write_log(moleculeA, plist, idList)
        write_to_pickle(subMoleculeA, aliveID)
        writeInitial = False

    curr = os.getcwd()
    os.chdir('Output')
    fw = open("logfile.pcl", "a+")
    os.chdir(curr)

    #print ("Simulation is running, Current time: ",t)
    fw.write("Simulation is running, Current time: " + str(t) + "\n")


    # When load balancing is not applied
    groups = shuffle_positions(N, C, plist)

    previousEnv = [0.0 for i in range(no_mole)]
    for j in range(len(envr)):
        for i in range(N):
            if plist[i]:
                previousEnv[envr[j]] = moleculeA[i][envr[j]]


    LP = p.map(f,[[[each for each in groups[idv] if plist[each]],
                   moleculeA[[each for each in groups[idv] if plist[each]],:],t] for idv in range(C)])

    #Copy data

    for coredata in LP:
        for cell in coredata:
            id = cell[2]
            moleculeA[id] = np.copy(cell[0])
            P[id] = cell[1]
            if cell[1] == None:
                plist[cell[2]] = False
                idList[cell[2]] = -1
                #print 'Error: Reactant is over for cell id %d' % (cell[2])
                fw.write("Warning: Reactant is over for cell id  " + str(cell[2]) + "\n")

    if list(set(plist)) == [False]:
        fw.write("All cells are Inactive. Either reactant is over or cell death occur. Simulation ending. \n")
        break

    isIt = False

    if bM != None:
        birthArray, idList, maxID, moleculeA, plist, isIt \
            = changeBirth(plist,t,birthArray,idList,maxID,moleculeA,bM,envr, N)
        if isIt:
            idList,plist = checkDeath(idList,plist,t, N)

    if dM != None:
        idList, plist, no_cell = changeDeath2(idList, plist, t, no_cell, deathArray)


    if cellular_birth_exist:
        birthArray, idList, maxID, moleculeA, plist, no_cell, isIt \
            = changeBirth1(plist,t,birthArray,idList,maxID,moleculeA,bM,envr, no_cell)
    
    if cellular_death_exist:
        idList, plist, no_cell = changeDeath1(idList, plist, t, no_cell)
        


    if environment_exist:
        updateExt = environment(N, previousEnv, moleculeA, envr)
        environment1(N, previousEnv, moleculeA, envr, updateExt)



    t = t + Grain


    if t - lastWrite >= grainWrite or isIt:
        subMoleculeA, aliveID = write_log(moleculeA, plist, idList)
        write_to_pickle(subMoleculeA,aliveID)

        lastWrite = t



    if t>=T:
        fw.write("Simulation is running, Current time: " + str(t) + "\n")
        fw.write("Simulation run successfully.\n")
        break

    if break_exist:
        breakCheck = 0
        if breakCondition(t, T, no_cell, breakCheck) > 0:
            fw.write("Simulation is running, Current time: " + str(t) + "\n")
            fw.write("Simulation Completed with user provided condition: " + str(simulation_end_rules))
            break

    fw.close()


