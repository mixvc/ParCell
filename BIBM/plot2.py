import pickle,os
import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
#from constantz import *

#np.set_printoptions(threshold=np.nan)


def read_dictionary_from_file(fname):

    moleculeA = {}
    f = open(fname,'r')
    for l in f.readlines():
        kv = l.split(' ')
        moleculeA[kv[0]] = int(kv[1])

    f.close()
    return moleculeA


global grainWrite

Grain = grainWrite

curr = os.getcwd()
print curr


'''
os.chdir('Output')
history = pickle.load(open('history.p', 'rb'))
ID_history = pickle.load(open('ID_history.p', 'rb'))
os.chdir(curr)

# finding the maximum column size of ID history
max_column_size = max([len(each[0]) for each in ID_history])
print max_column_size

    #for m in moleculeOfInterest:

curr = os.getcwd()
os.chdir('Output')
moleculeA = read_dictionary_from_file('moleculeIndices.txt')
os.chdir(curr)
#plotter([moleculeA['E'], moleculeA['S'], moleculeA['ES'], moleculeA['P']])
plotter([moleculeA['P']])
'''
