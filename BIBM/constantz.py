import numpy as np

from copy import deepcopy

from generate import *

from input2_parcell import *


# constant parameter from software
#constant_parameter = open("constant_parameter_input.txt", "r")
#constant_parameter_data = constant_parameter.readlines()
#numberOfCells = int(constant_parameter_data[0])
#totalSimulationTime = float(constant_parameter_data[1])
#timeInterval = float(constant_parameter_data[2])
#cellVolume = float(constant_parameter_data[3])
#totalVolume = float(constant_parameter_data[4])
#numberOfCores = int(constant_parameter_data[5])
#meanBirthTime = float(constant_parameter_data[6])
#meanDeathTime = float(constant_parameter_data[7])

#Default system values

Default = {'N' : 2, 'T' : 100, 'cores' : 4, 'grain' : 1, 'grainWrite':1, 'meanDivisionTime' : None,
           'meanCellDeath' : None, 'KValue' : 2}

#Assign default values
for k in S_Dict.keys():
    if S_Dict[k] == None:
        S_Dict[k] = Default[k]

#print S_Dict

# Number of Cells
no_cell = int(S_Dict['N'])

N = int(S_Dict['N']) * int(S_Dict['KValue'])

# Simulation Time
T = S_Dict['T']

# Number of cores to be used
C = int(S_Dict['cores'])

# Interval of time increment
Grain = S_Dict['grain']
grainWrite = S_Dict['grainWrite']


# Number of molecules in each cell
no_mole = np.amax(np.amax(np.array(group))) + 1


# For all cases (with or without noise analysis)
con_template = np.array(con_template)

#print con_template
con = np.zeros((N, len(group)))

for i in range(N):
    for j in range(len(group)):

        if 'constant' in distributionType[j][0]:
            con[i][j] = con_template[j]

        if 'uniform' in distributionType[j][0]:
            con[i][j] = np.random.uniform(float(distributionType[j][1]), float(distributionType[j][2]))

        if 'normal' in distributionType[j][0]:
            con[i][j] = np.random.normal(float(distributionType[j][1]), float(distributionType[j][2]))

        if 'lognormal' in distributionType[j][0]:
            con[i][j] = np.random.lognormal(float(distributionType[j][1]), float(distributionType[j][2]))



# Number of reactions
no_reac = len(group)

# Array of molecular concentration values
moleculeAEach = [0.0 for i in range(int(no_mole))]
for i in range(len(molecule_ID)):
    moleculeAEach[int(molecule_ID[i])] = moleculeInitialValue[i]
moleculeA = np.array([deepcopy(moleculeAEach) for _ in range(N)])
####### here was range(N)

# Array of reaction rate information
reactionRateArray = [0.0 for _ in range(int(no_reac))]


# birth and death

bM = S_Dict['meanDivisionTime']
dM = S_Dict['meanCellDeath']


if bM != None:
    birthArray = np.array([-bM for i in range(N)])

if dM != None:
    deathArray = np.array([-dM for i in range(N)])


# Unique id list
idList = [-1 for i in range(N)]
maxID = 0

# Alive list
plist = [False for i in range(N)]

# List of alive nodes
for i in range(N):
    if i % int(S_Dict['KValue']) == 0:
        plist[i] = True

        if dM != None:
            while deathArray[i] <= 0:
                deathArray[i] += generateTime(dM)

        if bM != None:
            while birthArray[i] <= 0 and bM != None:
                birthArray[i] += generateTime(bM)

        idList[i] = maxID
        maxID = maxID + 1


exID1 = DRR_table[1]
exID2 = DRR_table[2]
exID3 = DRR_table[3]
exID4 = DRR_table[4]
exID5 = DRR_table[5]
exID6 = DRR_table[6]
exID7 = DRR_table[7]
exID8 = DRR_table[8]


history = []
ID_history = []


