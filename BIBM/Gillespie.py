import math, time
import numpy as np
import random

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


def gillespie(T, moleculeA, q,IDs):


    t0 = time.time()

    global con, group, reactionRateArray, no_reac, exID, Grain
    initial = T


    while (True):


        reactionRateArray = rules(con, moleculeA, group,  reactionRateArray, IDs)


        cumulative = [0.0 for k in range(int(no_reac) + 1)]

        reactionRateArraySum = np.sum(reactionRateArray)
        if reactionRateArraySum <= 0:
            return [moleculeA, None, q]

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

