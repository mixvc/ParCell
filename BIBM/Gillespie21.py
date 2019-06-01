import math, time
import numpy as np
import random
import os

from constantz import *



def rules(con, moleculeA, group, reactionRateArray, IDs):


    for i in range(len(group)):
        l = group[i]
        l = l[:l.index(-1)]
        val = con[IDs][i]
        reactionRateArray[i] = val

        for j in range(len(l)):
            col = l[j]
            if len(l) > 1 and len(set(l)) == 1:
                if moleculeA[col] <= 1:
                    reactionRateArray[i] = 0.0
                else:
                    reactionRateArray[i] = 0.7071111111 * reactionRateArray[i] * moleculeA[col]
            else:
                reactionRateArray[i] = reactionRateArray[i] * moleculeA[col]


    return reactionRateArray


def gillespie1(T, moleculeA, q,IDs):


    t0 = time.time()

    global con, group, reactionRateArray, no_reac, exID, Grain
    initial = T


    while (True):


        reactionRateArray = rules(con, moleculeA, group,  reactionRateArray, IDs)

        try:
            for DRR1 in exID1:
                dummy = 0
                reactionRateArray#input1

            for DRR2 in exID2:
                dummy = 0
                reactionRateArray#input2

            for DRR3 in exID3:
                dummy = 0
                reactionRateArray#input3

            for DRR4 in exID4:
                dummy = 0
                reactionRateArray#input4

            for DRR5 in exID5:
                dummy = 0
                reactionRateArray#input5

            for DRR6 in exID6:
                dummy = 0
                reactionRateArray#input6

            for DRR6 in exID7:
                dummy = 0
                reactionRateArray#input6

            for DRR6 in exID8:
                dummy = 0
                reactionRateArray#input8

        except:
            curr = os.getcwd()
            os.chdir('Output')
            fw = open("logfile.pcl", "a+")
            os.chdir(curr)
            fw.write("Error in defining the dependent reaction rules block, Please use proper notation and equation.\n")
            fw.close()

            for DRR1 in exID1:
                dummy = 0
                reactionRateArray#input1

            for DRR2 in exID2:
                dummy = 0
                reactionRateArray#input2

            for DRR3 in exID3:
                dummy = 0
                reactionRateArray#input3

            for DRR4 in exID4:
                dummy = 0
                reactionRateArray#input4

            for DRR5 in exID5:
                dummy = 0
                reactionRateArray#input5

            for DRR6 in exID6:
                dummy = 0
                reactionRateArray#input6

            for DRR6 in exID7:
                dummy = 0
                reactionRateArray#input6

            for DRR6 in exID8:
                dummy = 0
                reactionRateArray#input8


        cumulative = [0.0 for k in range(int(no_reac) + 1)]

        reactionRateArraySum = np.sum(reactionRateArray)
        if reactionRateArraySum <= 0:
            return [None, None, q]

        current = np.sum(reactionRateArray) * random.uniform(0, 1)

        curr_reac1 = 0

        for curr_reac in range(int(no_reac)):
            cumulative.append(cumulative[-1] + reactionRateArray[curr_reac])

            if current > cumulative[-2] and current <= cumulative[-1]:
                curr_reac1 = curr_reac
                break

        reac_info = group[int(curr_reac1)]

        ind = reac_info.index(-1)
        left = reac_info[:ind]
        right = reac_info[ind + 1:]

        for i in range(len(left)):
            j = left[i]
            moleculeA[j] -= 1

        for i in range(len(right)):
            j = right[i]
            moleculeA[j] += 1


        T += - float(math.log(random.uniform(0, 1))) / float(np.sum(reactionRateArray))


        if T >= initial + Grain:
            time_taken = time.time() - t0
            return [moleculeA, time_taken,q]


