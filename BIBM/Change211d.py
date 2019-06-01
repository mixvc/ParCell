import numpy as np
import os

from generate import *
from copy import deepcopy
from constantz import *

def changeDeath2(idList, plist,T,no_cell, deathArray):
    try:
        for i in range(len(plist)):
            if plist[i] and T >= deathArray[i]:
                idList[i] = -1
                plist[i] = False
                no_cell = no_cell - 1

    except:
        curr = os.getcwd()
        os.chdir('Output')
        fw = open("logfile.pcl", "a+")
        os.chdir(curr)
        fw.write("Error in defining the cellular death Array, Please use proper notation in simulate function.\n")
        fw.close()
        for i in range(len(plist)):
            if plist[i] and T >= deathArray[i]:
                idList[i] = -1
                plist[i] = False

    return idList, plist, no_cell

