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

np.set_printoptions(threshold=np.nan)


def plotter(moleculeOfInterest):

    global grainWrite

    Grain = grainWrite



    for m in moleculeOfInterest:
        curr = os.getcwd()
        os.chdir('Output')
        history = pickle.load(open('history.p', 'rb'))
        ID_history = pickle.load(open('ID_history.p', 'rb'))
        os.chdir(curr)
        '''
        if len(ID_history[-1]) == 0:
            ID_history = ID_history[:-1]
            history = history[:-1]
        '''
        print ID_history
        print history
        maxID = max([max(sub_array) for sub_array in ID_history])

        #print "maximum ID:",maxID

        NoOfSamples = len(history)
        print "Number of samples:",NoOfSamples


        xAvg = [(i * Grain) for i in range(NoOfSamples)]
        yAvg = [0.0 for i in range(NoOfSamples)]
        nPoi = [0.0 for i in range(NoOfSamples)]

        timestamp = []
        for i in range(maxID + 1):
            t = [j for j in range(len(ID_history)) if i in ID_history[j]]
            timestamp.append(t)
        print len(timestamp), len(timestamp[1])

        aliveList = [[] for i in range(NoOfSamples)]
        for i in range(maxID + 1):
            l = timestamp[i]
            for j in l:
                aliveList[j].append(i)

        #print 'al', aliveList

        for i in range(maxID + 1):
            yaxis = []
            xaxis = []

            for j in timestamp[i]:

                y = history[j][aliveList[j].index(i)][m]
                #print y
                yaxis.append(y)

                xaxis.append(j * Grain)

                yAvg[j] = yAvg[j] + y

                nPoi[j] += 1.0

                #print yAvg[j]


            plt.plot(xaxis,yaxis)

            #plt.ylim([0,1200.0])
            #plt.xlim([0,10000.0])
            #print len([float(yAvg[i]) for i in range(len(yAvg))])
            #print len([float(nPoi[i]) for i in range(len(yAvg))])
            #print "\n"

            # indices_with_zero = [i for i in range(len(nPoi)) if nPoi[i] == 0]
            # nPoi = [i for j, i in enumerate(nPoi) if j not in indices_with_zero]
            # yAvg = [i for j, i in enumerate(yAvg) if j not in indices_with_zero]
            #yAvg = [0.0 for i in range(len(yAvg))]


            #yAvg = [float(yAvg[i])/float(nPoi[i]) for i in range(len(yAvg))]


        #plt.plot(xAvg,yAvg,linewidth = 2,linestyle = 'dashed')
    #print moleculeA
    plt.ylabel('# of molecules')
    plt.xlabel('Time')
    #plt.legend(moleculeA, loc='upper right')
    plt.show()


def plotter2(moleculeOfInterest,LEGENDS):

    curr = os.getcwd()
    os.chdir('Output')
    history = pickle.load(open('history.p', 'rb'))
    ID_history = pickle.load(open('ID_history.p', 'rb'))
    os.chdir(curr)

    max_column_size = len(ID_history)

    xAvg = [i for i in range(max_column_size)]

    for m in moleculeOfInterest:

        yAvg = []

        for t in range(max_column_size):
            alive_list = ID_history[t][:]
            slice_of_history = [history[t][i][m] for i in range(len(alive_list))]
            yAvg.append(np.average(slice_of_history))


        if len(LEGENDS) > 0:
            plt.plot(xAvg,yAvg,linewidth = 2,linestyle = 'dashed',label = LEGENDS[moleculeOfInterest.index(m)])
        else:
            plt.plot(xAvg, yAvg, linewidth=2, linestyle='dashed')
    #print moleculeA
    plt.ylabel('# of molecules')
    plt.xlabel('Time')
    plt.legend(loc='upper left')
    plt.show()


curr = os.getcwd()
os.chdir('Output')
moleculeA = read_dictionary_from_file('moleculeIndices.txt')
os.chdir(curr)
#plotter([moleculeA['E'], moleculeA['S'], moleculeA['ES'], moleculeA['P']])


#plotter2([moleculeA['DNA'], moleculeA['P']],['DNA', 'P'])
plotter([moleculeA['LuxI']])
#plotter([moleculeA['mRNA']])
#plotter([moleculeA['AHL(EC)']])


