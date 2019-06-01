import os

curr = os.getcwd()
os.chdir('BIBM')
os.chdir('Output')
os.system('rm -r *')
os.chdir(curr)
os.system('zip -r BIBM.zip BIBM')
os.system('mv BIBM.zip BIBM')

os.chdir('BIBM')
os.system('mv BIBM.zip Output')
os.chdir(curr)