import os, sys
import math


def write_dictionary_to_file(D,fname):

    f = open(fname,'w')
    for k in D.keys():
        f.write(str(k) + ' ' + str(D[k]) + '\n')

    f.close()

def process_tag(TAGS,compartments):

    length_of_reactant = TAGS.index(-1)
    reactant = TAGS[:length_of_reactant]
    product = TAGS[length_of_reactant + 1:]

    #First order reaction
    if length_of_reactant == 1:
        return 1.0

    #Same reactant on the left side
    if len(set(TAGS[:length_of_reactant])) == 1:
        return math.pow(compartments[TAGS[0]],1.0 - length_of_reactant)

    #Otherwise
    t = set(list(set(reactant) - set(product)))
    #print 'Here:',list(t)[0]

    return math.pow(compartments[list(t)[0]],1.0 - length_of_reactant)

def block_calculation(block_name,diction,mode):

    #math_operator = ['*', '/']
    # 1. Read parameters

    for l in block_name:
        #print (l)

        if l[0] != '#':

            if '#' in l:
                l = l[:l.index('#')]

            if mode == 1:
                l = replace_keys(diction,l)

            v = l.split()
            #print v
            if len(v) > 0 and '+' not in l and '-' not in l and '*' not in l and '/' not in l:
                #print v
                diction[v[0]] = float(v[1])
            elif len(v) > 0:
                r = process(l, diction)
                diction[v[0]] = r

    return diction

def replace_keys(parameters,l):

    while (True):
        flag = False

        for k in parameters.keys():

            old = k

            if k in l:
                new = str(parameters[k])
                l = l.replace(old, new)
                flag = True

        if flag == False:
            break

    return l

def process(l,parameters):
    l = l[l.index(' ') + 1:]

    l = replace_keys(parameters,l)

    return eval(l)



def read_block(L,start_phrase,end_phrase):
    # Begin index
    start_index = -1
    end_index = -1


    for i in range(len(L)):
        if start_phrase in L[i]:
            start_index = i

        if end_phrase in L[i]:
            end_index = i

    s = L[start_index + 1:end_index]
    return s

#try:
f = open('rules_input.pcl','r')

environment_exist = False
break_exist = False
cellular_birth_exist = False
cellular_death_exist = False
environment_rules_exist = False
L = f.readlines()

#System parameter dictionary
S_Dict = {}
S_Dict['N'] = None
S_Dict['T'] = None
S_Dict['cores'] = None
S_Dict['grain'] = None
S_Dict['grainWrite'] = None
S_Dict['meanDivisionTime'] = None
S_Dict['meanCellDeath'] = None
S_Dict['KValue'] = None


curr = os.getcwd()
os.chdir('Output')

if os.path.exists('logfile.pcl'):
    os.remove('logfile.pcl')

fw = open("logfile.pcl", "a+")
os.chdir(curr)

#Read system parameters:
try:
    for l in L:
        if 'simulate(' in l and '#' not in l:
            important = l[l.index('simulate(') + len('simulate('):l.index(')')]

            for parameter_each in important.split(','):
                pp = parameter_each.split('=')
                if pp[1].strip() != 'None':
                    S_Dict[pp[0].strip()] = float(pp[1].strip())

except:
    fw.write("Error in calling simulate() function. Please use exact name and notation.\n")
    fw.close()
    sys.exit()

#print S_Dict

#Entire input file in string
f = open('rules_input.pcl','r')
s = f.read()

with open("check.pcl", "w") as f:  # open file
    f.write(s)

#Read blocks
parameter_block = read_block(L,'begin parameter','end parameter')
species_block = read_block(L,'begin species','end species')
initial_condition_block = read_block(L,'begin initial condition','end initial condition')
reaction_rules_block = read_block(L,'begin reaction rules','end reaction rules')

environmental_species_block = []
if 'begin environmental species' in s:
    environmental_species_block = read_block(L,'begin environmental species','end environmental species')

if len([each for each in environmental_species_block if each[0] != '#' and each.strip(' ') != '\n']) > 0:
    environment_exist = True

environmental_rules_block = []
if 'begin environmental rules' in s:
    environmental_rules_block = read_block(L,'begin environmental rules','end environmental rules')

if len([each for each in environmental_rules_block if each[0] != '#' and each.strip(' ') != '\n']) > 0:
    environment_rules_exist = True

dependent_reaction_rules_block = []
if 'begin dependent reaction rules' in s:
    dependent_reaction_rules_block = read_block(L,'begin dependent reaction rules','end dependent reaction rules')

cellular_birth_block = []
if 'begin cellular birth' in s:
    cellular_birth_block = read_block(L,'begin cellular birth','end cellular birth')

if len([each for each in cellular_birth_block if each[0] != '#' and each.strip(' ') != '\n']) > 0:
    cellular_birth_exist = True

cellular_death_block = []
if 'begin cellular death' in s:
    cellular_death_block = read_block(L,'begin cellular death','end cellular death')

if len([each for each in cellular_birth_block if each[0] != '#' and each.strip(' ') != '\n']) > 0:
    cellular_death_exist = True

compartment_block = []
if 'begin compartments' in s:
    compartment_block = read_block(L,'begin compartments','end compartments')

simulation_end_rules_block = []
if 'begin simulation end rules' in s:
    simulation_end_rules_block= read_block(L, 'begin simulation end rules', 'end simulation end rules')

if len([each for each in simulation_end_rules_block if each[0] != '#' and each.strip(' ') != '\n']) > 0:
    break_exist = True

#print cellular_death_exist, cellular_death_exist
#print break_exist

try:
    parameters = block_calculation(parameter_block,{},0)

except:
    fw.write("Error in Parameter block\n")
    fw.close()
    sys.exit()

#print parameters
try:
    compartments = block_calculation(compartment_block,parameters.copy(),1)
    compartments = {v:compartments[v] for v in compartments.keys() if v not in parameters.keys()}

except:
    fw.write("Error in Compartment block\n")
    fw.close()
    sys.exit()
#print compartments


#2. Index molecules
try:
    moleculeIndices = {}
    i = 0
    for l in species_block:
        if l[0] != '#':

            v = l.split()
            if len(v) > 0:
                moleculeIndices[v[0]] = i
                i += 1

    #print moleculeIndices
    curr = os.getcwd()
    os.chdir('Output')
    write_dictionary_to_file(moleculeIndices,'moleculeIndices.pcl')
    os.chdir(curr)

except:
    fw.write("Error in Species block\n")
    fw.close()
    sys.exit()

#3. initial condition block
try:
    molecule_ID = []
    moleculeInitialValue = []
    index = []

    for l in initial_condition_block:
        v = l.split()
        if l[0] != '#' and len(v) > 0:
            molecule_ID.append(moleculeIndices[v[0]])
            moleculeInitialValue.append(float(v[1]))

except:
    fw.write("Error in Initial condition block\n")
    fw.close()
    sys.exit()

#print molecule_ID, moleculeInitialValue

#4. Create reaction rules and constant array
try:
    group = []
    con_template = [0.0 for i in range(len(parameters.keys()))]
    j = 0
    distributionType = []

    loop_cnt = 0
    DRR_table = [[] for z in range(9)]


    for l in reaction_rules_block:

        if l[0] != '#' and '$' in l:

            if '#' in l:
                l = l[:l.index('#')]

            TAGS = []

            #For reaction rules
            ind = l.index('$')
            l1 = l[:ind]

            g = []

            R = l1.split()

            flag_tag = False
            for r in R:
                if r in moleculeIndices.keys():
                    g.append(moleculeIndices[r])
                    if '@' in r:
                        tag = r[r.index('@') + 1:]
                        TAGS.append(tag)
                        flag_tag = True

                if r == '->':
                    g.append(-1)
                    if flag_tag:
                        TAGS.append(-1)

            #print (TAGS)

            loop_cnt += 1

            group.append(g)

            #For constant array
            ind2 = l.index('$$',ind)
            #print ind2

            l1 = l[ind + 1:ind2]

            denominator = 1.0
            if len(TAGS) > 0:
                denominator = process_tag(TAGS,compartments)


            con_template[j] = parameters[l1.split()[0]]/denominator


            j = j + 1

            ind3 = l.index('$$')
            d1 = l[ind3 + 2:]

            if '(' in d1:
                d1 = d1[d1.index('(') + 1:d1.index(')')]
                d1 = d1.strip()
                d1 = d1.split(',')

            distributionType.append(d1)

        if '$$$' in l:
            ind4 = l.index('$$$')
            d2 = l[ind4 + 2:].strip()
            #print (d2[-1])

            d2 = int(d2[-1])

            DRR_table[d2].append(loop_cnt - 1)

except:
    fw.write("Error in Reaction rules block\n")
    fw.close()
    sys.exit()

#print DRR_table


#5. environmental_species_block
try:
    envr = []
    for l in environmental_species_block:
        z = l.split()
        if l[0] != '#' and len(z)> 0:
            envr.append(moleculeIndices[z[0]])

except:
    fw.write("Error in environmental species block\n")
    fw.close()
    sys.exit()



#5. Environmental Rules block
try:
    environmental_rules_block = [x for x in environmental_rules_block if x!='\n']
    cnt = 1
    envirinment_function_copy = open("default_environment21.py").read()
    envirinment_function_copy_file = open("default_environment22.py", 'w')
    envirinment_function_copy_file.write(envirinment_function_copy)
    envirinment_function_copy_file.close()


    for environmentRules in environmental_rules_block:
        if environmentRules[0] != '#':
            l = len(environmental_rules_block)
            environmentRules = environmentRules.strip()

            while (True):
                flag = False

                for k in moleculeIndices.keys():

                    old = '[' + k + ']'

                    if k in environmentRules:
                        new = '[' + str(moleculeIndices[k]) + ']'
                        environmentRules = environmentRules.replace(old, new)
                        flag = True

                if flag == False:
                    break


            s = open("default_environment22.py").read()

            st_input = '#input' + str(cnt)
            s = s.replace(st_input, '%s'%environmentRules)

            f = open("default_environment22.py", 'w')
            f.write(s)
            f.close()
            cnt += 1


except:
    fw.write("Error in environmental rules block\n")
    fw.close()
    sys.exit()

#6. Dependent Reaction Rules block
try:
    dependent_reaction_rules_block = [x for x in dependent_reaction_rules_block if x!='\n']
    cnt1 = 1
    Gillespie_copy = open("Gillespie21.py").read()
    Gillespie_copy_file = open("Gillespie22.py", 'w')
    Gillespie_copy_file.write(Gillespie_copy)
    Gillespie_copy_file.close()

    for dependentReactionRules in dependent_reaction_rules_block:
        if dependentReactionRules[0] != '#':
            l = len(dependent_reaction_rules_block)
            dependentReactionRules = dependentReactionRules.strip()

            while (True):
                flag = False

                for k in moleculeIndices.keys():

                    old = '[' + k + ']'

                    if k in dependentReactionRules:
                        new = '[' + str(moleculeIndices[k]) + ']'
                        dependentReactionRules = dependentReactionRules.replace(old, new)
                        flag = True

                if flag == False:
                    break

            s = open("Gillespie22.py").read()
            st_input = '#input' + str(cnt1)
            s = s.replace(st_input, '%s' % dependentReactionRules)
            #print len(environmental_rules_block)
            f = open("Gillespie22.py", 'w')
            f.write(s)
            f.close()
            cnt1 += 1

except:
    fw.write("Error in dependent reaction rules block\n")
    fw.close()
    sys.exit()


#7. Cellular birth death block
try:
    cellular_birth_block = [x for x in cellular_birth_block if x!='\n']
    for cellularBirth in cellular_birth_block:
        if cellularBirth[0] != '#':
            cellularBirth = cellularBirth.strip()

            s = open("Change21b.py").read()
            s = s.replace('input1:', '%s:\n'%cellularBirth)
            #print len(environmental_rules_block)
            f = open("Change22b.py", 'w')
            f.write(s)
            f.close()

except:
    fw.write("Error in cellular birth block\n")
    fw.close()
    sys.exit()

try:
    cellular_death_block = [x for x in cellular_death_block if x!='\n']
    for cellulardeath in cellular_death_block:
        if cellulardeath[0] != '#':
            cellulardeath = cellulardeath.strip()

            s = open("Change21d.py").read()
            s = s.replace('input1:', '%s:\n'%cellulardeath)
            f = open("Change22d.py", 'w')
            f.write(s)
            f.close()

except:
    fw.write("Error in cellular death block\n")
    fw.close()
    sys.exit()
# 8. Simulation end rules block
try:
    simulation_end_rules_block = [x for x in simulation_end_rules_block if x!='\n']
    for simulation_end_rules in simulation_end_rules_block:
        if simulation_end_rules[0] != '#':
            simulation_end_rules = simulation_end_rules.strip()
            #print simulation_end_rules_block

            s = open("break_condition21.py").read()
            s = s.replace('input1:', '%s:\n'%simulation_end_rules)
            f = open("break_condition22.py", 'w')
            f.write(s)
            f.close()
except:
    fw.write("Error in simulation end rules block\n")
    fw.close()
    sys.exit()


#print group
#print con_template
#print molecule_ID, moleculeInitialValue
# print distributionType
