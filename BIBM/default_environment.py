import numpy as np
import math

from constantz import *
from copy import deepcopy

def environment(N, previousEnv, moleculeA, envr):

    updateExt = deepcopy(previousEnv)

    for j in range(len(envr)):
        for i in range(N):
            if plist[i]:
                updateExt[envr[j]] += (moleculeA[i][envr[j]] - previousEnv[envr[j]])

    #print "updateExt",updateExt
    #print "previousEnvr", previousEnv
    for j in range(len(envr)):
        for i in range(N):
            if plist[i]:
                if updateExt[envr[j]] < 0:
                    moleculeA[i][envr[j]] = 0
                else:
                    moleculeA[i][envr[j]] = updateExt[envr[j]]

    return updateExt
