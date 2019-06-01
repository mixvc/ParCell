import pickle
import numpy as np
import matplotlib.pyplot as plt

def MeanDeviation(moleculeOfInterest,Grain):

    history = np.array(pickle.load(open('history-0.0.p', 'r')))
    ID_history = np.array(pickle.load(open('ID_history-0.0.p', 'r')))

    #print (history)
    #print (ID_history)

    #MEAN DEVIATION ARRAY:
    MDA = []
    #MEAN DEVIATION METRIC:
    MDM = 0.0

    maxID = max([max(sub_array) for sub_array in ID_history])
    #print "maximum ID:",maxID

    NoOfSamples = len(history)
    #print "Number of samples:",NoOfSamples


    xAvg = [(i * Grain) for i in range(NoOfSamples)]
    yAvg = [0.0 for i in range(NoOfSamples)]
    nPoi = [0.0 for i in range(NoOfSamples)]

    timestamp = []
    for i in range(maxID + 1):
        t = [j for j in range(len(ID_history)) if i in ID_history[j]]
        timestamp.append(t)
    #print timestamp

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
            #print i,j
            y = history[j,aliveList[j].index(i),moleculeOfInterest]
            #print "Y:",y
            yaxis.append(y)
            xaxis.append(j * Grain)

            yAvg[j] = yAvg[j] + y
            nPoi[j] += 1.0

        MDA.append(yaxis)

        print np.array(yaxis).shape

    #print yAvg
    yAvg = [float(yAvg[i])/float(nPoi[i]) for i in range(len(yAvg))]

    MDA = np.array(MDA)
    print MDA.shape

    for i in range(MDA.shape[1]):
        #Deviation
        MDM += max([abs(yAvg[i] - MDA[j,i]) for j in range(MDA.shape[0])])



        #plt.plot(xaxis,yaxis)

    #plt.ylim([0,60.0])
    #plt.xlim([0,10000.0])



    #print yAvg
    plt.plot(xAvg[:200],yAvg[:200],linewidth = 2,color = 'blue')
    #plt.ylabel('Molecular Conc.')
    #plt.xlabel('Time in min')
    #plt.show()
    #os.chdir('/usr/local/home/sr3k2/sandbox/BIBM/BIBM')
    #pickle.dump(yAvg, open('Parallel.p', 'wb'))
    #pickle.dump(xAvg, open('yaxis.p', 'wb'))
    #os.chdir(curr)

    return yAvg[:200],float(MDM)/float(MDA.shape[1])

yAvg,MDM = MeanDeviation(0,0.005)
print MDM

#358958.59596
#360710.272727
#360118.646465
#365154.111111