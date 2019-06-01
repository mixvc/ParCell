import numpy as np
import math
import os
from constantz import *
from copy import deepcopy

def environment1(N, previousEnv, moleculeA, envr, updateExt):


    try:
        for j in range(len(envr)):
            for i in range(N):
                if plist[i]:
                    dummy = 0
                    #input1
                    #input2
                    #input3
                    #input4
                    #input5
                    #input6
                    #input7
                    #input8
    except:
        curr = os.getcwd()
        os.chdir('Output')
        fw = open("logfile.pcl", "a+")
        os.chdir(curr)
        fw.write("Error in defining the environmental rules block, Please use proper notation and equation.\n")
        fw.close()
        for j in range(len(envr)):
            for i in range(N):
                if plist[i]:
                    dummy = 0
                    #input1
                    #input2
                    #input3
                    #input4
                    #input5
                    #input6
                    #input7
                    #input8

    #print "updateExt",updateExt
    #print "previousEnvr", previousEnv
    for j in range(len(envr)):
        for i in range(N):
            if plist[i]:
                if updateExt[envr[j]] < 0:
                    moleculeA[i][envr[j]] = 0
                else:
                    moleculeA[i][envr[j]] = updateExt[envr[j]]
