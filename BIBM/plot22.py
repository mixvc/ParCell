import pickle,os
import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from constantz import *


def read_dictionary_from_file(fname):

    moleculeA = {}
    f = open(fname,'r')
    for l in f.readlines():
        kv = l.split(' ')
        moleculeA[kv[0]] = int(kv[1])

    f.close()
    return moleculeA

#np.set_printoptions(threshold=np.nan)



def plotter(moleculeOfInterest, LEGENDS):

    global grainWrite

    Grain = grainWrite
    curr = os.getcwd()
    os.chdir('Output')
    history = pickle.load(open('history.p', 'rb'))
    ID_history = pickle.load(open('ID_history.p', 'rb'))
    os.chdir(curr)

    for m in moleculeOfInterest:
        legend_exist = True

        if len(ID_history[-1]) == 0:
            ID_history = ID_history[:-1]
            history = history[:-1]

        maxID = max([max(sub_array) for sub_array in ID_history])

        NoOfSamples = len(history)

        xAvg = [(i * Grain) for i in range(NoOfSamples)]
        yAvg = [0.0 for i in range(NoOfSamples)]
        nPoi = [0.0 for i in range(NoOfSamples)]

        timestamp = []
        for i in range(maxID + 1):
            t = [j for j in range(len(ID_history)) if i in ID_history[j]]
            timestamp.append(t)

        aliveList = [[] for i in range(NoOfSamples)]
        for i in range(maxID + 1):
            l = timestamp[i]
            for j in l:
                aliveList[j].append(i)


        for i in range(maxID + 1):
            yaxis = []
            xaxis = []

            for j in timestamp[i]:
                y = history[j][aliveList[j].index(i)][m]
                yaxis.append(y)

                xaxis.append(j * Grain)


            #plt.plot(xaxis,yaxis)
            if len(LEGENDS) > 0 and legend_exist:
                plt.plot(xaxis, yaxis, label=LEGENDS[moleculeOfInterest.index(m)])
                legend_exist = False
            else:
                plt.plot(xaxis, yaxis)
    plt.ylabel('# of molecules')
    plt.xlabel('Time')
    plt.legend(loc='upper left', frameon=False)
    plt.show()



def plotterA(moleculeOfInterest,LEGENDS):

    global grainWrite

    Grain = grainWrite

    curr = os.getcwd()
    os.chdir('Output')
    history = pickle.load(open('history.p', 'rb'))
    ID_history = pickle.load(open('ID_history.p', 'rb'))
    os.chdir(curr)

    max_column_size = len(ID_history)

    xAvg = [i*Grain for i in range(max_column_size)]

    for m in moleculeOfInterest:

        yAvg = []

        for t in range(max_column_size):
            alive_list = ID_history[t][:]
            slice_of_history = [history[t][i][m] for i in range(len(alive_list))]
            yAvg.append(np.average(slice_of_history))

        if len(LEGENDS) > 0:
            plt.plot(xAvg, yAvg, linewidth=2, linestyle='dashed', label=LEGENDS[moleculeOfInterest.index(m)])
        else:
            plt.plot(xAvg, yAvg, linewidth=2, linestyle='dashed')

    plt.ylabel('# of molecules')
    plt.xlabel('Time')
    plt.legend(loc='upper left', frameon=False)
    plt.show()


curr = os.getcwd()
os.chdir('Output')
moleculeA = read_dictionary_from_file('moleculeIndices.pcl')
fw = open("logfile.pcl", "a+")
os.chdir(curr)

try:
    dummy = 0
    plotterA([moleculeA['LuxR']], ['LuxR'])
    #input2
    #input3
    #input4
    #input5
    #input6
    #input7
    #input8

except:
    fw.write("Error: Plot function is not callable")



