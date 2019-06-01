import os, sys
import math


f = open('plot_rules.pcl','r')

L = f.readlines()

plot_rules_block = [x for x in L if x!='\n']
cnt = 1
plot_function_copy = open("plot21.py").read()
plot_copy_file = open("plot22.py", 'w')
plot_copy_file.write(plot_function_copy)
plot_copy_file.close()


for plotRules in plot_rules_block:
    if plotRules[0] != '#':
        l = len(plot_rules_block)
        plotRules = plotRules.strip()

        s = open("plot22.py").read()

        st_input = '#input' + str(cnt)
        s = s.replace(st_input, '%s'%plotRules)

        f = open("plot22.py", 'w')
        f.write(s)
        f.close()
        cnt += 1


