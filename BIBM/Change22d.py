import numpy as np
import os

from generate import *
from copy import deepcopy
from constantz import *

def changeDeath1(idList, plist,T,N):
    global no_cell
    try:
        for i in range(len(plist)):
            if plist[i] and T >= deathArray[i]:

                idList[i] = -1
                plist[i] = False
                no_cell = no_cell - 1

    except:
        curr = os.getcwd()
        os.chdir('Output')
        fw = open("logfile.txt", "a+")
        os.chdir(curr)
        fw.write("Error in defining the cellular death block, Please use proper notation and equation.\n")
        fw.close()
        for i in range(len(plist)):
            if plist[i] and T >= deathArray[i]:

                idList[i] = -1
                plist[i] = False

    return idList, plist, no_cell

